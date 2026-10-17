"""
scan.py -- photon-energy scan of sigma(gamma N -> pi N) through Sherpa.

Runs the four single-pion photoproduction channels

    gamma p -> p pi0      (p A -> p Pi0)     key  pi0p
    gamma p -> n pi+      (p A -> n Pi+)     key  pi+n
    gamma n -> n pi0      (n A -> n Pi0)     key  pi0n
    gamma n -> p pi-      (n A -> p Pi-)     key  pi-p

each with and without the Delta form factor (the two UFO builds in MODELS), and
lays the result on top of the semi-analytic curves of Fig. 33 of
nucl-th/0509020v2 -- the Fig. 33 prescription itself, and that prescription plus
t-channel omega/rho exchange.

EVERYTHING IS CACHED IN CSV.  Nothing here has to be recomputed to redraw a
figure:

    scan_results.csv               Sherpa points, long format, all channels
    beam_scan_pA_pPi0.txt          the pi0p subset in the historical layout
    fig33_reference_scan_grid.csv  semi-analytic curves on the scan grid
    fig33_vecmeson_scan_grid.csv   ... plus omega/rho (from fig33_vecmeson.m)

`--plot-only` reads those and draws; `plot_scan.py` does the same with a
single-panel layout.  The Sherpa results file is rewritten after every
(channel, model) pair, so an interrupted scan keeps everything it had finished.

WHY THE PHOTON ENERGY NEEDS CORRECTING.  BEAM_ENERGIES sets the beam ENERGY, not
its momentum, and the template gives the nucleon E = 0.938273 GeV against a mass
of 0.938272 GeV.  The target therefore is not at rest: it keeps

    pz = sqrt(E^2 - M^2) = 1.37 MeV

of residual momentum, and the two beams collide head-on, so

    s = M^2 + 2 Egamma (E_beam + pz)

rather than the fixed-target M^2 + 2 M Egamma.  Fig. 33's abscissa is the lab
photon energy on a nucleon AT REST, which is

    Egamma_corr = (s - M^2) / (2 M) = Egamma (E_beam + pz) / M

i.e. 0.15% above the number in the run card -- half an MeV at the peak.  The
proton and the neutron carry the same MNucleon in this model, so the correction
is common to all four channels.

Sampling is dense across the Delta(1232): the resonance sits at
Egamma = (M_Delta^2 - M^2)/(2M) = 0.310 GeV and is ~100 MeV wide, so a uniform
grid over 0.15-1.5 GeV puts only a couple of points on the peak.

CHARGED VS NEUTRAL PION MASS.  Sherpa uses the physical MPi+ = 0.13957 GeV in
the charged channels, so their threshold sits at Egamma = 0.1500 GeV rather than
0.1447; the grid points below it are simply not run.  The semi-analytic
machinery (fig33_from_ufo.py, Fig33v2.m) uses MPi0 in every channel, following
the paper, so its curves are defined on the whole grid.  The two therefore
disagree in the first ~5 MeV above threshold BY CONSTRUCTION.

Run:  python3 scan.py [--channels pi0p,pi+n,...] [--plot-only]
"""

import argparse
import collections
import glob
import os
import re
import shutil
import subprocess
import zipfile

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# === USER CONFIGURATION ===
EXECUTABLE = os.path.expanduser(
    "~/Documents/Projects/sherpa/570-update-achilles-interface/build/bin/Sherpa")
RESULTS_ZIP = "Results.zip"
TEMPLATE_FILE = "Sherpa_ChiPT_Template.yaml"
RUN_FILE = "Sherpa_ChiPT.yaml"

MPI0 = 0.1349768             # MPi0 in the UFO
MPIC = 0.1395704             # MPiP in the UFO
MDELTA = 1.209
E_BEAM_NUCLEON = 0.938273    # BEAM_ENERGIES[0] in the template
MN_FALLBACK = 0.938272

# The four channels.  `key` is also the channel name used by fig33_from_ufo.py
# and by the column headers of the cached csv files, so one name identifies a
# channel everywhere.  `stem` names the output figures.  `mpi` is the pion mass
# SHERPA uses, which fixes where the scan can start.
Channel = collections.namedtuple(
    "Channel", "key stem beam process mpi label ymax")

CHANNELS = collections.OrderedDict((c.key, c) for c in [
    Channel("pi0p", "pA_pPi0", 2212, "2212 22 -> 2212 111", MPI0,
            r'\gamma p \to p\,\pi^{0}', 500),
    Channel("pi+n", "pA_nPip", 2212, "2212 22 -> 2112 211", MPIC,
            r'\gamma p \to n\,\pi^{+}', 400),
    Channel("pi0n", "nA_nPi0", 2112, "2112 22 -> 2112 111", MPI0,
            r'\gamma n \to n\,\pi^{0}', 500),
    Channel("pi-p", "nA_pPim", 2112, "2112 22 -> 2212 -211", MPIC,
            r'\gamma n \to p\,\pi^{-}', 400),
])

# (model directory, parameter card, label, the semi-analytic scheme it should
# reproduce, colour, line style, marker).  Listing more than one model runs the
# scan once per model; the Process/ cache is cleared in between.
#
# Colours are the two categorical slots of the palette validated in
# fig33_from_ufo.py (#2a78d6 / #eb6834: CVD dE 24.7 protan, 33.6 normal vision).
# Line style and marker shape carry the same distinction, so nothing rests on
# colour alone.
MODELS = [
    ("ChiPT_UFO", "param_ChiPT_UFO.dat", r"no $\Delta$ FF",
     "none", "#2a78d6", (0, (4.5, 2.2)), "o"),
    ("ChiPT_UFO_DeltaFF", "param_ChiPT_UFO_DeltaFF.dat",
     r"$F_{\pi N\Delta}=\sqrt{X_\pi}$",
     "vertexfix", "#eb6834", (0, (5.5, 1.8, 1.0, 1.8)), "s"),
]

# CHIPT_SCAN_MODELS overrides the table above, as
#     CHIPT_SCAN_MODELS="ChiPT_UFO_V13:param_ChiPT_UFO_V13.dat:V13 (pole)"
# with entries separated by commas.  The scheme is always `vertexfix` -- every
# build from V10 on carries the Delta form factor -- and the style slots cycle
# through the same validated palette.  It exists so a new UFO can be scanned
# without editing this file, which is what the two historical rows are for.
_ENV_MODELS = os.environ.get("CHIPT_SCAN_MODELS", "").strip()
if _ENV_MODELS:
    _STYLES = [("#2a78d6", (0, (4.5, 2.2)), "o"),
               ("#eb6834", (0, (5.5, 1.8, 1.0, 1.8)), "s"),
               ("#117733", (0, (1.6, 1.6)), "^")]
    MODELS = []
    for _i, _spec in enumerate(_ENV_MODELS.split(",")):
        _f = _spec.split(":")
        _model = _f[0].strip()
        _card = _f[1].strip() if len(_f) > 1 and _f[1].strip() else \
            "param_%s.dat" % _model
        _label = _f[2].strip() if len(_f) > 2 and _f[2].strip() else _model
        _c, _ls, _mk = _STYLES[_i % len(_STYLES)]
        MODELS.append((_model, _card, _label, "vertexfix", _c, _ls, _mk))

# Semi-analytic curves, computed on the scan grid with the Fig33v2.m machinery
# (validated against nucl-th/0509020v2 Appendix A) through fig33_from_ufo.py.
# `reference` is the Fig. 33 prescription itself and is the ratio denominator.
# Columns are named <channel>_<scheme>; a bare <scheme> is read as pi0p, which
# is the layout the file had when it held that channel alone.
REFERENCE_CACHE = "fig33_reference_scan_grid.csv"
SCHEMES = ("reference", "none", "vertexfix")
DENOMINATOR = "reference"

# What that curve is called in a legend, and what the ratio panel divides by.
# The paper, not the figure number: these plots are no longer only Fig. 33's
# channel, and the prescription is what is being compared against.
REFERENCE_LABEL = r'nucl-th/0509020: Born + $\Delta$'
RATIO_LABEL = r'ratio to Born + $\Delta$'
# Which marks are calculated and which are simulated.  It rides on the legend
# rather than sitting loose in the ratio panel: every corner of that panel is
# occupied in one channel or another, and the legend box moves out of the way
# on its own.
LEGEND_TITLE = 'lines: semi-analytic,  markers: Sherpa'

# Born + Delta + t-channel omega/rho, on the same grid, from fig33_vecmeson.m.
# ChiPT.fr has no vector mesons, so this one cannot come from the UFO: the
# couplings are the ELA fit values of nucl-th/0509020v2 Eqs. (15)-(16).  Run
#     math -script fig33_vecmeson.m
# after any change to the grid; the file is optional and simply omitted if
# absent.  Columns <channel>_vec and <channel>_novec, the latter being the
# script's own reproduction of `reference` and only a cross-check.
VECMESON_CSV = "fig33_vecmeson_scan_grid.csv"
VECMESON_KEY = "vec"

# Measured sigma(gamma p -> pi0 p), the points Fig. 33 itself shows.  Parsed by
# fig33_from_ufo.read_pi0p_data, which returns (Eg, sigma, err) for the two sets
# the file carries: `low` covers the Delta and is tabulated in W, `high` is the
# higher-resonance set.  Only the pi0p channel has data here; the other three
# are drawn without measurements.
#
# CAVEAT on the high set: its rows carry cos(theta) limits (-0.85 to 0.65/0.75),
# so it is an angle-RESTRICTED integral, not a full total cross section -- which
# is why it sits ~25% under the low set where the two overlap.  Both are plotted
# here because both are what Fig. 33 shows, but only the low set is strictly
# commensurate with the curves.
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                         'ELA-Pion-Photoproduction', 'pi0p_data.m')
DATA_CHANNEL = 'pi0p'
DATA_STYLE = {                       # set -> (label, marker, filled)
    'low':  (r'data, $\Delta$ region', 'o', True),
    'high': ('data, higher res.', '^', False),
}

# Figures stop where Fig. 33 does; the scan itself runs to 1.5 GeV and all of it
# is written to the csv.
XMAX_EG = 1.0
RATIO_LIM = (0.75, 1.25)

# 2x2 overview only: where the legend sits inside its panel, and the photon
# energy above which a panel is judged for headroom (just past the resonance --
# only what is under the legend corner matters).
LEGEND_BBOX = (0.99, 0.86)          # with loc='upper right', under the label
# with loc='upper left': right of the (a)/(b)/... tag, and high enough to clear
# the pi0 peak, which reaches ~0.76 of the shared axis
LEGEND_BBOX_LEFT = (0.10, 0.97)
LEGEND_EG_MIN = 0.35

SCAN_CSV = "scan_results.csv"
LEGACY_TXT = "beam_scan_pA_pPi0.txt"   # the pi0p subset, historical layout

PB_TO_UB = 1e-6

# === END CONFIGURATION ===


def nucleon_mass(param_card):
    """Nucleon mass actually used by the model, from its parameter card."""
    try:
        with open(param_card) as f:
            for line in f:
                if "# MNucleon" in line and not line.strip().startswith("#"):
                    return float(line.split()[1])
    except OSError:
        pass
    return MN_FALLBACK


def threshold(mn, mpi):
    """Lab photon energy at which gamma N -> pi N opens up."""
    return ((mn + mpi) ** 2 - mn ** 2) / (2 * mn)


def photon_grid(mn):
    """Dense across the Delta, coarse in the wings.

    One grid for every channel, starting at the pi0 threshold: the analytic
    curves use MPi0 throughout, and the charged channels drop the handful of
    points below their own (higher) threshold when they run.
    """
    e_thr = threshold(mn, MPI0)                              # 0.1447 GeV
    return np.unique(np.concatenate([
        np.arange(e_thr + 0.002, 0.20, 0.010),               # rise from threshold
        np.arange(0.200, 0.500, 0.005),                      # Delta(1232)
        np.arange(0.500, 0.800, 0.020),                      # falling edge
        np.arange(0.800, 1.501, 0.050),                      # tail
    ]).round(6))


def kinematics(egamma, mn):
    """(sqrt(s), corrected Egamma) for the template's head-on beam setup."""
    pz = np.sqrt(max(E_BEAM_NUCLEON ** 2 - mn ** 2, 0.0))
    s = mn ** 2 + 2.0 * egamma * (E_BEAM_NUCLEON + pz)
    return np.sqrt(s), (s - mn ** 2) / (2.0 * mn)


def eg_to_w(eg, mn):
    return np.sqrt(mn ** 2 + 2.0 * mn * np.asarray(eg))


# ------------------------------------------------------------------- running
def modify_yaml(template_path, output_path, ch, beam_energy, model, param_card):
    """Write the run card for one (channel, model, energy).

    Everything channel-dependent is substituted by line, so the template stays a
    valid stand-alone run card for gamma p -> p pi0.
    """
    with open(template_path) as f:
        content = f.read()
    content = content.replace("${BEAM_ENERGY}", str(beam_energy))
    content = re.sub(r"^MODEL:.*$", "MODEL: " + model, content, flags=re.M)
    content = re.sub(r"^UFO_PARAM_CARD:.*$", "UFO_PARAM_CARD: " + param_card,
                     content, flags=re.M)
    content = re.sub(r"^BEAMS:.*$", "BEAMS: [%d, 22]" % ch.beam,
                     content, flags=re.M)
    content = re.sub(r"^BEAM_ENERGIES:.*$",
                     "BEAM_ENERGIES: [%s, %s]" % (E_BEAM_NUCLEON, beam_energy),
                     content, flags=re.M)
    content, n = re.subn(r"^- \d+ 22 -> .*:[ \t]*$", "- %s:" % ch.process,
                         content, flags=re.M)
    if n != 1:
        raise RuntimeError(
            "%s: expected exactly one '- <pdg> 22 -> ...:' process line, found %d"
            % (template_path, n))
    graphs = "diagrams_" + ch.stem
    content = re.sub(r"^(\s*Print_Graphs:).*$", r"\1 " + graphs,
                     content, flags=re.M)
    os.makedirs(graphs, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(content)


def run_simulation(retries=1):
    """Run Sherpa on RUN_FILE, retrying a crash on the COLD Comix build.

    The two charged-pion channels segfault inside COMIX::Amplitude::GaugeTest
    the first time a process is built from scratch (empty Process/).  The
    crashed run still leaves its Process/Comix/<proc>.map behind, and the next
    invocation gets through -- and, checked at OUTPUT: 15, it genuinely REBUILDS
    the amplitude ('not pre-mapped') and RUNS the gauge test, which is satisfied
    to 4e-16.  So the retry is not hiding a bad amplitude: the numbers come from
    a build whose gauge invariance was verified.  It is a cold-build crash in
    Comix, worth reporting upstream, not a result to distrust.

    Only the first energy point of each (channel, model) pair is ever cold, so
    this fires at most once per pair.
    """
    for attempt in range(retries + 1):
        result = subprocess.run([EXECUTABLE, RUN_FILE],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.STDOUT)
        if result.returncode == 0:
            return
        if attempt == retries:
            raise RuntimeError(f"Sherpa failed with code {result.returncode}")
        print(f"\n    Sherpa exited with {result.returncode} on the cold Comix "
              "build; retrying against the cached process map", end="",
              flush=True)


def extract_results(zip_path):
    """Total cross section and its error, in pb, then delete the zip.

    The Statistics.dat is located by glob rather than by a hard-coded process
    name: Sherpa mangles the process into the directory name, and one run holds
    exactly one process here.

    Deleting the zip matters: Sherpa reuses a Results.zip it finds, so a
    leftover one would hand the next energy point the previous point's
    integration.
    """
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall("Results")
    hits = sorted(glob.glob(os.path.join("Results", "*", "*", "Statistics.dat")))
    if len(hits) != 1:
        shutil.rmtree("Results", ignore_errors=True)
        raise FileNotFoundError(
            "expected exactly one Statistics.dat in %s, found %d: %s"
            % (zip_path, len(hits), hits))
    with open(hits[0]) as f:
        last_line = f.readlines()[-1].strip().split()
    shutil.rmtree("Results", ignore_errors=True)
    os.remove(zip_path)
    return float(last_line[1]), float(last_line[2])


def scan_model(ch, model, param_card, energies, mn):
    """A Scan over `energies` for one channel and one model."""
    # A stale Process/ cache is keyed to the previous model and process and will
    # either be reused silently or come back as "No hard process found".
    shutil.rmtree("Process", ignore_errors=True)
    if os.path.exists(RESULTS_ZIP):
        os.remove(RESULTS_ZIP)

    run, sig, err = [], [], []
    for i, energy in enumerate(energies, 1):
        print(f"  [{i:3d}/{len(energies)}] {ch.key:5s} {model}  "
              f"Egamma = {energy:.4f} GeV", end="", flush=True)
        modify_yaml(TEMPLATE_FILE, RUN_FILE, ch, energy, model, param_card)
        run_simulation()
        xs, dxs = extract_results(RESULTS_ZIP)
        run.append(energy)
        sig.append(xs * PB_TO_UB)
        err.append(dxs * PB_TO_UB)
        print(f"   ->  {sig[-1]:9.2f} ub")
    run = np.array(run)
    return Scan(run, np.array([kinematics(e, mn)[1] for e in run]),
                np.array(sig), np.array(err))


def runnable(ch, energies, mn):
    """The grid points above this channel's own threshold.

    Compared against the CORRECTED photon energy, which is what actually sets
    sqrt(s), and kept a hair clear of the threshold itself so the integrator is
    never handed a vanishing phase space.
    """
    eg_corr = np.array([kinematics(e, mn)[1] for e in energies])
    return energies[eg_corr > threshold(mn, ch.mpi) + 1e-4]


# ------------------------------------------------------------- results on disk
# A scan result is a Scan: the beam energies that were run, the corrected
# photon energies those correspond to (what every figure and every semi-analytic
# curve is a function of), and sigma with its error in ub.
Scan = collections.namedtuple("Scan", "eg_beam eg_corr sigma err")


def write_scan_csv(results, mn, path=SCAN_CSV):
    """Long format: one row per (channel, model, energy).

    Long rather than wide because the channels do not share a grid -- the
    charged ones start a couple of points later -- and because a model or a
    channel can then be added without touching the layout.
    """
    with open(path, "w") as f:
        f.write("channel,process,model,Egamma_beam,sqrt_s,Egamma_corr,"
                "sigma_ub,err_ub\n")
        # Every model in `results`, not just this run's MODELS: results starts
        # from the existing file, and writing only MODELS used to drop the rows
        # of every other model on each run.
        listed = [m for m, *_ in MODELS]
        others = sorted({m for _, m in results} - set(listed))
        for key in CHANNELS:
            ch = CHANNELS[key]
            for model in listed + others:
                if (key, model) not in results:
                    continue
                r = results[(key, model)]
                for i, e in enumerate(r.eg_beam):
                    f.write("%s,%s,%s,%.6f,%.6f,%.6f,%.6f,%.6f\n"
                            % (key, ch.process, model, e, kinematics(e, mn)[0],
                               r.eg_corr[i], r.sigma[i], r.err[i]))
    print(f"wrote {path}")

    # The historical single-channel file, kept so anything that reads it still
    # works.  Only written when pi0p was scanned for every model on one grid.
    pi0p = [(m, results[(DATA_CHANNEL, m)]) for m, *_ in MODELS
            if (DATA_CHANNEL, m) in results]
    if len(pi0p) == len(MODELS) and all(
            np.array_equal(pi0p[0][1].eg_beam, r.eg_beam) for _, r in pi0p):
        eg = pi0p[0][1].eg_beam
        with open(LEGACY_TXT, "w") as f:
            f.write("# Egamma_beam[GeV]  sqrt_s[GeV]  Egamma_corr[GeV]  "
                    + "  ".join(f"sigma_{m}[ub]  err_{m}[ub]" for m, _ in pi0p)
                    + "\n")
            for i, e in enumerate(eg):
                w, ec = kinematics(e, mn)
                cols = [f"{e:.6f}", f"{w:.6f}", f"{ec:.6f}"]
                for _, r in pi0p:
                    cols += [f"{r.sigma[i]:.6f}", f"{r.err[i]:.6f}"]
                f.write("  ".join(cols) + "\n")
        print(f"wrote {LEGACY_TXT}")


def read_scan_csv(path=SCAN_CSV):
    """{(channel, model): Scan} from a previous run.

    Falls back to the historical pi0p txt if the csv is not there, so a scan
    made before this script grew the other three channels still replots.
    """
    out = {}
    if os.path.exists(path):
        rows = collections.defaultdict(list)
        with open(path) as f:
            head = f.readline().strip().split(",")
            idx = [head.index(c) for c in ("channel", "model", "Egamma_beam",
                                           "Egamma_corr", "sigma_ub", "err_ub")]
            for line in f:
                c = line.strip().split(",")
                if len(c) < len(head):
                    continue
                ic, im, *rest = idx
                rows[(c[ic], c[im])].append([float(c[j]) for j in rest])
        for k, v in rows.items():
            out[k] = Scan(*np.array(sorted(v)).T)
        print(f"{path}: " + ", ".join(
            f"{c}/{m} ({len(out[(c, m)].eg_beam)} pts)" for c, m in sorted(out)))
        return out

    if os.path.exists(LEGACY_TXT):
        d = np.loadtxt(LEGACY_TXT)
        with open(LEGACY_TXT) as f:
            names = [c[6:-4] for c in f.readline().split()
                     if c.startswith("sigma_")]
        for i, n in enumerate(names):
            out[(DATA_CHANNEL, n)] = Scan(d[:, 0], d[:, 2],
                                          d[:, 3 + 2 * i], d[:, 4 + 2 * i])
        print(f"{LEGACY_TXT}: {len(d)} pi0p points, models {', '.join(names)}")
        return out

    raise SystemExit(f"neither {path} nor {LEGACY_TXT} found -- run the scan "
                     "first (python3 scan.py)")


# Column names these caches used when they held gamma p -> p pi0 alone, so a
# file written before the other three channels existed still reads.
LEGACY_COLUMNS = {
    'reference': ('pi0p', 'reference'),
    'none': ('pi0p', 'none'),
    'vertexfix': ('pi0p', 'vertexfix'),
    'reference_vec': ('pi0p', 'vec'),
    'reference_novec': ('pi0p', 'novec'),
}


def read_wide_csv(path, eg_corr):
    """{(channel, name): array} from a csv whose first column is Egamma_corr.

    Columns are <channel>_<name>, with LEGACY_COLUMNS covering the older
    single-channel headers.  A file computed for a different grid is dropped
    rather than interpolated: the caches sit on exactly the scan points.
    """
    if not os.path.exists(path):
        return {}
    d = np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)
    with open(path) as f:
        names = [n.strip().strip('"') for n in f.readline().strip().split(",")[1:]]
    if d.shape[0] != len(eg_corr) or not np.allclose(d[:, 0], eg_corr, atol=1e-6):
        print(f"note: {path} is for a different grid -- ignored")
        return {}
    out = {}
    for i, n in enumerate(names):
        key, _, rest = n.partition("_")
        if key in CHANNELS and rest:
            out[(key, rest)] = d[:, i + 1]
        elif n in LEGACY_COLUMNS:
            out[LEGACY_COLUMNS[n]] = d[:, i + 1]
        else:
            print(f"note: {path}: ignoring unrecognised column {n!r}")
    return out


def write_wide_csv(path, eg_corr, cols):
    """cols is {(channel, name): array}, written as <channel>_<name>."""
    keys = [k for k in sorted(cols, key=lambda k: (list(CHANNELS).index(k[0])
                                                   if k[0] in CHANNELS else 99,
                                                   k[1]))]
    with open(path, "w") as f:
        f.write("Egamma_corr," + ",".join("%s_%s" % k for k in keys) + "\n")
        for i, e in enumerate(eg_corr):
            f.write(",".join([f"{e:.6f}"]
                             + [f"{cols[k][i]:.6f}" for k in keys]) + "\n")
    print(f"wrote {path}")


# -------------------------------------------------------- semi-analytic curves
def reference_curves(eg_corr, mn, channels):
    """{(channel, scheme): sigma_ub} on the scan grid, from fig33_from_ufo.py.

    Evaluated at the CORRECTED photon energies, i.e. at exactly the sqrt(s) of
    the Sherpa points, so the ratios need no interpolation.  Cached, and only
    the missing (channel, scheme) pairs are computed -- adding a channel does
    not re-run the ones already in the file.
    """
    have = read_wide_csv(REFERENCE_CACHE, eg_corr)
    want = [(c, s) for c in channels for s in SCHEMES]
    todo = [k for k in want if k not in have]
    if not todo:
        print(f"reference curves: {REFERENCE_CACHE}")
        return have
    if have:
        print(f"reference curves: {REFERENCE_CACHE} is missing "
              + ", ".join("%s/%s" % k for k in todo))

    try:
        import fig33_from_ufo as F
        import compare_delta_ff as C
    except ImportError as exc:
        print(f"note: cannot compute reference curves ({exc})")
        return have

    print(f"computing {len(todo)} reference curves on the scan grid "
          "(a few minutes) ...")
    Pa, Va = F.load_ufo(MODELS[0][0])
    na = F.parameter_namespace(Pa)
    Pb, Vb = F.load_ufo(MODELS[1][0])
    nb = F.parameter_namespace(Pb)
    base = dict(born=True, delta=True, ff=True)
    schemes = {
        # the Fig. 33 recipe: sqrt(X_pi(s,u)) at amplitude level, running width
        "reference": (Va, na, C.NUCFF, dict(base, edw=True)),
        # what each Sherpa model should reproduce: fixed width, form factor
        # either absent or supplied by the vertex
        "none":      (Vb, nb, C.deltaff(nb, False), dict(base, edw=False)),
        "vertexfix": (Vb, nb, C.deltaff(nb, True), dict(base, edw=False)),
    }
    for ch, name in todo:
        V, ns, ff0, opt = schemes[name]
        have[(ch, name)] = np.array([
            F.sigma_tot(ch, np.sqrt(mn ** 2 + 2 * mn * e),
                        V, ns, ff0, opt).real for e in eg_corr])
        print(f"  {ch} {name} done", flush=True)

    write_wide_csv(REFERENCE_CACHE, eg_corr, have)
    return have


def vecmeson_curves(eg_corr):
    """{(channel, 'vec'|'novec'): sigma_ub} on the scan grid, or {}."""
    if not os.path.exists(VECMESON_CSV):
        print(f"note: {VECMESON_CSV} not found -- no vector-meson curves "
              "(make it with: math -script fig33_vecmeson.m)")
        return {}
    return read_wide_csv(VECMESON_CSV, eg_corr)


def measured_data(channel):
    """{'low'|'high': (Eg, sigma_ub, err)} -- the points plotted in Fig. 33."""
    if channel != DATA_CHANNEL:
        return {}
    try:
        import fig33_from_ufo as F
        low, high = F.read_pi0p_data(DATA_FILE, MN_FALLBACK)
    except Exception as exc:
        print(f"note: no measured data ({exc})")
        return {}
    if low is None:
        print(f"note: {DATA_FILE} not found -- no measured data")
        return {}
    return {'low': low, 'high': high}


# -------------------------------------------------------------------- figures
def _journal_style():
    """PRC/PRD conventions: serif face, inward ticks all round, hairline axes."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['STIXGeneral', 'DejaVu Serif'],
        'mathtext.fontset': 'stix',
        'font.size': 9, 'axes.labelsize': 9,
        'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 7.5,
        'axes.linewidth': 0.7,
        'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'xtick.major.width': 0.7, 'ytick.major.width': 0.7,
        'xtick.minor.width': 0.5, 'ytick.minor.width': 0.5,
        'xtick.major.size': 3.4, 'ytick.major.size': 3.4,
        'xtick.minor.size': 1.9, 'ytick.minor.size': 1.9,
        'legend.frameon': False, 'legend.handlelength': 2.4,
        'legend.labelspacing': 0.35, 'legend.borderpad': 0.0,
        'savefig.bbox': 'tight', 'savefig.pad_inches': 0.02,
    })


INK = '#111111'


def _draw_channel(ax, rx, ch, eg_grid, scans, refs, x_of_eg, data=()):
    """Everything belonging to one channel, on a sigma axis and a ratio axis.

    `eg_grid` is the corrected photon energy the semi-analytic curves live on;
    `x_of_eg` maps a corrected photon energy onto the figure's abscissa (the
    identity, or Eg -> sqrt(s)).  The Sherpa points carry their own corrected
    energies, a SUBSET of eg_grid for the charged channels, so ratios look the
    denominator up rather than dividing elementwise.  `rx` may be None, in which
    case no ratio panel is drawn.
    """
    xgrid = x_of_eg(eg_grid)
    den = refs.get((ch.key, DENOMINATOR))

    def ratio_at(eg):
        return np.interp(eg, eg_grid, den, left=np.nan, right=np.nan)

    def inside(r):
        return (r >= RATIO_LIM[0]) & (r <= RATIO_LIM[1])

    if den is not None:
        ax.plot(xgrid, den, color=INK, ls='-', lw=1.3, zorder=4,
                solid_joinstyle='round')
        if rx is not None:
            rx.axhline(1.0, color=INK, ls='-', lw=0.9, zorder=2)

    vec = refs.get((ch.key, VECMESON_KEY))
    if vec is not None:
        ax.plot(xgrid, vec, color=INK, ls=(0, (5.0, 2.0)), lw=1.1, zorder=4)
        if den is not None and rx is not None:
            r = vec / den
            rx.plot(xgrid, np.where(inside(r), r, np.nan), color=INK,
                    ls=(0, (5.0, 2.0)), lw=1.1, zorder=3)

    # Measured points, drawn first so the curves read on top of them.
    for name, (label, marker, filled) in DATA_STYLE.items():
        if name not in data:
            continue
        eg, sig, err = data[name].T
        kw = dict(ls='none', marker=marker, ms=2.6 if filled else 3.0,
                  mfc=INK if filled else 'none', mec=INK, mew=0.7,
                  ecolor=INK, elinewidth=0.5, capsize=0, zorder=2)
        ax.errorbar(x_of_eg(eg), sig, yerr=err, **kw)
        if den is not None and rx is not None:
            r, dr = sig / ratio_at(eg), err / ratio_at(eg)
            m = inside(r)
            rx.errorbar(x_of_eg(eg)[m], r[m], yerr=dr[m], **kw)

    for model, card, label, scheme, colour, ls, marker in MODELS:
        curve = refs.get((ch.key, scheme))
        sc = scans.get((ch.key, model))
        if curve is not None:
            ax.plot(xgrid, curve, color=colour, ls=ls, lw=1.1, zorder=3)
        if sc is not None:
            ax.errorbar(x_of_eg(sc.eg_corr), sc.sigma, yerr=sc.err, ls='none',
                        marker=marker, ms=2.8,
                        mfc=colour if marker == 'o' else 'none',
                        mec=colour, mew=0.7, ecolor=colour, elinewidth=0.6,
                        capsize=0, zorder=5)
        if den is None or rx is None:
            continue
        if sc is not None:
            r = sc.sigma / ratio_at(sc.eg_corr)
            m = inside(r)
            rx.plot(x_of_eg(sc.eg_corr)[m], r[m], ls='none', marker=marker,
                    ms=2.8, mfc=colour if marker == 'o' else 'none', mec=colour,
                    mew=0.7, zorder=5)
        if curve is not None:
            r = curve / den
            rx.plot(xgrid, np.where(inside(r), r, np.nan), color=colour, ls=ls,
                    lw=1.1, zorder=3)


def _curve_legend(ax, ch, scans, refs, loc='upper right', bbox=None):
    """Names the semi-analytic curves and the two Sherpa models.

    `bbox` (axes fraction) lets a caller tuck the box under a panel label
    instead of into the corner it occupies.
    """
    handles = []
    if (ch.key, DENOMINATOR) in refs:
        handles.append(Line2D([], [], color=INK, ls='-', lw=1.3,
                              label=REFERENCE_LABEL))
    if (ch.key, VECMESON_KEY) in refs:
        handles.append(Line2D([], [], color=INK, ls=(0, (5.0, 2.0)), lw=1.1,
                              label=r'  $+\ \omega,\rho$ exchange'))
    handles += [Line2D([], [], color=c, ls=ls, lw=1.1, marker=m, ms=2.8,
                       mfc=c if m == 'o' else 'none', mec=c, mew=0.7, label=lab)
                for mo, _, lab, sch, c, ls, m in MODELS
                if (ch.key, mo) in scans or (ch.key, sch) in refs]
    if not handles:
        return None
    leg = ax.legend(handles=handles, loc=loc, bbox_to_anchor=bbox,
                    borderaxespad=0.7, title=LEGEND_TITLE)
    leg.get_title().set(fontsize=7, color='0.35')
    return leg


def _data_legend(ax, data, keep=None, loc='upper left', bbox=None):
    """Names the measured sets.  `keep` is a legend already on this axis."""
    dh = [Line2D([], [], ls='none', marker=m, ms=2.8 if f else 3.2,
                 mfc=INK if f else 'none', mec=INK, mew=0.7, label=lab)
          for k, (lab, m, f) in DATA_STYLE.items() if k in data]
    if not dh:
        return
    if keep is not None:
        ax.add_artist(keep)
    ax.legend(handles=dh, loc=loc, bbox_to_anchor=bbox, borderaxespad=0.7)


def _headroom(key, eg_grid, scans, refs, eg_min):
    """Tallest thing drawn for `key` above eg_min -- i.e. under a corner legend.

    Used to pick which panel of the overview hosts the legend: the corner has to
    clear the curves, and on a shared y-scale the channels differ a lot in how
    high they run out to the right of the resonance.
    """
    top = [np.nanmax(refs[(key, n)][eg_grid >= eg_min])
           for n in SCHEMES + (VECMESON_KEY,) if (key, n) in refs]
    top += [np.nanmax(scans[(key, m)].sigma[scans[(key, m)].eg_corr >= eg_min])
            for m, *_ in MODELS if (key, m) in scans
            and (scans[(key, m)].eg_corr >= eg_min).any()]
    return max(top) if top else 0.0


def make_figure(ch, eg_grid, xlabel, xlim, scans, refs, stem, x_of_eg,
                data=(), mark_delta=False):
    """One publication figure: sigma on top, ratio to Fig. 33 below.

    Anything outside the ratio window is simply not drawn -- no off-scale
    markers on the frame.
    """
    _journal_style()
    fig, (ax, rx) = plt.subplots(
        2, 1, figsize=(3.5, 4.1), sharex=True,
        gridspec_kw=dict(height_ratios=[2.5, 1.0], hspace=0.06))

    _draw_channel(ax, rx, ch, eg_grid, scans, refs, x_of_eg, data)
    _data_legend(ax, data, keep=_curve_legend(ax, ch, scans, refs))

    if mark_delta:
        for a in (ax, rx):
            a.axvline(MDELTA, color='0.75', lw=0.7, ls=':', zorder=0)
        # low, not high: the upper-left corner belongs to the data legend
        ax.annotate(r'$M_\Delta$', (MDELTA, 0.02),
                    xycoords=('data', 'axes fraction'), ha='left', va='bottom',
                    fontsize=8, color='0.45', xytext=(2.5, 0),
                    textcoords='offset points')

    ax.set_ylabel(r'$\sigma(%s)$  ($\mu$b)' % ch.label)
    ax.set_ylim(0, ch.ymax)
    ax.set_yticks(np.arange(0, ch.ymax - 50, 100))
    rx.set_ylabel(RATIO_LABEL)
    rx.set_ylim(*RATIO_LIM)
    rx.set_yticks([0.8, 0.9, 1.0, 1.1, 1.2])
    rx.set_xlabel(xlabel)
    rx.set_xlim(*xlim)

    for ext in ('pdf', 'png'):
        fig.savefig(f'{stem}.{ext}', dpi=600)
    plt.close(fig)
    print(f"wrote {stem}.pdf and {stem}.png")


def make_overview(channels, eg_corr, scans, refs, stem='scan_all_channels'):
    """All four channels on one 2x2 sheet, in the layout of Fig. 33 itself."""
    _journal_style()
    order = ['pi-p', 'pi+n', 'pi0p', 'pi0n']            # Fig. 33's own order
    order = [k for k in order if k in channels]
    ymax = max(CHANNELS[k].ymax for k in order)
    ncol = 2 if len(order) > 1 else 1
    nrow = int(np.ceil(len(order) / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(7.0, 2.5 * nrow + 0.1),
                             sharex=True, sharey=True, squeeze=False)
    panel = ['(a)', '(b)', '(c)', '(d)']

    panel_ax = {}
    for n, (ax, key) in enumerate(zip(axes.ravel(), order)):
        ch = CHANNELS[key]
        panel_ax[key] = ax
        _draw_channel(ax, None, ch, eg_corr, scans, refs, np.asarray,
                      measured_data(key))
        ax.set_xlim(0.10, XMAX_EG)
        ax.set_ylim(0, ymax)
        ax.set_yticks(np.arange(0, ymax - 50, 100))
        ax.text(0.035, 0.93, panel[n], transform=ax.transAxes, va='top',
                fontsize=8.5)
        ax.text(0.965, 0.93, r'$%s$' % ch.label, transform=ax.transAxes,
                va='top', ha='right', fontsize=11)
        if n // ncol == nrow - 1:
            ax.set_xlabel(r'$E_{\gamma}$  (GeV)')
        if n % ncol == 0:
            ax.set_ylabel(r'$\sigma$  ($\mu$b)')
    for ax in axes.ravel()[len(order):]:
        ax.set_visible(False)

    # The legend is a whole panel's worth of text, so it goes where there is
    # actually room: the channel that runs lowest to the right of the
    # resonance, and anchored below that panel's channel label rather than in
    # the corner the label already holds.
    host = min(order, key=lambda k: _headroom(k, eg_corr, scans, refs,
                                              LEGEND_EG_MIN))
    _curve_legend(panel_ax[host], CHANNELS[host], scans, refs,
                  bbox=LEGEND_BBOX)
    # The measured points are pi0p's alone, so their key belongs on that panel.
    if DATA_CHANNEL in panel_ax:
        _data_legend(panel_ax[DATA_CHANNEL], measured_data(DATA_CHANNEL),
                     bbox=LEGEND_BBOX_LEFT, loc='upper left')
    fig.subplots_adjust(hspace=0.06, wspace=0.06)
    for ext in ('pdf', 'png'):
        fig.savefig(f'{stem}.{ext}', dpi=600)
    plt.close(fig)
    print(f"wrote {stem}.pdf and {stem}.png")


# -------------------------------------------------------------------- summary
def summary(channels, eg_corr, w_beam, scans, refs, mn):
    """Peak of every curve in the window, then the ratios to `reference`."""
    win = eg_corr <= XMAX_EG
    print("\n%-6s %-22s %10s %10s %12s   (Delta region)"
          % ("chan", "curve", "peak (ub)", "at Eg", "at sqrt(s)"))
    for key in channels:
        for model, *_ in MODELS:
            sc = scans.get((key, model))
            if sc is None:
                continue
            i = int(np.argmax(np.where(sc.eg_corr <= XMAX_EG, sc.sigma, -np.inf)))
            print("%-6s %-22s %10.1f %10.4f %12.4f"
                  % (key, model, sc.sigma[i], sc.eg_corr[i],
                     eg_to_w(sc.eg_corr[i], mn)))
        for name in SCHEMES + (VECMESON_KEY,):
            sig = refs.get((key, name))
            if sig is None:
                continue
            i = int(np.argmax(np.where(win, sig, -np.inf)))
            print("%-6s %-22s %10.1f %10.4f %12.4f"
                  % (key, name, sig[i], eg_corr[i], w_beam[i]))
        print()

    print("%-6s %-22s %12s %12s" % ("chan", "ratio to Born+Delta", "at peak",
                                    "worst in window"))
    for key in channels:
        den = refs.get((key, DENOMINATOR))
        if den is None:
            continue
        e_peak = eg_corr[int(np.argmax(np.where(win, den, -np.inf)))]
        for model, *_ in MODELS:
            sc = scans.get((key, model))
            if sc is None:
                continue
            r = sc.sigma / np.interp(sc.eg_corr, eg_corr, den)
            ipk = int(np.argmin(np.abs(sc.eg_corr - e_peak)))
            w = sc.eg_corr <= XMAX_EG
            iw = int(np.argmax(np.abs(r[w] - 1.0)))
            print("%-6s %-22s %12.3f %12.3f" % (key, model, r[ipk], r[w][iw]))


def main():
    ap = argparse.ArgumentParser(
        description="Photon-energy scan of gamma N -> pi N through Sherpa, "
                    "against the Fig. 33 curves of nucl-th/0509020v2.")
    ap.add_argument("--channels", default=",".join(CHANNELS),
                    help="comma-separated subset of " + ", ".join(CHANNELS))
    ap.add_argument("--plot-only", action="store_true",
                    help="redraw from %s (or %s); run no simulation"
                         % (SCAN_CSV, LEGACY_TXT))
    ap.add_argument("--no-plot", action="store_true",
                    help="scan and write the csv, draw nothing")
    args = ap.parse_args()

    channels = [c.strip() for c in args.channels.split(",") if c.strip()]
    bad = [c for c in channels if c not in CHANNELS]
    if bad:
        raise SystemExit("unknown channel(s): %s;  known: %s"
                         % (", ".join(bad), ", ".join(CHANNELS)))

    mn = nucleon_mass(MODELS[0][1])
    energies = photon_grid(mn)
    w_beam, eg_corr = np.transpose([kinematics(e, mn) for e in energies])

    if args.plot_only:
        scans = read_scan_csv()
    else:
        print(f"M_N = {mn} GeV,  {len(energies)} photon energies "
              f"({energies[0]:.4f} - {energies[-1]:.3f} GeV)")
        print("correction factor Egamma_corr/Egamma = "
              f"{eg_corr[0]/energies[0]:.6f}")
        print("channels: " + ", ".join(channels) + "\n")
        scans = read_scan_csv() if os.path.exists(SCAN_CSV) else {}
        for key in channels:
            ch = CHANNELS[key]
            egs = runnable(ch, energies, mn)
            if len(egs) < len(energies):
                print(f"{key}: {len(energies) - len(egs)} grid point(s) below "
                      f"the m_pi = {ch.mpi} GeV threshold, not run")
            for model, card, *_ in MODELS:
                if not os.path.isdir(model):
                    print(f"skipping {model}: directory not found")
                    continue
                print(f"scanning {key}  ({ch.process})  with {model}")
                scans[(key, model)] = scan_model(ch, model, card, egs, mn)
                # Rewritten after every pair: an interrupted scan keeps
                # everything that had already finished.
                write_scan_csv(scans, mn)

    if args.no_plot:
        return

    refs = reference_curves(eg_corr, mn, channels)
    refs.update(vecmeson_curves(eg_corr))

    for key in channels:
        ch = CHANNELS[key]
        data = measured_data(key)
        make_figure(ch, eg_corr, r'$\sqrt{s}$  (GeV)',
                    (mn + MPI0, eg_to_w(XMAX_EG, mn)), scans, refs,
                    f'scan_{ch.stem}_sqrts',
                    x_of_eg=lambda eg: eg_to_w(eg, mn), data=data,
                    mark_delta=True)
        make_figure(ch, eg_corr, r'$E_{\gamma}$  (GeV)', (0.10, XMAX_EG),
                    scans, refs, f'scan_{ch.stem}_Egamma',
                    x_of_eg=np.asarray, data=data)
    if len(channels) > 1:
        make_overview(channels, eg_corr, scans, refs)

    summary(channels, eg_corr, w_beam, scans, refs, mn)


if __name__ == "__main__":
    main()
