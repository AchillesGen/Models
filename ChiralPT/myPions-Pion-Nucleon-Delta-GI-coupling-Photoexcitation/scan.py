"""
scan.py -- photon-energy scan of sigma(gamma p -> p pi0) through Sherpa.

Plots against sqrt(s) and against the CORRECTED photon energy, so the result can
be laid on top of Fig. 33 of nucl-th/0509020v2 directly.

WHY THE PHOTON ENERGY NEEDS CORRECTING.  BEAM_ENERGIES sets the beam ENERGY, not
its momentum, and the template gives the proton E = 0.938273 GeV against a mass
of 0.938272 GeV.  The target therefore is not at rest: it keeps

    pz = sqrt(E^2 - M^2) = 1.37 MeV

of residual momentum, and the two beams collide head-on, so

    s = M^2 + 2 Egamma (E_beam + pz)

rather than the fixed-target M^2 + 2 M Egamma.  Fig. 33's abscissa is the lab
photon energy on a nucleon AT REST, which is

    Egamma_corr = (s - M^2) / (2 M) = Egamma (E_beam + pz) / M

i.e. 0.15% above the number in the run card -- half an MeV at the peak.  The old
version of this script plotted `Egamma + M`, which is the total lab energy, not
an invariant, and is not what either axis of Fig. 33 means.

Sampling is dense across the Delta(1232): the resonance sits at
Egamma = (M_Delta^2 - M^2)/(2M) = 0.310 GeV and is ~100 MeV wide, so a uniform
grid over 0.15-1.5 GeV puts only a couple of points on the peak.

Run:  python3 scan.py
"""

import os
import re
import shutil
import subprocess
import sys
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
RESULTS_TXT_PATH = "Comix/MC_2_2__p__A__p__Pi0/Statistics.dat"
TEMPLATE_FILE = "Sherpa_ChiPT_Template.yaml"
RUN_FILE = "Sherpa_ChiPT.yaml"

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

# Semi-analytic curves, computed on the scan grid with the Fig33v2.m machinery
# (validated against nucl-th/0509020v2 Appendix A) through fig33_from_ufo.py.
# `reference` is the Fig. 33 prescription itself and is the ratio denominator.
REFERENCE_CACHE = "fig33_reference_scan_grid.csv"
REFERENCE_CHANNEL = "pi0p"

# Born + Delta + t-channel omega/rho, on the same grid, from fig33_vecmeson.m.
# ChiPT.fr has no vector mesons, so this one cannot come from the UFO: the
# couplings are the ELA fit values of nucl-th/0509020v2 Eqs. (15)-(16).  Run
#     math -script fig33_vecmeson.m
# after any change to the grid; the file is optional and simply omitted if absent.
VECMESON_CSV = "fig33_vecmeson_scan_grid.csv"
VECMESON_KEY = "reference_vec"
DENOMINATOR = "reference"

# Measured sigma(gamma p -> pi0 p), the points Fig. 33 itself shows.  Parsed by
# fig33_from_ufo.read_pi0p_data, which returns (Eg, sigma, err) for the two sets
# the file carries: `low` covers the Delta and is tabulated in W, `high` is the
# higher-resonance set.
#
# CAVEAT on the high set: its rows carry cos(theta) limits (-0.85 to 0.65/0.75),
# so it is an angle-RESTRICTED integral, not a full total cross section -- which
# is why it sits ~25% under the low set where the two overlap.  Both are plotted
# here because both are what Fig. 33 shows, but only the low set is strictly
# commensurate with the curves.
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                         'ELA-Pion-Photoproduction', 'pi0p_data.m')
DATA_STYLE = {                       # set -> (label, marker, filled)
    'low':  (r'data, $\Delta$ region', 'o', True),
    'high': ('data, higher res.', '^', False),
}

# Figures stop where Fig. 33 does; the scan itself runs to 1.5 GeV and all of it
# is written to the txt.
XMAX_EG = 1.0
YMAX_SIGMA = 500
RATIO_LIM = (0.75, 1.25)

E_BEAM_PROTON = 0.938273     # BEAM_ENERGIES[0] in the template
MN_FALLBACK = 0.938272
MPI0 = 0.1349768
MDELTA = 1.209

PB_TO_UB = 1e-6

# === END CONFIGURATION ===


def nucleon_mass(param_card):
    """Proton mass actually used by the model, from its parameter card."""
    try:
        with open(param_card) as f:
            for line in f:
                if "# MNucleon" in line and not line.strip().startswith("#"):
                    return float(line.split()[1])
    except OSError:
        pass
    return MN_FALLBACK


def photon_grid(mn):
    """Dense across the Delta, coarse in the wings."""
    e_thr = ((mn + MPI0) ** 2 - mn ** 2) / (2 * mn)          # 0.1447 GeV
    return np.unique(np.concatenate([
        np.arange(e_thr + 0.002, 0.20, 0.010),               # rise from threshold
        np.arange(0.200, 0.500, 0.005),                      # Delta(1232)
        np.arange(0.500, 0.800, 0.020),                      # falling edge
        np.arange(0.800, 1.501, 0.050),                      # tail
    ]).round(6))


def kinematics(egamma, mn):
    """(sqrt(s), corrected Egamma) for the template's head-on beam setup."""
    pz = np.sqrt(max(E_BEAM_PROTON ** 2 - mn ** 2, 0.0))
    s = mn ** 2 + 2.0 * egamma * (E_BEAM_PROTON + pz)
    return np.sqrt(s), (s - mn ** 2) / (2.0 * mn)


def eg_to_w(eg, mn):
    return np.sqrt(mn ** 2 + 2.0 * mn * np.asarray(eg))


def modify_yaml(template_path, output_path, beam_energy, model, param_card):
    with open(template_path) as f:
        content = f.read()
    content = content.replace("${BEAM_ENERGY}", str(beam_energy))
    content = re.sub(r"^MODEL:.*$", "MODEL: " + model, content, flags=re.M)
    content = re.sub(r"^UFO_PARAM_CARD:.*$", "UFO_PARAM_CARD: " + param_card,
                     content, flags=re.M)
    with open(output_path, "w") as f:
        f.write(content)


def run_simulation():
    result = subprocess.run([EXECUTABLE, RUN_FILE],
                            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        raise RuntimeError(f"Sherpa failed with code {result.returncode}")


def extract_results(zip_path, txt_path):
    """Total cross section and its error, in pb, then delete the zip.

    Deleting it matters: Sherpa reuses a Results.zip it finds, so a leftover one
    would hand the next energy point the previous point's integration.
    """
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall("Results")
    data_file = os.path.join("Results", txt_path)
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"Expected file not found: {data_file}")
    with open(data_file) as f:
        last_line = f.readlines()[-1].strip().split()
    shutil.rmtree("Results", ignore_errors=True)
    os.remove(zip_path)
    return float(last_line[1]), float(last_line[2])


def scan_model(model, param_card, energies):
    """sigma(Egamma) in ub for one model."""
    # A stale Process/ cache is keyed to the previous model and will either be
    # reused silently or come back as "No hard process found".
    shutil.rmtree("Process", ignore_errors=True)
    if os.path.exists(RESULTS_ZIP):
        os.remove(RESULTS_ZIP)

    sig, err = [], []
    for i, energy in enumerate(energies, 1):
        print(f"  [{i:3d}/{len(energies)}] {model}  Egamma = {energy:.4f} GeV",
              end="", flush=True)
        modify_yaml(TEMPLATE_FILE, RUN_FILE, energy, model, param_card)
        run_simulation()
        xs, dxs = extract_results(RESULTS_ZIP, RESULTS_TXT_PATH)
        sig.append(xs * PB_TO_UB)
        err.append(dxs * PB_TO_UB)
        print(f"   ->  {sig[-1]:9.2f} ub")
    return np.array(sig), np.array(err)


def reference_curves(eg_corr, mn):
    """{scheme: sigma_ub} on the scan grid, from the Fig33v2.m machinery.

    Evaluated at the CORRECTED photon energies, i.e. at exactly the sqrt(s) of
    the Sherpa points, so the ratios need no interpolation.  Cached, because it
    costs a couple of minutes and never changes for a given grid.
    """
    if os.path.exists(REFERENCE_CACHE):
        cached = np.loadtxt(REFERENCE_CACHE, delimiter=",", skiprows=1)
        with open(REFERENCE_CACHE) as f:
            names = f.readline().strip().split(",")[1:]
        if cached.shape[0] == len(eg_corr) and np.allclose(cached[:, 0], eg_corr):
            print(f"reference curves: {REFERENCE_CACHE}")
            return {n: cached[:, i + 1] for i, n in enumerate(names)}
        print(f"reference curves: {REFERENCE_CACHE} is for a different grid, "
              "recomputing")

    try:
        import fig33_from_ufo as F
        import compare_delta_ff as C
    except ImportError as exc:
        print(f"note: cannot compute reference curves ({exc})")
        return {}

    print("computing reference curves on the scan grid (a few minutes) ...")
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
    out = {}
    for name, (V, ns, ff0, opt) in schemes.items():
        out[name] = np.array([
            F.sigma_tot(REFERENCE_CHANNEL, np.sqrt(mn ** 2 + 2 * mn * e),
                        V, ns, ff0, opt).real for e in eg_corr])
        print(f"  {name} done")

    with open(REFERENCE_CACHE, "w") as f:
        f.write("Egamma_corr," + ",".join(out) + "\n")
        for i, e in enumerate(eg_corr):
            f.write(",".join([f"{e:.6f}"] + [f"{out[k][i]:.6f}" for k in out]) + "\n")
    return out


def vecmeson_curve(eg_corr):
    """Born + Delta + omega/rho on the scan grid, or None."""
    if not os.path.exists(VECMESON_CSV):
        print(f"note: {VECMESON_CSV} not found -- no vector-meson curve "
              "(make it with: math -script fig33_vecmeson.m)")
        return None
    d = np.loadtxt(VECMESON_CSV, delimiter=",", skiprows=1)
    if d.shape[0] != len(eg_corr) or not np.allclose(d[:, 0], eg_corr, atol=1e-6):
        print(f"note: {VECMESON_CSV} is for a different grid -- ignored")
        return None
    return d[:, 1]


def measured_data():
    """{'low'|'high': (Eg, sigma_ub, err)} -- the points plotted in Fig. 33."""
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


def make_figure(x, xlabel, xlim, scans, refs, stem, eg_grid, data=(), xof=None,
                mark_delta=False):
    """One publication figure: sigma on top, ratio to Fig. 33 below.

    Anything outside the ratio window is simply not drawn -- no off-scale
    markers on the frame.
    """
    _journal_style()
    INK = '#111111'
    fig, (ax, rx) = plt.subplots(
        2, 1, figsize=(3.5, 4.1), sharex=True,
        gridspec_kw=dict(height_ratios=[2.5, 1.0], hspace=0.06))

    den = refs.get(DENOMINATOR)
    if den is not None:
        ax.plot(x, den, color=INK, ls='-', lw=1.3, zorder=4,
                solid_joinstyle='round')
        rx.axhline(1.0, color=INK, ls='-', lw=0.9, zorder=2)

    vec = refs.get(VECMESON_KEY)
    if vec is not None:
        ax.plot(x, vec, color=INK, ls=(0, (5.0, 2.0)), lw=1.1, zorder=4)
        if den is not None:
            r = vec / den
            inside = (r >= RATIO_LIM[0]) & (r <= RATIO_LIM[1])
            rx.plot(x, np.where(inside, r, np.nan), color=INK,
                    ls=(0, (5.0, 2.0)), lw=1.1, zorder=3)

    # Measured points, drawn first so the curves read on top of them.
    for name, (label, marker, filled) in DATA_STYLE.items():
        if name not in data:
            continue
        eg, sig, err = data[name].T
        xd = eg if xof is None else xof(eg)
        kw = dict(ls='none', marker=marker, ms=2.6 if filled else 3.0,
                  mfc=INK if filled else 'none', mec=INK, mew=0.7,
                  ecolor=INK, elinewidth=0.5, capsize=0, zorder=2)
        ax.errorbar(xd, sig, yerr=err, **kw)
        if den is not None:
            ref_at = np.interp(eg, eg_grid, den, left=np.nan, right=np.nan)
            r, dr = sig / ref_at, err / ref_at
            inside = (r >= RATIO_LIM[0]) & (r <= RATIO_LIM[1])
            rx.errorbar(xd[inside], r[inside], yerr=dr[inside], **kw)

    for model, card, label, scheme, colour, ls, marker in MODELS:
        if model not in scans:
            continue
        sig, err = scans[model]
        if scheme in refs:
            ax.plot(x, refs[scheme], color=colour, ls=ls, lw=1.1, zorder=3)
        ax.errorbar(x, sig, yerr=err, ls='none', marker=marker, ms=2.8,
                    mfc=colour if marker == 'o' else 'none', mec=colour,
                    mew=0.7, ecolor=colour, elinewidth=0.6, capsize=0, zorder=5)
        if den is None:
            continue
        for values, kw in ((sig, dict(ls='none', marker=marker, ms=2.8,
                                      mfc=colour if marker == 'o' else 'none',
                                      mec=colour, mew=0.7, zorder=5)),
                           (refs.get(scheme), dict(ls=ls, lw=1.1, color=colour,
                                                   zorder=3))):
            if values is None:
                continue
            r = values / den
            inside = (r >= RATIO_LIM[0]) & (r <= RATIO_LIM[1])
            rx.plot(x, np.where(inside, r, np.nan), color=colour,
                    **{k: v for k, v in kw.items() if k != 'color'})

    if mark_delta:
        for a in (ax, rx):
            a.axvline(MDELTA, color='0.75', lw=0.7, ls=':', zorder=0)
        # low, not high: the upper-left corner belongs to the data legend
        ax.annotate(r'$M_\Delta$', (MDELTA, 0.02),
                    xycoords=('data', 'axes fraction'), ha='left', va='bottom',
                    fontsize=8, color='0.45', xytext=(2.5, 0),
                    textcoords='offset points')

    handles = [Line2D([], [], color=INK, ls='-', lw=1.3,
                      label='Fig. 33 prescription')]
    if vec is not None:
        handles.append(Line2D([], [], color=INK, ls=(0, (5.0, 2.0)), lw=1.1,
                              label=r'  $+\ \omega,\rho$ exchange'))
    handles += [Line2D([], [], color=c, ls=ls, lw=1.1, marker=m, ms=2.8,
                       mfc=c if m == 'o' else 'none', mec=c, mew=0.7, label=lab)
                for mo, _, lab, _, c, ls, m in MODELS if mo in scans]
    leg = ax.legend(handles=handles, loc='upper right', borderaxespad=0.7)
    dh = [Line2D([], [], ls='none', marker=m, ms=2.8 if f else 3.2,
                 mfc=INK if f else 'none', mec=INK, mew=0.7, label=lab)
          for k, (lab, m, f) in DATA_STYLE.items() if k in data]
    if dh:
        ax.add_artist(leg)
        ax.legend(handles=dh, loc='upper left', borderaxespad=0.7)
    # In the ratio panel: the top axes are full once the measured points are on.
    rx.text(0.985, 0.06, 'lines: semi-analytic,  markers: Sherpa',
            transform=rx.transAxes, va='bottom', ha='right', fontsize=7,
            color='0.35')

    ax.set_ylabel(r'$\sigma(\gamma p \to p\,\pi^{0})$  ($\mu$b)')
    ax.set_ylim(0, YMAX_SIGMA)
    ax.set_yticks(np.arange(0, 401, 100))
    rx.set_ylabel('ratio to Fig. 33')
    rx.set_ylim(*RATIO_LIM)
    rx.set_yticks([0.8, 0.9, 1.0, 1.1, 1.2])
    rx.set_xlabel(xlabel)
    rx.set_xlim(*xlim)

    for ext in ('pdf', 'png'):
        fig.savefig(f'{stem}.{ext}', dpi=600)
    plt.close(fig)
    print(f"wrote {stem}.pdf and {stem}.png")


SCAN_TXT = "beam_scan_pA_pPi0.txt"


def write_scan(energies, w_beam, eg_corr, scans):
    with open(SCAN_TXT, "w") as f:
        f.write("# Egamma_beam[GeV]  sqrt_s[GeV]  Egamma_corr[GeV]  "
                + "  ".join(f"sigma_{m}[ub]  err_{m}[ub]" for m in scans) + "\n")
        for i, e in enumerate(energies):
            cols = [f"{e:.6f}", f"{w_beam[i]:.6f}", f"{eg_corr[i]:.6f}"]
            for m in scans:
                cols += [f"{scans[m][0][i]:.6f}", f"{scans[m][1][i]:.6f}"]
            f.write("  ".join(cols) + "\n")


def read_scan():
    """Re-read a previous scan, for --plot-only."""
    d = np.loadtxt(SCAN_TXT)
    with open(SCAN_TXT) as f:
        names = [c[6:-4] for c in f.readline().split() if c.startswith("sigma_")]
    scans = {n: (d[:, 3 + 2 * i], d[:, 4 + 2 * i]) for i, n in enumerate(names)}
    return d[:, 0], d[:, 1], d[:, 2], scans


def main():
    plot_only = "--plot-only" in sys.argv
    mn = nucleon_mass(MODELS[0][1])

    if plot_only:
        energies, w_beam, eg_corr, scans = read_scan()
        print(f"re-plotting {len(energies)} points from {SCAN_TXT}")
    else:
        energies = photon_grid(mn)
        w_beam, eg_corr = np.transpose([kinematics(e, mn) for e in energies])
        print(f"M_N = {mn} GeV,  {len(energies)} photon energies "
              f"({energies[0]:.4f} - {energies[-1]:.3f} GeV)")
        print("correction factor Egamma_corr/Egamma = "
              f"{eg_corr[0]/energies[0]:.6f}\n")
        scans = {}
        for model, card, label, scheme, colour, ls, marker in MODELS:
            if not os.path.isdir(model):
                print(f"skipping {model}: directory not found")
                continue
            print(f"scanning {model}")
            scans[model] = scan_model(model, card, energies)
        write_scan(energies, w_beam, eg_corr, scans)

    refs = reference_curves(eg_corr, mn)
    vec = vecmeson_curve(eg_corr)
    if vec is not None:
        refs[VECMESON_KEY] = vec

    data = measured_data()

    make_figure(w_beam, r'$\sqrt{s}$  (GeV)',
                (mn + MPI0, eg_to_w(XMAX_EG, mn)), scans, refs,
                'scan_pA_pPi0_sqrts', eg_grid=eg_corr, data=data,
                xof=lambda eg: eg_to_w(eg, mn), mark_delta=True)
    make_figure(eg_corr, r'$E_{\gamma}$  (GeV)', (0.10, XMAX_EG),
                scans, refs, 'scan_pA_pPi0_Egamma', eg_grid=eg_corr, data=data)

    # ------------------------------------------------------------- summary
    win = eg_corr <= XMAX_EG
    print("\n%-22s %10s %10s %12s   (Delta region)"
          % ("curve", "peak (ub)", "at Eg", "at sqrt(s)"))
    curves = [(m, scans[m][0]) for m, *_ in MODELS if m in scans]
    curves += list(refs.items())
    for name, sig in curves:
        i = int(np.argmax(np.where(win, sig, -np.inf)))
        print("%-22s %10.1f %10.4f %12.4f" % (name, sig[i], eg_corr[i], w_beam[i]))

    den = refs.get(DENOMINATOR)
    if den is not None:
        print("\n%-22s %12s %12s" % ("ratio to Fig. 33", "at peak", "worst in window"))
        for model, card, label, scheme, *_ in MODELS:
            if model not in scans:
                continue
            r = scans[model][0] / den
            ipk = int(np.argmax(den))
            iw = int(np.argmax(np.abs(r[win] - 1.0)))
            print("%-22s %12.3f %12.3f" % (model, r[ipk], r[win][iw]))
    print(f"\nwrote {SCAN_TXT}")


if __name__ == "__main__":
    main()
