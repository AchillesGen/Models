#!/usr/bin/env python3
"""Ward identity on the hadronic current: q_mu <pi N'| V^mu |N> = 0.

This is the check that was missing.  cvc_ndelta.py and pcac_nucleon.py test the
three-point currents -- the N -> Delta transition and the nucleon pole -- and
those are the vertices whose form factors were put in deliberately.  Nothing
tested the BACKGROUND as a set, and that is exactly where a form factor breaks
current conservation: the pion-in-flight and the contact term have to carry the
same F1V the nucleon poles do, or the four diagrams stop cancelling.

    q_mu [ NP + CNP + PF + CT ]^mu = 0      (conserved vector current)
    q_mu [ Delta_s ]^mu = q_mu [ Delta_u ]^mu = 0

The Delta terms are conserved one at a time because the model couples the
photon to the Delta through the field strength (the Pascalutsa coupling), so
q_mu F^{mu nu} vanishes identically; the Born terms are conserved only as a
group.  Both are reported, because a violation in the Delta sector and a
violation in the Born sector mean different things.

WHICH DIRAC STRUCTURE IS "VECTOR".  Not the one without gamma5.  Expanding
u = exp(i pi.tau / 2 fPi), the one-pion piece of the vector source combination
(L~ + R~)/2 carries the AXIAL source and vice versa, so

    contact  Nbar gamma^mu N pi        (Weinberg-Tomozawa)  -> axial current
    contact  Nbar gamma^mu gamma5 N pi (Kroll-Ruderman)     -> VECTOR current

The photon settles this on its own: for the photon l = r, so the axial source
vanishes and the gamma^mu contact does not exist at all -- the only photon
contact term in the UFO is the Kroll-Ruderman one, and the low-energy theorem
for charged-pion photoproduction needs precisely that term to close the
electromagnetic Ward identity.  Structures are therefore selected here BY THE
FORM FACTOR THEY CARRY (FW1 for the vector half, FrhoCT for the axial half),
never by testing for Gamma5.

PCAC IS NOT TESTED HERE and does not hold: q_mu A^mu is saturated by the pion
pole, and the model has no pion-pole diagram (FeynRules does not export the
two-point W-pi mixing).  The axial residual is printed for the record, not as
a pass/fail.

Usage:
    python3 tools/ward_background.py              # CHIPT_MODEL selects the UFO
    python3 tools/ward_background.py --pointlike  # all form factors at Q^2 = 0

THE CC VECTOR CURRENT DOES NOT COME OUT EXACTLY CONSERVED, AND IT SHOULD NOT.
CVC holds in the isospin limit, and this model is run with the PHYSICAL pion
masses -- m_pi+ = 139.57, m_pi0 = 134.98 MeV.  For W+ p -> pi+ p the pion in
flight is a pi0 while the outgoing pion is a pi+, so the two pion propagators
the identity has to cancel between are evaluated at different masses and the
cancellation is short by roughly

    (m_pi+^2 - m_pi0^2) / |t|  =  0.00126 GeV^2 / |t| ,

about 1e-3 at these kinematics.  That is what the table shows.  Run with
--isospin-exact and the same residual drops to 1.5e-16.  The photon and the
neutral current are untouched because their pion masses do not change across
the diagram.  So the CC line is a measurement of isospin breaking, not a bug --
and the script now demonstrates that rather than just printing FAIL.
"""
import argparse

import numpy as np

from _vertex import load, with_ff                              # sets sys.path

from fig33_from_ufo import (build, build_scalar_vec, eval_structure,
                            uspinor, ubar, prop_fermion, prop_scalar,
                            rs_numerator, dot, METRIC)          # noqa: E402


def vertex_by_particles(V, names):
    """The one vertex with exactly this particle content.

    fig33_from_ufo's version of this takes the vertices MODULE; _vertex.load()
    hands back a plain list, so it is repeated here over the list.
    """
    want = sorted(names)
    out = [v for v in V if sorted(p.name for p in v.particles) == want]
    if not out:
        raise KeyError("no UFO vertex with particles %s" % (names,))
    if len(out) > 1:
        raise KeyError("several UFO vertices with particles %s" % (names,))
    return out[0]


# --------------------------------------------------------------- bookkeeping
CHARGE = {'p': 1, 'n': 0, 'Pi+': 1, 'Pi0': 0, 'Pi-': -1,
          'A': 0, 'Z': 0, 'W+': 1, 'W-': -1}
NUCLEON = {1: 'p', 0: 'n'}
DELTA = {2: 'Delta++', 1: 'Delta+', 0: 'Delta0', -1: 'Delta-'}
ANTIPI = {'Pi0': 'Pi0', 'Pi+': 'Pi-', 'Pi-': 'Pi+'}

# The form factors that belong to the VECTOR current at each three-point
# boson-N-N vertex.  The photon is entirely vector, so it needs no filter.
VECTOR_FF = {'A': None, 'Z': ('FZ1p', 'FZ1n', 'FZ2p', 'FZ2n'),
             'W+': ('FW1', 'FW2')}
# The N -> Delta transition current.  The photon vertex is all vector; the W
# and Z ones carry C5A/C6A as well, and only their FVND (CVC dipole) half is
# a vector current.  Selecting by form factor rather than by Gamma5 matters
# doubly here: the C5A structure has an explicit Gamma5 and so does one of the
# two G1/G2 vector structures.
VECTOR_ND = {'A': None, 'Z': ('FVND',), 'W+': ('FVND',)}
# ... and at the four-point contact.  The Kroll-Ruderman half is the vector
# one; it carries FW1 on the photon and the W and FZ1pi on the Z (the two
# differ by the constant sin^2(theta_W) ratio -- see formfactors.FZ1pi).  The
# Weinberg-Tomozawa half carries FrhoCT and belongs to the axial current.
CT_VECTOR_FF = ('FW1', 'FZ1pi')
# The pion pole rides on the same four-point vertex from V11 on, and it is
# AXIAL: it exists because the axial source mixes with a single pion, and a
# vector current has no such pole.  Leaving it out of this list does not make
# the test fail, it makes the test not see the diagram at all -- the numbers
# come out byte-identical to the model without it, which is a very convincing
# way to be wrong.
CT_AXIAL_FF = ('FrhoCT', 'FPPpi', 'FPPZpi')


def anti(name):
    return ANTIPI.get(name, name + '~')


def boson_leg(boson):
    """The UFO leg name an INCOMING boson enters under (all legs outgoing)."""
    return {'A': 'A', 'Z': 'Z', 'W+': 'W-', 'W-': 'W+'}[boson]


def build_part(v, mom, ns, ff, keep_ff):
    """The vertex tensor from only the structures carrying one of `keep_ff`.

    `keep_ff is None` means the whole vertex.  Selecting by form factor rather
    than by structure name matters: FeynRules numbers FFV1..FFVn in emission
    order, so the names move whenever a term is added to the model.
    """
    if keep_ff is None:
        return build(v, mom, ns, ff)
    keep = with_ff(v, *keep_ff)
    if not keep:
        return None
    names = [p.name for p in v.particles]
    legs = {i + 1: mom[names[i]] for i in range(len(names))}
    tot = None
    for (ci, li), c in v.couplings.items():
        if v.lorentz[li].name not in keep:
            continue
        val = eval(str(c.value), dict(ns, **ff))
        piece = eval_structure(v.lorentz[li].structure, legs, ff) * val
        tot = piece if tot is None else tot + piece
    if tot is None:
        return None
    ferm = [(i + 1, v.particles[i]) for i in range(len(names))
            if v.particles[i].spin in (2, 4)]
    vec = [i + 1 for i in range(len(names)) if v.particles[i].spin == 3]
    rs = [i + 1 for i in range(len(names)) if v.particles[i].spin == 4]
    row = max(ferm, key=lambda x: x[1].pdg_code)[0]
    col = min(ferm, key=lambda x: x[1].pdg_code)[0]
    order = ([('L', n) for n in rs] + [('L', n) for n in vec]
             + [('S', row), ('S', col)])
    return np.transpose(tot.a, [tot.axes.index(x) for x in order])


# ------------------------------------------------------------------ currents
def born_current(V, ns, ff, boson, Ni, Nf, pion, p, q, k, pp, part='V'):
    """H[mu, row, col] for the four background topologies of B(q) N(p) -> pi N'.

    `part` selects which piece of each vertex is kept: 'V' the vector current,
    'A' the axial, 'all' both.  The nucleon poles are split by the form factor
    on the boson-N-N vertex, the contact term by FW1 (Kroll-Ruderman, vector)
    against FrhoCT (Weinberg-Tomozawa, axial), and the pion-in-flight is pure
    vector and therefore absent from the axial current altogether.
    """
    MN = ns['MNucleon']
    bl = boson_leg(boson)
    qB = CHARGE[boson]
    aNi, aNf = anti(Ni), anti(Nf)
    vs, vu = p + q, p - k
    H = np.zeros((4, 4, 4), dtype=complex)

    if part == 'all':
        nn_ff, ct_ff = None, None
    elif part == 'V':
        nn_ff, ct_ff = VECTOR_FF[boson], CT_VECTOR_FF
    else:
        nn_ff, ct_ff = 'complement', CT_AXIAL_FF

    def nn_vertex(vtx, mom):
        """Boson-N-N vertex, vector or axial half."""
        if nn_ff is None:
            return build(vtx, mom, ns, ff)
        if nn_ff != 'complement':
            return build_part(vtx, mom, ns, ff, nn_ff)
        full = build(vtx, mom, ns, ff)
        vec = build_part(vtx, mom, ns, ff, VECTOR_FF[boson])
        return full if vec is None else full - vec

    # ---- s-channel nucleon pole (NP)
    qs = CHARGE[Ni] + qB
    if qs in NUCLEON:
        Ns_ = NUCLEON[qs]
        Vb = nn_vertex(vertex_by_particles(V, [aNi, Ns_, bl]),
                       {aNi: -p, Ns_: vs, bl: -q})
        if Vb is not None:
            Vp = build(vertex_by_particles(V, [anti(Ns_), Nf, pion]),
                       {anti(Ns_): -vs, Nf: pp, pion: k}, ns, ff)
            S = prop_fermion(vs, MN)
            for m in range(4):
                H[m] += Vp @ S @ Vb[m]

    # ---- u-channel nucleon pole (CNP)
    qu = CHARGE[Ni] - CHARGE[pion]
    if qu in NUCLEON:
        Nu_ = NUCLEON[qu]
        Vp = build(vertex_by_particles(V, [aNi, Nu_, pion]),
                   {aNi: -p, Nu_: vu, pion: k}, ns, ff)
        Vb = nn_vertex(vertex_by_particles(V, [anti(Nu_), Nf, bl]),
                       {anti(Nu_): -vu, Nf: pp, bl: -q})
        if Vb is not None:
            S = prop_fermion(vu, MN)
            for m in range(4):
                H[m] += Vb[m] @ S @ Vp

    # ---- t-channel pion in flight (PF).  Pure vector current.
    if part != 'A':
        qt = qB - CHARGE[pion]
        pi_t = {1: 'Pi+', 0: 'Pi0', -1: 'Pi-'}.get(qt)
        vt = q - k
        if pi_t is not None and pi_t != pion:
            try:
                Vbpp = build_scalar_vec(
                    vertex_by_particles(V, [bl, pion, pi_t]),
                    {bl: -q, pion: k, pi_t: vt}, ns, ff)
                Vpi = build(vertex_by_particles(V, [aNi, Nf, anti(pi_t)]),
                            {aNi: -p, Nf: pp, anti(pi_t): -vt}, ns, ff)
                mpi_t = ns['MPi0'] if pi_t == 'Pi0' else ns['MPiP']
                D = prop_scalar(vt, mpi_t)
                for m in range(4):
                    H[m] += Vbpp[m] * D * Vpi
            except KeyError:
                pass

    # ---- four-point contact (CT)
    try:
        vct = vertex_by_particles(V, [aNi, Nf, bl, pion])
        K = build_part(vct, {aNi: -p, Nf: pp, bl: -q, pion: k}, ns, ff,
                       None if ct_ff is None else ct_ff)
        if K is not None:
            H += K
    except KeyError:
        pass
    return H


def delta_current(V, ns, ff, boson, Ni, Nf, pion, p, q, k, pp, which,
                  part='V'):
    """H[mu, row, col] for one Delta topology, 's' or 'u'.

    No width is used: a complex denominator would make the residual complex for
    a reason that has nothing to do with the Ward identity, and the identity
    holds pole by pole.  Kinematics are chosen off the resonance so that the
    real propagator never blows up.
    """
    MN, MD = ns['MNucleon'], ns['MDelta']
    bl = boson_leg(boson)
    aNi = anti(Ni)
    vs, vu = p + q, p - k
    H = np.zeros((4, 4, 4), dtype=complex)
    if which == 's':
        qD = CHARGE[Ni] + CHARGE[boson]
        if qD not in DELTA:
            return H
        D_ = DELTA[qD]
        try:
            VbD = build_part(vertex_by_particles(V, [aNi, D_, bl]),
                             {aNi: -p, D_: vs, bl: -q}, ns, ff,
                             None if part == 'all' else VECTOR_ND[boson])
            VpD = build(vertex_by_particles(V, [anti(D_), Nf, pion]),
                        {anti(D_): -vs, Nf: pp, pion: k}, ns, ff)
        except KeyError:
            return H
        if VbD is None:
            return H
        den = dot(vs, vs) - MD ** 2
        N = rs_numerator(vs, MD)
        for m in range(4):
            acc = np.zeros((4, 4), dtype=complex)
            for nu in range(4):
                for et in range(4):
                    acc += (METRIC[nu, nu] * METRIC[et, et]
                            * VpD[nu] @ (1j * N[nu, et] / den) @ VbD[et, m])
            H[m] += acc
    else:
        qD = CHARGE[Ni] - CHARGE[pion]
        if qD not in DELTA:
            return H
        D_ = DELTA[qD]
        try:
            VpD = build(vertex_by_particles(V, [aNi, D_, pion]),
                        {aNi: -p, D_: vu, pion: k}, ns, ff)
            VbD = build_part(vertex_by_particles(V, [anti(D_), Nf, bl]),
                             {anti(D_): -vu, Nf: pp, bl: -q}, ns, ff,
                             None if part == 'all' else VECTOR_ND[boson])
        except KeyError:
            return H
        if VbD is None:
            return H
        den = dot(vu, vu) - MD ** 2
        N = rs_numerator(vu, MD)
        for m in range(4):
            acc = np.zeros((4, 4), dtype=complex)
            for nu in range(4):
                for et in range(4):
                    acc += (METRIC[nu, nu] * METRIC[et, et]
                            * VbD[nu, m] @ (1j * N[nu, et] / den) @ VpD[et])
            H[m] += acc
    return H


# ---------------------------------------------------------------- kinematics
def kinematics(ns, W, Q2, th, pion):
    """B(q) N(p) -> pi(k) N'(p') in the hadronic CM, with q^2 = -Q^2."""
    MN = ns['MNucleon']
    mpi = ns['MPi0'] if pion == 'Pi0' else ns['MPiP']
    q0 = (W ** 2 - MN ** 2 - Q2) / (2 * W)
    qz = np.sqrt(q0 ** 2 + Q2)
    ks = np.sqrt((W ** 2 - (MN + mpi) ** 2) * (W ** 2 - (MN - mpi) ** 2)) / (2 * W)
    Epi = np.sqrt(ks ** 2 + mpi ** 2)
    q = np.array([q0, 0, 0, qz], dtype=complex)
    p = np.array([W - q0, 0, 0, -qz], dtype=complex)
    k = np.array([Epi, ks * np.sin(th), 0, ks * np.cos(th)], dtype=complex)
    pp = np.array([W - Epi, -ks * np.sin(th), 0, -ks * np.cos(th)], dtype=complex)
    return p, q, k, pp


def residual(H, q, p, pp, MN):
    """(||q.H||, ||H||) summed over on-shell nucleon spins."""
    G = np.diag(METRIC).real
    C = sum(G[m] * q[m] * H[m] for m in range(4))
    num = den = 0.0
    for s1 in range(2):
        u1 = uspinor(p, MN, s1)
        for s2 in range(2):
            u2b = ubar(uspinor(pp, MN, s2))
            num += abs(u2b @ C @ u1) ** 2
            for m in range(4):
                den += abs(u2b @ H[m] @ u1) ** 2
    return np.sqrt(num), np.sqrt(den)


# --------------------------------------------------------------------- driver
CHANNELS = {
    'A': [('p', 'p', 'Pi0'), ('p', 'n', 'Pi+'),
          ('n', 'n', 'Pi0'), ('n', 'p', 'Pi-')],
    'Z': [('p', 'p', 'Pi0'), ('p', 'n', 'Pi+'),
          ('n', 'n', 'Pi0'), ('n', 'p', 'Pi-')],
    'W+': [('p', 'p', 'Pi+'), ('n', 'p', 'Pi0'), ('n', 'n', 'Pi+')],
}


def run(V, ns, ff, boson, Q2list, W=1.40, th=0.7, part='V', label=''):
    MN = ns['MNucleon']
    print("\n%s   boson %s, W = %.2f GeV, theta = %.2f rad" % (label, boson, W, th))
    print("  %-18s %8s %12s %12s %12s"
          % ("channel", "Q^2", "Born", "Delta_s", "Delta_u"))
    worst = 0.0
    for Ni, Nf, pion in CHANNELS[boson]:
        for Q2 in Q2list:
            p, q, k, pp = kinematics(ns, W, Q2, th, pion)
            row = []
            H = born_current(V, ns, ff, boson, Ni, Nf, pion, p, q, k, pp, part)
            n, d = residual(H, q, p, pp, MN)
            row.append(n / (d * W) if d else float('nan'))
            for which in ('s', 'u'):
                Hd = delta_current(V, ns, ff, boson, Ni, Nf, pion,
                                   p, q, k, pp, which, part)
                n2, d2 = residual(Hd, q, p, pp, MN)
                row.append(n2 / (d2 * W) if d2 else 0.0)
            if part == 'V':
                worst = max(worst, max(x for x in row if x == x))
            print("  %-18s %8.3f %12.2e %12.2e %12.2e"
                  % ("%s -> %s %s" % (Ni, pion, Nf), Q2,
                     row[0], row[1], row[2]))
    return worst


def unit_ff(ff):
    """Every Q^2 form factor frozen at Q^2 = 0, i.e. the point-like model.

    Not "all form factors = 1": F1n(0) = 0 and F2p(0) = kappa_p, and setting
    those to 1 would give the neutron a charge and break the identity for a
    reason that has nothing to do with the background.  FpiNDelta is left alone
    -- its argument is the Delta leg's invariant mass, not Q^2, and it sits once
    per Delta diagram, so it factors out of the identity.
    """
    out = {}
    for name, fn in ff.items():
        if name == 'FpiNDelta':
            out[name] = fn
        else:
            out[name] = (lambda f: lambda x: f(0.0))(fn)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pointlike', action='store_true',
                    help='freeze every Q^2 form factor at Q^2 = 0')
    ap.add_argument('--isospin-exact', action='store_true',
                    help='set m_pi+ = m_pi0; isolates the residual left by the '
                         'physical pion mass splitting')
    ap.add_argument('--W', type=float, default=1.40)
    ap.add_argument('--theta', type=float, default=0.7)
    a = ap.parse_args()

    ns, ff, V = load()
    # FpiNDelta OFF.  It is not a Q^2 form factor: it damps the strong vertex by
    # the Delta leg's own invariant mass, and below the pi N threshold -- which
    # is where the u-channel Delta always sits -- it is exactly zero, so the
    # u-channel current would be identically zero and nothing would be tested.
    # It multiplies each Delta diagram once, so it cannot affect conservation.
    ff = dict(ff, FpiNDelta=lambda l: 1.0)
    if a.isospin_exact:
        ns = dict(ns, MPiP=ns['MPi0'])
        print("m_pi+ SET TO m_pi0 (exact isospin)")
    if a.pointlike:
        ff = unit_ff(ff)
        print("FORM FACTORS FROZEN AT Q^2 = 0 (point-like reference)")

    worst = 0.0
    cc = 0.0
    # gamma N -> pi N : real photon, Q^2 = 0
    worst = max(worst, run(V, ns, ff, 'A', [0.0], a.W, a.theta, 'V',
                           "gamma N -> pi N   (real photon)"))
    # e N -> e N pi : the same current off the photon point
    worst = max(worst, run(V, ns, ff, 'A', [0.1, 0.5, 1.0, 2.0], a.W, a.theta,
                           'V', "e N -> e' N pi   (virtual photon)"))
    # nu N -> nu N pi : neutral current, vector part
    worst = max(worst, run(V, ns, ff, 'Z', [0.1, 0.5, 1.0, 2.0], a.W, a.theta,
                           'V', "nu N -> nu N pi  (NC, vector part)"))
    # nu N -> mu- N pi : charged current, vector part
    cc = run(V, ns, ff, 'W+', [0.1, 0.5, 1.0, 2.0], a.W, a.theta,
             'V', "nu N -> mu- N pi (CC, vector part)")
    worst = max(worst, cc)

    print("\nworst vector-current residual: %.2e" % worst)
    if worst < 1e-10:
        print("PASS")
    elif not a.isospin_exact and cc == worst:
        # Do not just say FAIL.  CVC holds in the ISOSPIN LIMIT, and the CC is
        # the one channel whose diagrams straddle the physical pion mass
        # splitting, so a residual of order (m_pi+^2 - m_pi0^2)/|t| is the
        # right answer, not a defect.  Prove it here instead of leaving the
        # reader to wonder, by redoing the same channel with m_pi+ = m_pi0.
        dmpi2 = float(np.real(ns['MPiP'])) ** 2 - float(np.real(ns['MPi0'])) ** 2
        print("the worst residual is the CHARGED CURRENT; re-running it with "
              "m_pi+ = m_pi0")
        print("(m_pi+^2 - m_pi0^2 = %.5f GeV^2, so ~1e-3 at these |t| is "
              "expected)\n" % dmpi2)
        ex = run(V, dict(ns, MPiP=ns['MPi0']), ff, 'W+', [0.1, 0.5, 1.0, 2.0],
                 a.W, a.theta, 'V',
                 "nu N -> mu- N pi (CC, vector part, m_pi+ = m_pi0)")
        print("\nCC residual: %.2e physical, %.2e degenerate" % (cc, ex))
        print("PASS -- the CC residual is the pion mass splitting"
              if ex < 1e-10 else
              "FAIL -- degenerate masses do not explain it")
    else:
        print("FAIL")

    # For the record only: the axial current is NOT conserved and must not be.
    run(V, ns, ff, 'W+', [0.5], a.W, a.theta, 'A',
        "CC AXIAL current (not conserved -- it is not supposed to be)")


if __name__ == '__main__':
    main()
