#!/usr/bin/env python3
"""run_w.py -- drive Sherpa over the CC single-pion channels on the ANL/BNL grid.

Laid out like scan.py: a channel table, a default energy grid, one Sherpa run
per (channel, model, energy, seed), and a long-format csv keyed by
(channel, model, param_card, E_nu, wcut) that is MERGED rather than appended, so
re-running a point overwrites it instead of leaving two rows behind.

    python3 run_w.py --wcut 1.4                      # all three channels
    python3 run_w.py --channels ppip --energies 0.875,1.25 --wcut 1.4
    python3 run_w.py --wcut 1.4 --outputs outputs -v  # keep cards + Sherpa logs

Writes w_scan_results.csv.  run_w_all.py is the runner that does the full
W < 1.4 GeV scan over every channel.

THE W_CUT BUG THIS SCRIPT USED TO HAVE.  Sherpa_ChiPT_W_Template.yaml carried a
hard-coded

    SELECTORS:
      - [Mass, 2212, 211, 0, 4]

and NO ${SELECTORS} placeholder, while write_card did s.replace("${SELECTORS}",
...).  The replace matched nothing, so --wcut never reached the card: every run
integrated with whatever upper limit happened to be typed into the template, and
on the two neutron-target channels it was cut on a (p, pi+) pair that is not
even in the final state.  That is why W < 1.4 and W < 5.0 came back identical to
six digits, and it is the real explanation for the "Sherpa's Mass selector is
inert for this process" claim in build_cc1pi_csv.py's header -- the selector was
never inert, it just never carried the requested number.  With the placeholder
in place, ppip at E_nu = 1.5 GeV gives 6.5608e-09 ub at W < 1.4 against
1.0123e-08 ub uncut, a 35% cut.  The selector works.

WHY THE W IS INTERNAL.  The natural weak analogue of gamma N -> pi N is
W N -> pi N with a W beam, and this card started life that way.  It cannot work:
the W is massive, so an on-shell W+ beam needs E >= MW = 80.94 GeV and every
point lands at sqrt(s) >= 81.9 GeV, decades above the Delta(1232) region the
model describes -- and Comix does not terminate there, it spins forever in
PS_Channel::TChannelBounds on the 80 GeV / 0.14 GeV mass hierarchy.  Exchanging
the W inside nu_mu N -> mu- N' pi reaches the resonance region with the same
weak vertices and needs no modified W mass.

The companion analytic calculation is wprod_from_ufo.py, which builds the same
amplitude out of the same UFO by hand and takes the same cut as --wmax.
"""

import argparse
import collections
import glob
import os
import re
import shutil
import subprocess
import sys
import threading
import zipfile

# === USER CONFIGURATION ===
EXECUTABLE = os.path.expanduser(
    "~/Documents/Projects/sherpa/570-update-achilles-interface/build/bin/Sherpa")
TEMPLATE = "Sherpa_ChiPT_W_Template.yaml"
RUN_FILE = "Sherpa_ChiPT_W_run.yaml"
RESULTS_ZIP = "Results.zip"
OUT_CSV = "w_scan_results.csv"
PB_TO_UB = 1.0e-6

MN = 0.938272
MMU = 0.10566
MPI0 = 0.1349768
MPIC = 0.1395704

# The three CC single-pion channels the ANL/BNL comparison uses.  `key` is the
# same name build_cc1pi_csv.py and wprod_from_ufo.py use, so one name identifies
# a channel everywhere; `stem` names the Print_Graphs directory.
Channel = collections.namedtuple("Channel", "key process stem mpi label")

CHANNELS = collections.OrderedDict((c.key, c) for c in [
    Channel("ppip", "14 2212 -> 13 2212 211", "numu_p_mu_p_pip", MPIC,
            r"$\nu_\mu p \to \mu^- p\,\pi^+$"),
    Channel("ppi0", "14 2112 -> 13 2212 111", "numu_n_mu_p_pi0", MPI0,
            r"$\nu_\mu n \to \mu^- p\,\pi^0$"),
    Channel("npip", "14 2112 -> 13 2112 211", "numu_n_mu_n_pip", MPIC,
            r"$\nu_\mu n \to \mu^- n\,\pi^+$"),
])

# The energies the ANL/BNL comparison is drawn AT -- the points
# build_cc1pi_csv.py writes into cc1pi_all_channels.csv.  Kept as a named set
# because the model is compared with the data at exactly these energies, so
# every scan grid must contain them and reproduce them bit for bit.
ANL_BNL_ENERGIES = (0.4, 0.5, 0.625, 0.75, 0.875, 1.0, 1.125, 1.25, 1.375, 1.5)


def _grid():
    """The default scan grid: a SUPERSET of ANL_BNL_ENERGIES, spaced so the
    plotted curve is smooth on its own and the eye is not being asked to trust
    an interpolator between widely separated points.

    Spacing follows the curvature, which is wildly uneven in E_nu:

      0.300-0.650, step 0.025   sigma(ppip) climbs from 1.1e-13 to 1.7e-09 ub
                                across this window -- four orders of magnitude,
                                the muon-mass threshold turn-on followed by the
                                steep leading edge of the Delta.  Measured: at
                                0.05 spacing the point at 0.550 sat 16% off a
                                log-interpolation of its own neighbours in ppip
                                (13.6% ppi0, 9.0% npip), so 0.05 is NOT enough
                                here even though it is fine 200 MeV higher.
      0.650-1.000, step 0.050   the top of the Delta rise, where the same test
                                gives <4%.
      1.000-1.600, step 0.100   the plateau above the resonance, where the curve
                                is nearly straight and the test gives <1%.

    Starts at 0.300, just above the 0.277 GeV (ppip/npip) and 0.271 GeV (ppi0)
    thresholds, so the turn-on itself is resolved rather than extrapolated, and
    runs to 1.600 so the last DATA point at 1.5 is interior to the curve rather
    than sitting on its end.
    """
    pts = set(ANL_BNL_ENERGIES)
    pts |= {round(0.300 + 0.025 * i, 4) for i in range(15)}   # 0.300 .. 0.650
    pts |= {round(0.650 + 0.050 * i, 4) for i in range(8)}    # 0.650 .. 1.000
    pts |= {round(1.000 + 0.100 * i, 4) for i in range(7)}    # 1.000 .. 1.600
    return tuple(sorted(pts))


ENERGIES = _grid()

# === END CONFIGURATION ===


def threshold(mpi):
    """Lowest E_nu that opens mu- N' pi off a nucleon at rest.

    The muon mass is NOT negligible here: it moves the ppip threshold from
    0.15 to 0.277 GeV and costs a factor 17 at 0.4 GeV.
    """
    return ((MN + mpi + MMU) ** 2 - MN ** 2) / (2 * MN)


def hadron_pair(process):
    """The two final-state hadrons -- what the invariant-mass cut acts on."""
    fs = [int(x) for x in process.split("->")[1].split()]
    had = [k for k in fs if abs(k) not in (11, 12, 13, 14, 15, 16)]
    if len(had) != 2:
        raise RuntimeError("expected 2 final-state hadrons in %r, found %s"
                           % (process, had))
    return had


def write_card(ch, energy, model, param_card, wcut, seed=None):
    """Fill the template for one point.

    BEAMS is derived from the process's own initial state so the two can never
    drift apart -- Sherpa fixes the order of the initial-state particles and
    then insists BEAMS repeats it, and a mismatch shows up only as 'Error in
    initialising ISR' with no cross section written.

    The W < wcut selector is built from THIS process's final-state hadrons.
    Sherpa's syntax is [Mass, kf1, kf2, min, max] (Standard_Selector.C).
    """
    beam0, beam1 = ch.process.split("->")[0].split()[:2]
    s = open(TEMPLATE).read()
    s = s.replace("${BEAM_ENERGY}", "%.6f" % energy)
    s = s.replace("${BEAM0}", beam0).replace("${BEAM1}", beam1)
    s = s.replace("${PARAM_CARD}", param_card)
    s = s.replace("${MODEL}", model)

    if wcut:
        a, b = hadron_pair(ch.process)
        sel = "SELECTORS:\n  - [Mass, %d, %d, 0.0, %.4f]\n" % (a, b, wcut)
    else:
        sel = ""
    s, n = re.subn(r"^\$\{SELECTORS\}\n", sel, s, flags=re.M)
    if n != 1:
        raise RuntimeError("%s: expected exactly one ${SELECTORS} placeholder "
                           "line, found %d -- this is the bug that made --wcut "
                           "a no-op, do not paper over it" % (TEMPLATE, n))

    s, n = re.subn(r"^- .*->.*:[ \t]*$", "- %s:" % ch.process, s, flags=re.M)
    if n != 1:
        raise RuntimeError("%s: expected exactly one process line, found %d"
                           % (TEMPLATE, n))
    graphs = "diagrams_" + ch.stem
    s = re.sub(r"^(\s*Print_Graphs:).*$", r"\1 " + graphs, s, flags=re.M)
    if seed is not None:
        s += "\nRANDOM_SEED: %d\n" % seed
    os.makedirs(graphs, exist_ok=True)
    with open(RUN_FILE, "w") as f:
        f.write(s)

    # Sanity check on what was actually written, because the failure this
    # script is named after was a substitution that silently did nothing.
    if wcut and ("%.4f" % wcut) not in s:
        raise RuntimeError("W cut %.4f did not make it into %s" % (wcut, RUN_FILE))
    return s


def save_card(outputs, ch, model, energy, wcut, seed, text):
    """Keep the exact card that was run, for validation."""
    if not outputs:
        return None
    os.makedirs(outputs, exist_ok=True)
    name = "%s_%s_E%.4f_W%s%s.yaml" % (
        ch.key, model, energy, ("%.2f" % wcut) if wcut else "none",
        "" if seed is None else "_seed%d" % seed)
    path = os.path.join(outputs, name)
    with open(path, "w") as f:
        f.write(text)
    return path


def run_sherpa(timeout, verbose, log_path=None, retries=1):
    """Run Sherpa on RUN_FILE, retrying a crash on the COLD Comix build.

    The charged-pion channels segfault inside COMIX::Amplitude::GaugeTest the
    first time a process is built from scratch (empty Process/).  The crashed
    run still leaves its Process/Comix/<proc>.map behind and the next invocation
    gets through -- and it genuinely REBUILDS the amplitude and runs the gauge
    test, satisfied to 4e-16.  So the retry is not hiding a bad amplitude.

    Output is captured either way; `verbose` also streams it, and `log_path`
    keeps it on disk next to the run card.
    """
    for attempt in range(retries + 1):
        buf = []
        timed_out = []
        p = subprocess.Popen([EXECUTABLE, RUN_FILE], stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, bufsize=1)

        def kill():
            timed_out.append(True)
            p.kill()

        watchdog = threading.Timer(timeout, kill)
        watchdog.start()
        try:
            for line in p.stdout:
                buf.append(line)
                if verbose:
                    sys.stdout.write("      | " + line)
                    sys.stdout.flush()
            rc = p.wait()
        finally:
            watchdog.cancel()
            p.stdout.close()

        if log_path:
            mode = "a" if attempt else "w"
            with open(log_path, mode) as f:
                f.write("=== attempt %d: %s %s ===\n"
                        % (attempt + 1, EXECUTABLE, RUN_FILE))
                f.writelines(buf)

        if timed_out:
            raise RuntimeError("Sherpa did not finish within %ds -- the phase "
                               "space integration is not converging" % timeout)
        if rc == 0:
            return
        if attempt == retries:
            tail = "".join(buf[-20:])
            raise RuntimeError("Sherpa failed with code %d\n%s" % (rc, tail))
        if not verbose:
            print("  [cold-build crash, retrying against the cached map]",
                  end="", flush=True)


def extract():
    """Total cross section and its error, in pb, then delete the zip.

    Deleting it matters: Sherpa reuses a Results.zip it finds, so a leftover one
    would hand the next energy point the previous point's integration.
    """
    with zipfile.ZipFile(RESULTS_ZIP) as z:
        z.extractall("Results")
    hits = sorted(glob.glob(os.path.join("Results", "*", "*", "Statistics.dat")))
    if len(hits) != 1:
        shutil.rmtree("Results", ignore_errors=True)
        raise FileNotFoundError("expected exactly one Statistics.dat, found %d"
                                % len(hits))
    with open(hits[0]) as f:
        last = f.readlines()[-1].split()
    shutil.rmtree("Results", ignore_errors=True)
    os.remove(RESULTS_ZIP)
    return float(last[1]), float(last[2])


# ------------------------------------------------------------- results on disk
COLS = ["channel", "process", "model", "param_card", "E_nu", "wcut",
        "sigma_ub", "err_ub", "nruns"]


def key_of(row):
    return (row["channel"], row["model"], row["param_card"],
            "%.4f" % float(row["E_nu"]), row["wcut"])


def read_csv(path=OUT_CSV):
    """Existing rows as {key: row}.  Missing or legacy files give {}."""
    if not os.path.exists(path):
        return collections.OrderedDict()
    with open(path) as f:
        lines = [l for l in f if l.strip() and not l.startswith("#")]
    if not lines:
        return collections.OrderedDict()
    head = [c.strip() for c in lines[0].rstrip("\n").split(",")]
    out = collections.OrderedDict()
    for line in lines[1:]:
        vals = line.rstrip("\n").split(",")
        if len(vals) != len(head):
            continue
        row = dict(zip(head, vals))
        if not set(COLS) <= set(row):     # the old append-only layout
            continue
        out[key_of(row)] = row
    return out


def write_csv(rows, path=OUT_CSV):
    """Long format, one row per (channel, model, param card, E_nu, cut)."""
    order = {k: i for i, k in enumerate(CHANNELS)}
    ordered = sorted(rows.values(),
                     key=lambda r: (order.get(r["channel"], 99), r["model"],
                                    r["wcut"], float(r["E_nu"])))
    with open(path, "w") as f:
        f.write("# CC single-pion cross sections from Sherpa, in ub.\n")
        f.write("# wcut is the upper limit on the invariant mass of the "
                "final-state pi-N pair,\n")
        f.write("# applied as SELECTORS: [Mass, kf1, kf2, 0, wcut]; "
                "'none' means no selector.\n")
        f.write("# nruns > 1 means RANDOM_SEED 1..n were averaged and err_ub "
                "is the scatter of\n")
        f.write("# those runs, not Comix's own per-run estimate.\n")
        f.write(",".join(COLS) + "\n")
        for r in ordered:
            f.write(",".join(str(r[c]) for c in COLS) + "\n")


def scan_channel(ch, model, param_card, energies, wcut, a, rows):
    """Every energy point for one channel, merging into `rows` as it goes."""
    # A stale Process/ cache is keyed to the previous model and process and will
    # either be reused silently or come back as "No hard process found".
    if not a.keep_process:
        shutil.rmtree("Process", ignore_errors=True)
    if os.path.exists(RESULTS_ZIP):
        os.remove(RESULTS_ZIP)

    emin = threshold(ch.mpi)
    todo = [e for e in energies if e > emin + 1e-4]
    for e in energies:
        if e <= emin + 1e-4:
            print("  %-5s E_nu = %6.4f GeV   below threshold (%.4f), skipped"
                  % (ch.key, e, emin))

    cutname = ("%.2f" % wcut) if wcut else "none"
    failed = []
    for i, e in enumerate(todo, 1):
        key = (ch.key, model, param_card, "%.4f" % e, cutname)
        if a.skip_existing and key in rows:
            print("  [%2d/%2d] %-5s %s  E_nu = %6.4f GeV  W < %s   "
                  "-> cached %s ub" % (i, len(todo), ch.key, model, e, cutname,
                                       rows[key]["sigma_ub"]))
            continue

        print("  [%2d/%2d] %-5s %s  E_nu = %6.4f GeV  W < %s"
              % (i, len(todo), ch.key, model, e, cutname),
              end="\n" if a.verbose else "", flush=True)
        try:
            vals, errs = [], []
            for seed in range(1, a.seeds + 1):
                s = seed if a.seeds > 1 else None
                text = write_card(ch, e, model, param_card, wcut, s)
                card = save_card(a.outputs, ch, model, e, wcut, s, text)
                log = card[:-5] + ".log" if card else None
                run_sherpa(a.timeout, a.verbose, log)
                xs, dxs = extract()
                vals.append(xs * PB_TO_UB)
                errs.append(dxs * PB_TO_UB)
        except Exception as exc:
            # One energy point that will not integrate must not cost the other
            # 29; the run is long and unattended.  The point is left OUT of the
            # csv rather than written as a zero, and reported at the end.
            if not a.keep_going:
                raise
            print("   ->  FAILED: %s" % exc)
            failed.append(e)
            continue

        xs = sum(vals) / len(vals)
        if len(vals) > 1:
            # the scatter of the runs, not Comix's own per-run estimate
            var = sum((v - xs) ** 2 for v in vals) / (len(vals) - 1)
            dxs = (var / len(vals)) ** 0.5
        else:
            dxs = errs[0]

        print("   ->  %12.5g +- %-10.3g ub" % (xs, dxs))
        row = dict(channel=ch.key, process=ch.process, model=model,
                   param_card=param_card, E_nu="%.6f" % e, wcut=cutname,
                   sigma_ub="%.8g" % xs, err_ub="%.8g" % dxs,
                   nruns=len(vals))
        rows[key_of(row)] = row
        write_csv(rows, a.csv)          # checkpoint after every point
    return failed


def main():
    ap = argparse.ArgumentParser(
        description="Scan the CC single-pion channels over the ANL/BNL "
                    "energies with Sherpa.")
    ap.add_argument("--channels", default=",".join(CHANNELS),
                    help="comma-separated: " + ", ".join(CHANNELS))
    ap.add_argument("--energies", default=None,
                    help="comma-separated E_nu in GeV (default: the ANL/BNL "
                         "grid, %s)" % ",".join(str(e) for e in ENERGIES))
    ap.add_argument("--wcut", type=float, default=None,
                    help="upper limit on the pi-N invariant mass, e.g. 1.4 to "
                         "match the ANL/BNL W<1.4 GeV data sets")
    ap.add_argument("--model", default="ChiPT_UFO_V8")
    ap.add_argument("--param", default="param_ChiPT_UFO_V8.dat")
    ap.add_argument("--seeds", type=int, default=1,
                    help="repeat each point with RANDOM_SEED 1..N and average")
    ap.add_argument("--csv", default=OUT_CSV)
    ap.add_argument("--outputs", default=None, metavar="DIR",
                    help="save every run card and its Sherpa log here")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="stream Sherpa's own output")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--keep-process", action="store_true",
                    help="do not clear Process/ between channels")
    ap.add_argument("--skip-existing", action="store_true",
                    help="reuse points already in the csv for this "
                         "(channel, model, param card, E_nu, wcut); makes a "
                         "long scan resumable")
    ap.add_argument("--keep-going", action="store_true",
                    help="report an energy point that fails to integrate and "
                         "carry on instead of aborting the channel")
    a = ap.parse_args()

    keys = [k.strip() for k in a.channels.split(",") if k.strip()]
    bad = [k for k in keys if k not in CHANNELS]
    if bad:
        ap.error("unknown channel(s) %s; known: %s"
                 % (", ".join(bad), ", ".join(CHANNELS)))
    energies = ([float(x) for x in a.energies.split(",")] if a.energies
                else list(ENERGIES))

    print("model %s  param %s  W < %s  %d seed%s"
          % (a.model, a.param, ("%.2f GeV" % a.wcut) if a.wcut else "no cut",
             a.seeds, "" if a.seeds == 1 else "s"))
    if a.outputs:
        print("cards and logs -> %s/" % a.outputs)

    print("%d energy points: %s GeV"
          % (len(energies), ", ".join("%.3f" % e for e in energies)))

    rows = read_csv(a.csv)
    failed = []
    for k in keys:
        failed += [(k, e) for e in
                   scan_channel(CHANNELS[k], a.model, a.param, energies,
                                a.wcut, a, rows)]
    write_csv(rows, a.csv)
    print("wrote %s (%d rows)" % (a.csv, len(rows)))
    if failed:
        print("FAILED points: %s"
              % ", ".join("%s@%.4f" % (k, e) for k, e in failed))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
