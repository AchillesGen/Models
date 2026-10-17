#!/usr/bin/env python3
"""
fig33_from_ufo.py -- gamma N -> pi N total cross sections computed directly from
the ChiPT UFO model.

Everything that defines the interaction is READ FROM THE UFO: the vertex list,
the Lorentz structure strings, the coupling values and the parameters.  Nothing
about the vertices is hard-coded here.  The only physics supplied by this script
is what a UFO does not contain: propagators, the Delta width, the phase space,
and the Davidson-Workman form factor applied at amplitude level (see below).

Form factors are set to their Q^2 -> 0 limits, which is the photoproduction
point:

    F1p(0) = 1        F2p(0) = kappa_p = +1.792847
    F1n(0) = 0        F2n(0) = kappa_n = -1.913043

Run:
    python3 fig33_from_ufo.py [path/to/ChiPT_UFO]

Writes fig33_from_ufo.csv and, if fig33_chipt_data.csv (produced by
Fig33_ChiPT.m) is present, prints a channel-by-channel comparison against it.
That comparison is the validation of this script: the Mathematica calculation
is the one checked against nucl-th/0509020v2 Appendix A to 1e-16.
"""

import os
import sys
import cmath
import math
import importlib
import itertools

import numpy as np

# ----------------------------------------------------------------- UFO loading
def load_ufo(path):
    path = os.path.abspath(path)
    parent, pkg = os.path.split(path)
    if parent not in sys.path:
        sys.path.insert(0, parent)
    P = importlib.import_module(pkg + '.parameters')
    V = importlib.import_module(pkg + '.vertices')
    return P, V


def parameter_namespace(P):
    """Resolve the UFO parameters to numbers, external first then internal."""
    ns = {'cmath': cmath, 'math': math, 'complex': complex}
    for p in P.all_parameters:
        if p.nature == 'external':
            ns[p.name] = p.value
    todo = [p for p in P.all_parameters if p.nature != 'external']
    for _ in range(200):
        rest = []
        for p in todo:
            try:
                ns[p.name] = eval(str(p.value), ns)
            except Exception:
                rest.append(p)
        if len(rest) == len(todo):
            break
        todo = rest
    if todo:
        print("  warning: unresolved parameters:", [p.name for p in todo][:6])
    return ns


# ------------------------------------------------------------- Dirac algebra
# metric diag(1,-1,-1,-1); Dirac representation, matching Fig33v2.m so the two
# calculations can be compared directly.
METRIC = np.diag([1.0, -1.0, -1.0, -1.0]).astype(complex)

_s = [np.array([[0, 1], [1, 0]], dtype=complex),
      np.array([[0, -1j], [1j, 0]], dtype=complex),
      np.array([[1, 0], [0, -1]], dtype=complex)]
_I2 = np.eye(2, dtype=complex)
_Z2 = np.zeros((2, 2), dtype=complex)

GAMMA = np.zeros((4, 4, 4), dtype=complex)
GAMMA[0] = np.block([[_I2, _Z2], [_Z2, -_I2]])
for i in range(3):
    GAMMA[i + 1] = np.block([[_Z2, _s[i]], [-_s[i], _Z2]])
GAMMA5 = 1j * GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3]
ID4 = np.eye(4, dtype=complex)

# sigma^{mu nu} = (i/2)[gamma^mu, gamma^nu]
SIGMA = np.zeros((4, 4, 4, 4), dtype=complex)
for m in range(4):
    for n in range(4):
        SIGMA[m, n] = 0.5j * (GAMMA[m] @ GAMMA[n] - GAMMA[n] @ GAMMA[m])

# Levi-Civita with all indices UP.  EPS_SIGN fixes eps^{0123}; it is validated
# against the Mathematica result rather than assumed.
EPS_SIGN = float(os.environ.get("EPS_SIGN", "-1"))
EPS = np.zeros((4, 4, 4, 4), dtype=complex)
for perm in itertools.permutations(range(4)):
    sgn = 1
    pl = list(perm)
    for a in range(4):
        for b in range(a + 1, 4):
            if pl[a] > pl[b]:
                sgn = -sgn
    EPS[perm] = EPS_SIGN * sgn


def slash(v):
    return sum(v[m] * METRIC[m, m] * GAMMA[m] for m in range(4))


def dot(a, b):
    return complex(a @ METRIC @ b)


# ------------------------------------------------- UFO Lorentz structure eval
class T:
    """A tensor with labelled axes.

    axes entries are ('L', k) for a Lorentz index labelled k and ('S', k) for a
    spinor index labelled k.  Negative labels are summed over (UFO convention);
    Lorentz sums carry the metric, spinor sums do not.
    """

    __slots__ = ('a', 'axes')

    def __init__(self, a, axes):
        self.a = np.asarray(a, dtype=complex)
        self.axes = list(axes)

    def __mul__(self, o):
        if not isinstance(o, T):
            return T(self.a * o, self.axes)
        a = np.tensordot(self.a, o.a, axes=0)
        axes = self.axes + o.axes
        return T(a, axes)._contract()

    __rmul__ = __mul__

    def __truediv__(self, o):
        return T(self.a / o, self.axes)

    def __neg__(self):
        return T(-self.a, self.axes)

    def __pow__(self, n):
        if int(n) != n or n < 1:
            raise ValueError("only positive integer powers of a tensor")
        r = self
        for _ in range(int(n) - 1):
            r = r * self
        return r

    def __add__(self, o):
        if not isinstance(o, T):
            raise TypeError("cannot add scalar to tensor")
        if self.axes == o.axes:
            return T(self.a + o.a, self.axes)
        perm = [o.axes.index(x) for x in self.axes]
        return T(self.a + np.transpose(o.a, perm), self.axes)

    def __sub__(self, o):
        return self + (-o)

    def _contract(self):
        """Contract every axis label that occurs exactly twice."""
        while True:
            dup = None
            for lab in self.axes:
                if self.axes.count(lab) == 2:
                    dup = lab
                    break
            if dup is None:
                return complex(self.a) if not self.axes else self
            i = self.axes.index(dup)
            j = self.axes.index(dup, i + 1)
            if dup[0] == 'L':
                a = np.tensordot(self.a, METRIC, axes=([i], [0]))
                # the contracted metric axis is now last; contract with axis j
                jj = j - 1 if j > i else j
                a = np.trace(a, axis1=jj, axis2=a.ndim - 1)
            else:
                a = np.trace(self.a, axis1=i, axis2=j)
            axes = [x for n, x in enumerate(self.axes) if n not in (i, j)]
            if not axes:
                # everything contracted -> an ordinary number, so that it can be
                # fed to a form factor function such as F1p(-P(-1,3)**2)
                return complex(a)
            self = T(a, axes)


def make_evaluator(mom, ff0):
    """Return the namespace used to eval() a UFO Lorentz structure string.

    mom[i] is the (all-incoming) four-momentum of external particle i, 1-based.
    """
    def P(mu, n):
        return T(mom[n], [('L', mu)])

    def Gamma(mu, i, j):
        return T(np.transpose(GAMMA, (0, 1, 2)), [('L', mu), ('S', i), ('S', j)])

    def Gamma5(i, j):
        return T(GAMMA5, [('S', i), ('S', j)])

    def Identity(i, j):
        return T(ID4, [('S', i), ('S', j)])

    def Metric(mu, nu):
        return T(METRIC, [('L', mu), ('L', nu)])

    def Sigma(mu, nu, i, j):
        return T(SIGMA, [('L', mu), ('L', nu), ('S', i), ('S', j)])

    def Epsilon(a, b, c, d):
        return T(EPS, [('L', a), ('L', b), ('L', c), ('L', d)])

    def ProjM(i, j):
        return T(0.5 * (ID4 - GAMMA5), [('S', i), ('S', j)])

    def ProjP(i, j):
        return T(0.5 * (ID4 + GAMMA5), [('S', i), ('S', j)])

    ns = dict(P=P, Gamma=Gamma, Gamma5=Gamma5, Identity=Identity, Metric=Metric,
              Sigma=Sigma, Epsilon=Epsilon, ProjM=ProjM, ProjP=ProjP,
              complex=complex, cmath=cmath)
    ns.update(ff0)
    return ns


def eval_structure(struct, mom, ff0):
    return eval(struct, make_evaluator(mom, ff0))


def _declared_form_factors(path):
    """Every form factor function name the UFO's Lorentz structures call."""
    import re
    lz = importlib.import_module(os.path.split(os.path.abspath(path))[1]
                                 + '.lorentz')
    out = set()
    for l in lz.all_lorentz:
        out |= set(re.findall(r'\b(F[A-Za-z0-9]*)\(\s*-?\s*P\(', l.structure))
    return sorted(out)


# --------------------------------------------------------------- UFO helpers
def vertex_by_particles(V, names):
    want = sorted(names)
    out = [v for v in V.all_vertices if sorted(p.name for p in v.particles) == want]
    if not out:
        raise KeyError("no UFO vertex with particles %s" % (names,))
    if len(out) > 1:
        raise KeyError("several UFO vertices with particles %s" % (names,))
    return out[0]


def vertex_tensor(v, order, mom, ns, ff0):
    """Sum over the vertex's (colour, lorentz) pairs, returning one T.

    `order` maps the UFO particle slot (1-based) to our momentum labels, i.e.
    order[i] is the momentum to use for UFO leg i.
    """
    legs = {i + 1: mom[order[i + 1]] for i in range(len(v.particles))}
    tot = None
    for (ci, li), c in v.couplings.items():
        val = eval(str(c.value), ns)
        piece = eval_structure(v.lorentz[li].structure, legs, ff0) * val
        tot = piece if tot is None else tot + piece
    return tot


# ------------------------------------------------------------------- spinors
def uspinor(p, m, s):
    """Dirac-representation u(p,s), normalisation ubar u = 2m (as Fig33v2.m)."""
    E = p[0].real
    chi = np.array([1.0, 0.0]) if s == 0 else np.array([0.0, 1.0])
    sp = sum(p[i + 1] * _s[i] for i in range(3))
    lower = (sp @ chi) / (E + m)
    return np.sqrt(E + m) * np.concatenate([chi, lower]).astype(complex)


def ubar(u):
    return np.conjugate(u) @ GAMMA[0]


POL = [(-1.0 / np.sqrt(2)) * np.array([0, 1, 1j, 0], dtype=complex),
       (+1.0 / np.sqrt(2)) * np.array([0, 1, -1j, 0], dtype=complex)]


# --------------------------------------------------------------- propagators
def prop_fermion(v, m):
    return 1j * (slash(v) + m * ID4) / (dot(v, v) - m ** 2)


def prop_scalar(v, m):
    return 1j / (dot(v, v) - m ** 2)


def rs_numerator(v, M):
    """Rarita-Schwinger numerator, Eq. (43); returns N[nu, eta] of 4x4 blocks."""
    sl = slash(v) + M * ID4
    out = np.zeros((4, 4, 4, 4), dtype=complex)
    for nu in range(4):
        for et in range(4):
            br = (-METRIC[nu, et] * ID4
                  + (1.0 / 3.0) * GAMMA[nu] @ GAMMA[et]
                  + (2.0 / (3.0 * M ** 2)) * v[nu] * v[et] * ID4
                  - (1.0 / (3.0 * M)) * (v[nu] * GAMMA[et] - GAMMA[nu] * v[et]))
            out[nu, et] = sl @ br
    return out


# ------------------------------------------------------- width and form factor
def kmom(l, m, MN):
    r = (l - MN ** 2 - m ** 2) ** 2 - 4.0 * m ** 2 * MN ** 2
    return 0.0 if (r <= 0.0 or l <= 0.0) else np.sqrt(r) / (2.0 * np.sqrt(l))


def make_Xpi(MN, mpi, MD):
    k0 = kmom(MD ** 2, mpi, MN)

    def Xpi(l):
        if l < (MN + mpi) ** 2:
            return 0.0
        r = kmom(l, mpi, MN) / k0
        return 2.0 * r ** 3 / (1.0 + r ** 5)
    return Xpi


def FhatB(s, u, t, MN, mpi, Lam):
    F1 = Lam ** 4 / (Lam ** 4 + (s - MN ** 2) ** 2)
    F2 = Lam ** 4 / (Lam ** 4 + (u - MN ** 2) ** 2)
    F3 = Lam ** 4 / (Lam ** 4 + (t - mpi ** 2) ** 2)
    return 1.0 - (1.0 - F1) * (1.0 - F2) * (1.0 - F3)


# ------------------------------------------------------------------ channels
# For gamma(q) N(p) -> pi(k) N(p'), UFO legs are all OUTGOING, so an incoming
# particle enters a vertex with minus its momentum.  In each vertex the leg
# named after the PARTICLE (not the antiparticle) carries the row (ubar) index.
CHANNELS = {
    # dlt_s: gamma N_i -> Delta ;  dlt_u: N_i -> Delta + pi.  For the charged
    # pion channels these are DIFFERENT charge states.
    'pi-p': dict(Ni='n', Nf='p', pion='Pi-', dlt_s='Delta0', dlt_u='Delta+'),
    'pi+n': dict(Ni='p', Nf='n', pion='Pi+', dlt_s='Delta+', dlt_u='Delta0'),
    'pi0p': dict(Ni='p', Nf='p', pion='Pi0', dlt_s='Delta+', dlt_u='Delta+'),
    'pi0n': dict(Ni='n', Nf='n', pion='Pi0', dlt_s='Delta0', dlt_u='Delta0'),
}


def build(v, momout, ns, ff0):
    """Evaluate a UFO vertex to a plain array.

    momout maps each leg's particle NAME to that leg's OUTGOING four-momentum.
    Axis order of the result: [RS Lorentz, vector Lorentz, row spinor, col
    spinor], omitting whichever are absent.  The row index is the fermionic leg
    with positive PDG (the particle leg, i.e. ubar); the column is the other.
    """
    names = [p.name for p in v.particles]
    legs = {i + 1: momout[names[i]] for i in range(len(names))}
    tot = None
    for (ci, li), c in v.couplings.items():
        val = eval(str(c.value), dict(ns, **ff0))
        piece = eval_structure(v.lorentz[li].structure, legs, ff0) * val
        tot = piece if tot is None else tot + piece
    ferm = [(i + 1, v.particles[i]) for i in range(len(names))
            if v.particles[i].spin in (2, 4)]
    vec = [(i + 1) for i in range(len(names)) if v.particles[i].spin == 3]
    rs = [(i + 1) for i in range(len(names)) if v.particles[i].spin == 4]
    row = max(ferm, key=lambda x: x[1].pdg_code)[0]
    col = min(ferm, key=lambda x: x[1].pdg_code)[0]
    order = [('L', n) for n in rs] + [('L', n) for n in vec] + [('S', row), ('S', col)]
    return np.transpose(tot.a, [tot.axes.index(x) for x in order])


def amplitude(ch, W, th, V, ns, ff0, opt):
    """Return M[mu, row, col] for gamma(q) N(p) -> pi(k) N(p')."""
    MN, MD, mpi = ns['MNucleon'], ns['MDelta'], ns['MPi0']
    Gam0, Lam = ns['WDeltaP'], ns['LambdaFF']
    c = CHANNELS[ch]
    Ni, Nf, pion = c['Ni'], c['Nf'], c['pion']
    dlt_s, dlt_u = c['dlt_s'], c['dlt_u']
    aNi, aNf = Ni + '~', Nf + '~'
    adlt_s, adlt_u = dlt_s + '~', dlt_u + '~'
    apion = {'Pi0': 'Pi0', 'Pi+': 'Pi-', 'Pi-': 'Pi+'}[pion]

    qs = (W ** 2 - MN ** 2) / (2 * W)
    ks = np.sqrt((W ** 2 - (MN + mpi) ** 2) * (W ** 2 - (MN - mpi) ** 2)) / (2 * W)
    Epi = np.sqrt(ks ** 2 + mpi ** 2)
    p = np.array([W - qs, 0, 0, -qs], dtype=complex)
    q = np.array([qs, 0, 0, qs], dtype=complex)
    k = np.array([Epi, ks * np.sin(th), 0, ks * np.cos(th)], dtype=complex)
    pp = np.array([W - Epi, -ks * np.sin(th), 0, -ks * np.cos(th)], dtype=complex)
    vs, vu, vt = p + q, p - k, k - q
    s, u, t = dot(vs, vs), dot(vu, vu), dot(vt, vt)

    M = np.zeros((4, 4, 4), dtype=complex)

    if opt.get('born', True):
        B = np.zeros((4, 4, 4), dtype=complex)
        # s-channel: gamma N -> N* -> pi N
        Vg = build(vertex_by_particles(V, [aNi, Ni, 'A']),
                   {aNi: -p, Ni: vs, 'A': -q}, ns, ff0)
        Vp = build(vertex_by_particles(V, [aNi, Nf, pion]),
                   {aNi: -vs, Nf: pp, pion: k}, ns, ff0)
        S = prop_fermion(vs, MN)
        for m in range(4):
            B[m] += Vp @ S @ Vg[m]
        # u-channel
        Vp2 = build(vertex_by_particles(V, [aNi, Nf, pion]),
                    {aNi: -p, Nf: vu, pion: k}, ns, ff0)
        Vg2 = build(vertex_by_particles(V, [aNf, Nf, 'A']),
                    {aNf: -vu, Nf: pp, 'A': -q}, ns, ff0)
        Su = prop_fermion(vu, MN)
        for m in range(4):
            B[m] += Vg2[m] @ Su @ Vp2
        # t-channel pion exchange (charged pions only)
        if pion != 'Pi0':
            try:
                Vgpp = build_scalar_vec(vertex_by_particles(V, ['A', pion, apion]),
                                        {'A': -q, pion: k, apion: -vt}, ns, ff0)
                Vpi = build(vertex_by_particles(V, [aNi, Nf, pion]),
                            {aNi: -p, Nf: pp, pion: vt}, ns, ff0)
                D = prop_scalar(vt, mpi)
                for m in range(4):
                    B[m] += Vgpp[m] * D * Vpi
            except KeyError:
                pass
            # Kroll-Ruderman contact
            try:
                VK = build(vertex_by_particles(V, ['A', Nf, aNi, pion]),
                           {'A': -q, Nf: pp, aNi: -p, pion: k}, ns, ff0)
                B += VK
            except KeyError:
                pass
        if opt.get('ff', True):
            B = B * FhatB(s.real, u.real, t.real, MN, mpi, Lam)
        M += B

    if opt.get('delta', True):
        # Overall sign of the Delta sector relative to the Born.  Fig33v2.m
        # carries the same relative minus (its explicit s-channel sign fix).
        # Delta-only is insensitive to it; the Born/Delta interference is not.
        sD = opt.get('dsign', 1.0)
        Xpi = make_Xpi(MN, mpi, MD)
        if opt.get('edw', True):
            X = Xpi(s.real) + Xpi(u.real) - Xpi(s.real) * Xpi(u.real)
            Gam, ffD = Gam0 * X, np.sqrt(X)
            # opt['ffD']=False: keep the running width but drop the amplitude-
            # level sqrt(X), because the UFO's own FpiNDelta already supplies a
            # form factor on the strong vertex (CHIPT_FF=Delta builds).  Without
            # this the two would multiply.
            if not opt.get('ffD', True):
                ffD = 1.0
            Ds = s - MD ** 2 + 1j * MD * Gam
            Du = u - MD ** 2 + 1j * MD * Gam
        else:
            ffD = 1.0
            Ds = s - MD ** 2 + 1j * MD * Gam0
            Du = u - MD ** 2
        # s-channel: gamma N -> Delta -> pi N
        VgD = build(vertex_by_particles(V, ['A', dlt_s, aNi]),
                    {'A': -q, dlt_s: vs, aNi: -p}, ns, ff0)         # [nu, mu, r, c]
        VpD = build(vertex_by_particles(V, [adlt_s, Nf, pion]),
                    {adlt_s: -vs, Nf: pp, pion: k}, ns, ff0)        # [eta, r, c]
        Ns = rs_numerator(vs, MD)
        for m in range(4):
            acc = np.zeros((4, 4), dtype=complex)
            for nu in range(4):
                for et in range(4):
                    # The RS numerator N[nu,eta] is NOT symmetric: the vertex on
                    # the LEFT of the fermion line pairs with its FIRST index.  In
                    # the s-channel that is the strong vertex (the u-channel below
                    # is the other way round because the EM vertex is on the left).
                    acc += (METRIC[nu, nu] * METRIC[et, et]
                            * VpD[nu] @ (1j * Ns[nu, et] / Ds) @ VgD[et, m])
            M[m] += sD * ffD * acc
        # u-channel: N -> Delta pi, then gamma Delta -> N
        VpD2 = build(vertex_by_particles(V, [aNi, dlt_u, pion]),
                     {aNi: -p, dlt_u: vu, pion: k}, ns, ff0)
        VgD2 = build(vertex_by_particles(V, [adlt_u, Nf, 'A']),
                     {adlt_u: -vu, Nf: pp, 'A': -q}, ns, ff0)
        Nu = rs_numerator(vu, MD)
        for m in range(4):
            acc = np.zeros((4, 4), dtype=complex)
            for nu in range(4):
                for et in range(4):
                    acc += (METRIC[nu, nu] * METRIC[et, et]
                            * VgD2[nu, m] @ (1j * Nu[nu, et] / Du) @ VpD2[et])
            M[m] += sD * ffD * acc
    return M, p, pp


def build_scalar_vec(v, momout, ns, ff0):
    """A vertex with no fermions: returns an array indexed by the vector leg."""
    names = [p.name for p in v.particles]
    legs = {i + 1: momout[names[i]] for i in range(len(names))}
    tot = None
    for (ci, li), c in v.couplings.items():
        val = eval(str(c.value), dict(ns, **ff0))
        piece = eval_structure(v.lorentz[li].structure, legs, ff0) * val
        tot = piece if tot is None else tot + piece
    vec = [i + 1 for i in range(len(names)) if v.particles[i].spin == 3][0]
    return np.transpose(tot.a, [tot.axes.index(('L', vec))])


# ---------------------------------------------------------------- observables
HBARC2 = 389.379  # GeV^-2 -> microbarn


def sigma_tot(ch, W, V, ns, ff0, opt, nth=24):
    MN, mpi = ns['MNucleon'], ns['MPi0']
    qs = (W ** 2 - MN ** 2) / (2 * W)
    ks = np.sqrt((W ** 2 - (MN + mpi) ** 2) * (W ** 2 - (MN - mpi) ** 2)) / (2 * W)
    xs = [-1.0 + (i + 0.5) * (2.0 / nth) for i in range(nth)]
    tot = 0.0
    for x in xs:
        M, p, pp = amplitude(ch, W, np.arccos(x), V, ns, ff0, opt)
        acc = 0.0
        for s1 in range(2):
            ui = uspinor(p, MN, s1)
            for s2 in range(2):
                ub = ubar(uspinor(pp, MN, s2))
                for lam in range(2):
                    amp = sum(METRIC[m, m] * POL[lam][m] * (ub @ M[m] @ ui)
                              for m in range(4))
                    acc += abs(amp) ** 2
        tot += acc / 4.0
    tot *= 2.0 / nth
    return 2 * np.pi * HBARC2 * ks / (64 * np.pi ** 2 * W ** 2 * qs) * tot


# ------------------------------------------------------------- measured points
def read_pi0p_data(path, MN):
    """Parse ELA-Pion-Photoproduction/pi0p_data.m for the measured TOTAL
    sigma(gamma p -> pi0 p).  Returns (low, high) as (Eg, sigma, err) arrays;
    the low-energy set is tabulated in W and converted with the same nucleon
    mass used for the curves."""
    if not os.path.exists(path):
        return None, None
    txt = open(path).read()

    def block(name, ncol):
        i = txt.index(name)
        i = txt.index('{', i) + 1
        j = txt.index('}', i)
        nums = [float(x) for x in txt[i:j].replace('\n', ' ').split(',') if x.strip()]
        return np.array(nums).reshape(-1, ncol)

    hi = block('dHiRaw = Partition[', 6)
    lo = block('dLoRaw = Partition[', 4)
    low = np.column_stack([(lo[:, 0] ** 2 - MN ** 2) / (2 * MN), lo[:, 1], lo[:, 2]])
    high = np.column_stack([hi[:, 0] / 1000.0, hi[:, 1], hi[:, 2]])
    return low, high


VECMESON_CSV = 'fig33_vecmeson_scan_grid.csv'


def read_vecmeson(path=VECMESON_CSV):
    """{channel: (Eg, sigma_ub)} for Born + Delta + t-channel omega/rho.

    Written by fig33_vecmeson.m on scan.py's photon grid, which is NOT the grid
    this script uses -- the curves are simply drawn on their own abscissa.  The
    vector mesons cannot come from the UFO: ChiPT.fr has none, so those couplings
    are the ELA fit values of nucl-th/0509020v2 Eqs. (15)-(16).  Optional; the
    figure just omits the curves if the file is absent.
    """
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        names = [n.strip().strip('"') for n in f.readline().strip().split(',')]
    d = np.loadtxt(path, delimiter=',', skiprows=1, ndmin=2)
    return {n[:-4]: (d[:, 0], d[:, i]) for i, n in enumerate(names)
            if n.endswith('_vec')}


def make_plot(rows, ns, stem='fig33_from_ufo'):
    """Publication-quality 2x2 figure (PDF + PNG).

    Conventions follow a physics journal (PRC/PRD): double-column width, serif
    face matching a LaTeX manuscript, ticks inward on all four sides with minor
    ticks, hairline axes and no grid, vector output.

    Colours are the two categorical slots of a validated colourblind-safe
    palette (#2a78d6 / #eb6834: CVD dE 24.7 protan, 33.6 normal vision).  The
    curves are additionally separated by line style and the two data sets by
    marker shape, so no identity rests on colour alone.
    """
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
    except ImportError:
        print("matplotlib not available -- skipping the plot")
        return

    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['STIXGeneral', 'DejaVu Serif'],
        'mathtext.fontset': 'stix',
        'font.size': 9, 'axes.labelsize': 9,
        'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 7.5,
        'axes.linewidth': 0.7,
        'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'xtick.major.width': 0.7, 'ytick.major.width': 0.7,
        'xtick.minor.width': 0.5, 'ytick.minor.width': 0.5,
        'xtick.major.size': 3.4, 'ytick.major.size': 3.4,
        'xtick.minor.size': 1.9, 'ytick.minor.size': 1.9,
        'legend.frameon': False, 'legend.handlelength': 2.0,
        'legend.labelspacing': 0.35, 'legend.borderpad': 0.0,
        'savefig.bbox': 'tight', 'savefig.pad_inches': 0.02,
    })

    C_DB, C_D, INK = '#2a78d6', '#eb6834', '#111111'
    chans  = ['pi-p', 'pi+n', 'pi0p', 'pi0n']
    titles = {'pi-p': r'$\pi^{-}p$', 'pi+n': r'$\pi^{+}n$',
              'pi0p': r'$\pi^{0}p$', 'pi0n': r'$\pi^{0}n$'}
    # Common y-scale across all four panels so the channels are directly
    # comparable (the largest curve is the Delta-only pi0 p peak at ~380 ub).
    YMAX, YSTEP = 400, 100
    panel  = ['(a)', '(b)', '(c)', '(d)']

    datafile = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                            'ELA-Pion-Photoproduction', 'pi0p_data.m')
    low, high = read_pi0p_data(datafile, ns['MNucleon'])
    vec = read_vecmeson()

    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.0), sharex=True, sharey=True)
    for n, (ax, ch) in enumerate(zip(axes.ravel(), chans)):
        if ch == 'pi0p' and low is not None:
            ax.errorbar(low[:, 0], low[:, 1], yerr=low[:, 2], fmt='o', ms=2.2,
                        mfc=INK, mec=INK, ecolor=INK, elinewidth=0.5,
                        capsize=0, ls='none', zorder=2)
            ax.errorbar(high[:, 0], high[:, 1], yerr=high[:, 2], fmt='s', ms=2.6,
                        mfc='none', mec=INK, mew=0.7, ecolor=INK, elinewidth=0.5,
                        capsize=0, ls='none', zorder=2)
        for cv, col, ls in (('Delta only', C_D, (0, (4.5, 2.2))),
                            ('Delta+Born', C_DB, '-')):
            sel = sorted([(r[2], r[3]) for r in rows if r[0] == cv and r[1] == ch])
            ax.plot([x for x, _ in sel], [y for _, y in sel],
                    color=col, ls=ls, lw=1.3, zorder=3, solid_joinstyle='round')
        # On its own (denser) grid -- see read_vecmeson.
        if ch in vec:
            ax.plot(*vec[ch], color=INK, ls=(0, (5.0, 2.0)), lw=1.1, zorder=4)
        ax.set_xlim(0.1, 1.0)
        ax.set_ylim(0, YMAX)
        ax.set_yticks(np.arange(0, YMAX + 1, YSTEP))
        ax.text(0.035, 0.93, panel[n], transform=ax.transAxes, va='top', fontsize=8.5)
        ax.text(0.965, 0.93, titles[ch], transform=ax.transAxes,
                va='top', ha='right', fontsize=11)
        if n >= 2:
            ax.set_xlabel(r'$E_{\gamma}$  (GeV)')
        if n % 2 == 0:                      # shared scale -> label the left column only
            ax.set_ylabel(r'$\sigma$  ($\mu$b)')

    handles = [Line2D([], [], color=C_DB, ls='-', lw=1.3,
                      label=r'$\Delta(1232)$ + Born'),
               Line2D([], [], color=C_D, ls=(0, (4.5, 2.2)), lw=1.3,
                      label=r'$\Delta(1232)$ only')]
    if vec:
        handles.append(Line2D([], [], color=INK, ls=(0, (5.0, 2.0)), lw=1.1,
                              label=r'  $+\ \omega,\rho$ exchange'))
    axes[0, 0].legend(handles=handles, loc='upper right',
                      bbox_to_anchor=(0.99, 0.86))
    dh = [Line2D([], [], ls='none', marker='o', ms=2.8, mfc=INK, mec=INK,
                 label=r'data, $\Delta$ region'),
          Line2D([], [], ls='none', marker='s', ms=3.0, mfc='none', mec=INK,
                 mew=0.7, label='data, higher resonances')]
    axes[1, 0].legend(handles=dh, loc='upper right', bbox_to_anchor=(0.99, 0.86))

    fig.subplots_adjust(hspace=0.06, wspace=0.06)
    for ext in ('pdf', 'png'):
        fig.savefig('%s.%s' % (stem, ext), dpi=600)
    print("wrote %s.pdf and %s.png" % (stem, stem))


def main():
    ufo = sys.argv[1] if len(sys.argv) > 1 else 'ChiPT_UFO'
    P, V = load_ufo(ufo)
    ns = parameter_namespace(P)
    kp, kn = 1.792847, -1.913043
    ff0 = {'F1p': lambda q2: 1.0, 'F1n': lambda q2: 0.0,
           'F2p': lambda q2: kp, 'F2n': lambda q2: kn}
    # Everything else the UFO declares is set to 1.  Two different reasons, and
    # both are exact here rather than approximations:
    #   * every Q^2 form factor in the model is a ratio normalised to 1 at
    #     Q^2 = 0, and this is real photoproduction, so Q^2 = 0 throughout;
    #   * FpiNDelta is not a Q^2 form factor at all, and this script applies
    #     the paper's sqrt(X_pi(s,u)) at AMPLITUDE level instead (opt['ffD']),
    #     so leaving it in the vertex as well would square it.
    # Reading the names off the model rather than listing them means this keeps
    # working when a form factor is added; without it the script dies with
    # "NameError: FVND is not defined" on any build newer than ChiPT_UFO_V3.
    for _name in _declared_form_factors(ufo):
        ff0.setdefault(_name, lambda x: 1.0)
    MN, mpi = ns['MNucleon'], ns['MPi0']
    print("UFO: %s   ee=%.6f  MN=%.6f  MDelta=%.4f  Gamma=%.4f  Lambda=%.4f"
          % (ufo, ns['ee'].real, MN, ns['MDelta'], ns['WDeltaP'], ns['LambdaFF']))
    print("form factors at Q^2=0: F1p=1  F1n=0  F2p=%.6f  F2n=%.6f" % (kp, kn))

    Ethr = ((MN + mpi) ** 2 - MN ** 2) / (2 * MN)
    egs = [Ethr + 0.002] + [round(0.16 + 0.02 * i, 4) for i in range(43)]
    opts = {'Delta only': dict(born=False, delta=True, ff=True, edw=True),
            'Delta+Born': dict(born=True, delta=True, ff=True, edw=True)}
    rows = []
    for lbl, opt in opts.items():
        for ch in CHANNELS:
            for eg in egs:
                W = np.sqrt(MN ** 2 + 2 * MN * eg)
                rows.append((lbl, ch, eg, sigma_tot(ch, W, V, ns, ff0, opt).real))
    with open('fig33_from_ufo.csv', 'w') as f:
        f.write("curve,channel,Eg,sigma_ub\n")
        for r in rows:
            f.write("%s,%s,%.5f,%.6f\n" % r)
    print("\nwrote fig33_from_ufo.csv")
    make_plot(rows, ns)
    print("\n%-12s %-6s %10s %10s" % ("curve", "chan", "peak", "s(1GeV)"))
    for lbl in opts:
        for ch in CHANNELS:
            sel = [r for r in rows if r[0] == lbl and r[1] == ch]
            print("%-12s %-6s %10.1f %10.1f"
                  % (lbl, ch, max(x[3] for x in sel), sel[-1][3]))
    return rows


if __name__ == '__main__':
    main()
