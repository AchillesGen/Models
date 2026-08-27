#!/usr/bin/env python3
"""The two Delta decay widths, computed FROM the generated vertices.

This is the acceptance test for V10's headline change.  Through V9 the Delta's
couplings hD, G1 and G2 were external numbers and the widths were whatever they
came out to be; from V10 the widths GamNPi and GamNGam are the external inputs
and the couplings are derived from them.  That inversion is only worth anything
if the model actually delivers the widths it was handed, so this recomputes them
from the UFO vertices -- not from the formulae ChiPT.fr inverts -- and compares.

    Gamma(Delta++ -> p pi+)   from  ['p~', 'Delta++', 'Pi-']
    Gamma(Delta+  -> p gamma) from  ['p~', 'DeltaP',  'A']

Both are two-body decays of a spin-3/2 state at rest,

    Gamma = k/(8 pi M^2) * (1/4) sum_{lambda, spins} |M|^2

with the 1/4 averaging over the four Delta polarisations.  The Rarita-Schwinger
spinors come from delta_couplings.rs_spinor, which is a REST-FRAME construction,
so the Delta is put at rest and nothing has to be boosted.

FORM FACTORS ARE SET TO 1.  FpiNDelta is sqrt(X_pi(p_Delta^2)) and equals 1 at
p_Delta^2 = M_Delta^2 by construction, so at the pole it makes no difference;
setting it to 1 makes that explicit rather than relying on it.

Usage:  python3 tools/delta_widths.py        (CHIPT_MODEL selects the UFO)
"""
import os

import numpy as np

from _vertex import load, vertex                              # sets sys.path

import wprod_from_ufo as w                                    # noqa: E402
import delta_couplings as dc                                  # noqa: E402
from fig33_from_ufo import kmom, METRIC                       # noqa: E402

ONE = {n: (lambda x: 1.0) for n in
       ('FpiNDelta', 'FgNDeltaPG1', 'FgNDeltaPG2',
        'FgNDeltaNG1', 'FgNDeltaNG2')}


def rp(x):
    return float(x.real) if isinstance(x, complex) else float(x)


def photon_pols(k):
    """Two transverse polarisation vectors for a photon along +/- z."""
    n = np.array([0.0, k[1], k[2], k[3]])
    n = n / np.linalg.norm(n[1:])
    # build two unit vectors orthogonal to n
    a = np.array([0.0, 1.0, 0.0, 0.0])
    if abs(np.dot(n[1:], a[1:])) > 0.9:
        a = np.array([0.0, 0.0, 1.0, 0.0])
    e1 = a - np.dot(a[1:], n[1:]) * n
    e1 = e1 / np.linalg.norm(e1[1:])
    e2 = np.zeros(4)
    e2[1:] = np.cross(n[1:], e1[1:])
    return [e1.astype(complex), e2.astype(complex)]


def main():
    ns, ff, V = load()
    ff = dict(ff, **ONE)
    MN, MD = rp(ns['MNucleon']), rp(ns['MDelta'])
    mpi = rp(ns['MPiP'])
    G = np.diag(METRIC).real
    pD = np.array([MD, 0, 0, 0], dtype=complex)

    print("Delta widths recomputed from the vertices    model %s"
          % os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V9'))
    print("M_Delta = %.4f   hD = %.6f   G1 = %.6f   G2 = %.6f\n"
          % (MD, rp(ns['hD']), rp(ns['G1']), rp(ns['G2'])))

    # ---------------------------------------------------------- Delta -> N pi
    k = kmom(MD ** 2, mpi, MN)
    kpi = np.array([np.sqrt(k ** 2 + mpi ** 2), 0, 0, k], dtype=complex)
    pN = np.array([np.sqrt(k ** 2 + MN ** 2), 0, 0, -k], dtype=complex)
    # ['p~','Delta++','Pi-'] with an OUTGOING p (so the 'p~' leg carries -pN)
    # and an OUTGOING pi+ (the 'Pi-' leg at -kpi); the Delta is the incoming
    # one, entering its own leg at +pD... all legs outgoing sum to zero:
    #   -pN + pD - kpi = 0.
    v = vertex(V, ('p~', 'Delta++', 'Pi-'))
    T = w.build(v, {'p~': -pN, 'Delta++': pD, 'Pi-': -kpi}, ns, ff)
    acc = 0.0
    for tl in dc.LAMBDAS:
        urs = dc.rs_spinor(pD, MD, tl)
        for s in range(2):
            ub = w.ubar(w.uspinor(pN, MN, s))
            acc += abs(sum(G[a] * (ub @ T[a] @ urs[a]) for a in range(4))) ** 2
    gpi = k / (8 * np.pi * MD ** 2) * acc / 4.0
    want = rp(ns['GamNPi']) if 'GamNPi' in ns else float('nan')
    print("  Gamma(Delta++ -> p pi+)   k = %.5f   = %.6f GeV" % (k, gpi))
    print("  card GamNPi                                = %.6f GeV" % want)
    print("  ratio                                      = %.6f\n" % (gpi / want))

    # ------------------------------------------------------- Delta -> N gamma
    kg = (MD ** 2 - MN ** 2) / (2 * MD)
    kph = np.array([kg, 0, 0, kg], dtype=complex)
    pN = np.array([np.sqrt(kg ** 2 + MN ** 2), 0, 0, -kg], dtype=complex)
    v = vertex(V, ('p~', 'Delta+', 'A'))
    T = w.build(v, {'p~': -pN, 'Delta+': pD, 'A': -kph}, ns, ff)
    acc = 0.0
    for eps in photon_pols(kph):
        for tl in dc.LAMBDAS:
            urs = dc.rs_spinor(pD, MD, tl)
            for s in range(2):
                ub = w.ubar(w.uspinor(pN, MN, s))
                amp = sum(G[a] * G[m] * np.conj(eps[m])
                          * (ub @ T[a, m] @ urs[a])
                          for a in range(4) for m in range(4))
                acc += abs(amp) ** 2
    ggam = kg / (8 * np.pi * MD ** 2) * acc / 4.0
    want = rp(ns['GamNGam']) if 'GamNGam' in ns else float('nan')
    print("  Gamma(Delta+ -> p gamma)  k = %.5f   = %.8f GeV" % (kg, ggam))
    print("  card GamNGam                               = %.8f GeV" % want)
    print("  ratio                                      = %.6f" % (ggam / want))
    print("\n  Both ratios must be 1.  They are the statement that V10's")
    print("  inversion of the width formulae is right; a V9-style model with")
    print("  external couplings has no GamNPi/GamNGam to compare against.")


if __name__ == '__main__':
    main()
