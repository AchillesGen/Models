#!/usr/bin/env python3
"""
eprod_from_ufo.py -- the running-width factor for ELECTRON scattering,
gamma*(q) N -> pi N' computed directly from the ChiPT UFO.

The electromagnetic counterpart of the width_study.py / wprod_from_ufo.py
calculation behind the neutrino running-width factor.  The hadronic current is
the same five (here: up to six) topologies, read from the same UFO with the same
evaluator, spinors and propagators (imported from fig33_from_ufo), with the
photon in place of the W:

    s- and u-channel nucleon, t-channel pion (charged pions), the Kroll-Ruderman
    contact (charged pions), s- and u-channel Delta.

Unlike fig33_from_ufo.py the photon is VIRTUAL and every form factor is the
one Sherpa evaluates (wprod_from_ufo.form_factors, i.e. FormFactors.C), and no
Davidson-Workman F_B is applied, because Sherpa does not have it.  So with the
fixed pole width this is the amplitude Achilles generates the electron events
with.

What changes between the two prescriptions is exactly what width_study.py
changes for the neutrino factor:

    pole   the UFO as shipped: M = 1.209, Gamma = 0.102 FIXED, in the s- and
           u-channel Delta alike (Comix's DECAY-block width)
    bw     the PDG Breit-Wigner numbers M = 1.232, Gamma(N pi) = 0.117,
           Gamma(N gamma) = 0.66 MeV, with G1, G2, hD re-derived from them, and
           the HNV running width Gamma(s) = Gamma_0 (M/sqrt s)(k/k_0)^3, zero
           below the pi N threshold (so zero in the u channel)

OUTPUT.  For each channel and (W, Q^2) the angle-integrated virtual-photon
responses

    S_T = 1/2 sum_spins int dcos(th*) (|eps_+ . J|^2 + |eps_- . J|^2)
    S_L =     sum_spins int dcos(th*) (Q^2/|q*|^2) |J^0|^2        (= |eps_0 . J|^2)

times k*/W, in the hadronic CM with q along +z.  sigma_T + eps sigma_L is
proportional to S_T + eps S_L with a factor that is the same for both
prescriptions (the flux and k* do not depend on the Delta), so the event weight
is

    w = (S_T^bw + eps S_L^bw) / (S_T^pole + eps S_L^pole)      at the event's
                                                               W, Q^2, eps.

The pion azimuth is not integrated: the spin-summed |eps_lambda . J|^2 is
invariant under rotations about q, so phi* = 0 is exact for S_T and S_L.
S_L uses eps_0 . J = (Q/|q*|) J^0, which holds by current conservation and is
finite at Q^2 -> 0; q.J is checked at every point (--check).

Channels (gamma* N_i -> N_f pi):
    ppi0  p -> p pi0      npip  p -> n pi+      nnpi0  n -> n pi0      ppim  n -> p pi-

Run:
    python3 eprod_from_ufo.py --ufo ChiPT_UFO_V16 --out eprod_width_V16.csv
        [--W 1.08:1.80:0.01] [--Q2 0,0.05,...] [--nth 16] [--check]
"""
import argparse
import csv
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig33_from_ufo import (load_ufo, parameter_namespace, build,
                            build_scalar_vec, vertex_by_particles, uspinor,
                            ubar, prop_fermion, prop_scalar, rs_numerator,
                            kmom, dot, METRIC, POL)
import wprod_from_ufo as W
import vecmeson as VM

CHANNELS = {
    'ppi0':  dict(Ni='p', Nf='p', pion='Pi0', D_s='Delta+', D_u='Delta+'),
    'npip':  dict(Ni='p', Nf='n', pion='Pi+', D_s='Delta+', D_u='Delta0'),
    'nnpi0': dict(Ni='n', Nf='n', pion='Pi0', D_s='Delta0', D_u='Delta0'),
    'ppim':  dict(Ni='n', Nf='p', pion='Pi-', D_s='Delta0', D_u='Delta+'),
}
ANTI = {'Pi0': 'Pi0', 'Pi+': 'Pi-', 'Pi-': 'Pi+'}
BWSET = {'MDelta': 1.232, 'GamNPi': 0.117, 'GamNGam': 0.00066}


def anti(n):
    return ANTI.get(n, n + '~')


def _rp(x):
    return float(x.real) if isinstance(x, complex) else float(x)


def _vertex(V, names):
    try:
        return vertex_by_particles(V, names)
    except (KeyError, StopIteration, IndexError, ValueError):
        return None


def setup(ufo, pset):
    """(V, ns, ff, running) for one prescription, as width_study.py sets it up."""
    P, V = load_ufo(ufo)
    if pset == 'bw':
        tot = BWSET['GamNPi'] + BWSET['GamNGam']
        for p in P.all_parameters:
            if p.name in BWSET:
                p.value = BWSET[p.name]
            elif p.name.startswith('WDelta'):
                p.value = tot
    ns = parameter_namespace(P)
    ns['WDeltaP'] = _rp(ns['GamNPi']) + _rp(ns['GamNGam'])
    ff = W.form_factors(ns, os.path.exists(os.path.join(ufo, 'form_factors.py')))
    return V, ns, ff, pset == 'bw'


def current(ch, q, P, k, pp, V, ns, ff, running, delta=True, born=True, vec=None):
    """H[mu, row, col] for gamma*(q) N(P) -> pi(k) N'(p'), photon index up.

    vec: None, or a dict of vecmeson.current options (e.g. {'vmff': 'monopole'})
    to add the t-channel rho/omega exchange of nucl-th/0509020 (vecmeson.py).
    """
    c = CHANNELS[ch]
    Ni, Nf, pion = c['Ni'], c['Nf'], c['pion']
    aNi, aNf, apion = anti(Ni), anti(Nf), anti(pion)
    MN, MD = _rp(ns['MNucleon']), _rp(ns['MDelta'])
    GD = _rp(ns['WDeltaP'])
    mpi = _rp(ns['MPi0'] if pion == 'Pi0' else ns['MPiP'])
    vs, vu, vt = P + q, P - k, q - k
    H = np.zeros((4, 4, 4), dtype=complex)

    if born:
        # s-channel nucleon
        Vg = build(_vertex(V, [aNi, Ni, 'A']), {aNi: -P, Ni: vs, 'A': -q}, ns, ff)
        Vp = build(_vertex(V, [aNi, Nf, pion]), {aNi: -vs, Nf: pp, pion: k}, ns, ff)
        S = prop_fermion(vs, MN)
        for m in range(4):
            H[m] += Vp @ S @ Vg[m]
        # u-channel nucleon (the photon does not change the nucleon)
        Vp2 = build(_vertex(V, [aNi, Nf, pion]), {aNi: -P, Nf: vu, pion: k}, ns, ff)
        Vg2 = build(_vertex(V, [aNf, Nf, 'A']), {aNf: -vu, Nf: pp, 'A': -q}, ns, ff)
        Su = prop_fermion(vu, MN)
        for m in range(4):
            H[m] += Vg2[m] @ Su @ Vp2
        if pion != 'Pi0':
            # pion in flight: gamma* -> pi(k) + pi_bar(vt), pi_bar absorbed by the nucleon
            Vgpp = build_scalar_vec(_vertex(V, ['A', pion, apion]),
                                    {'A': -q, pion: k, apion: vt}, ns, ff)
            Vpi = build(_vertex(V, [aNi, Nf, pion]), {aNi: -P, Nf: pp, pion: -vt}, ns, ff)
            D = prop_scalar(vt, mpi)
            for m in range(4):
                H[m] += Vgpp[m] * D * Vpi
            vk = _vertex(V, [aNi, Nf, 'A', pion])
            if vk is not None:
                H += build(vk, {aNi: -P, Nf: pp, 'A': -q, pion: k}, ns, ff)

    if delta:
        # Delta, with the prescription's width
        def X(l):                       # HNV: (M/sqrt l)(k/k0)^3, 0 below threshold
            mp0 = _rp(ns['MPi0'])
            if l < (MN + mp0) ** 2:
                return 0.0
            return (MD / np.sqrt(l)) * (kmom(l, mp0, MN) / kmom(MD ** 2, mp0, MN)) ** 3
        s2, u2 = dot(vs, vs).real, dot(vu, vu).real
        Gs = GD * X(s2) if running else GD
        Gu = GD * X(u2) if running else GD
        Ds = dot(vs, vs) - MD ** 2 + 1j * MD * Gs
        Du = dot(vu, vu) - MD ** 2 + 1j * MD * Gu
        Dsn, Dun = c['D_s'], c['D_u']
        VgD = build(_vertex(V, [aNi, Dsn, 'A']), {aNi: -P, Dsn: vs, 'A': -q}, ns, ff)
        VpD = build(_vertex(V, [anti(Dsn), Nf, pion]), {anti(Dsn): -vs, Nf: pp, pion: k}, ns, ff)
        Ns = rs_numerator(vs, MD)
        VpD2 = build(_vertex(V, [aNi, Dun, pion]), {aNi: -P, Dun: vu, pion: k}, ns, ff)
        VgD2 = build(_vertex(V, [anti(Dun), Nf, 'A']), {anti(Dun): -vu, Nf: pp, 'A': -q}, ns, ff)
        Nu = rs_numerator(vu, MD)
        for m in range(4):
            acc = np.zeros((4, 4), dtype=complex)
            for nu in range(4):
                for et in range(4):
                    g = METRIC[nu, nu] * METRIC[et, et]
                    acc += g * VpD[nu] @ (1j * Ns[nu, et] / Ds) @ VgD[et, m]
                    acc += g * VgD2[nu, m] @ (1j * Nu[nu, et] / Du) @ VpD2[et]
            H[m] += acc
    if vec is not None:
        # Fig33v2.m conventions; -1 relative to this amplitude, fixed by
        # reproducing fig33_vecmeson.m on shell to 1e-4 in all four channels
        Q2 = -dot(q, q).real
        H -= VM.current(ch, q, k, Q2=Q2, **vec)
    return H


def responses(ch, Wh, Q2, setup_, nth=16, check=False, vec=None):
    """(S_T, S_L) times k*/W, angle-integrated, at (W, Q^2)."""
    V, ns, ff, running = setup_
    MN = _rp(ns['MNucleon'])
    pion = CHANNELS[ch]['pion']
    mpi = _rp(ns['MPi0'] if pion == 'Pi0' else ns['MPiP'])
    if Wh <= MN + mpi:
        return 0.0, 0.0, 0.0
    nu = (Wh ** 2 - MN ** 2 - Q2) / (2 * Wh)
    qa = np.sqrt(nu ** 2 + Q2)
    q = np.array([nu, 0, 0, qa], dtype=complex)
    P = np.array([Wh - nu, 0, 0, -qa], dtype=complex)
    ks = kmom(Wh ** 2, mpi, MN)
    Epi = np.sqrt(ks ** 2 + mpi ** 2)
    x, wts = np.polynomial.legendre.leggauss(nth)
    ST = SL = 0.0
    worst = 0.0
    for xi, wi in zip(x, wts):
        sth = np.sqrt(1 - xi ** 2)
        k = np.array([Epi, ks * sth, 0, ks * xi], dtype=complex)
        pp = P + q - k
        H = current(ch, q, P, k, pp, V, ns, ff, running, vec=vec)
        for si in range(2):
            ui = uspinor(P, MN, si)
            for sf in range(2):
                ub = ubar(uspinor(pp, MN, sf))
                J = np.array([ub @ H[m] @ ui for m in range(4)])
                for e in POL:
                    ST += wi * 0.5 * abs(sum(METRIC[m, m] * e[m] * J[m] for m in range(4))) ** 2
                SL += wi * (Q2 / qa ** 2) * abs(J[0]) ** 2
                if check:
                    qJ = sum(METRIC[m, m] * q[m] * J[m] for m in range(4))
                    worst = max(worst, abs(qJ) / (np.abs(J).max() * qa + 1e-300))
    f = ks / Wh
    return ST * f, SL * f, worst


def _grid(spec):
    if ':' in spec:
        a, b, d = (float(v) for v in spec.split(':'))
        return list(np.round(np.arange(a, b + d / 2, d), 6))
    return [float(v) for v in spec.split(',')]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ufo', default='ChiPT_UFO_V16')
    ap.add_argument('--out', default='eprod_width_V16.csv')
    ap.add_argument('--channels', default='ppi0,npip,nnpi0,ppim')
    ap.add_argument('--W', default='1.08:1.80:0.01')
    ap.add_argument('--Q2', default='0,0.05,0.1,0.15,0.2,0.3,0.4,0.55,0.7,0.85,1.0')
    ap.add_argument('--nth', type=int, default=16)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    S = {p: setup(a.ufo, p) for p in ('pole', 'bw')}
    print("pole: M=%.4f G=%.5f   bw: M=%.4f G0=%.5f (running)"
          % (_rp(S['pole'][1]['MDelta']), _rp(S['pole'][1]['WDeltaP']),
             _rp(S['bw'][1]['MDelta']), _rp(S['bw'][1]['WDeltaP'])), flush=True)
    rows, t0 = [], time.time()
    for ch in a.channels.split(','):
        for Q2 in _grid(a.Q2):
            for Wh in _grid(a.W):
                tp, lp, cp = responses(ch, Wh, Q2, S['pole'], a.nth, a.check)
                tb, lb, cb = responses(ch, Wh, Q2, S['bw'], a.nth, a.check)
                rows.append(dict(channel=ch, W=Wh, Q2=Q2, ST_pole=tp, SL_pole=lp,
                                 ST_bw=tb, SL_bw=lb))
                if a.check:
                    print("  %s W=%.3f Q2=%.2f  R_T=%.4f R_L=%s  |q.J|/|q||J| %.1e %.1e"
                          % (ch, Wh, Q2, tb / tp if tp else 0,
                             '%.4f' % (lb / lp) if lp else '-', cp, cb), flush=True)
            print("%s Q2=%.2f done [%.0fs]" % (ch, Q2, time.time() - t0), flush=True)
    with open(a.out, 'w', newline='') as f:
        f.write("# eprod_from_ufo.py, UFO %s; S_T, S_L x k*/W (arbitrary common units);"
                " pole = fixed width at the pole, bw = PDG BW params + HNV running width\n"
                % a.ufo)
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    print("wrote", a.out, len(rows), "rows")


if __name__ == '__main__':
    main()
