#!/usr/bin/env python3
"""Audit every UFO vertex that touches a composite particle.

Three questions, asked of the exported model rather than of the Lagrangian:

  1. Does every vertex with a hadron on it carry a form factor?  A point-like
     pion, nucleon or Delta is a statement, and an unintended one is invisible
     -- the vertex simply works and gives the wrong Q^2 or W dependence.

  2. Is each form factor's ARGUMENT the leg it was meant to be?  A form factor
     Value is a raw Python string, so FeynRules splices the leg index in
     verbatim and never relabels it to match the exported vertex ordering.
     `-P(-9,n)**2` is Q^2 only if leg n is the gauge boson; `+P(-9,n)**2` is an
     invariant mass squared only if leg n is a hadron.  Getting this wrong is
     completely silent.

  3. Does the vertex actually depend on more than one invariant?  A UFO form
     factor is a function of ONE argument, and Sherpa's reader allows one form
     factor per Lorentz structure.  Where a vertex sits between two internal
     lines its exact form factor is a function of two invariants and the model
     has to approximate -- usually by keeping the dominant one, sometimes by
     factorising the two across neighbouring vertices.  Those are the cases
     worth stating in the paper, so they are flagged here.

The internal-leg information in ROLES is not guessed: it is the set of
topologies the model's own amplitude builders construct (fig33_from_ufo.py for
gamma N -> pi N, wprod_from_ufo.py for nu N -> l N pi, tools/ward_background.py
for the rest).  A leg is "internal" if some topology puts a propagator on it.

Usage:  python3 tools/ff_audit.py [--all]      (CHIPT_MODEL selects the UFO)
"""
import argparse
import re

from _vertex import load                                       # sets sys.path

FF_CALL = re.compile(r'\b(F[A-Za-z0-9]*)\(\s*(-?)\s*P\(-?\d+,(\d+)\)\*\*2\s*\)')

# Composite = made of quarks in this model.  Everything else (leptons, gauge
# bosons, Higgs, ghosts) is elementary and needs no form factor.
COMPOSITE = re.compile(r'^(p|n|Pi0|Pi\+|Pi-|Delta(\+\+|\+|0|-))(~)?$')

SPINNAME = {1: 'scalar', 2: 'fermion', 3: 'vector', 4: 'RS'}


def is_composite(name):
    return bool(COMPOSITE.match(name))


def kind(names):
    """A coarse role for the vertex, from its particle content."""
    nb = sum(1 for x in names if x in ('A', 'Z', 'W+', 'W-'))
    npi = sum(1 for x in names if x.startswith('Pi'))
    nnuc = sum(1 for x in names if x.strip('~') in ('p', 'n'))
    ndel = sum(1 for x in names if x.startswith('Delta'))
    nlep = sum(1 for x in names
               if x.strip('~') in ('e-', 'mu-', 'ta-', 've', 'vm', 'vt'))
    if nlep:
        return 'leptonic'
    if nnuc == 2 and nb == 1 and npi == 0:
        return 'NNV'
    if nnuc == 2 and npi == 1 and nb == 0:
        return 'NNpi'
    if nnuc == 2 and nb == 1 and npi == 1:
        return 'contact'
    if nnuc == 2 and npi >= 2 and nb == 0:
        return 'NNpipi'
    if nnuc == 1 and ndel == 1 and nb == 1 and npi == 0:
        return 'NDV'
    if nnuc == 1 and ndel == 1 and nb >= 1 and npi >= 1:
        return 'NDVpi'
    if nnuc == 1 and ndel == 1 and npi >= 1:
        return 'NDpi'
    if ndel == 2:
        return 'DD'
    if npi >= 2 and nb >= 1:
        return 'Vpipi'
    if npi >= 1 and nb >= 2:
        return 'VVpi'
    if npi >= 3 and nb == 0:
        return 'pipipipi'
    return 'other'


# For each role: which legs carry a propagator somewhere in the model's own
# topologies, and what the exact vertex function would depend on.
ROLES = {
    'NNV':   ("one nucleon (s- or u-channel pole)",
              "Q^2 and the off-shell nucleon's p^2",
              "Q^2 only; the p^2 dependence is left to the propagator, which "
              "is the standard choice and is what CVC is formulated with"),
    'NNpi':  ("one nucleon (NP/CNP) OR the pion (pion-in-flight)",
              "the off-shell nucleon's p^2 AND the exchanged pion's t",
              "point-like in the UFO. fig33_from_ufo.py applies the "
              "Davidson-Workman Fhat_B(s,u,t) at AMPLITUDE level instead, "
              "because it is a function of three invariants and no "
              "single-argument vertex form factor can express it"),
    'contact': ("none: every leg is external except the gauge boson",
                "Q^2 only",
                "Q^2, exactly right"),
    'NDV':   ("the Delta",
              "Q^2 AND the Delta leg's invariant mass W^2",
              "FACTORISED ACROSS TWO VERTICES: FCA5(Q^2)/FVND(Q^2) here, and "
              "sqrt(X_pi(W^2)) on the strong Delta -> N pi vertex, one factor "
              "per Delta diagram. Exact only if the true form factor "
              "factorises as F(Q^2) g(W^2)"),
    'NDVpi': ("the Delta",
              "the Delta leg's invariant mass W^2 AND the boson's Q^2",
              "sqrt(X_pi(P_Delta^2)) only. These are the four-point terms the "
              "gauged strong vertex generates; the Q^2 damping that belongs "
              "to them is the transition one, already carried by the "
              "neighbouring three-point vertex in every topology the model "
              "builds"),
    'NNpipi': ("one nucleon",
               "the off-shell nucleon's p^2 and the pion invariants",
               "point-like. Weinberg-Tomozawa two-pion contact; no topology "
               "in this model uses it at tree level"),
    'VVpi':  ("none in single-pion production",
              "both boson virtualities",
              "point-like. Two-boson seagulls, reached only by Compton-like "
              "processes this model is not used for"),
    'NDpi':  ("the Delta",
              "the Delta leg's invariant mass W^2",
              "FpiNDelta(P_Delta^2), exactly right"),
    'DD':    ("both Delta legs",
              "both Delta invariant masses",
              "point-like. Only reached in Delta -> Delta pi / Delta -> Delta "
              "gamma, which no topology in this model uses at tree level"),
    'Vpipi': ("the exchanged pion (pion-in-flight)",
              "Q^2 AND the exchanged pion's t",
              "Q^2 only (FW1). The t dependence is dropped, which is the "
              "usual treatment and is what keeps the Ward identity exact"),
    'pipipipi': ("any pion",
                 "the off-shell pion invariants",
                 "point-like. Pure chiral contact terms, not used by any "
                 "topology in this model"),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--all', action='store_true',
                    help='list every vertex, not only the composite ones')
    a = ap.parse_args()

    ns, ff, V = load()
    rows, bad_leg, missing, twovar = [], [], [], set()

    for v in V:
        names = [p.name for p in v.particles]
        spins = [p.spin for p in v.particles]
        comp = [x for x in names if is_composite(x)]
        if not comp and not a.all:
            continue
        role = kind(names)
        if role == 'leptonic':
            continue
        found = []
        for l in v.lorentz:
            for fn, sign, leg in FF_CALL.findall(l.structure):
                leg = int(leg)
                want = 'vector' if sign == '-' else 'hadron'
                got = SPINNAME.get(spins[leg - 1], '?')
                ok = (got == 'vector') if want == 'vector' else (got != 'vector')
                found.append((fn, sign, leg, got, ok))
                if not ok:
                    bad_leg.append((v.name, names, fn, sign, leg, got))
        rows.append((v.name, names, role, found))
        if comp and not found:
            missing.append((v.name, names, role))
        if found and role in ROLES and 'AND' in ROLES[role][1]:
            twovar.add(role)
        if not found and role in ROLES and 'AND' in ROLES[role][1]:
            twovar.add(role)

    print("=" * 78)
    print("FORM FACTOR AUDIT -- vertices with at least one composite leg")
    print("=" * 78)
    print("%-7s %-34s %-9s %s" % ("vertex", "particles", "role", "form factors"))
    for name, names, role, found in rows:
        tag = ", ".join("%s(%sP%d:%s)%s" % (fn, sg, lg, gt, "" if ok else " <-BAD")
                        for fn, sg, lg, gt, ok in found) or "-- none --"
        print("%-7s %-34s %-9s %s" % (name, " ".join(names), role, tag))

    print("\n" + "-" * 78)
    print("1. ARGUMENT LEG CHECK")
    print("-" * 78)
    if bad_leg:
        for name, names, fn, sg, leg, got in bad_leg:
            print("  MISMATCH %s %s: %s reads %sP(leg %d), which is a %s"
                  % (name, " ".join(names), fn, sg, leg, got))
    else:
        n = sum(len(f) for _, _, _, f in rows)
        print("  %d form factor placements, 0 mismatches."
              "  '-P**2' always names a gauge boson (= Q^2) and '+P**2'"
              " always names a hadron (= invariant mass squared)." % n)

    print("\n" + "-" * 78)
    print("2. COMPOSITE VERTICES WITH NO FORM FACTOR")
    print("-" * 78)
    if not missing:
        print("  none")
    else:
        by_role = {}
        for name, names, role in missing:
            by_role.setdefault(role, []).append((name, names))
        for role, items in sorted(by_role.items()):
            note = ROLES.get(role, ('', '', 'not classified'))[2]
            print("  %s  (%d vertices)" % (role, len(items)))
            print("      %s" % " ".join(items[0][1]) +
                  ("  ... and %d more" % (len(items) - 1) if len(items) > 1 else ""))
            print("      -> %s" % note)

    print("\n" + "-" * 78)
    print("3. VERTICES WHOSE EXACT FORM FACTOR NEEDS MORE THAN ONE VARIABLE")
    print("-" * 78)
    print("  A UFO form factor takes ONE argument and Sherpa allows one per")
    print("  Lorentz structure, so these are approximations by construction.")
    for role in sorted(twovar):
        internal, exact, have = ROLES[role]
        print("\n  %s" % role)
        print("     internal legs : %s" % internal)
        print("     exact F is a function of : %s" % exact)
        print("     what the model does : %s" % have)
    if not twovar:
        print("  none")


if __name__ == '__main__':
    main()
