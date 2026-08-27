#!/usr/bin/env python3
"""PCAC on the nucleon weak axial current, charged and neutral.

The nucleon axial current is

    ubar [ F_A gamma^mu gamma5 + F_P q^mu gamma5 ] u

and PCAC / the off-diagonal Goldberger-Treiman relation fixes the induced
pseudoscalar to F_P = 2 MN F_A / (Q^2 + mpi^2), with no free parameter.  Its
consequence is that the contracted current is suppressed,

    q_mu <N'|A^mu|N> = 2 MN F_A mpi^2/(Q^2 + mpi^2) ubar gamma5 u

vanishing in the chiral limit.  This script measures that suppression on the
generated vertices.

The test also fixes the sign of the term, which is not obvious from the
Lagrangian: with the opposite sign the same contraction is ENHANCED by
1 + Q^2/(Q^2 + mpi^2) rather than suppressed by mpi^2/(Q^2 + mpi^2), so the two
possibilities are separated by roughly a factor 100 at Q^2 = 1 GeV^2.

MIND THE MOMENTUM ASSIGNMENT.  Everything above is a RATIO of two contractions
that share a q, and the q also appears inside the structure being tested, so a
sign slip in q is invisible in the answer's plausibility and fatal to its
meaning -- see the comment at the assignment below.  tools/nucleon_ff.py is the
independent cross-check: it solves for F_1, F_2, F_A and F_P directly and
contracts nothing.

The pseudoscalar contributes to rates only through the lepton mass, since q^mu
against the lepton tensor is proportional to m_lepton^2.

Usage:  python3 tools/pcac_nucleon.py          (CHIPT_MODEL selects the UFO)
"""
import numpy as np

from _vertex import build_named, load, vertex, with_ff        # sets sys.path

import wprod_from_ufo as w                                     # noqa: E402


def run(V, ns, ff, particles, axial_ff, pp_ff, mpi, label):
    v = vertex(V, particles)
    axial = with_ff(v, axial_ff)
    pp = with_ff(v, pp_ff)
    if not pp:
        print("\n%s: model has no %s term" % (label, pp_ff))
        return
    MN = float(ns['MNucleon'])
    G = np.diag(w.METRIC).real
    names = list(particles)
    print("\n%s   vertex %s" % (label, names))
    print("  %6s %14s %14s %10s %10s"
          % ("Q^2", "|q.J| axial", "|q.J| A+PP", "ratio", "PCAC pred"))
    for Q2 in (0.05, 0.2, 0.5, 1.0):
        pz = np.sqrt(Q2) / 2.0
        p1 = np.array([np.sqrt(MN ** 2 + pz ** 2), 0, 0, pz])
        p2 = np.array([np.sqrt(MN ** 2 + pz ** 2), 0, 0, -pz])
        # q is the OUTGOING boson momentum.  With all-outgoing UFO legs the
        # incoming nucleon enters as its antiparticle at -p1, so momentum
        # conservation is -p1 + p2 + q = 0, i.e. q = p1 - p2.  The other sign
        # does not conserve momentum, and because the boson leg supplies the
        # q^mu of the pseudoscalar structure while the contraction supplies a
        # second q, using it flips q^mu gamma5 relative to gamma^mu gamma5 and
        # reports the suppression for a model that is actually enhanced.  That
        # is exactly how the V7-V9 sign error in LNNPPFF survived this test.
        q = p1 - p2                                   # spacelike, q^2 = -Q^2
        mom = {names[0]: -p1, names[1]: p2, names[2]: q}
        out = []
        for keep in (axial, axial | pp):
            T = build_named(v, mom, ns, ff, keep)
            C = sum(G[m] * q[m] * T[m] for m in range(4))
            acc = sum(abs(w.ubar(w.uspinor(p2, MN, s2)) @ C
                          @ w.uspinor(p1, MN, s1)) ** 2
                      for s1 in range(2) for s2 in range(2))
            out.append(np.sqrt(acc))
        print("  %6.2f %14.6g %14.6g %10.5f %10.5f"
              % (Q2, out[0], out[1], out[1] / out[0], mpi ** 2 / (Q2 + mpi ** 2)))


def main():
    ns, ff, V = load()
    run(V, ns, ff, ('p~', 'n', 'W+'), 'FWA', 'FPP',
        float(ns['MPiP']), "CHARGED CURRENT")
    run(V, ns, ff, ('p~', 'p', 'Z'), 'FZA', 'FPPZ',
        float(ns['MPi0']), "NEUTRAL CURRENT (proton)")
    run(V, ns, ff, ('n~', 'n', 'Z'), 'FZA', 'FPPZ',
        float(ns['MPi0']), "NEUTRAL CURRENT (neutron)")


if __name__ == '__main__':
    main()
