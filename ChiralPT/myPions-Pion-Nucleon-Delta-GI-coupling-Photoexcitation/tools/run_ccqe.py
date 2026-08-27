#!/usr/bin/env python3
"""run_ccqe.py -- drive Sherpa over nu_mu n -> mu- p, for tools/ccqe_ls.py.

Quasi-elastic is a 2 -> 2 with exactly one diagram, so there is no W cut, no
channel table and no phase-space subtlety -- everything run_w.py needs for
single-pion production is beside the point here.  Writes ccqe_sherpa.csv, keyed
by (model, param_card, E_nu) and MERGED, so re-running a point overwrites it.

    python3 tools/run_ccqe.py                     # the default energy grid
    python3 tools/run_ccqe.py --energies 1.0,2.0

TWO THINGS THE RUN CARD HAS TO GET RIGHT, both learned the hard way elsewhere
in this project:

  * BEAMS must repeat the process's initial-state order.  Sherpa fixes that
    order (it rejects "2112 14" and asks for "14 2112"), and a BEAMS list in
    the other order drops the process while still exiting 0.

  * A NEUTRON bunch needs MPI_PDF_SET as well as PDF_SET set to None.  Sherpa
    builds an ISR handler for the hard subprocess too and that one reads
    MPI_PDF_SET; Initialization_Handler::LoadPDFLibraries only defines a
    default for p+, e/mu, photon, pomeron and reggeon, so a neutron bunch gets
    the empty set name and dies with "PDF '' does not exist" before the matrix
    element is ever built.  The proton hides this because its default resolves.

BEAM_ENERGIES is the ENERGY, not the kinetic energy: the target's entry is its
MASS so that it sits at rest with no residual pz.
"""
import argparse
import csv
import os
import re
import shutil
import subprocess
import sys
import tempfile

SHERPA = os.environ.get("SHERPA_EXE", os.path.expanduser(
    "~/Documents/Projects/sherpa/570-update-achilles-interface/build/bin/Sherpa"))

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_CSV = os.path.join(ROOT, "ccqe_sherpa.csv")
PB_TO_UB = 1.0e-6
MN = 0.938272

ENERGIES = (0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5, 2.0, 3.0, 5.0)

CARD = """# nu_mu n -> mu- p, fixed target.  Written by tools/run_ccqe.py.
EVENTS: 100
EVENT_GENERATION_MODE: Weighted
INIT_ONLY: 3

ME_GENERATORS: Comix
SCALES: VAR{{Abs2(p[0]+p[1])}}

MODEL: {model}

MI_HANDLER: None
FRAGMENTATION: None
BEAM_REMNANTS: False
BEAMMODE: Fixed_Target
SHOWER_GENERATOR: None
PDF_SET: None
MPI_PDF_SET: None

INTEGRATION_ERROR: 0.005

PARTICLE_DATA:
  1: {{Massive: false}}
  2: {{Massive: false}}
  3: {{Massive: false}}
  4: {{Massive: false}}
  5: {{Massive: false}}
  11: {{Massive: false}}
  13: {{Massive: true}}
  15: {{Massive: false}}

BEAMS: [14, 2112]
BEAM_ENERGIES: [{enu:.6f}, {mn:.6f}]

PROCESSES:
- 14 2112 -> 13 2212:
    Order: {{QCD: 0, QED: 2}}

UFO_PARAM_CARD: {param}

RANDOM_SEED: {seed}
"""

XS = re.compile(r"^\s*\S*2_2__vm__n__p__mu-\S*\s*:\s*\S*\s*([0-9.eE+-]+)\s*pb"
                r".*?([0-9.eE+-]+)\s*pb", re.M)
XS_ANY = re.compile(r":\s*\x1b?\[?[0-9;]*m?\s*([0-9.eE+-]+)\s*pb\s*\+-\s*\(\s*"
                    r"\x1b?\[?[0-9;]*m?\s*([0-9.eE+-]+)\s*pb", re.M)


def strip_ansi(s):
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


def run_point(model, param, E, seed, workdir, verbose=False, timeout=1800):
    card = CARD.format(model=model, param=os.path.basename(param), enu=E,
                       mn=MN, seed=seed)
    d = tempfile.mkdtemp(prefix="ccqe_", dir=workdir)
    with open(os.path.join(d, "run.yaml"), "w") as f:
        f.write(card)
    os.symlink(os.path.abspath(param), os.path.join(d, os.path.basename(param)))
    os.symlink(os.path.abspath(os.path.join(ROOT, model)),
               os.path.join(d, model))
    p = subprocess.run([SHERPA, "-f", "run.yaml"], cwd=d, timeout=timeout,
                       capture_output=True, text=True)
    out = strip_ansi(p.stdout + p.stderr)
    if verbose:
        print(out[-3000:])
    hits = XS_ANY.findall(out)
    if not hits:
        print("  FAILED at E = %.3f (seed %d); last lines:" % (E, seed))
        print("\n".join(out.strip().splitlines()[-8:]))
        return None
    xs, err = hits[-1]
    shutil.rmtree(d, ignore_errors=True)
    return float(xs) * PB_TO_UB, float(err) * PB_TO_UB


def merge(rows):
    old = {}
    if os.path.exists(OUT_CSV):
        with open(OUT_CSV) as f:
            for r in csv.DictReader(l for l in f if not l.startswith("#")):
                old[(r["model"], r["param_card"], round(float(r["E_nu"]), 4))] = r
    for r in rows:
        old[(r["model"], r["param_card"], round(float(r["E_nu"]), 4))] = r
    cols = ["model", "param_card", "E_nu", "sigma_ub", "err_ub", "nruns"]
    with open(OUT_CSV, "w") as f:
        f.write("# sigma(nu_mu n -> mu- p) from Sherpa, in microbarn.\n"
                "# Free nucleon at rest, massive muon, no nuclear effects.\n"
                "# Compare with tools/ccqe_ls.py.\n")
        f.write(",".join(cols) + "\n")
        for k in sorted(old, key=lambda k: (k[0], k[2])):
            f.write(",".join(str(old[k][c]) for c in cols) + "\n")
    print("wrote %s (%d rows)" % (OUT_CSV, len(old)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="ChiPT_UFO_V9")
    ap.add_argument("--param", default=None)
    ap.add_argument("--energies", default=None)
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    param = a.param or os.path.join(ROOT, "param_%s.dat" % a.model)
    energies = ([float(x) for x in a.energies.split(",")]
                if a.energies else list(ENERGIES))

    work = tempfile.mkdtemp(prefix="ccqe_work_")
    rows = []
    try:
        for E in energies:
            vals = []
            for seed in range(1, a.seeds + 1):
                r = run_point(a.model, param, E, seed, work, a.verbose)
                if r:
                    vals.append(r)
            if not vals:
                continue
            xs = sum(v[0] for v in vals) / len(vals)
            er = sum(v[1] for v in vals) / len(vals) / max(len(vals) ** 0.5, 1)
            rows.append(dict(model=a.model, param_card=os.path.basename(param),
                             E_nu="%.6f" % E, sigma_ub="%.6e" % xs,
                             err_ub="%.4g" % er, nruns=len(vals)))
            print("  E_nu = %6.3f GeV  ->  %.6e +- %.3g ub" % (E, xs, er))
    finally:
        shutil.rmtree(work, ignore_errors=True)
    merge(rows)


if __name__ == "__main__":
    main()
