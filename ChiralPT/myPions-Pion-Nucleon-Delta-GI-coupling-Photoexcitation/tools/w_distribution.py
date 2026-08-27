#!/usr/bin/env python3
"""sigma(W < Wmax) for one channel, i.e. the cumulative hadronic-mass
distribution.

Differences between successive Wmax give the fraction of the cross section in
each W bin, which is what decides how much a W-dependent effect (a resonance, a
form factor, a t-channel exchange calibrated in photoproduction) can move the
total.

Usage:  python3 tools/w_distribution.py <channel> <E_nu/GeV> <Wmax/GeV>
        for w in 1.15 1.25 1.30 1.35 1.40; do
            python3 tools/w_distribution.py ppip 1.25 $w
        done
"""
import os
import sys

import numpy as np                                            # noqa: F401

sys.path.insert(0, os.environ.get(
    'CHIPT_DIR', os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import wprod_from_ufo as w                                     # noqa: E402

MODEL = os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V8')


def main():
    ch, enu, wmax = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    sys.argv = ['x']                       # wprod_from_ufo parses argv on import
    P, V = w.load_ufo(MODEL)
    ns = w.parameter_namespace(P)
    ff = w.form_factors(ns, True)
    opt = dict(born=True, delta=True, dwidth=True, wwidth=True,
               wmax=wmax, mmu=float(ns['MMU']))
    print("%-5s %.4f %.3f %.6g"
          % (ch, enu, wmax, w.sigma(ch, enu, V, ns, ff, opt, (20, 12, 12, 8))),
          flush=True)


if __name__ == '__main__':
    main()
