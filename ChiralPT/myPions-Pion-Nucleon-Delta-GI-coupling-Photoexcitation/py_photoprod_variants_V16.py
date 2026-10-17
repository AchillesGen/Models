#!/usr/bin/env python3
"""py_photoprod_variants_V16.py -- the semi-analytic photoproduction curves of the
paper's Fig. 2, Fig. A3 (line shape) and Fig. A4, for model V16.

Everything is the V16 UFO evaluated by eprod_from_ufo.current at Q^2 = 0 (the
same vertices, form factors and fixed pole width Sherpa uses; with the fixed
width it reproduces the Sherpa V16 scan to ~1%, the known complex-mass RS
numerator offset).  The variants:

  base    V16 itself (vertex-level form factors, fixed pole width): the Python
          twin of the Sherpa curve, the reference the next two build on.
  vec     base + t-channel omega/rho exchange (vecmeson.py, ELA couplings;
          reproduces fig33_vecmeson.m to 1e-4).
  bw      vec with the Breit-Wigner parameters M = 1.232, Gamma(N pi) = 117 MeV,
          Gamma(N gamma) = 0.66 MeV (h_D, G1, G2 re-derived from them) and the
          HNV width Gamma_0 (M/W)(k/k0)^3, zero below threshold (u channel).
          Vertex form factors kept as in V16.
  v15     base with the V16 piNDelta vertex form factor FDeltaLam
          set to 1, i.e. the V15 mode; couplings unchanged.
  ampff   ALTERNATIVE, not part of the chain: form factors at AMPLITUDE level
          instead of on the vertices, the prescription of Ref. [34]:
          Fhat_B(s,u,t) on the Born terms and sqrt(X_pi(s,u)) on both Delta
          diagrams, vertex Delta form factor FDeltaLam set to 1, fixed width.
          (Before 2026-10-15 vec and bw were built on ampff; that CSV is kept
          as photoprod_variants_V16.ampbase.csv.)

and, for the line-shape figure (Delta diagrams only, gamma p -> p pi0):

  delta_const   V16 Delta term alone, constant width at the pole (this work)
  delta_k3      the same with the HNV energy-dependent width, nothing else changed
  bw_formula    the Breit-Wigner cross section, Eq. (E2), pole mass and widths,
                Gamma_Npi ~ k^3, Gamma_Ngamma ~ q^3, isospin factor 2/3

Writes photoprod_variants_V16.csv (Egamma, channel, curve, sigma_ub).
Run:  python3 py_photoprod_variants_V16.py [--nth 16] [--de 0.005]
"""
import argparse, csv, time
import numpy as np
import eprod_from_ufo as E
import vecmeson as VM
from fig33_from_ufo import (FhatB, make_Xpi, kmom, uspinor, ubar, METRIC, POL, HBARC2)

CH = {'pi-p': 'ppim', 'pi+n': 'npip', 'pi0p': 'ppi0', 'pi0n': 'nnpi0'}


def sigma_curves(ch, Wh, setups, nth):
    """{curve: sigma_ub} at W for one fig33-named channel."""
    ech = CH[ch]
    out = {}
    x, wts = np.polynomial.legendre.leggauss(nth)
    for name, (S, ampff, vec, which) in setups.items():
        V, ns, ff, running = S
        MN = E._rp(ns['MNucleon'])
        pion = E.CHANNELS[ech]['pion']
        mpi = E._rp(ns['MPi0'] if pion == 'Pi0' else ns['MPiP'])
        if Wh <= MN + mpi:
            out[name] = 0.0
            continue
        MD = E._rp(ns['MDelta'])
        Xpi = make_Xpi(MN, E._rp(ns['MPi0']), MD)
        qs = (Wh ** 2 - MN ** 2) / (2 * Wh)
        q = np.array([qs, 0, 0, qs], dtype=complex)
        P = np.array([Wh - qs, 0, 0, -qs], dtype=complex)
        ks = kmom(Wh ** 2, mpi, MN)
        Epi = np.sqrt(ks ** 2 + mpi ** 2)
        ST = 0.0
        for xi, wi in zip(x, wts):
            sth = np.sqrt(1 - xi ** 2)
            k = np.array([Epi, ks * sth, 0, ks * xi], dtype=complex)
            pp = P + q - k
            vs, vu, vt = P + q, P - k, k - q
            s, u, t = (E.dot(v, v).real for v in (vs, vu, vt))
            H = np.zeros((4, 4, 4), dtype=complex)
            if which in ('all',):
                Hb = E.current(ech, q, P, k, pp, V, ns, ff, running, delta=False)
                Hd = E.current(ech, q, P, k, pp, V, ns, ff, running, born=False)
                if ampff:
                    Hb = Hb * FhatB(s, u, t, MN, E._rp(ns['MPi0']), 1.121)
                    Xs, Xu = Xpi(s), Xpi(u)
                    Hd = Hd * np.sqrt(Xs + Xu - Xs * Xu)
                H = Hb + Hd
                if vec:
                    H = H - VM.current(ech, q, k, Q2=0.0)
            else:                        # Delta diagrams only
                H = E.current(ech, q, P, k, pp, V, ns, ff, running, born=False)
            acc = 0.0
            for si in range(2):
                ui = uspinor(P, MN, si)
                for sf in range(2):
                    ub = ubar(uspinor(pp, MN, sf))
                    J = np.array([ub @ H[m] @ ui for m in range(4)])
                    for e in POL:
                        acc += abs(sum(METRIC[m, m] * e[m] * J[m] for m in range(4))) ** 2
            ST += wi * acc / 4.0
        out[name] = float((2 * np.pi * HBARC2 * ks / (64 * np.pi ** 2 * Wh ** 2 * qs) * ST).real)
    return out


def bw_formula(Wh, MN, MD, GNpi, GNg, mpi0):
    """Eq. (E2) for gamma p -> p pi0: unitary BW, Gamma_Npi ~ k^3, Gamma_Ng ~ q^3."""
    if Wh <= MN + mpi0:
        return 0.0
    q = (Wh ** 2 - MN ** 2) / (2 * Wh)
    q0 = (MD ** 2 - MN ** 2) / (2 * MD)
    k, k0 = kmom(Wh ** 2, mpi0, MN), kmom(MD ** 2, mpi0, MN)
    Gpi, Gg = GNpi * (k / k0) ** 3, GNg * (q / q0) ** 3
    G = Gpi + Gg
    J, sg, sN = 1.5, 1.0, 0.5
    spin = (2 * J + 1) / (2 * (2 * sN + 1))      # (2 s_gamma + 1) = 2 helicities
    return float(4 * np.pi / q ** 2 * spin * (Gg * Gpi / 4) / ((Wh - MD) ** 2 + G ** 2 / 4)
                 * (2.0 / 3.0) * HBARC2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ufo', default='ChiPT_UFO_V16')
    ap.add_argument('--nth', type=int, default=16)
    ap.add_argument('--de', type=float, default=0.005)
    ap.add_argument('--out', default='photoprod_variants_V16.csv')
    ap.add_argument('--channels', default='pi-p,pi+n,pi0p,pi0n')
    a = ap.parse_args()
    Sp = E.setup(a.ufo, 'pole')
    Sb = E.setup(a.ufo, 'bw')
    Spr = (Sp[0], Sp[1], Sp[2], True)          # pole parameters, k^3 width
    # amplitude-level prescriptions: no vertex Delta form factor
    def novtx(S):
        ff = dict(S[2]); ff['FDeltaLam'] = lambda l: 1.0; ff['FpiNDelta'] = lambda l: 1.0
        return (S[0], S[1], ff, S[3])
    def nolam(S):                              # V15 mode: no piNDelta form factor
        ff = dict(S[2]); ff['FDeltaLam'] = lambda l: 1.0
        return (S[0], S[1], ff, S[3])
    full = {'base': (Sp, False, False, 'all'),
            'vec': (Sp, False, True, 'all'),
            'bw': (Sb, False, True, 'all'),
            'ampff': (novtx(Sp), True, False, 'all'),
            'v15': (nolam(Sp), False, False, 'all')}
    dline = {'delta_const': (Sp, False, False, 'delta'),
             'delta_k3': (Spr, False, False, 'delta')}
    ns = Sp[1]
    MN, MD = E._rp(ns['MNucleon']), E._rp(ns['MDelta'])
    rows, t0 = [], time.time()
    egs = np.round(np.arange(0.150, 0.600 + a.de / 2, a.de), 4)
    for ch in a.channels.split(','):
        for eg in egs:
            Wh = np.sqrt(MN ** 2 + 2 * MN * eg)
            for c, v in sigma_curves(ch, Wh, full, a.nth).items():
                rows.append((eg, ch, c, v))
            if ch == 'pi0p':
                for c, v in sigma_curves(ch, Wh, dline, a.nth).items():
                    rows.append((eg, ch, c, v))
                rows.append((eg, ch, 'bw_formula',
                             bw_formula(Wh, MN, MD, E._rp(ns['GamNPi']), E._rp(ns['GamNGam']),
                                        E._rp(ns['MPi0']))))
        print(f"{ch} done [{time.time() - t0:.0f}s]", flush=True)
    with open(a.out, 'w', newline='') as f:
        f.write(f"# py_photoprod_variants_V16.py, UFO {a.ufo}, sigma in microbarn; curves: base, vec, bw (vertex FFs), ampff, v15 "
                f"(all four channels), delta_const, delta_k3, bw_formula (pi0p)\n")
        w = csv.writer(f); w.writerow(['Egamma', 'channel', 'curve', 'sigma_ub'])
        w.writerows(rows)
    print('wrote', a.out, len(rows), 'rows')


if __name__ == '__main__':
    main()
