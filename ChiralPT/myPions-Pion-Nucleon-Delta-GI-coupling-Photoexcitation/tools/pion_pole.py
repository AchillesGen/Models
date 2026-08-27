#!/usr/bin/env python3
"""Is the effective pion-pole operator the factorised diagram it claims to be?

LPPoleFF folds a two-point mixing, a propagator and the Weinberg-Tomozawa
pi-pi-N-N vertex into ONE four-point operator, because the UFO format has no
two-point vertices.  That is a legitimate device -- the virtual pion carries
exactly the boson's momentum, so mixing and propagator together are a function
of q^2 alone and can live in a form factor -- but it means the operator's
normalisation and its isospin algebra are hand-written and have to be checked
against the thing they stand for:

    A)  the FPPpi structure of the four-point vertex, straight out of the UFO
    B)  [ (fPi/2) x SrcDiv x q^mu ] x [ i/(q^2 - mpi^2) ] x [ pi-pi-N-N vertex ]

where the pi-pi-N-N vertex is the UFO's OWN, taken with the virtual pion at the
boson's momentum.  A NON-CONSTANT A/B would mean the Lorentz structure itself is
wrong, and that is the first thing this checks.

A/B IS NOT REQUIRED TO BE 1, and reading it that way is how this test goes
wrong.  B is written in the charged-pion basis while the operator lives in the
cartesian one, which costs a sqrt2, and a sign rides on the direction of q.  So
the script does the SAME construction a second time on a pole the model already
gets right -- the nucleon's own induced pseudoscalar, whose residue is
Goldberger-Treiman and was pinned independently by tools/pcac_nucleon.py and
tools/nucleon_ff.py -- and the test is that the two ratios AGREE.  They do, at
-sqrt2 with residuals of 1e-16, which says the pion-pole operator carries the
same f_pi as the pole the model already gets right.

THE MIXING COEFFICIENT IS NOT INDEPENDENT INPUT.  It is (fPi/2) Tr[sigma^a
(l-r)^mu], the O(pi) cross term of (fPi^2/4) Tr[D_mu U (D^mu U)^+], and
ChiPT.fr computes it as PiPoleSrc[a].  Its value for the charged current is
ee Vud/(sqrt2 sw), which this script hardcodes because it is what FeynRules
printed for PiPoleSrc[1] -- so B does NOT get its normalisation from the same
hand algebra that A does; what it shares is only the chiral Lagrangian.

Usage:  python3 tools/pion_pole.py     (CHIPT_MODEL must be a model with PP)
"""
import os

import numpy as np

from _vertex import load, vertex, with_ff, build_named          # sets sys.path

import wprod_from_ufo as w                                      # noqa: E402
from fig33_from_ufo import dot                                  # noqa: E402


def rp(x):
    return float(x.real) if isinstance(x, complex) else float(x)


def ratio(A, B, p_in, p_out, MN):
    """A/B after sandwiching both between on-shell spinors.

    Taking the ratio of raw Dirac matrices is wrong here: the pi-N-N vertex is
    pseudovector, so the factorised amplitude carries gamma5 q-slash where the
    operator carries a bare gamma5, and the two are equal only BETWEEN ON-SHELL
    SPINORS (ubar q-slash gamma5 u = -2 MN ubar gamma5 u).  Comparing the
    matrices componentwise picks an entry where one of them vanishes and
    reports 0.  The least-squares ratio over all (mu, spin, spin) also gives a
    residual, which is what says the two are proportional at all.
    """
    a, b = [], []
    for m in range(4):
        for s2 in range(2):
            for s1 in range(2):
                ub = w.ubar(w.uspinor(p_out, MN, s2))
                u = w.uspinor(p_in, MN, s1)
                a.append(ub @ A[m] @ u)
                b.append(ub @ B[m] @ u)
    a, b = np.array(a), np.array(b)
    if np.abs(b).max() == 0:
        return float('nan'), float('nan')
    r = np.vdot(b, a) / np.vdot(b, b)
    res = np.abs(a - r * b).max() / max(np.abs(a).max(), 1e-30)
    return r, res


def main():
    ns, ff, V = load()
    MN, mpi, fpi = rp(ns['MNucleon']), rp(ns['MPiP']), rp(ns['fPi'])
    ee, sw, Vud = rp(ns['ee']), rp(ns['sw']), rp(ns['Vud'])
    # PiPoleSrc[1] as FeynRules prints it: ee Vud/(sqrt2 sw) (del.W + del.Wbar)
    src = ee * Vud / (np.sqrt(2.0) * sw)

    v4 = vertex(V, ('n~', 'n', 'W-', 'Pi+'))
    keep = with_ff(v4, 'FPPpi')
    if not keep:
        raise SystemExit("this model has no FPPpi structure -- PP not built in")
    v2 = vertex(V, ('n~', 'n', 'Pi-', 'Pi+'))

    print("pion-pole operator vs the factorised diagram   model %s"
          % os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V11'))
    print("vertex %s, structure carrying FPPpi: %s\n"
          % ([p.name for p in v4.particles], sorted(keep)))
    print("  %8s %8s %14s %14s %10s %9s"
          % ("Q^2", "W", "|A/B|", "ref", "A/B", "resid"))
    for W in (1.209, 1.30):
        for Q2 in (0.01, 0.05, 0.2, 0.5, 1.0):
            q0 = (W ** 2 - MN ** 2 - Q2) / (2 * W)
            qz = np.sqrt(q0 ** 2 + Q2)
            q = np.array([q0, 0, 0, qz], dtype=complex)
            P = np.array([W - q0, 0, 0, -qz], dtype=complex)
            kk = w.kmom(W ** 2, mpi, MN)
            th = 0.7
            k = np.array([np.sqrt(kk ** 2 + mpi ** 2), kk * np.sin(th), 0,
                          kk * np.cos(th)], dtype=complex)
            pp = np.array([W - k[0].real, -kk * np.sin(th), 0,
                           -kk * np.cos(th)], dtype=complex)
            # all legs outgoing: -P (incoming n) + pp + (-q) + k = 0 requires
            # the W- leg to carry -q, i.e. the boson is INCOMING at q.
            mom4 = {'n~': -P, 'n': pp, 'W-': -q, 'Pi+': k}
            A = build_named(v4, mom4, ns, ff, keep)      # [mu, row, col]

            # B: the same thing, factorised.  The virtual pion is the 'Pi-'
            # leg and carries -q, exactly what the W- leg carried above.
            T = w.build(v2, {'n~': -P, 'n': pp, 'Pi-': -q, 'Pi+': k}, ns, ff)
            pole = 1j / (dot(q, q) - mpi ** 2)
            # the form factor the operator carries, divided back out so that
            # what is compared is the two ALGEBRAS, not the dressing
            fx = ff['FPPpi'](Q2) * (Q2 + mpi ** 2)
            B = [(fpi / 2.0) * src * q[m] * pole * T * fx for m in range(4)]

            r, res = ratio(A, B, P, pp, MN)
            print("  %8.3f %8.3f %14.6g %14.6g %10.5f %9.1e"
                  % (Q2, W, np.abs(r), 1.0, r.real, res))
    print("\n  Flatness is the Lorentz-structure test and it has to hold to")
    print("  machine precision.  The VALUE is not required to be 1 -- see the")
    print("  calibration below, which is what it has to match.")

    # ---------------------------------------------------------------------
    # The SAME construction on a case where the model already has the answer.
    # LNNPPFF is the nucleon's induced pseudoscalar, and it IS this pole with
    # the pi-N-N vertex on the other end instead of the pi-pi-N-N one; its
    # residue is Goldberger-Treiman and was verified independently by
    # tools/pcac_nucleon.py.  So building it the factorised way here calibrates
    # the mixing coefficient WITHOUT any of the algebra LPPoleFF uses -- and
    # whatever constant comes out of this block has to be divided out of the
    # block above before that one means anything.
    v3 = vertex(V, ('p~', 'n', 'W+'))
    kpp = with_ff(v3, 'FPP')
    vpi = vertex(V, ('p~', 'n', 'Pi+'))
    print("\nCALIBRATION on the nucleon induced pseudoscalar, same construction")
    print("vertex %s, structure carrying FPP: %s"
          % ([p.name for p in v3.particles], sorted(kpp)))
    print("  %8s %14s %14s %10s %9s"
          % ("Q^2", "|A/B|", "ref", "A/B", "resid"))
    for Q2 in (0.05, 0.2, 0.5, 1.0):
        pz = np.sqrt(Q2) / 2.0
        E = np.sqrt(MN ** 2 + pz ** 2)
        p1 = np.array([E, 0, 0, pz], dtype=complex)
        p2 = np.array([E, 0, 0, -pz], dtype=complex)
        q = p1 - p2
        A = build_named(v3, {'p~': -p1, 'n': p2, 'W+': q}, ns, ff, kpp)
        T = w.build(vpi, {'p~': -p1, 'n': p2, 'Pi+': q}, ns, ff)
        pole = 1j / (dot(q, q) - mpi ** 2)
        # divide the axial form factor back out, as fx does above: the UFO
        # structure carries FPP = FWA/(Q^2+mpi^2) while the pi-N-N vertex the
        # factorised side uses is point-like.  What is being compared is the
        # two algebras, not the dressing.
        fa = ff['FWA'](Q2)
        B = [(fpi / 2.0) * src * q[m] * pole * T * fa for m in range(4)]
        r, res = ratio(A, B, p1, p2, MN)
        print("  %8.3f %14.6g %14.6g %10.5f %9.1e"
              % (Q2, np.abs(r), 1.0, r.real, res))
    print("\n  THE TEST IS THAT THE TWO TABLES AGREE, not that either is 1.")
    print("  Their common value is this script's own mixing convention -- the")
    print("  charged-pion basis costs a sqrt2 against the cartesian one the")
    print("  operator is written in, and a sign goes with the direction of q --")
    print("  and it cancels in the comparison.  The second table is anchored on")
    print("  LNNPPFF, whose residue is Goldberger-Treiman and was verified")
    print("  independently by tools/pcac_nucleon.py and tools/nucleon_ff.py, so")
    print("  agreement means the pion-pole operator carries the same f_pi as a")
    print("  pole the model already gets right.")


if __name__ == '__main__':
    main()
