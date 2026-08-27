#!/usr/bin/env python3
"""nu_mu n -> mu- p : the model against Llewellyn Smith.

Quasi-elastic is the sharpest test of the nucleon weak vertex there is, and the
one thing in this model that had never been checked against an EXTERNAL result.
Everything else in tools/ tests the model against itself -- CVC against its own
photon vertex, PCAC against its own axial current, the Ward identity against its
own background.  Those cannot see a wrong overall normalisation, a wrong V_ud, a
wrong 1/4M on the Pauli term or a wrong sign on F_A relative to F_1.  A closed
formula from 1972 can.

WHY THE COMPARISON IS CLEAN.  The model's W-N-N vertex is EXACTLY the
Llewellyn-Smith current, structure for structure -- there is nothing else in
nu_mu n -> mu- p at tree level.  No Delta (a Delta cannot be an internal line
with no pion emitted), no background, no form factor of this project's own
invention.  Reading the four couplings off the UFO,

    Dirac         +i (g/2) FW1 gamma^mu
    axial         -i (g/2) ga FWA gamma^mu gamma5
    Pauli            (g/4M) FW2 sigma^{mu nu} q_nu
    pseudoscalar  -i g ga M FPP q^mu gamma5          g = e V_ud / (s_W sqrt2)

against the standard current

    J^mu = ubar [ F_1 gamma^mu + i sigma^{mu nu} q_nu F_2 / 2M
                + F_A gamma^mu gamma5 + F_P q^mu gamma5 / M ] u

gives F_1 = FW1, F_A = -ga FWA (so F_A(0) = -1.271, the usual sign relative to
F_1), F_2 = +-FW2 (the sign rides on the UFO's Sigma convention and is settled
numerically below, not asserted), and

    F_P = -2 ga M^2 FPP = 2 M^2 F_A / (Q^2 + mpi^2)

which is the Goldberger-Treiman / PCAC value with no freedom in it.  So the
model IS Llewellyn Smith, and the only question is whether the numbers come out.

THREE COLUMNS, ON PURPOSE.  A two-way comparison cannot tell a convention slip
from a physics error, so this computes the cross section three ways:

  LS      the 1972 closed formula, with the model's own form factors,
          its own G_F built from ee/s_W/M_W, and its own V_ud;
  UFO     the same process contracted numerically from the UFO vertex and the
          UFO's own leptonic vertex, which shares no code with LS;
  Sherpa  read from ccqe_sherpa.csv, written by tools/run_ccqe.py.

LS against UFO isolates conventions (they use the same form factors but nothing
else in common).  UFO against Sherpa isolates the generator.  All three agreeing
means the vertex is right in an absolute sense.

WHAT IT FOUND (2026-08-26, ChiPT_UFO_V9), and what became of it.  Two things,
both invisible to every other check in this directory, and BOTH NOW FIXED --
this section is kept because the way each one hid is worth remembering.

1. THE INDUCED PSEUDOSCALAR HAD THE WRONG SIGN.  Decomposing the UFO vertex on
   the four Lorentz structures at Q^2 = 0.5 GeV^2 (residual 3e-16) gave

       F_1 = +0.446013     F_2 = +1.181403
       F_A = -0.539944     F_P = +1.830068

   against the PCAC value -1.830068.  The magnitude agreed to seven digits, so
   it was a pure sign, not a modelling choice.  Flipping it makes the UFO
   contraction agree with LS to a FLAT 0.07% from 0.3 to 5 GeV; leaving it, the
   disagreement grew to 4.2% at threshold.  (The residual 0.07% is the W WIDTH:
   LS is a four-fermion contact formula, the UFO carries the full propagator,
   and 1/(1+Gamma_W^2/M_W^2) = 0.99934.)

   HOW IT HID.  tools/pcac_nucleon.py handed the W leg a momentum that violates
   conservation: with 'p~' -> -p1 and 'n' -> p2 the outgoing W+ momentum must be
   p1-p2, and the script passed p2-p1.  It then contracted with that same
   flipped q, which reverses the F_P term relative to F_A and turns the
   enhancement into the suppression it reported.  The lesson is that a test
   built entirely out of RATIOS cannot see a sign error in the vector it
   divides by; tools/nucleon_ff.py exists to solve for the four form factors
   directly and contract nothing.

   FIXED in ChiPT_UFO_V10 (the leading minus removed from LNNPPFF) and in the
   test (the momentum assignment).  Both had to move together.

2. SHERPA WAS EXACTLY A FACTOR 2 BELOW THE DIRECT CONTRACTION, at every energy
   from 0.3 to 5 GeV, to the 1e-4 the Monte Carlo error allowed.  Nothing but
   spin counting produces exactly 2: Sherpa averaged over BOTH neutrino
   helicity states, whereas a neutrino beam is 100% left-handed and only the
   two nucleon spins should be averaged.

   CONFIRMED at the time by tools/imd_check.py on nu_mu e- -> mu- nu_e -- a
   pure V-A four-fermion process with no hadrons, no form factors and no model
   input beyond G_F -- which gave 2.00000 / 2.00001 / 2.00003 / 2.00006 /
   2.00015 at E_nu = 20 to 500 GeV, flat to five digits over a factor 25 in s.

   RESOLVED 2026-08-26: Sherpa was rebuilt to stop counting the neutrino spin.
   The same IMD test now reads 1.00000 / 1.00001 / 1.00001 / 1.00003 / 1.00007.
   wprod_from_ufo.py was changed to match (its average is over the two nucleon
   spins only, 1/2 not 1/4) and plot_c5a_vs_data.py's hand correction retired.
   EVERY WEAK NUMBER PRODUCED BEFORE THAT REBUILD IS A FACTOR 2 LOW.

Usage:
    python3 tools/ccqe_ls.py                 # CHIPT_MODEL selects the UFO
    python3 tools/ccqe_ls.py --dsigma 1.0    # dsigma/dQ^2 table at E_nu
    python3 tools/run_ccqe.py                # refresh the Sherpa column
"""
import argparse
import os

import numpy as np

from _vertex import load                                       # sets sys.path

from fig33_from_ufo import (build, uspinor, ubar, dot, METRIC)  # noqa: E402

HBARC2 = 389.379                     # GeV^-2 -> microbarn
UB_TO_1E38 = 1e8                     # microbarn -> 1e-38 cm^2


# ----------------------------------------------------------------- kinematics
def q2_range(E, M, Mp, m):
    """(Q2_min, Q2_max) for nu(E) N(M) -> l(m) N'(Mp) off a nucleon at rest."""
    s = M ** 2 + 2 * M * E
    rs = np.sqrt(s)
    if rs <= m + Mp:
        return None
    Enu = (s - M ** 2) / (2 * rs)                       # |k1*| = E1* (massless)
    El = (s + m ** 2 - Mp ** 2) / (2 * rs)
    kl = np.sqrt(max(El ** 2 - m ** 2, 0.0))
    return (2 * Enu * (El - kl) - m ** 2, 2 * Enu * (El + kl) - m ** 2)


# ------------------------------------------------------- Llewellyn Smith 1972
def ls_dsigma_dq2(Q2, E, ff, M, m, GF, Vud, ga, mpi, anti=False, f2sign=1.0):
    """dsigma/dQ^2 in GeV^-4, Llewellyn Smith Eq. (3.18) in the modern form.

        dsigma/dQ^2 = M^2 GF^2 cos^2(theta_C) / (8 pi E^2)
                      [ A -+ B (s-u)/M^2 + C (s-u)^2/M^4 ]

    with the minus sign for neutrinos.  A, B, C exactly as in Formaggio and
    Zeller, Rev. Mod. Phys. 84 (2012) 1307, Eqs. (60)-(63).
    """
    tau = Q2 / (4 * M ** 2)
    F1 = ff['FW1'](Q2)
    F2 = f2sign * ff['FW2'](Q2)
    FA = -ga * ff['FWA'](Q2)
    FP = 2 * M ** 2 * FA / (Q2 + mpi ** 2)

    A = ((m ** 2 + Q2) / M ** 2) * (
        (1 + tau) * FA ** 2
        - (1 - tau) * F1 ** 2
        + tau * (1 - tau) * F2 ** 2
        + 4 * tau * F1 * F2
        - (m ** 2 / (4 * M ** 2)) * ((F1 + F2) ** 2 + (FA + 2 * FP) ** 2
                                     - 4 * (1 + tau) * FP ** 2))
    B = (Q2 / M ** 2) * FA * (F1 + F2)
    C = 0.25 * (FA ** 2 + F1 ** 2 + tau * F2 ** 2)

    su = 4 * M * E - Q2 - m ** 2                        # s - u
    sgn = +1.0 if anti else -1.0
    return (M ** 2 * GF ** 2 * Vud ** 2 / (8 * np.pi * E ** 2)) * (
        A + sgn * B * su / M ** 2 + C * su ** 2 / M ** 4)


def ls_sigma(E, ff, M, m, GF, Vud, ga, mpi, anti=False, n=400, f2sign=1.0):
    """sigma in microbarn."""
    r = q2_range(E, M, M, m)
    if r is None:
        return 0.0
    lo, hi = r
    # Gauss-Legendre in Q^2; the integrand is smooth and this converges to
    # machine precision at n = 400, checked against n = 100 and n = 1600.
    x, w = np.polynomial.legendre.leggauss(n)
    Q2 = 0.5 * (hi - lo) * x + 0.5 * (hi + lo)
    jac = 0.5 * (hi - lo)
    vals = np.array([ls_dsigma_dq2(q, E, ff, M, m, GF, Vud, ga, mpi,
                                   anti, f2sign) for q in Q2])
    return HBARC2 * jac * np.sum(w * vals)


# ------------------------------------------------ the same thing from the UFO
def ufo_sigma(E, V, ns, ff, m, n=400):
    """sigma(nu_mu n -> mu- p) in microbarn, contracted from the UFO vertices.

    Shares no code with ls_sigma above: the hadronic and leptonic currents are
    both built by fig33_from_ufo.build straight off the UFO's Lorentz
    structures and couplings, and the W propagator is the full massive one
    rather than a four-fermion contact term.  Legs are all OUTGOING, so an
    incoming particle enters under its antiparticle name with minus its
    momentum -- the convention wprod_from_ufo.py uses.
    """
    M = float(ns['MNucleon'])
    MW, GW = float(ns['MW'].real), float(ns['WW'])
    r = q2_range(E, M, M, m)
    if r is None:
        return 0.0
    lo, hi = r
    s = M ** 2 + 2 * M * E
    rs = np.sqrt(s)
    Enu = (s - M ** 2) / (2 * rs)
    El = (s + m ** 2 - M ** 2) / (2 * rs)
    kl = np.sqrt(max(El ** 2 - m ** 2, 0.0))

    x, w = np.polynomial.legendre.leggauss(n)
    # integrate in cos(theta*) and convert; dQ^2 = 2 Enu kl dcos
    tot = 0.0
    for xi, wi in zip(x, w):
        ct = xi
        k1 = np.array([Enu, 0, 0, Enu], dtype=complex)          # incoming nu
        p1 = np.array([Enu, 0, 0, -Enu], dtype=complex)         # dummy; set below
        # neutron at rest in the lab is boosted; work entirely in the CM
        En = np.sqrt(Enu ** 2 + M ** 2)
        p1 = np.array([En, 0, 0, -Enu], dtype=complex)          # incoming n
        st = np.sqrt(max(1 - ct ** 2, 0.0))
        k2 = np.array([El, kl * st, 0, kl * ct], dtype=complex)  # outgoing mu-
        p2 = np.array([np.sqrt(kl ** 2 + M ** 2),
                       -kl * st, 0, -kl * ct], dtype=complex)    # outgoing p
        q = k1 - k2

        # leptonic vertex: incoming nu_mu is the 'vm~' leg at -k1, outgoing
        # mu- the 'mu-' leg at +k2, W+ leaving at q
        Vl = build(vertex(V, ['vm~', 'mu-', 'W+']),
                   {'vm~': -k1, 'mu-': k2, 'W+': q}, ns, ff)
        # hadronic vertex: incoming n is the 'n~' leg at -p1, outgoing p the
        # 'p' leg at +p2, and the W+ ARRIVES, so it is the 'W-' leg at -q
        Vh = build(vertex(V, ['n~', 'p', 'W-']),
                   {'n~': -p1, 'p': p2, 'W-': -q}, ns, ff)

        den = dot(q, q) - MW ** 2 + 1j * MW * GW
        G = np.diag(METRIC).real
        acc = 0.0
        # SUM over both neutrino helicity labels rather than picking one: the
        # wrong-helicity amplitude vanishes identically against a V-A vertex
        # (wprod_from_ufo.py checks this), so summing is safe and does not
        # depend on which index the spinor routine calls left-handed.  The beam
        # is 100% one helicity, so there is NO 1/2 for the neutrino -- only the
        # two initial nucleon spins are averaged.
        for snu in range(2):
            un = uspinor(k1, 0.0, snu)
            for sl in range(2):
                ubl = ubar(uspinor(k2, m, sl))
                for sn in range(2):
                    ubp = ubar(uspinor(p2, M, sn))
                    for si in range(2):
                        ui = uspinor(p1, M, si)
                        amp = 0.0
                        for mu in range(4):
                            L = ubl @ Vl[mu] @ un
                            H = ubp @ Vh[mu] @ ui
                            amp += G[mu] * L * H
                        acc += abs(amp / den) ** 2
        tot += wi * acc / 2.0
    # sigma = int dcos |Mbar|^2 /(32 pi s) * |k_f|/|k_i|; the phi integral is
    # 2 pi and is already inside that 1/(32 pi s).  The q^mu q^nu piece of the
    # W propagator is dropped: it is suppressed by m_mu^2/M_W^2 ~ 2e-6.
    flux = 1.0 / (32 * np.pi * s) * (kl / Enu)
    return HBARC2 * tot * flux


def vertex(V, names):
    want = sorted(names)
    out = [v for v in V if sorted(p.name for p in v.particles) == want]
    if not out:
        raise KeyError(names)
    return out[0]


# --------------------------------------------------------------------- driver
ENERGIES = (0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5, 2.0, 3.0, 5.0)


def read_sherpa(path=None, model=None):
    # run_ccqe.py writes into the REPOSITORY ROOT, not into tools/, so resolve
    # the path relative to this file rather than to the working directory.
    path = path or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'ccqe_sherpa.csv')
    model = model or os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V9')
    import csv
    out = {}
    if not os.path.exists(path):
        return out
    for r in csv.DictReader(l for l in open(path) if not l.startswith('#')):
        if r.get('model') != model:
            continue
        out[round(float(r['E_nu']), 4)] = (float(r['sigma_ub']),
                                           float(r['err_ub']))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dsigma', type=float, default=None,
                    help='print dsigma/dQ^2 at this E_nu instead of sigma(E)')
    ap.add_argument('--anti', action='store_true',
                    help='antineutrino, nu_mu-bar p -> mu+ n')
    ap.add_argument('--no-ufo', action='store_true',
                    help='skip the UFO-contraction column (it is the slow one)')
    a = ap.parse_args()

    ns, ff, V = load()
    M = float(ns['MNucleon'])
    m = float(ns['MMU']) if 'MMU' in ns else 0.10566
    ga = float(ns['ga'])
    Vud = float(ns['Vud'].real)
    ee, sw, MW = float(ns['ee'].real), float(ns['sw'].real), float(ns['MW'].real)
    GF = ee ** 2 / (4 * np.sqrt(2) * sw ** 2 * MW ** 2)
    mpi = float(ns['MPiP'])

    # THE PAULI SIGN IS MEASURED, NOT ASSERTED.  The UFO's Sigma convention
    # decides whether F_2 = +FW2 or -FW2, and getting it backwards moves the
    # cross section by ~15% at 1 GeV -- large enough to matter, small enough to
    # look like a form factor disagreement.  Pick whichever reproduces the UFO
    # contraction, and say which was picked.
    f2sign = 1.0
    if not a.no_ufo:
        Etest = 1.0
        u = ufo_sigma(Etest, V, ns, ff, m)
        best, f2sign = None, 1.0
        for sgn in (+1.0, -1.0):
            l = ls_sigma(Etest, ff, M, m, GF, Vud, ga, mpi, a.anti, f2sign=sgn)
            d = abs(l / u - 1) if u else 9e9
            if best is None or d < best:
                best, f2sign = d, sgn
        print("Pauli sign vs the UFO Sigma convention: F_2 = %+.0f x FW2  "
              "(mismatch %.2e)" % (f2sign, best))

    print("\nnu_mu n -> mu- p   %s" % ("ANTINEUTRINO" if a.anti else ""))
    print("M = %.6f  m_mu = %.5f  g_A = %.4f  V_ud = %.6f  G_F = %.6e"
          % (M, m, ga, Vud, GF))
    print("form factors: F1V/F2V from the model's Kelly Sachs fit, "
          "F_A from its axial z-expansion, F_P from PCAC")

    if a.dsigma is not None:
        E = a.dsigma
        lo, hi = q2_range(E, M, M, m)
        print("\ndsigma/dQ^2 at E_nu = %.2f GeV   (1e-38 cm^2 / GeV^2)" % E)
        print("  %8s %16s" % ("Q^2", "LS"))
        for Q2 in np.linspace(lo, min(hi, 2.0), 15):
            v = ls_dsigma_dq2(Q2, E, ff, M, m, GF, Vud, ga, mpi, a.anti, f2sign)
            print("  %8.4f %16.6g" % (Q2, v * HBARC2 * UB_TO_1E38))
        return

    sh = read_sherpa()
    print("\n  %6s %14s %14s %16s %9s %9s"
          % ("E_nu", "LS", "UFO", "Sherpa", "UFO/LS", "Shr/LS"))
    print("  %6s %14s %14s %16s %9s %9s"
          % ("(GeV)", "(1e-38 cm2)", "(1e-38 cm2)", "(1e-38 cm2)", "", ""))
    for E in ENERGIES:
        l = ls_sigma(E, ff, M, m, GF, Vud, ga, mpi, a.anti, f2sign=f2sign)
        u = None if a.no_ufo else ufo_sigma(E, V, ns, ff, m)
        s = sh.get(round(E, 4))
        row = "  %6.2f %14.6g" % (E, l * UB_TO_1E38)
        row += " %14.6g" % (u * UB_TO_1E38) if u is not None else " %14s" % "-"
        row += (" %10.6g+-%.0e" % (s[0] * UB_TO_1E38, s[1] * UB_TO_1E38)
                if s else " %16s" % "-")
        row += " %9.5f" % (u / l) if (u is not None and l) else " %9s" % "-"
        row += " %9.5f" % (s[0] / l) if (s and l) else " %9s" % "-"
        print(row)


if __name__ == '__main__':
    main()
