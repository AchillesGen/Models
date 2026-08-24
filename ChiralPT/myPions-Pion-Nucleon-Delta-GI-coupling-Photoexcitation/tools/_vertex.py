"""Shared helper for the verification scripts: evaluate a chosen subset of a
UFO vertex's Lorentz structures.

Selecting structures BY NAME matters.  wprod_from_ufo.build_split separates
vector from axial by testing for Gamma5 in the structure string, which is right
for the four-point contact term but wrong for the N -> Delta vertex, where the
C5A structure carries an explicit Gamma5 while one of the two vector (G1/G2)
structures does too.  These scripts therefore name the structures explicitly.
"""
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.environ.get(
    'CHIPT_DIR', os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import wprod_from_ufo as w                                    # noqa: E402

MODEL = os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V8')


def build_named(v, momout, ns, ff, keep):
    """The vertex tensor built from only the Lorentz structures named in `keep`.

    The full `lorentz` list is kept so the (colour, lorentz) coupling indices
    stay valid; only the couplings are filtered.  Index order of the result is
    [Rarita-Schwinger legs, vector legs, row spinor, column spinor], with the
    row taken as the larger PDG code, matching wprod_from_ufo.
    """
    names = [p.name for p in v.particles]
    legs = {i + 1: momout[names[i]] for i in range(len(names))}
    tot = None
    for (ci, li), c in v.couplings.items():
        if v.lorentz[li].name not in keep:
            continue
        val = eval(str(c.value), dict(ns, **ff))
        piece = w.eval_structure(v.lorentz[li].structure, legs, ff) * val
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


def with_ff(v, *ffnames):
    """Names of the Lorentz structures of `v` that carry one of these form factors.

    Select structures this way, never by their generated names: FeynRules
    numbers them in the order it happens to emit them, so FRV1..FRVn are
    reshuffled whenever a term is added to the model.  The form factor a
    structure carries is a property of the physics and is stable.
    """
    want = set(ffnames)
    out = set()
    for l in v.lorentz:
        if want & set(re.findall(r'\b(F[A-Za-z0-9]+)\(', l.structure)):
            out.add(l.name)
    return out


def vertex(V, names):
    """The vertex with exactly this particle-name tuple."""
    for v in V:
        if tuple(p.name for p in v.particles) == tuple(names):
            return v
    raise KeyError(names)


def load(model=None):
    """(parameters namespace, form factors, vertex list) for a UFO model."""
    P, Vm = w.load_ufo(model or MODEL)
    ns = w.parameter_namespace(P)
    ff = w.form_factors(ns, True)
    V = Vm.all_vertices if hasattr(Vm, 'all_vertices') else list(Vm)
    return ns, ff, V
