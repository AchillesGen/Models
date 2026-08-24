#!/usr/bin/env python3
"""CVC check on the weak vector N -> Delta transition.

The isovector source in ChiPT.fr is normalised so its third component carries
the photon with coefficient exactly 1.  CVC therefore fixes the W vector
N -> Delta transition to be

    V_ud sqrt(3) / (2 sw sqrt(2))

times the model's own photon N -> Delta transition, the sqrt(3) being the
p -> Delta++ isospin Clebsch.  The test is internal: it compares the model
against itself, so it needs no external input and no reference calculation.

A sign error here is invisible in photoproduction (which lives at Q^2 = 0, where
the transition form factor is 1) but makes the weak vector piece interfere
destructively with the axial one instead of constructively.

Usage:  python3 tools/cvc_ndelta.py          (CHIPT_MODEL selects the UFO)
"""
import numpy as np

from _vertex import build_named, load, vertex, with_ff

# The vector transition is identified by the form factor it carries, not by
# the generated structure names, which FeynRules reshuffles between versions.


def main():
    ns, ff, V = load()
    ff['FVND'] = lambda q2: 1.0    # compare normalisations, not form factors
    for n in ('FgNDeltaPG1', 'FgNDeltaPG2', 'FgNDeltaNG1', 'FgNDeltaNG2'):
        ff[n] = lambda q2: 1.0

    MN = ns['MNucleon']
    P = np.array([MN, 0.0, 0.0, 0.0])
    q = np.array([0.30, 0.10, 0.05, 0.35])
    vs = P + q

    vW = vertex(V, ('p~', 'Delta++', 'W-'))
    vA = vertex(V, ('p~', 'Delta+', 'A'))
    W = build_named(vW, {'p~': -P, 'Delta++': vs, 'W-': -q},
                    ns, ff, with_ff(vW, 'FVND'))
    A = build_named(vA, {'p~': -P, 'Delta+': vs, 'A': -q},
                    ns, ff, with_ff(vA, 'FVND'))

    a, b = np.asarray(W), np.asarray(A)
    m = np.abs(b) > 1e-12 * np.abs(b).max()
    got = (a[m] * np.conj(b[m])).sum() / (np.abs(b[m]) ** 2).sum()
    resid = np.abs(a[m] - got * b[m]).max() / np.abs(a).max()
    real = lambda x: x.real if isinstance(x, complex) else float(x)
    want = real(ns['Vud']) * np.sqrt(3.0) / (2 * real(ns['sw']) * np.sqrt(2))

    print("W / photon  measured = %+.8f      residual %.2e" % (got.real, resid))
    print("CVC expects          = %+.8f" % want)
    print("measured / expected  = %+.8f" % (got.real / want))


if __name__ == '__main__':
    main()
