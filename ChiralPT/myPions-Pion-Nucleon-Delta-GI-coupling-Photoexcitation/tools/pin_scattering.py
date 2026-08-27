#!/usr/bin/env python3
"""pi+ p -> pi+ p from the model, against the unitarity limit at the Delta.

THIS IS THE TEST WITH NO NEUTRINO IN IT.  Every other check on the weak sector
runs through a neutrino beam and is therefore entangled with the helicity
factor of 2 that tools/imd_check.py measured.  Pion-nucleon elastic scattering
uses the SAME strong pi-N-Delta and pi-N-N vertices that the weak single-pion
Delta diagram is built from, and none of the weak machinery -- no lepton
current, no W propagator, no spin average over a neutrino.  If the strong
sector carries a factor, it shows up here, cleanly.

AND THE ANSWER IS FIXED BY UNITARITY, WITH NO PARAMETERS.  pi+ p is pure
I = 3/2, and at the Delta the resonance is elastic (BR(Delta -> N pi) = 1), so
the peak elastic cross section is pinned:

    sigma_peak = (4 pi / k^2) (2J+1)/((2s1+1)(2s2+1)) = 8 pi / k^2

with k the pi-N centre-of-mass momentum at W = M_Delta.  That is ~190 mb at the
physical Delta, and it is what is measured -- pi+ p peaks near 200 mb.  A tree
model cannot exceed it except by violating unitarity, so this is a ceiling, not
a fit.  A model that lands at 2x the limit has found its factor 2.

WHAT THE MODEL SHOULD GIVE, allowing for its own imperfections: the Delta
coupling in the UFO produces Gamma(Delta++ -> p pi+) = 96.7 MeV (computed from
scratch in tools/adler_ndelta.py's companion check) while the propagator uses
the card's 102 MeV, so the implemented elasticity is 96.7/102 = 0.948 and the
peak should come out at about 0.948^2 = 0.90 of the unitarity limit.

X_pi AT THE PEAK IS EXACTLY 1.  Both vertices of the s-channel Delta here are
strong pi-N-Delta vertices, so both carry FpiNDelta and the diagram picks up
X_pi rather than sqrt(X_pi) -- the double-counting ChiPT.fr warns about.  At
W = M_Delta, X_pi = 1 by construction, so the peak value is untouched by it;
away from the peak it is, which is why the scan is read for its peak.

Usage:  python3 tools/pin_scattering.py        (CHIPT_MODEL selects the UFO)
"""
import argparse
import os

import numpy as np

from _vertex import load                                       # sets sys.path

from fig33_from_ufo import (build, build_scalar_vec, uspinor, ubar,
                            prop_fermion, rs_numerator, dot, METRIC, kmom)

MB = 0.389379            # 1 GeV^-2 in mb


def vertex(V, names):
    want = sorted(names)
    out = [v for v in V if sorted(p.name for p in v.particles) == want]
    if not out:
        raise KeyError(names)
    return out[0]


def amplitude(V, ns, ff, W, ct, opt):
    """M[row, col] for pi+(k) p(p) -> pi+(k') p(p') at cms energy W."""
    MN, MD, mpi = ns['MNucleon'], ns['MDelta'], ns['MPiP']
    GD = float(ns['WDeltaP'])
    k = kmom(W ** 2, mpi, MN)
    Epi, EN = np.sqrt(k ** 2 + mpi ** 2), np.sqrt(k ** 2 + MN ** 2)
    st = np.sqrt(max(1 - ct ** 2, 0.0))
    kin = np.array([Epi, 0, 0, k], dtype=complex)
    p = np.array([EN, 0, 0, -k], dtype=complex)
    kout = np.array([Epi, k * st, 0, k * ct], dtype=complex)
    pp = np.array([EN, -k * st, 0, -k * ct], dtype=complex)
    vs = p + kin                       # s-channel
    vu = p - kout                      # u-channel
    M = np.zeros((4, 4), dtype=complex)

    if opt.get('delta_s', True):
        # pi+ p -> Delta++ -> pi+ p.  Incoming pi+ enters as the 'Pi-' leg at
        # -k; the outgoing pi+ is the 'Pi+' leg at +k'.
        Vp = build(vertex(V, ['p~', 'Delta++', 'Pi-']),
                   {'p~': -p, 'Delta++': vs, 'Pi-': -kin}, ns, ff)
        Vd = build(vertex(V, ['Delta++~', 'p', 'Pi+']),
                   {'Delta++~': -vs, 'p': pp, 'Pi+': kout}, ns, ff)
        N = rs_numerator(vs, MD)
        den = dot(vs, vs) - MD ** 2 + 1j * MD * GD
        for a in range(4):
            for b in range(4):
                M += (METRIC[a, a] * METRIC[b, b]
                      * Vd[a] @ (1j * N[a, b] / den) @ Vp[b])

    if opt.get('nucleon_u', True):
        # p -> n pi+ (emit the FINAL pion), then pi+ n -> p
        Ve = build(vertex(V, ['p~', 'n', 'Pi+']),
                   {'p~': -p, 'n': vu, 'Pi+': kout}, ns, ff)
        Va = build(vertex(V, ['n~', 'p', 'Pi-']),
                   {'n~': -vu, 'p': pp, 'Pi-': -kin}, ns, ff)
        M += Va @ prop_fermion(vu, MN) @ Ve

    if opt.get('delta_u', True):
        try:
            Ve = build(vertex(V, ['p~', 'Delta0', 'Pi+']),
                       {'p~': -p, 'Delta0': vu, 'Pi+': kout}, ns, ff)
            Va = build(vertex(V, ['Delta0~', 'p', 'Pi-']),
                       {'Delta0~': -vu, 'p': pp, 'Pi-': -kin}, ns, ff)
            N = rs_numerator(vu, MD)
            den = dot(vu, vu) - MD ** 2 + 1j * MD * GD
            for a in range(4):
                for b in range(4):
                    M += (METRIC[a, a] * METRIC[b, b]
                          * Va[a] @ (1j * N[a, b] / den) @ Ve[b])
        except KeyError:
            pass

    if opt.get('contact', True):
        # the Weinberg-Tomozawa two-pion contact term
        try:
            M += build(vertex(V, ['p~', 'p', 'Pi-', 'Pi+']),
                       {'p~': -p, 'p': pp, 'Pi-': -kin, 'Pi+': kout}, ns, ff)
        except KeyError:
            pass
    return M, p, pp


def sigma(V, ns, ff, W, opt, n=48):
    """Total elastic cross section in mb."""
    MN = ns['MNucleon']
    x, w = np.polynomial.legendre.leggauss(n)
    tot = 0.0
    for ct, wt in zip(x, w):
        M, p, pp = amplitude(V, ns, ff, W, ct, opt)
        acc = 0.0
        for s1 in range(2):
            u1 = uspinor(p, MN, s1)
            for s2 in range(2):
                acc += abs(ubar(uspinor(pp, MN, s2)) @ M @ u1) ** 2
        tot += wt * acc / 2.0            # average over the initial proton spin
    return MB * tot / (32 * np.pi * W ** 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--delta-only', action='store_true')
    a = ap.parse_args()
    ns, ff, V = load()
    MN, MD, mpi = ns['MNucleon'], ns['MDelta'], ns['MPiP']
    opt = dict(delta_s=True, nucleon_u=not a.delta_only,
               delta_u=not a.delta_only, contact=not a.delta_only)

    kpk = kmom(MD ** 2, mpi, MN)
    lim = MB * 8 * np.pi / kpk ** 2
    print("pi+ p -> pi+ p     model %s" % os.environ.get('CHIPT_MODEL',
                                                         'ChiPT_UFO_V9'))
    print("M_Delta = %.4f  Gamma(card) = %.4f  k(peak) = %.4f GeV"
          % (MD, ns['WDeltaP'], kpk))
    print("UNITARITY LIMIT at the peak: 8 pi / k^2 = %.1f mb" % lim)
    print("   (measured pi+ p peaks near 200 mb; the physical Delta sits at")
    print("    1232 MeV where the limit is ~190 mb)\n")
    # The bound is W-dependent (k grows with W), so each row is compared with
    # 8 pi / k(W)^2 at ITS OWN W.  Comparing everything with the value at the
    # pole makes the high-W rows look like violations when they are not.
    print("  %8s %12s %12s %12s"
          % ("W (GeV)", "sigma (mb)", "8pi/k(W)^2", "ratio"))
    for W in (1.12, 1.16, 1.19, MD, 1.23, 1.26, 1.30, 1.40):
        s = sigma(V, ns, ff, W, opt)
        kW = kmom(W ** 2, mpi, MN)
        lw = MB * 8 * np.pi / kW ** 2
        print("  %8.4f %12.2f %12.1f %12.3f" % (W, s, lw, s / lw))
    speak = sigma(V, ns, ff, MD, opt)
    print("\n  peak / unitarity limit = %.3f" % (speak / lim))
    print("  expected ~0.90 from the implemented elasticity "
          "(Gamma_vertex/Gamma_prop = 96.7/102)")
    if speak / lim > 1.0:
        print("\n  *** ABOVE THE UNITARITY LIMIT -- by %.2fx ***"
              % (speak / lim))


if __name__ == '__main__':
    main()
