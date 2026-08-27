#!/usr/bin/env python3
"""Inverse muon decay: the normalisation test with no hadrons in it.

    nu_mu e-  ->  mu- nu_e

This exists to answer one question that tools/ccqe_ls.py raised and could not
close: Sherpa's weak cross sections sit a factor of exactly 2 below a direct
contraction of the same UFO vertices, and the candidate explanation is that
Sherpa averages over BOTH neutrino helicity states when a neutrino beam has
only one.  CCQE cannot settle it, because a disagreement there could always be
blamed on a form factor.  Inverse muon decay can: it is a pure V-A four-fermion
process whose tree-level cross section is a closed expression with NO free
parameters, no form factors, no hadrons, and no model input beyond G_F,

    sigma = (G_F^2 / pi) (s - m_mu^2)^2 / s ,        s = m_e^2 + 2 m_e E_nu

exact for m_e -> 0 in the matrix element (the neglected terms are O(m_e^2/s),
which is 3e-6 here).  Any disagreement is a normalisation, and a factor of
exactly 2 that is flat in energy is spin counting and nothing else.

THRESHOLD.  s must exceed m_mu^2, so E_nu > (m_mu^2 - m_e^2)/(2 m_e) = 10.9 GeV.
There is no point below that, which is why the grid starts at 20 GeV.

UNITS, since this is exactly where the first attempt at this went wrong:
1 GeV^-2 = 0.3894 mb = 3.894e8 pb.  Getting that factor wrong by 1e3 and also
dropping the (1 - m_mu^2/s)^2 phase-space factor made the disagreement look
like 2000x instead of 2x, and nearly buried the result.

Usage:
    python3 tools/imd_check.py                # runs Sherpa and compares
    python3 tools/imd_check.py --no-sherpa    # just the closed formula
"""
import argparse
import os
import re
import shutil
import subprocess
import tempfile

SHERPA = os.environ.get("SHERPA_EXE", os.path.expanduser(
    "~/Documents/Projects/sherpa/570-update-achilles-interface/build/bin/Sherpa"))

GEV2_TO_PB = 3.893793e8          # 1 GeV^-2 in pb
ME = 0.000510999
MMU = 0.1056584
ENERGIES = (20.0, 50.0, 100.0, 200.0, 500.0)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CARD = """EVENTS: 100
EVENT_GENERATION_MODE: Weighted
INIT_ONLY: 3
ME_GENERATORS: Comix
SCALES: VAR{{Abs2(p[0]+p[1])}}
MODEL: {model}
MI_HANDLER: None
FRAGMENTATION: None
BEAM_REMNANTS: False
SHOWER_GENERATOR: None
PDF_SET: None
MPI_PDF_SET: None
INTEGRATION_ERROR: 0.002
PARTICLE_DATA:
  11: {{Massive: true, Mass: {me}}}
  13: {{Massive: true, Mass: {mmu}}}
BEAMS: [14, 11]
BEAM_ENERGIES: [{enu:.8f}, {me}]
PROCESSES:
- 14 11 -> 13 12:
    Order: {{QCD: 0, QED: 2}}
UFO_PARAM_CARD: {param}
RANDOM_SEED: 1
"""

XS = re.compile(r"2_2__\S+\s*:\s*([0-9.eE+-]+)\s*pb\s*\+-\s*\(\s*"
                r"([0-9.eE+-]+)\s*pb")


def strip_ansi(s):
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


def analytic(E, GF, me=ME, mmu=MMU):
    """sigma in pb, tree level, m_e kept only in s."""
    s = me ** 2 + 2 * me * E
    if s <= mmu ** 2:
        return 0.0, s
    return (GF ** 2 / 3.14159265358979) * (s - mmu ** 2) ** 2 / s * GEV2_TO_PB, s


def run_sherpa(model, param, E, workdir):
    d = tempfile.mkdtemp(prefix="imd_", dir=workdir)
    with open(os.path.join(d, "run.yaml"), "w") as f:
        f.write(CARD.format(model=model, param=os.path.basename(param),
                            enu=E, me=repr(ME), mmu=repr(MMU)))
    os.symlink(os.path.abspath(param), os.path.join(d, os.path.basename(param)))
    os.symlink(os.path.join(ROOT, model), os.path.join(d, model))
    p = subprocess.run([SHERPA, "-f", "run.yaml"], cwd=d, timeout=1800,
                       capture_output=True, text=True)
    out = strip_ansi(p.stdout + p.stderr)
    hits = XS.findall(out)
    if not hits:
        print("  FAILED at E = %g; last lines:" % E)
        print("\n".join(out.strip().splitlines()[-10:]))
        return None
    shutil.rmtree(d, ignore_errors=True)
    return float(hits[-1][0]), float(hits[-1][1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=os.environ.get("CHIPT_MODEL",
                                                      "ChiPT_UFO_V9"))
    ap.add_argument("--no-sherpa", action="store_true")
    a = ap.parse_args()
    param = os.path.join(ROOT, "param_%s.dat" % a.model)

    import sys
    sys.path.insert(0, ROOT)
    from fig33_from_ufo import load_ufo, parameter_namespace
    P, _ = load_ufo(os.path.join(ROOT, a.model))
    ns = parameter_namespace(P)
    ee, sw, MW = (float(ns['ee'].real), float(ns['sw'].real),
                  float(ns['MW'].real))
    GF = ee ** 2 / (4 * 2 ** 0.5 * sw ** 2 * MW ** 2)
    print("nu_mu e- -> mu- nu_e     model %s" % a.model)
    print("G_F from the model's own ee, s_W, M_W = %.6e  (card Gf = %.6e)"
          % (GF, float(ns['Gf'])))
    print("m_e = %.9g   m_mu = %.7g   threshold E_nu = %.4f GeV\n"
          % (ME, MMU, (MMU ** 2 - ME ** 2) / (2 * ME)))

    work = tempfile.mkdtemp(prefix="imd_work_")
    # THE CONTACT FORMULA HAS NO W WIDTH.  Sherpa propagates the W with
    # 1/(q^2 - M_W^2 + i M_W Gamma_W), whose modulus squared is smaller than
    # the contact limit by 1/(1 + Gamma_W^2/M_W^2) at q^2 << M_W^2.  That is
    # 0.99934 here, i.e. +0.066% on the ratio -- the whole of the observed
    # departure from 2.  Dividing it out leaves the spin factor alone, and the
    # residual drift with energy is the q^2/M_W^2 term, ~1e-5 over this grid.
    GW = float(ns['WW'])
    wfac = 1.0 / (1.0 + (GW / MW) ** 2)
    print("W width correction 1/(1 + Gamma_W^2/M_W^2) = %.8f  "
          "(Gamma_W = %.4f)\n" % (wfac, GW))
    print("  %8s %12s %16s %18s %10s %11s"
          % ("E_nu", "s (GeV^2)", "analytic (pb)", "Sherpa (pb)", "ana/Shr",
             "spin factor"))
    try:
        for E in ENERGIES:
            an, s = analytic(E, GF)
            row = "  %8.1f %12.6f %16.6g" % (E, s, an)
            if a.no_sherpa:
                print(row + " %18s %10s %11s" % ("-", "-", "-"))
                continue
            r = run_sherpa(a.model, param, E, work)
            if r is None:
                print(row + " %18s %10s %11s" % ("FAILED", "-", "-"))
                continue
            sh, err = r
            print(row + " %13.6g+-%.0e %10.5f %11.5f"
                  % (sh, err, an / sh, (an / sh) * wfac))
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
