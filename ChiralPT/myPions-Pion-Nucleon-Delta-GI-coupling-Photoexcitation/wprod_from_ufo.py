#!/usr/bin/env python3
"""
wprod_from_ufo.py -- sigma(nu_l N -> l- N' pi) computed directly from the ChiPT
UFO model, the weak-sector counterpart of fig33_from_ufo.py.

Everything that defines the interaction is READ FROM THE UFO, exactly as in the
photoproduction script: the vertex list, the Lorentz structure strings, the
coupling values and the parameters.  The Dirac algebra, the UFO structure
evaluator, the spinors, the fermion/scalar propagators and the Rarita-Schwinger
numerator are IMPORTED from fig33_from_ufo, so the two calculations share one
validated implementation and can only differ where the physics differs.  What
this script adds is what the charged current needs and photoproduction did not:

  * the leptonic current  ubar(l) Gamma^mu P_L u(nu)  from the UFO's own
    ['vm~','mu-','W+'] vertex,
  * the massive W propagator,
  * the five hadronic topologies of W+ N -> pi N',
  * three-body phase space.

WHY 2 -> 3 AND NOT A W BEAM.  The obvious analogue of gamma N -> pi N is
W N -> pi N with the W in the initial state, and Sherpa_ChiPT_W.yaml was
originally written that way.  It cannot work: the W is massive, so an on-shell
W+ beam needs E >= MW = 80.94 GeV and every point sits at sqrt(s) >= 81.9 GeV,
decades above the Delta(1232) this model describes.  (Comix does not even
terminate there -- PS_Channel::TChannelBounds spins forever on the 80 GeV /
0.14 GeV mass hierarchy.)  Putting the W INSIDE the diagram, as the exchange in
nu_mu p -> mu- p pi+, reaches the resonance region with the same weak vertices.

CONVENTIONS, all inherited from fig33_from_ufo:
  * metric diag(1,-1,-1,-1), Dirac representation, ubar u = 2m;
  * UFO legs are all OUTGOING, so an INCOMING particle enters a vertex under its
    ANTIparticle name carrying MINUS its momentum -- an incoming W+ is the
    'W-' leg with -q;
  * in build(), the row (ubar) index is the fermionic leg with the larger PDG
    code, i.e. the outgoing one, and the column (u) index is the incoming leg.

MATCHING THE SHERPA RUN.  The numbers are meant to be compared point-blank with
Sherpa_ChiPT_W.yaml, so the defaults follow Sherpa rather than the paper:

  * the leptons are MASSLESS, because the run card sets 13: {Massive: false};
  * the Delta width is the FIXED 0.102 GeV of the DECAY block, in BOTH the s-
    and the u-channel propagator, because Comix knows nothing about which is
    which (fig33_from_ufo's energy-dependent width is the paper's prescription,
    not Sherpa's);
  * the physical MPi+ is used for charged pions and MPi0 for neutral ones
    (fig33_from_ufo follows the paper and uses MPi0 throughout);
  * no Davidson-Workman Born form factor: it lives in fig33_from_ufo at
    amplitude level and is not part of the UFO, so Sherpa cannot apply it;
  * FpiNDelta, which IS in the UFO, is evaluated exactly as Sherpa's
    FormFactors.C plugin does, sqrt(X_pi(p_Delta^2)) with MPi0.  Against the
    plain ChiPT_UFO build (no form factors) it is switched off automatically.

VALIDATION.  Against Sherpa (run_w.py, eight seeds averaged) this agrees to
better than 1% everywhere tested and to 0.3% or better over most of it, which is
the level at which the two are separately converged -- see w_vs_analytic.csv:

    nu p -> mu- p pi+   E_nu = 0.5 / 0.7 / 1.0 / 1.5 / 2.0 GeV
                        +0.89 / +0.57 / +0.25 / -0.03 / -0.27 %
    nu n -> mu- p pi0   E_nu = 1.0 GeV   +0.16 %
    nu n -> mu- n pi+   E_nu = 1.0 GeV   -0.03 %

Internal checks that come for free and are worth rerunning after any change:
the leptonic current is conserved to 1e-17, so the q^mu q^nu piece of the W
propagator changes |M|^2 by exactly zero and the gauge does not matter; and the
wrong-helicity neutrino amplitude vanishes identically.

Run:
    python3 wprod_from_ufo.py [--ufo ChiPT_UFO_DeltaFF] [--enu 1.0]
                              [--channel ppip] [--grid 24,12,12,8]
"""

import argparse
import os
import sys

import numpy as np

from fig33_from_ufo import (load_ufo, parameter_namespace, build,
                            build_scalar_vec, vertex_by_particles, uspinor,
                            ubar, prop_fermion, prop_scalar, rs_numerator,
                            eval_structure, kmom, dot, METRIC, ID4, HBARC2)


# ------------------------------------------------------------------ channels
# For W+(q) N(P) -> pi(k) N'(p'), naming every leg the way the UFO does (all
# outgoing).  `None` means the topology does not exist for that charge state:
# W+ p has charge +2, so it has no s-channel nucleon, and n -> N pi+ would need
# a nucleon of charge -1, so W+ n -> n pi+ has no u-channel nucleon.
CHANNELS = {
    # nu p -> mu- p pi+
    'ppip': dict(Ni='p', Nf='p', pion='Pi+', pi_t='Pi0',
                 N_s=None,  N_u='n', D_s='Delta++', D_u='Delta0'),
    # nu n -> mu- p pi0
    'ppi0': dict(Ni='n', Nf='p', pion='Pi0', pi_t='Pi+',
                 N_s='p',   N_u='n', D_s='Delta+',  D_u='Delta0'),
    # nu n -> mu- n pi+
    'npip': dict(Ni='n', Nf='n', pion='Pi+', pi_t='Pi0',
                 N_s='p',   N_u=None, D_s='Delta+', D_u='Delta-'),
}

ANTI = {'Pi0': 'Pi0', 'Pi+': 'Pi-', 'Pi-': 'Pi+'}


def anti(name):
    return ANTI.get(name, name + '~')


# ------------------------------------------------------------- form factors
def form_factors(ns, ufo_has_ff):
    """The namespace Sherpa's FormFactors.C plugin provides.

    Everything except FpiNDelta comes from formfactors.py, which is driven by
    the UFO's own CHIPTFF parameters -- so this and the Sherpa plugin evaluate
    the same functions with the same numbers, and neither has a fit compiled in.

    FpiNDelta stays here because it is not a Q^2 form factor at all: its
    argument is the Delta leg's own invariant mass squared, and it reproduces
    Sherpa's FormFactors.C, sqrt(X_pi(p_Delta^2)) with MPi0 whatever the
    channel's pion is.

    Against a UFO built without form factors every entry collapses to its
    point-like value, so the same code path serves both builds.
    """
    MN, MD, mpi0 = ns['MNucleon'], ns['MDelta'], ns['MPi0']
    k0 = kmom(MD ** 2, mpi0, MN)

    def Xpi(l):
        if l < (MN + mpi0) ** 2:
            return 0.0
        r = kmom(l, mpi0, MN) / k0
        return 2.0 * r ** 3 / (1.0 + r ** 5)

    def real(x):
        return x.real if isinstance(x, complex) else float(x)

    if not ufo_has_ff:
        one = lambda q2: 1.0
        ff = {'F1p': one, 'F1n': lambda q2: 0.0,
              'F2p': lambda q2: 1.792847, 'F2n': lambda q2: -1.913043,
              'FpiNDelta': lambda l: 1.0}
        for n in ('FW1', 'FWA', 'FW2', 'FZ1p', 'FZ1n', 'FZA', 'FZ2p', 'FZ2n',
                  'FCA5', 'FVND', 'FPP', 'FPPZ', 'FC6A', 'FgNDeltaPG1', 'FgNDeltaPG2', 'FgNDeltaNG1',
                  'FgNDeltaNG2'):
            ff[n] = one
        return ff

    from formfactors import FormFactors
    F = FormFactors(ns, allow_defaults=True)
    ff = {'FpiNDelta': lambda l: np.sqrt(Xpi(real(l)))}
    for name in ('F1p', 'F1n', 'F2p', 'F2n', 'FW1', 'FWA', 'FW2',
                 'FZ1p', 'FZ1n', 'FZA', 'FZ2p', 'FZ2n'):
        ff[name] = (lambda f: lambda q2: f(real(q2)))(getattr(F, name))
    ff['FCA5'] = lambda q2: F.C5A_ratio(real(q2))
    # The CVC vector N -> Delta dipole.  Baked into the UFO from V4 on; before
    # that the analytic code applied it by hand in vector_ndelta, and the UFO
    # had no vector damping at all.
    ff['FVND'] = lambda q2: F.VND_ratio(real(q2))
    # induced pseudoscalar; contributes only through the lepton mass
    ff['FPP'] = lambda q2: F.FPP(real(q2))
    ff['FPPZ'] = lambda q2: F.FPPZ(real(q2))
    ff['FC6A'] = lambda q2: F.FC6A(real(q2))
    # PCAC partner on the axial contact term; see FormFactors.C.  Its pion-pole
    # partner does not exist in the UFO, so PCAC is not restored the way CVC is.
    mrho2 = float(ns.get('MRhoCT', 0.7758)) ** 2
    ff['FrhoCT'] = lambda q2: mrho2 / (mrho2 + real(q2))
    # The electromagnetic N -> Delta transition form factors are 1 by
    # construction -- they multiply the fitted G1 and G2, so anything else
    # would silently rescale the Fig. 33 photoproduction fit.
    for n in ('FgNDeltaPG1', 'FgNDeltaPG2', 'FgNDeltaNG1', 'FgNDeltaNG2'):
        ff[n] = lambda q2: 1.0
    return ff


def build_split(v, momout, ns, ff):
    """build(), but returning (vector part, axial part) separately.

    A UFO Lorentz structure carrying Gamma5 is the axial half; everything else
    is the vector half.  Needed because CVC and PCAC put DIFFERENT form factors
    on the two halves of the same four-point contact vertex.
    """
    names = [p.name for p in v.particles]
    legs = {i + 1: momout[names[i]] for i in range(len(names))}
    tot = {'V': None, 'A': None}
    for (ci, li), c in v.couplings.items():
        struct = v.lorentz[li].structure
        key = 'A' if 'Gamma5' in struct else 'V'
        val = eval(str(c.value), dict(ns, **ff))
        piece = eval_structure(struct, legs, ff) * val
        tot[key] = piece if tot[key] is None else tot[key] + piece
    ferm = [(i + 1, v.particles[i]) for i in range(len(names))
            if v.particles[i].spin in (2, 4)]
    vec = [(i + 1) for i in range(len(names)) if v.particles[i].spin == 3]
    rs = [(i + 1) for i in range(len(names)) if v.particles[i].spin == 4]
    row = max(ferm, key=lambda x: x[1].pdg_code)[0]
    col = min(ferm, key=lambda x: x[1].pdg_code)[0]
    order = [('L', n) for n in rs] + [('L', n) for n in vec] + [('S', row), ('S', col)]
    out = {}
    for k, t in tot.items():
        out[k] = (np.transpose(t.a, [t.axes.index(x) for x in order])
                  if t is not None else None)
    return out['V'], out['A']


# ------------------------------------------ CVC / PCAC on the background terms
# Gonzalez-Jimenez et al., arXiv:1612.05511 Eq. (18): once the isovector nucleon
# form factors are put on the nucleon-pole diagrams, CVC REQUIRES the same F1V on
# the pion-in-flight and on the VECTOR half of the contact term,
#     F_PF(Q^2) = F_CT(Q^2) = F1V(Q^2) = F1p(Q^2) - F1n(Q^2).
# Leaving them point-like -- which is what this file did before -- breaks the
# Ward identity in the background, which is precisely the property this model
# exists to preserve.
#
# The axial partner is not symmetric.  Those references put a rho-dominance
# factor F_rho(t) = m_rho^2/(m_rho^2 - t) on the pion-pole term and the SAME
# factor on the axial half of the contact term, so that PCAC survives.  This
# model has no pion-pole (PP) diagram at all: it would come from the two-point
# W-pi mixing, which FeynRules does not export to a UFO.  So F_rho is applied to
# the axial contact here for consistency with the references, but PCAC is NOT
# fully restored -- the missing PP term is a genuine limitation of what a
# vertex-level framework can express, and is left to future work along with the
# NLO chiral counterterms the unitarisation would need.
MRHO2 = 0.775800 ** 2


def c4a_term(VwD, q, pD, MN, ratio=-0.25):
    """Adler's subleading axial N -> Delta form factor, C4A = -C5A/4.

    The standard decomposition of the axial N -> Delta current is
        ubar_alpha [ (C3A/M)(g^{am} qslash - q^a gamma^m)
                   + (C4A/M^2)(g^{am} q.p_D - q^a p_D^m)
                   + C5A g^{am} + (C6A/M^2) q^m q^a ] u
    and this model supplies C5A ALONE -- delta_couplings.py shows its weak
    N -> Delta vertex is exactly proportional to g^{am} x Identity, component by
    component.  So C3A = 0 already agrees with Adler; C4A = -C5A/4 does not, and
    is added here.

    C4A IS BUILT OUT OF THE VERTEX ITSELF, not from an extracted coefficient.
    The model's vertex behaves as V^{am} = c g^{am} BETWEEN SPINORS, but its
    actual Lorentz structure is an epsilon tensor, antisymmetric in a <-> m -- so
    any Lorentz trace of it vanishes identically and c cannot be read off that
    way (an earlier attempt did exactly that and silently returned zero).  Both
    pieces of the C4A tensor are instead obtained by contracting V:

        (q.p_D) V^{am}                      -> c (q.p_D) g^{am}
        q^a * sum_b g_bb (p_D)_b V^{bm}     -> c q^a p_D^m

    so whatever form factors V carries (FCA5, FpiNDelta) and whatever isospin
    factor its coupling has come along automatically, and C4A keeps exactly
    C5A's Q^2 dependence -- which C4A = -C5A/4 requires.
    """
    qp = dot(q, pD)
    pV = [sum(METRIC[b, b] * pD[b] * VwD[b, m] for b in range(4))
          for m in range(4)]
    out = np.zeros_like(VwD)
    for a in range(4):
        for m in range(4):
            out[a, m] = (ratio / MN ** 2) * (qp * VwD[a, m] - q[a] * pV[m])
    return out


# --------------------------------------------- CVC vector N -> Delta transition
# The model has NO vector piece on its weak N -> Delta vertex: gauging only ever
# produced the axial (C5A-like) structure, because LGammaNDelta in ChiPT.fr is
# written with the PHOTON field strength and the Delta isospin index hard-coded
# to 3.  So the W and the Z never inherit the fitted G1/G2 transition, and the
# weak vertex comes out exactly proportional to g^{alpha mu} (verified component
# by component in delta_couplings.py).
#
# CVC fixes what is missing with no new parameters: the N -> Delta transition is
# pure isovector, so the weak vector current is the same isotriplet as the
# electromagnetic one the model already fits to photoproduction.
#
# THE ISOSPIN FACTOR IS TAKEN FROM THE MODEL, NOT DERIVED.  For an isovector
# operator the ratio (charged transition)/(tau_3 transition) is the same for the
# vector and the axial current, and the model supplies it in its own axial
# couplings -- so no Clebsch is written by hand here:
#
#     iso = [axial CC coupling / g_cc] / [axial NC coupling / g_Z]
#
#   p -> Delta++ : (sqrt2 hD/MD) / (2 hD/(MD sqrt6)) = sqrt3
#   n -> Delta+  : (sqrt2 hD/(MD sqrt3)) / (2 hD/(MD sqrt6)) = 1
#
# and then   V_CC = (photon vertex / ee) * iso * g_cc.
#
# A DIPOLE IS APPLIED.  The model's FgNDelta* are 1, so an unsuppressed vector
# transition would blow up at large Q^2 -- the same artefact the C5A = 1 test
# exposed.  Achilles' MECVectorFormFactor shape is used,
# 1/(1+Q^2/Mv^2)^2 / (1+Q^2/(4 Mv^2)) with Mv^2 = 0.71 GeV^2.
#
# THE RELATIVE SIGN IS NOT FIXED HERE.  V and A interfere, and the sign of the
# vector piece relative to the model's axial one depends on Clebsch phase
# conventions that this construction deliberately avoids deriving.  opt['vecND']
# carries it explicitly (+1 or -1); run both and say which was used.
ISO_ND = {'p': np.sqrt(3.0), 'n': 1.0}
MV2_ND = 0.71


# G1/G2 as fitted carry the factor that the radiative width exposes: the model
# gives Gamma(Delta -> N gamma) = 2.23 MeV against the measured 0.66, i.e. g is
# 1.84 too large in amplitude.  A vector transition built from them inherits it,
# and it shows: switching the piece on with G1/G2 unscaled multiplies the cross
# section by a FLAT 3.5, against 1.84^2 = 3.39.  G_SCALE_ND puts g on its own
# measured width before CVC is applied.
G_SCALE_ND = 1.0 / 1.84


def vector_ndelta(V, ns, ff, Ni, D_tau3, momout, Q2, scale=None):
    """The CVC vector N -> Delta vertex, built from the model's own photon one."""
    Vem = build(vertex_by_particles(V, [Ni + '~', D_tau3, 'A']), momout, ns, ff)
    g_cc = ns['ee'] * ns['Vud'] / (2 * ns['sw'] * np.sqrt(2))
    fv = 1.0 / (1 + Q2 / MV2_ND) ** 2 / (1 + Q2 / (4 * MV2_ND))
    g = G_SCALE_ND if scale is None else scale
    return Vem * (g_cc / ns['ee']) * ISO_ND[Ni] * fv * g


# ------------------------------------------------------------------ currents
def w_propagator(q, MW, GW):
    """Unitary gauge, -i (g^{mu nu} - q^mu q^nu / MW^2) / (q^2 - MW^2 + i MW GW).

    Both indices up; contract with the metric on each side.  The q^mu q^nu piece
    drops out identically for massless leptons -- the leptonic current is then
    exactly conserved -- which is why the gauge Sherpa uses for the internal W
    does not have to be guessed.  It is kept in so that the check still holds
    when the muon is given its mass.
    """
    den = dot(q, q) - MW ** 2 + 1j * MW * GW
    D = np.zeros((4, 4), dtype=complex)
    for m in range(4):
        for n in range(4):
            D[m, n] = -1j * (METRIC[m, n] - q[m] * q[n] / MW ** 2) / den
    return D


def leptonic_current(k1, k2, V, ns, ff, mmu=0.0):
    """L[mu, s_lep, s_nu] = ubar(k2,s_lep) Gamma^mu P_L u(k1,s_nu).

    Legs: the incoming neutrino is the 'vm~' leg at -k1, the outgoing muon the
    'mu-' leg at +k2, and the W+ leaving the vertex is the 'W+' leg at q.
    """
    q = k1 - k2
    Vl = build(vertex_by_particles(V, ['vm~', 'mu-', 'W+']),
               {'vm~': -k1, 'mu-': k2, 'W+': q}, ns, ff)   # [mu, row=mu-, col=vm]
    out = np.zeros((4, 2, 2), dtype=complex)
    for sl in range(2):
        ub = ubar(uspinor(k2, mmu, sl))
        for sn in range(2):
            un = uspinor(k1, 0.0, sn)
            for m in range(4):
                out[m, sl, sn] = ub @ Vl[m] @ un
    return out


def hadronic_current(ch, q, P, k, pp, V, ns, ff, opt):
    """H[nu, row, col] for W+(q) N(P) -> pi(k) N'(p').

    The five topologies are the ones Comix builds for this process; with
    Print_Graphs on, nu p -> mu- p pi+ comes out as exactly Delta++ s-channel,
    the four-point contact, pi0 t-channel exchange, n u-channel and Delta0
    u-channel.
    """
    c = CHANNELS[ch]
    Ni, Nf, pion, pi_t = c['Ni'], c['Nf'], c['pion'], c['pi_t']
    aNi, apion, api_t = anti(Ni), anti(pion), anti(pi_t)
    MN, MD = ns['MNucleon'], ns['MDelta']
    GD = ns['WDeltaP'] if opt.get('dwidth', True) else 0.0
    # opt['edw']: Fig. 33's energy-dependent width, Gamma(l) = Gamma_0 X_pi(l).
    # It is the PARTNER of the sqrt(X_pi) that FpiNDelta puts on the vertex --
    # the paper's prescription is both together.  Sherpa can only do the fixed
    # width, so the default here matches Sherpa; turning this on measures what
    # that mismatch costs.
    edw = opt.get('edw', False)
    if edw:
        mpi0_, k0_ = ns['MPi0'], kmom(MD ** 2, ns['MPi0'], MN)

        def _X(l):
            if l < (MN + mpi0_) ** 2:
                return 0.0
            r = kmom(l, mpi0_, MN) / k0_
            return 2.0 * r ** 3 / (1.0 + r ** 5)
    mpi = ns['MPi0'] if pion == 'Pi0' else ns['MPiP']
    mpi_t = ns['MPi0'] if pi_t == 'Pi0' else ns['MPiP']

    vs, vu, vt = P + q, P - k, q - k        # s-, u- and t-channel momenta
    H = np.zeros((4, 4, 4), dtype=complex)

    if opt.get('born', True):
        # s-channel nucleon:  W+ N -> N_s -> pi N'
        if c['N_s']:
            Ns_ = c['N_s']
            Vw = build(vertex_by_particles(V, [aNi, Ns_, 'W-']),
                       {aNi: -P, Ns_: vs, 'W-': -q}, ns, ff)
            Vp = build(vertex_by_particles(V, [anti(Ns_), Nf, pion]),
                       {anti(Ns_): -vs, Nf: pp, pion: k}, ns, ff)
            S = prop_fermion(vs, MN)
            for m in range(4):
                H[m] += Vp @ S @ Vw[m]
        # u-channel nucleon:  N -> N_u pi, then W+ N_u -> N'
        if c['N_u']:
            Nu_ = c['N_u']
            Vp = build(vertex_by_particles(V, [aNi, Nu_, pion]),
                       {aNi: -P, Nu_: vu, pion: k}, ns, ff)
            Vw = build(vertex_by_particles(V, [anti(Nu_), Nf, 'W-']),
                       {anti(Nu_): -vu, Nf: pp, 'W-': -q}, ns, ff)
            S = prop_fermion(vu, MN)
            for m in range(4):
                H[m] += Vw[m] @ S @ Vp
        # t-channel pion in flight:  W+ -> pi pi_t, then pi_t N -> N'
        Vwpp = build_scalar_vec(vertex_by_particles(V, ['W-', pion, pi_t]),
                                {'W-': -q, pion: k, pi_t: vt}, ns, ff)
        Vpi = build(vertex_by_particles(V, [aNi, Nf, api_t]),
                    {aNi: -P, Nf: pp, api_t: -vt}, ns, ff)
        D = prop_scalar(vt, mpi_t)
        f1v = ff['FW1'](-dot(q, q).real) if opt.get('cvc', True) else 1.0
        for m in range(4):
            H[m] += f1v * Vwpp[m] * D * Vpi
        # four-point contact.  CVC puts F1V on the vector half; the axial half
        # takes the rho-dominance factor -- see the note above build_split.
        KV, KA = build_split(vertex_by_particles(V, [aNi, Nf, 'W-', pion]),
                             {aNi: -P, Nf: pp, 'W-': -q, pion: k}, ns, ff)
        if opt.get('cvc', True):
            frho = MRHO2 / (MRHO2 - dot(vt, vt).real)
            if KV is not None:
                H += f1v * KV
            if KA is not None:
                H += frho * KA
        else:
            if KV is not None:
                H += KV
            if KA is not None:
                H += KA

    if opt.get('delta', True):
        sD = opt.get('dsign', 1.0)
        # opt['fig33ff']: the paper's prescription instead of the vertex-level
        # one.  Fig. 33 multiplies BOTH Delta diagrams by sqrt(X_pi(s,u)) with
        # X_pi(s,u) = X(s) + X(u) - X(s)X(u); a UFO form factor can only see one
        # vertex's own momenta, so FpiNDelta(p_Delta^2) gives sqrt(X(u)) = 0 on
        # the u-channel Delta and deletes it.  With this on, FpiNDelta is set to
        # 1 in the vertices (see the caller) and the damping is applied here.
        ffD = 1.0
        if opt.get('fig33ff'):
            mpi0_ = ns['MPi0']
            k0f = kmom(MD ** 2, mpi0_, MN)

            def _Xf(l):
                if l < (MN + mpi0_) ** 2:
                    return 0.0
                r = kmom(l, mpi0_, k0f and MN) / k0f
                return 2.0 * r ** 3 / (1.0 + r ** 5)
            Xs, Xu = _Xf(dot(vs, vs).real), _Xf(dot(vu, vu).real)
            ffD = np.sqrt(Xs + Xu - Xs * Xu)
        s2, u2 = dot(vs, vs).real, dot(vu, vu).real
        Gs = GD * _X(s2) if edw else GD
        Gu = GD * _X(u2) if edw else GD
        Ds = dot(vs, vs) - MD ** 2 + 1j * MD * Gs
        Du = dot(vu, vu) - MD ** 2 + 1j * MD * Gu
        # s-channel Delta.  The RS numerator N[nu,eta] is NOT symmetric: the
        # vertex on the LEFT of the fermion line pairs with its FIRST index,
        # which here is the strong Delta -> N pi vertex.
        Ds_ = c['D_s']
        VwD = build(vertex_by_particles(V, [aNi, Ds_, 'W-']),
                    {aNi: -P, Ds_: vs, 'W-': -q}, ns, ff)      # [nu, mu, r, c]
        # opt['axND'] scales the AXIAL N -> Delta transition on its own, i.e.
        # decouples C5A from hD.  h -> 2h already puts the reduced C5A(0) at
        # 1.241; 0.9669 brings it to the phenomenological 1.2.  Note this breaks
        # the gauge relation that ties the transition to the strong vertex --
        # which is exactly what putting in a fitted C5A means.
        if opt.get('axND'):
            VwD = VwD * opt['axND']
        if opt.get('c4a') is not None:
            VwD = VwD + c4a_term(VwD, q, vs, MN, opt['c4a'])
        if opt.get('vecND'):
            # same index layout: row is the Delta leg either way (larger PDG)
            D3 = 'Delta+' if Ni == 'p' else 'Delta0'
            VwD = VwD + opt['vecND'] * vector_ndelta(
                V, ns, ff, Ni, D3, {aNi: -P, D3: vs, 'A': -q},
                -dot(q, q).real, opt.get('vecScale'))
        VpD = build(vertex_by_particles(V, [anti(Ds_), Nf, pion]),
                    {anti(Ds_): -vs, Nf: pp, pion: k}, ns, ff)  # [eta, r, c]
        Ns = rs_numerator(vs, MD)
        for m in range(4):
            acc = np.zeros((4, 4), dtype=complex)
            for nu in range(4):
                for et in range(4):
                    acc += (METRIC[nu, nu] * METRIC[et, et]
                            * VpD[nu] @ (1j * Ns[nu, et] / Ds) @ VwD[et, m])
            H[m] += sD * ffD * acc
        # u-channel Delta: the weak vertex is now the one on the left
        if c['D_u']:
            Du_ = c['D_u']
            VpD2 = build(vertex_by_particles(V, [aNi, Du_, pion]),
                         {aNi: -P, Du_: vu, pion: k}, ns, ff)
            VwD2 = build(vertex_by_particles(V, [anti(Du_), Nf, 'W-']),
                         {anti(Du_): -vu, Nf: pp, 'W-': -q}, ns, ff)
            Nu = rs_numerator(vu, MD)
            for m in range(4):
                acc = np.zeros((4, 4), dtype=complex)
                for nu in range(4):
                    for et in range(4):
                        acc += (METRIC[nu, nu] * METRIC[et, et]
                                * VwD2[nu, m] @ (1j * Nu[nu, et] / Du) @ VpD2[et])
                H[m] += sD * ffD * acc
    return H


# --------------------------------------------------------------- kinematics
def boost(X, W, a):
    """Boost the four-vector `a`, given in the rest frame of X, into X's frame."""
    Xv, av = X[1:], a[1:]
    xa = Xv @ av
    a0 = (X[0] * a[0] + xa) / W
    return np.concatenate([[a0], av + Xv * (a[0] / W + xa / (W * (X[0] + W)))])


def lepmom(s, Whad, mmu, rs=None):
    """|k2| of the outgoing lepton in the overall CM.

    The two-body break-up momentum for sqrt(s) -> lepton(m) + X(Whad):

        |k2| = sqrt(lambda(s, m^2, W^2)) / (2 sqrt(s))

    which collapses to the massless (s - W^2)/(2 sqrt(s)) when m = 0.  Both the
    phase-space prefactor in sigma() and the four-vector in msq_at() must use
    the SAME expression or the two disagree off the massless point.
    """
    if rs is None:
        rs = np.sqrt(s)
    if mmu == 0.0:
        return (s - Whad ** 2) / (2 * rs)
    lam = (s - (mmu + Whad) ** 2) * (s - (mmu - Whad) ** 2)
    return np.sqrt(max(0.0, lam)) / (2 * rs)


def msq_at(ch, s, Whad, ctl, cth, phi, V, ns, ff, opt):
    """Spin-summed |M|^2 at one phase-space point, in the overall CM frame."""
    MN = ns['MNucleon']
    mpi = ns['MPi0'] if CHANNELS[ch]['pion'] == 'Pi0' else ns['MPiP']
    rs = np.sqrt(s)

    E1 = (s - MN ** 2) / (2 * rs)                  # massless neutrino
    k1 = np.array([E1, 0, 0, E1], dtype=complex)
    P = np.array([rs - E1, 0, 0, -E1], dtype=complex)
    mmu = opt.get('mmu', 0.0)
    ql = lepmom(s, Whad, mmu, rs)                  # |k2| in the CM
    El = np.sqrt(ql ** 2 + mmu ** 2)
    stl = np.sqrt(max(0.0, 1.0 - ctl ** 2))
    k2 = np.array([El, ql * stl, 0, ql * ctl], dtype=complex)
    X = k1 + P - k2

    ks = kmom(Whad ** 2, mpi, MN)
    sth = np.sqrt(max(0.0, 1.0 - cth ** 2))
    krest = np.array([np.sqrt(ks ** 2 + mpi ** 2),
                      ks * sth * np.cos(phi), ks * sth * np.sin(phi), ks * cth],
                     dtype=complex)
    k = boost(X.real, Whad, krest.real).astype(complex)
    pp = X - k

    L = leptonic_current(k1, k2, V, ns, ff, opt.get('mmu', 0.0))
    H = hadronic_current(ch, k1 - k2, P, k, pp, V, ns, ff, opt)
    D = w_propagator(k1 - k2, ns['MW'], ns['WW'] if opt.get('wwidth', True) else 0.0)

    # M = L_mu D^{mu nu} H_nu, with L and H carrying upper indices
    G = np.diag(METRIC).real
    C = (G[:, None] * D * G[None, :])            # C[mu,nu] = g_mumu D^munu g_nunu

    tot = 0.0
    for sp in range(2):                          # target nucleon spin
        ui = uspinor(P, MN, sp)
        for sq in range(2):                      # final nucleon spin
            ub = ubar(uspinor(pp, MN, sq))
            Hn = np.array([ub @ H[n] @ ui for n in range(4)])
            for sl in range(2):                  # muon spin
                for sn in range(2):              # neutrino spin (one is zero)
                    amp = L[:, sl, sn] @ C @ Hn
                    tot += abs(amp) ** 2
    return tot


def sigma(ch, Enu, V, ns, ff, opt, grid=(24, 12, 12, 8), verbose=False):
    """Total cross section in microbarn.

    sigma = 1/(2(s-MN^2)) * 1/4 * int dW dcos(th_l) dcos(th_h) dphi_h
                 q_l k* / (128 pi^4 sqrt(s)) * sum|M|^2

    with the three-body phase space split as dPhi3 = dW^2/2pi dPhi2(s -> l, X)
    dPhi2(W^2 -> N' pi); the leptonic azimuth is integrated analytically (2 pi).
    Gauss-Legendre in every variable: phi_h enters only through cos(phi),
    cos(2phi) and their sine partners, so 8 nodes are already exact there.

    W is integrated in u, with W = Wlo + (Whi - Wlo) u^2.  The pion momentum k*
    in the prefactor vanishes like sqrt(W - Wlo) at the pion threshold, and
    Gauss-Legendre converges only like n^-3 on that square root; the u^2 map
    turns it into a factor linear in u and buys about a decade of accuracy at
    the same cost.  Without it the total drifts by ~1% between nW = 12 and 24,
    which is the size of the effect being measured.
    """
    MN = ns['MNucleon']
    mpi = ns['MPi0'] if CHANNELS[ch]['pion'] == 'Pi0' else ns['MPiP']
    s = MN ** 2 + 2 * MN * Enu
    rs = np.sqrt(s)
    mmu = opt.get('mmu', 0.0)
    Wlo, Whi = MN + mpi, rs - mmu                # W_max = sqrt(s) - m_lepton
    # ANL and BNL both publish a W < 1.4 GeV set alongside the uncut one; the
    # model has to be integrated with the SAME cut to be compared with it.
    wmax = opt.get('wmax')
    if wmax:
        Whi = min(Whi, float(wmax))
    if Whi <= Wlo:
        return 0.0
    nW, ncl, ncth, nphi = grid

    xW, wW = np.polynomial.legendre.leggauss(nW)
    xl, wl = np.polynomial.legendre.leggauss(ncl)
    xh, wh = np.polynomial.legendre.leggauss(ncth)
    xp = 2 * np.pi * (np.arange(nphi) + 0.5) / nphi
    wp = np.full(nphi, 2 * np.pi / nphi)         # trapezoid == exact, periodic

    us = 0.5 * (xW + 1.0)                        # u in [0,1]
    Ws = Wlo + (Whi - Wlo) * us ** 2
    jWs = 0.5 * 2.0 * (Whi - Wlo) * us           # dW/du times du/dx

    tot = 0.0
    for iW, Whad in enumerate(Ws):
        ql = lepmom(s, Whad, mmu, rs)
        ks = kmom(Whad ** 2, mpi, MN)
        pref = ql * ks / (128 * np.pi ** 4 * rs)
        jW = jWs[iW]
        if pref <= 0:
            continue
        acc = 0.0
        for icl in range(ncl):
            for ith in range(ncth):
                for ip in range(nphi):
                    acc += (wl[icl] * wh[ith] * wp[ip]
                            * msq_at(ch, s, Whad, xl[icl], xh[ith], xp[ip],
                                     V, ns, ff, opt))
        tot += wW[iW] * jW * pref * acc
        if verbose:
            print("    W = %.4f  running sigma = %.6g ub"
                  % (Whad, HBARC2 * tot / (8 * (s - MN ** 2))), flush=True)
    return HBARC2 * tot / (8 * (s - MN ** 2))    # 1/(2(s-MN^2)) * 1/4


# --------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ufo', default='ChiPT_UFO_DeltaFF')
    ap.add_argument('--enu', type=float, default=1.0)
    ap.add_argument('--channel', default='ppip', choices=sorted(CHANNELS))
    ap.add_argument('--grid', default='24,12,12,8',
                    help='nW,ncos_lep,ncos_had,nphi_had')
    ap.add_argument('--wmax', type=float, default=None,
                    help='cut on the hadronic invariant mass, e.g. 1.4 to match '
                         'the ANL/BNL W<1.4 GeV data sets')
    ap.add_argument('--no-delta', action='store_true')
    ap.add_argument('--no-born', action='store_true')
    ap.add_argument('--verbose', action='store_true')
    a = ap.parse_args()

    P, V = load_ufo(a.ufo)
    ns = parameter_namespace(P)
    has_ff = os.path.exists(os.path.join(a.ufo, 'form_factors.py'))
    ff = form_factors(ns, has_ff)
    grid = tuple(int(x) for x in a.grid.split(','))
    opt = dict(born=not a.no_born, delta=not a.no_delta,
               dwidth=True, wwidth=True, wmax=a.wmax)

    print("UFO: %s   MW=%.4f  WW=%.4f  MN=%.6f  MDelta=%.4f  WDelta=%.4f"
          % (a.ufo, ns['MW'].real, ns['WW'], ns['MNucleon'], ns['MDelta'],
             ns['WDeltaP']))
    print("     ee=%.6f  sw=%.6f  ga=%.4f  hD=%.4f  fPi=%.4f  FpiNDelta=%s"
          % (ns['ee'].real, ns['sw'].real, ns['ga'], ns['hD'], ns['fPi'],
             'on' if has_ff else 'off (plain UFO)'))
    s = ns['MNucleon'] ** 2 + 2 * ns['MNucleon'] * a.enu
    print("channel %s   E_nu = %.3f GeV   sqrt(s) = %.4f GeV   grid = %s   W < %s"
          % (a.channel, a.enu, np.sqrt(s), grid,
             ("%.2f GeV" % a.wmax) if a.wmax else "no cut"))

    xs = sigma(a.channel, a.enu, V, ns, ff, opt, grid, a.verbose)
    print("\nsigma = %.6g ub  =  %.6g x 1e-38 cm^2" % (xs, xs * 1e-30 / 1e-38))


if __name__ == '__main__':
    main()
