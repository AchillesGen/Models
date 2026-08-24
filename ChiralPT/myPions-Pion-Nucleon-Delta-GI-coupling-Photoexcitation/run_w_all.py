#!/usr/bin/env python3
"""run_w_all.py -- the full W < 1.4 GeV scan, every CC single-pion channel.

Drives run_w.py once per channel over the ANL/BNL energy grid, so the result is
directly comparable with the W<1.4 data sets that build_cc1pi_csv.py reads.

    python3 run_w_all.py                    # W < 1.4, all three channels
    python3 run_w_all.py --outputs outputs  # keep every run card and log
    python3 run_w_all.py -v                 # stream Sherpa's own output
    python3 run_w_all.py --wcut none        # the uncut scan, for comparison

One run_w.py PER CHANNEL rather than one call with all three: each is a separate
process, so a channel that fails to integrate is reported and the remaining ones
still run, and Process/ is cleared cleanly at each channel boundary.

Everything lands in w_scan_results.csv, which run_w.py merges by
(channel, model, param_card, E_nu, wcut) -- so the cut and uncut scans coexist
in one file and re-running a point overwrites it.
"""

import argparse
import os
import subprocess
import sys
import time

import run_w

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "run_w.py")


def main():
    ap = argparse.ArgumentParser(
        description="Run run_w.py over every CC single-pion channel.")
    ap.add_argument("--wcut", default="1.4",
                    help="pi-N invariant mass cut in GeV, or 'none' "
                         "(default: 1.4, the ANL/BNL cut)")
    ap.add_argument("--channels", default=",".join(run_w.CHANNELS))
    ap.add_argument("--energies", default=None,
                    help="override the ANL/BNL grid")
    ap.add_argument("--model", default="ChiPT_UFO_V8")
    ap.add_argument("--param", default="param_ChiPT_UFO_V8.dat")
    ap.add_argument("--seeds", type=int, default=2,
                    help="seeds averaged per point (default 2, as in "
                         "cc1pi_all_channels.csv)")
    ap.add_argument("--csv", default=run_w.OUT_CSV)
    ap.add_argument("--outputs", default=None, metavar="DIR",
                    help="save every run card and Sherpa log here, for "
                         "validation")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="stream Sherpa's own output")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--fresh", action="store_true",
                    help="recompute every point; by default a point already in "
                         "the csv for this (channel, model, param card, E_nu, "
                         "wcut) is reused, so an interrupted scan resumes")
    ap.add_argument("--stop-on-error", action="store_true",
                    help="abort a channel on the first energy point that fails "
                         "to integrate, instead of skipping it")
    a = ap.parse_args()

    channels = [c.strip() for c in a.channels.split(",") if c.strip()]
    bad = [c for c in channels if c not in run_w.CHANNELS]
    if bad:
        ap.error("unknown channel(s) %s; known: %s"
                 % (", ".join(bad), ", ".join(run_w.CHANNELS)))

    cut = None if a.wcut.lower() in ("none", "off", "") else float(a.wcut)

    print("=" * 72)
    print("CC single-pion scan   model %s   W < %s"
          % (a.model, ("%.2f GeV" % cut) if cut else "no cut"))
    print("channels: %s" % ", ".join(channels))
    grid = ([float(x) for x in a.energies.split(",")] if a.energies
            else run_w.ENERGIES)
    print("energies: %d points, %.3f - %.3f GeV"
          % (len(grid), min(grid), max(grid)))
    print("          %s" % ", ".join("%.3f" % e for e in grid))
    print("seeds:    %d per point  (%d Sherpa runs at most)"
          % (a.seeds, len(channels) * len(grid) * a.seeds))
    print("=" * 72)

    failed = []
    t0 = time.time()
    for ch in channels:
        cmd = [sys.executable, SCRIPT,
               "--channels", ch,
               "--model", a.model,
               "--param", a.param,
               "--seeds", str(a.seeds),
               "--csv", a.csv,
               "--timeout", str(a.timeout)]
        if cut:
            cmd += ["--wcut", str(cut)]
        if a.energies:
            cmd += ["--energies", a.energies]
        if a.outputs:
            cmd += ["--outputs", a.outputs]
        if a.verbose:
            cmd += ["--verbose"]
        if not a.fresh:
            cmd += ["--skip-existing"]
        if not a.stop_on_error:
            cmd += ["--keep-going"]

        print("\n--- %s ---" % ch, flush=True)
        r = subprocess.run(cmd, cwd=HERE)
        if r.returncode != 0:
            print("*** %s FAILED (exit %d); continuing" % (ch, r.returncode))
            failed.append(ch)

    dt = time.time() - t0
    print("\n" + "=" * 72)
    print("done in %dm%02ds -> %s" % (dt // 60, dt % 60, a.csv))
    if a.outputs:
        print("cards and logs in %s/" % a.outputs)
    if failed:
        print("FAILED: %s" % ", ".join(failed))
    print("=" * 72)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
