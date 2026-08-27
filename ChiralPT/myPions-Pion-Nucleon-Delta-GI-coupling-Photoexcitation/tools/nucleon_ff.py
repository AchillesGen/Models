#!/usr/bin/env python3
"""Decompose the nucleon weak vertex on its four Lorentz structures.

    <p(p2)| J^mu |n(p1)>  =  ubar(p2) [ F_1 gamma^mu
                                      + F_2 i sigma^{mu nu} q_nu / (2 MN)
                                      - F_A gamma^mu gamma5
                                      - F_P q^mu gamma5 ] u(p1)

and reports F_P against the Goldberger-Treiman / PCAC value.  With q taken as
the OUTGOING boson momentum -- q = p1 - p2 for an incoming nucleon p1, which is
what momentum conservation forces on the UFO's all-outgoing legs -- PCAC needs

    F_P = - 2 MN F_A / (Q^2 + mpi^2) ,

the minus being the whole content of the test.  It is the same statement as the
textbook  F_P = + 2 M^2 F_A/(mpi^2 - q^2)  written for a current whose q^mu is
q = p_out - p_in and whose pseudoscalar structure carries a 1/M; both give a
SUPPRESSED q_mu A^mu, and it is easy to import the textbook sign into the
opposite convention and call the result verified.

WHY THIS EXISTS.  tools/pcac_nucleon.py contracts q into the current and asks
for the mpi^2/(Q^2+mpi^2) suppression, which is the physically meaningful
statement -- but it is a RATIO, and a ratio cannot tell an overall sign of F_P
from a sign of the contraction vector.  This script never contracts anything:
it solves for the four coefficients directly, so the sign it reports is the
sign that is in the vertex.  The fit is exact (residual ~1e-16), which is what
makes a sign readable at all.

THE SIGN CONVENTION IS FIXED BY F_1, NOT ASSERTED.  F_1(0) = 1 for p <-> n
(times V_ud) is CVC, so the overall phase of the basis is pinned by a quantity
the model gets right for an independent reason, and F_P's sign is then read off
in that same basis.

Usage:  python3 tools/nucleon_ff.py        (CHIPT_MODEL selects the UFO)
"""
import os

import numpy as np

from _vertex import load, vertex                              # sets sys.path

import wprod_from_ufo as w                                    # noqa: E402
from fig33_from_ufo import GAMMA, GAMMA5                       # noqa: E402

G = np.diag(w.METRIC).real


def basis(p1, p2, q, MN, gam, g5):
    """The four structures as 4x(4x4) matrices, index [structure][mu]."""
    out = []
    out.append([gam[m] for m in range(4)])                        # F_1
    sig = [[0.5j * (gam[m] @ gam[n] - gam[n] @ gam[m]) for n in range(4)]
           for m in range(4)]
    out.append([sum(G[n] * 1j * sig[m][n] * q[n] for n in range(4)) / (2 * MN)
                for m in range(4)])                               # F_2
    out.append([-gam[m] @ g5 for m in range(4)])                  # F_A
    out.append([-q[m] * g5 for m in range(4)])                    # F_P
    return out


def main():
    ns, ff, V = load()
    MN = float(ns['MNucleon'].real if hasattr(ns['MNucleon'], 'real')
               else ns['MNucleon'])
    mpi = float(ns['MPiP'].real if hasattr(ns['MPiP'], 'real') else ns['MPiP'])
    gam = [np.array(GAMMA[m], dtype=complex) for m in range(4)]
    g5 = np.array(GAMMA5, dtype=complex)

    v = vertex(V, ('p~', 'n', 'W+'))
    print("nucleon weak vertex %s     model %s"
          % ([p.name for p in v.particles], os.environ.get('CHIPT_MODEL',
                                                           'ChiPT_UFO_V9')))
    print("legs are all OUTGOING, so the physical reading is")
    print("   incoming p(p1)  ->  outgoing n(p2) + outgoing W+(q),  q = p1 - p2")
    print("and momentum conservation REQUIRES q = p1 - p2; handing the W leg")
    print("p2 - p1 instead flips F_P relative to F_A and hides a sign error.\n")
    rows = []
    for Q2 in (0.0, 0.05, 0.2, 0.5, 1.0):
        pz = np.sqrt(Q2) / 2.0
        E = np.sqrt(MN ** 2 + pz ** 2)
        p1 = np.array([E, 0, 0, pz])
        p2 = np.array([E, 0, 0, -pz])
        q = p1 - p2
        mom = {'p~': -p1, 'n': p2, 'W+': q}
        T = w.build(v, mom, ns, ff)              # [mu, row=n, col=p]
        B = basis(p1, p2, q, MN, gam, g5)

        # sandwich everything between on-shell spinors and solve the linear
        # system; 4 structures, 4 mu x 4 spin combinations = 16 equations.
        eqs, rhs = [], []
        for m in range(4):
            for s2 in range(2):
                for s1 in range(2):
                    ub = w.ubar(w.uspinor(p2, MN, s2))
                    u = w.uspinor(p1, MN, s1)
                    eqs.append([ub @ B[k][m] @ u for k in range(4)])
                    rhs.append(ub @ T[m] @ u)
        A = np.array(eqs)
        b = np.array(rhs)
        c, *_ = np.linalg.lstsq(A, b, rcond=None)
        res = np.abs(A @ c - b).max() / max(np.abs(b).max(), 1e-30)
        rows.append((Q2, c, res))

    # The UFO coupling carries an overall i and the weak prefactor
    # i ee Vud/(2 sqrt2 s_W).  Dividing the table by the Q^2 = 0 value of F_1
    # normalises to F_1(0) = 1, which is CVC -- so the phase of the basis is
    # pinned by a quantity the model gets right for an independent reason, and
    # F_P's sign is then read off in that same basis.  Measuring the prefactor
    # from the vertex rather than rebuilding it from parameters means a
    # convention change in ChiPT.fr cannot silently rescale the table.
    norm = rows[0][1][0]
    print("  overall vertex factor divided out: %s  (fixes F_1(0) = 1)"
          % np.array2string(norm, precision=6))
    print("  %6s %10s %10s %10s %12s %12s %9s %8s"
          % ("Q^2", "F_1", "F_2", "F_A", "F_P", "PCAC F_P", "F_P/PCAC",
             "resid"))
    for Q2, c, res in rows:
        c = c / norm
        gt = -2 * MN * c[2] / (Q2 + mpi ** 2)
        if Q2 == 0.0:
            # q = 0 kills both the sigma^{mu nu} q_nu and the q^mu structures,
            # so F_2 and F_P are simply not determined at this point.  Say so
            # rather than print the zero the solver returns.
            print("  %6.2f %10.6f %10s %10.6f %12s %12s %9s %8.1e"
                  % (Q2, c[0].real, "--", c[2].real, "--", "--", "--", res))
            continue
        r = (c[3] / gt).real
        print("  %6.2f %10.6f %10.6f %10.6f %12.6f %12.6f %9.5f %8.1e"
              % (Q2, c[0].real, c[1].real, c[2].real, c[3].real, gt.real,
                 r, res))
    print("\n  Anchors, none of them fitted here: F_1(0) = 1 is CVC (it is the")
    print("  normalisation), F_A(0) should be g_A = 1.2723, and |F_2| -> 3.706")
    print("  = kappa_p - kappa_n as Q^2 -> 0.  F_2 prints NEGATIVE because this")
    print("  basis carries q = p_in - p_out throughout; the textbook +3.706 is")
    print("  the same number in a basis built on p_out - p_in.")
    print("\n  F_P/PCAC must be +1.  A flat -1 is the leading minus that")
    print("  LNNPPFF carried in V7-V9.")


if __name__ == '__main__':
    main()
