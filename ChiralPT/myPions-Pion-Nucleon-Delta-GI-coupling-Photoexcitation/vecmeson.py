#!/usr/bin/env python3
"""vecmeson.py -- t-channel rho/omega exchange in gamma(*) N -> pi N, in python.

A port of the vector-meson block of ../ELA-Pion-Photoproduction/Fig33v2.m (the
nucl-th/0509020v2 Eqs. (15)-(16) exchange that fig33_vecmeson.m bolts onto the
ChiPT amplitude), so it can be added to the UFO amplitudes of fig33_from_ufo.py
and eprod_from_ufo.py.  ChiPT.fr has no vector mesons; these are NOT model
parameters, they are the ELA fit values:

    omega   G = 0.2804   F = 21.11          K = -0.17   m = 0.78257
    rho0    G = 0.1161   F = 2.6            K = 6.3     m = 0.7685
    rho+-   G = 0.0906   F = sqrt(2) 2.6    K = 6.3     m = 0.7665

    pi0 p: omega + rho0      pi0 n: omega + rho0 with F -> -F (K unchanged)
    pi+ n, pi- p: charged rho

Vertices, exactly as Fig33v2.m (eps^{0123} = -1, metric diag(1,-1,-1,-1)):

    V pi gamma   (i e G / m_pi) eps^{mu_A mu_V a b} q_a (-k)_b
    V N N        -i F gamma^a + (i/4)(F K / M_N)(gamma^a Pslash - Pslash gamma^a),
                 P = q - k, the V momentum flowing into the nucleon line
    propagator   -i g / (t - m_V^2),  t = (k - q)^2
    form factor  Fhat_V(t) = Lambda^4 / (Lambda^4 + (t - m_V^2)^2),  Lambda = 1.121

and the overall -1 of Fig33v2.m.

VIRTUAL PHOTONS.  The V pi gamma vertex is a dual field strength, so it stays
gauge invariant at q^2 != 0 as it is; what it needs is the gamma* -> V pi
transition form factor.  Vector-meson dominance: the photon converts to the
OTHER vector meson of the pair (omega -> pi gamma* goes through a rho, rho ->
pi gamma* through an omega),

    F_Vpig(Q^2) = 1 / (1 + Q^2 / m_V'^2),   m_V' = m_rho for omega exchange,
                                             m_omega for rho exchange,

which is the standard monopole (e.g. the omega -> pi0 l+ l- transition form
factor is close to it).  `vmff='dipole'` uses 1/(1+Q^2/0.71)^2 instead, as a
variation.
"""
import numpy as np

EE = np.sqrt(4 * np.pi / 137.035999)
MN = 0.938272
MPI = 0.1349768          # fig33_vecmeson.m: mpiSv = MPi0 in every channel
LAMB = 1.121
M_RHO, M_OMEGA = 0.7685, 0.78257

OMEGA = dict(G=0.2804, F=21.11, K=-0.17, m=0.78257, mprime=M_RHO)
RHO0 = dict(G=0.1161, F=2.6, K=6.3, m=0.7685, mprime=M_OMEGA)
RHO0N = dict(RHO0, F=-2.6)
RHOC = dict(G=0.0906, F=np.sqrt(2) * 2.6, K=6.3, m=0.7665, mprime=M_OMEGA)
EXCHANGES = {
    # fig33 / ELA channel names, and eprod_from_ufo ones
    'pi0p': [OMEGA, RHO0], 'ppi0': [OMEGA, RHO0],
    'pi0n': [OMEGA, RHO0N], 'nnpi0': [OMEGA, RHO0N],
    'pi+n': [RHOC], 'npip': [RHOC],
    'pi-p': [RHOC], 'ppim': [RHOC],
}

G = np.diag([1.0, -1.0, -1.0, -1.0])
_I2, _Z2 = np.eye(2), np.zeros((2, 2))
_SX = np.array([[0, 1], [1, 0]], complex)
_SY = np.array([[0, -1j], [1j, 0]])
_SZ = np.array([[1, 0], [0, -1]], complex)
GAM = np.array([np.block([[_I2, _Z2], [_Z2, -_I2]]).astype(complex)]
               + [np.block([[_Z2, s], [-s, _Z2]]) for s in (_SX, _SY, _SZ)])
GAMLOW = np.einsum('ab,bij->aij', G, GAM)
EPSUP = np.zeros((4, 4, 4, 4))
import itertools as _it
for _p in _it.permutations(range(4)):
    EPSUP[_p] = -np.linalg.det(np.eye(4)[list(_p)])     # eps^{0123} = -1


def _dot(a, b):
    return a @ G @ b


def _slash(v):
    return np.einsum('a,aij->ij', v, GAMLOW)


def _lc2(a, b):
    """eps^{mu nu al be} a_al b_be, free indices upper."""
    return np.einsum('mnab,a,b->mn', EPSUP, G @ a, G @ b)


def _vmff(Q2, ex, kind):
    if not Q2 or kind in (None, 'none'):
        return 1.0
    if kind == 'dipole':
        return 1.0 / (1.0 + Q2 / 0.71) ** 2
    return 1.0 / (1.0 + Q2 / ex['mprime'] ** 2)


def current(ch, q, k, Q2=0.0, ff=True, vmff='monopole'):
    """M[mu, row, col] of the vector-meson exchange, photon index upper.

    q = photon momentum (incoming), k = pion momentum (outgoing); same
    orientation as fig33_from_ufo.amplitude and Fig33v2.m."""
    q = np.asarray(q, complex).real
    k = np.asarray(k, complex).real
    vt = k - q
    t = _dot(vt, vt)
    PV = -vt
    out = np.zeros((4, 4, 4), dtype=complex)
    for ex in EXCHANGES[ch]:
        dV = t - ex['m'] ** 2
        ffV = 1.0 / (1.0 + dV ** 2 / LAMB ** 4) if ff else 1.0
        vpg = (1j * EE * ex['G'] / MPI) * _lc2(q, -k) * _vmff(Q2, ex, vmff)
        sP = _slash(PV)
        vnn = np.array([-1j * ex['F'] * GAM[a]
                        + 0.25j * (ex['F'] * ex['K'] / MN) * (GAM[a] @ sP - sP @ GAM[a])
                        for a in range(4)])
        for mu in range(4):
            acc = np.zeros((4, 4), dtype=complex)
            for al in range(4):
                acc += G[al, al] * vpg[mu, al] * (-1j / dV) * vnn[al]
            out[mu] -= ffV * acc
    return out
