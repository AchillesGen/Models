#!/usr/bin/env python3
"""
delta_couplings.py -- two checks on the model's Delta sector, both done with
EXPLICIT Rarita-Schwinger spinors rather than the projector:

  1. Gamma(Delta -> N pi) from the UFO's own strong vertex, against the paper's
     closed form, nucl-th/0509020v2 Eq. (B.7)
         Gamma = h^2 k*^3 (E_N + M) / (3 pi f_pi^2 M*)

     THE SPIN AVERAGE IS THE WHOLE STORY, AND IT BELONGS.  Eq. (B.7), and
     Delta-Analytic-Calculations/DeltaWidth.nb which reproduces it, use the
     SUMMED |M|^2 -- there is no 1/(2J+1) = 1/4 anywhere in the notebook's
     amp2.  This file's |M|^2 agrees with the notebook's to six digits
     (17.691 vs 17.6909), so the matrix element is not in question; only the
     bookkeeping from |M|^2 to Gamma is.

     calibrate_fstar() settles which is right, independently of this model and
     of the paper, using the CONVENTIONAL pi-N-Delta coupling whose strength is
     standard: L = (f*/m_pi) Psibar^mu (d_mu pi) N with f* = 2.13,
     f*^2/4pi = 0.36.  Demanding Gamma = 117 MeV gives

         with the 1/4 :  f* = 2.19,  f*^2/4pi = 0.380   <- matches
         without      :  f* = 1.09,  f*^2/4pi = 0.095   <- off by 2 in f*

     So the spin average is required, Eq. (B.7) as printed is the spin-SUMMED
     quantity, i.e. FOUR TIMES the physical width, and the model's true
     Gamma(Delta -> N pi) is 25.0 MeV against the measured 117.

     WHAT THAT IMPLIES.  The paper fixes h from the measured widths using these
     formulas, so h = 0.744 is about a factor 2 SMALLER than the coupling that
     actually reproduces Gamma_Delta.  Photoproduction is immune -- g1 and g2
     are fitted to SAID multipoles with that same h, and the fit only ever
     constrains the product -- which is why nothing downstream of Fig. 33 ever
     caught it.  The weak sector is not immune: its Delta diagram carries h
     twice (the gauged transition and the decay), so the amplitude goes as h^2.

     Two things this rules out, both of which were guessed at before the check
     was done: the Rarita-Schwinger projector, and the model's coupling.
     check_projector() confirms sum_lambda u_alpha ubar_beta = rs_numerator to
     4e-16, and the notebook's truncated spin sum (which drops the
     2 p_mu p_nu / 3M^2 term and the overall minus) gives the IDENTICAL number,
     because p^mu contracted into this vertex vanishes -- the epsilon tensor
     already carries p_Delta.

     NOTE THAT NONE OF THIS TOUCHES A CROSS SECTION.  In photoproduction and in
     weak pion production the Delta is INTERNAL, so no Delta spin average ever
     enters; the ambiguity here is confined to interpreting the width.

  2. The EFFECTIVE C5A(0) that the model supplies.

  3. Gamma(Delta -> N gamma) from g1/g2, which is the only observable here that
     depends on g ALONE.  The Fig. 33 fit constrains the PRODUCT g x h, so it
     cannot separate them -- but the radiative width can, and it is measured.

WHY C5A(0) IS THE INTERESTING NUMBER.  This model has no independent axial
N -> Delta coupling.  Its weak transition current is whatever gauging the strong
pi-N-Delta vertex produces, so its strength is tied to hD -- while the
phenomenological value that CC1pi+ data demands, C5A(0) ~ 1.2, is fitted.  There
is no reason the two should agree, and the gap between them is the cleanest
statement of what the model is missing in the weak sector.

HOW IT IS EXTRACTED.  In the standard (Llewellyn Smith / Adler) decomposition
the axial N -> Delta current is
    <Delta(p')| A^mu |N(p)> = ubar_alpha(p') [ ... + C5A g^{alpha mu} + ... ] u(p)
and the C5A term dominates at low Q^2.  Both the model's W-N-N and its
W-N-Delta vertices carry the same overall charged-current factor
    g_cc = ee Vud / (2 sw Sqrt[2]),
so dividing the W-N-Delta coupling by g_cc puts the model's transition in
exactly the normalisation C5A is defined in -- no convention factor has to be
guessed.  The Delta++ channel is used because that is the one the standard
convention carries no extra isospin factor for (the model's Delta++ : Delta+
couplings are 1 : 1/Sqrt[3], the correct Clebsch).

The comparison is made at the on-shell photon point: Delta on shell, nucleon on
shell, Q^2 = 0.  The ratio is reported component by component, so whether the
model's epsilon-tensor (gauge-invariant / Pascalutsa) structure actually reduces
to a pure g^{alpha mu} there is a RESULT, not an assumption.

Run:  python3 delta_couplings.py [--ufo ChiPT_UFO_All]
"""

import argparse
import itertools
import sys

import numpy as np

from fig33_from_ufo import (load_ufo, parameter_namespace, build,
                            vertex_by_particles, rs_numerator, uspinor, ubar,
                            slash, dot, kmom, METRIC, ID4, GAMMA)
import wprod_from_ufo as W

# spin-1 polarisation vectors in the rest frame, m = +1, 0, -1
EPS1 = {+1: np.array([0, -1, -1j, 0]) / np.sqrt(2),
         0: np.array([0, 0, 0, 1], dtype=complex),
        -1: np.array([0, 1, -1j, 0]) / np.sqrt(2)}

# <1 m; 1/2 s | 3/2 lam>, s = +1/2 -> index 0, s = -1/2 -> index 1
CG = {
    (+3, +1): [(+1, 0, 1.0)],
    (+1, +1): [(+1, 1, np.sqrt(1 / 3)), (0, 0, np.sqrt(2 / 3))],
    (-1, -1): [(0, 1, np.sqrt(2 / 3)), (-1, 0, np.sqrt(1 / 3))],
    (-3, -1): [(-1, 1, 1.0)],
}
LAMBDAS = [+3, +1, -1, -3]          # twice the helicity


def rs_spinor(P, M, twolam):
    """u_alpha(P, lambda) in the REST frame of P, as a (4,4) array [alpha, spinor]."""
    out = np.zeros((4, 4), dtype=complex)
    for m, s, c in CG[(twolam, 1 if twolam > 0 else -1)]:
        out += c * np.outer(EPS1[m], uspinor(P, M, s))
    return out


def check_projector(M):
    """sum_lambda u_alpha ubar_beta must equal rs_numerator, up to its sign."""
    P = np.array([M, 0, 0, 0], dtype=complex)
    S = np.zeros((4, 4, 4, 4), dtype=complex)
    for tl in LAMBDAS:
        u = rs_spinor(P, M, tl)
        for a in range(4):
            for b in range(4):
                S[a, b] += np.outer(u[a], ubar(u[b]))
    N = rs_numerator(P, M)
    best = None
    for sgn in (1.0, -1.0):
        d = np.abs(S - sgn * N).max() / np.abs(N).max()
        if best is None or d < best[1]:
            best = (sgn, d)
    return best, S


def strong_width(V, ns, ff, delta, nucleon, pion, mpi):
    """Gamma(Delta -> N pi) with explicit RS spinors."""
    MD, MN = ns['MDelta'], ns['MNucleon']
    k = kmom(MD ** 2, mpi, MN)
    pD = np.array([MD, 0, 0, 0], dtype=complex)
    kk = np.array([np.sqrt(k ** 2 + mpi ** 2), 0, 0, k], dtype=complex)
    pp = pD - kk
    G = build(vertex_by_particles(V, [delta + '~', nucleon, pion]),
              {delta + '~': -pD, nucleon: pp, pion: kk}, ns, ff)   # [eta, row, col]
    tot = 0.0
    for tl in LAMBDAS:                       # Delta spin states
        u = rs_spinor(pD, MD, tl)
        for s in range(2):                   # nucleon spin states
            ub = ubar(uspinor(pp, MN, s))
            amp = sum(METRIC[a, a] * (ub @ G[a] @ u[a]) for a in range(4))
            tot += abs(amp) ** 2
    # Returned WITHOUT the 1/(2J+1) spin average -- see the note in main().
    return tot * k / (8 * np.pi * MD ** 2)


def calibrate_fstar(GAM=0.117, MD=1.232, MN=0.9389, mpi=0.1396):
    """Which width convention reproduces the standard f* = 2.13?

    Conventional coupling, Gamma^mu = (f*/m_pi) k^mu, Delta++ -> p pi+ (CG = 1).
    Independent of this model and of nucl-th/0509020v2.
    """
    k = kmom(MD ** 2, mpi, MN)
    pD = np.array([MD, 0, 0, 0], dtype=complex)
    kk = np.array([np.sqrt(k ** 2 + mpi ** 2), 0, 0, k], dtype=complex)
    pp = pD - kk
    tot = 0.0
    for tl in LAMBDAS:
        u = rs_spinor(pD, MD, tl)
        for s in range(2):
            ub = ubar(uspinor(pp, MN, s))
            amp = sum(METRIC[b, b] * kk[b] * (ub @ u[b]) for b in range(4))
            tot += abs(amp) ** 2
    pref = k / (8 * np.pi * MD ** 2)
    out = {}
    for lbl, div in (("averaged", 4.0), ("summed", 1.0)):
        fstar = np.sqrt(GAM / (tot / div * pref)) * mpi
        out[lbl] = (fstar, fstar ** 2 / (4 * np.pi))
    return out


def eq_B7(h, Ms, M, mpi, fpi):
    k = kmom(Ms ** 2, mpi, M)
    EN = np.sqrt(k * k + M * M)
    return h * h * k ** 3 * (EN + M) / (3 * np.pi * fpi ** 2 * Ms)


# Couplings in the W p -> Delta++ vertex whose Lorentz structures are NOT
# proportional to g^{alpha mu}.  They have to be switched off before the
# projection below measures anything, and on a V10+ UFO they are what made it
# collapse: the components come out with MIXED SIGN and the signed least
# squares cancels.  Measured on ChiPT_UFO_V13, where sqrt(3) sqrt(2/3) hD is
# 2.2018:
#
#     live                0.1576      C4AN = 0            0.0241
#     C6AN = 0            2.0201      C6AN = C4AN = 0     2.2018  (exact)
#
#   C6AN multiplies FRV2 = q^alpha q^mu (the induced pseudoscalar, whose
#     FC6A(0) = 1/mpi^2 = 51.3); q^mu contracted with the lepton current gives
#     the lepton mass, so this term is large HERE and absent from any
#     light-lepton cross section.  Nothing is wrong with it.
#   C4AN multiplies FRV5.
#
# The CVC vector pieces FRV3/FRV4 are epsilon-tensor structures orthogonal to
# g^{alpha mu} and need no isolation -- FVND -> 0 moves the result not at all.
# A model whose vertex has only the one structure (ChiPT_UFO_All) is unaffected
# either way: there every component is identically +2.0785j.
NON_G_COUPLINGS = ('C6AN', 'C4AN')


def signed_ratios(rows):
    """Per-component ratios with their common phase divided out.

    Every ratio here is a real number times the i of the Feynman rule, so the
    informative content is a SIGN.  Reporting |ratio| -- as this diagnostic used
    to -- hides precisely the cancellation that makes the projection meaningless
    when the vertex is not pure g^{alpha mu}.
    """
    if not rows:
        return []
    ref = max(rows, key=lambda r: abs(r[5]))[5]
    ref = ref / abs(ref)
    return [(r[5] / ref).real for r in rows]


def effective_C5A(V, ns, ff, isolate=True):
    """The coefficient of g^{alpha mu} the model's W p -> Delta++ vertex supplies.

    Kinematics: Delta on shell in its rest frame, nucleon on shell, Q^2 = 0, so
    q = p_Delta - p_N is lightlike -- the photon point, where C5A(0) is defined.

    With isolate=True the couplings in NON_G_COUPLINGS are set to zero first, so
    what is projected is the C5A structure alone; this is what makes the number
    a C5A at all on V10+.  Pass isolate=False for the raw projection over every
    structure in the vertex.  Returns (c5, rows, switched_off).
    """
    MD, MN = rp(ns['MDelta']), rp(ns['MNucleon'])
    Eq = (MD ** 2 - MN ** 2) / (2 * MD)          # |q| = Eq since Q^2 = 0
    pD = np.array([MD, 0, 0, 0], dtype=complex)
    q = np.array([Eq, 0, 0, Eq], dtype=complex)
    pN = pD - q
    assert abs(dot(q, q).real) < 1e-9 and abs(dot(pN, pN).real - MN ** 2) < 1e-9

    off = [k for k in NON_G_COUPLINGS if k in ns] if isolate else []
    ns_use = dict(ns, **{k: 0.0 for k in off}) if off else ns

    G = build(vertex_by_particles(V, ['p~', 'Delta++', 'W-']),
              {'p~': -pN, 'Delta++': pD, 'W-': -q}, ns_use, ff)  # [nu, mu, r, c]
    # strip the common charged-current factor so the result is in the
    # normalisation C5A is defined in
    ee, sw, Vud = ns['ee'], ns['sw'], ns['Vud']
    g_cc = ee * Vud / (2 * sw * np.sqrt(2))

    num = 0.0 + 0.0j
    den = 0.0
    rows = []
    for tl in LAMBDAS:
        u3 = rs_spinor(pD, MD, tl)
        for s in range(2):
            un = uspinor(pN, MN, s)
            for mu in range(4):
                # model:  ubar_alpha G^{alpha mu} u
                a_model = sum(METRIC[a, a] * (ubar(u3[a]) @ G[a, mu] @ un)
                              for a in range(4)) / g_cc
                # reference: ubar_alpha g^{alpha mu} u  = ubar^mu u
                a_ref = METRIC[mu, mu] * (ubar(u3[mu]) @ un)
                if abs(a_ref) > 1e-9:
                    rows.append((tl, s, mu, a_model, a_ref, a_model / a_ref))
                num += a_ref.conjugate() * a_model
                den += abs(a_ref) ** 2
    return num / den, rows, off


# ---------------------------------------------------------------------------
def radiative_width(V, ns, ff):
    """Gamma(Delta+ -> p gamma) from the model's own gamma-N-Delta vertex.

    This is the independent test of whether g1/g2 are anomalously large.  The
    Fig. 33 photoproduction fit only ever constrains the PRODUCT g x h, so it
    cannot separate them; the RADIATIVE width depends on g alone and is
    measured -- PDG, Review of Particle Physics, Delta(1232) 3/2+ listings,
    2024 edition, B(N gamma) = 0.55-0.65% of the 117 MeV Breit-Wigner width,
    i.e. Gamma(Delta -> N gamma) = 0.66 MeV.

    That Breit-Wigner number is the target only for a V9-style UFO.  From V10
    the width is an INPUT and the couplings are inverted from it, so the target
    is the card's own GamNGam and the ratio is 1 by construction; width_targets()
    picks the right one and main() reports which it used.

    Same machinery as strong_width(), including the 1/(2J+1) spin average that
    calibrate_fstar() verified, plus a sum over the two photon polarisations.
    """
    MD, MN = ns['MDelta'], ns['MNucleon']
    k = (MD ** 2 - MN ** 2) / (2 * MD)          # real photon, Delta rest frame
    pD = np.array([MD, 0, 0, 0], dtype=complex)
    kk = np.array([k, 0, 0, k], dtype=complex)
    pp = pD - kk
    G = build(vertex_by_particles(V, ['Delta+~', 'p', 'A']),
              {'Delta+~': -pD, 'p': pp, 'A': kk}, ns, ff)     # [nu_RS, mu_A, r, c]
    pol = [(-1 / np.sqrt(2)) * np.array([0, 1, 1j, 0], dtype=complex),
           (+1 / np.sqrt(2)) * np.array([0, 1, -1j, 0], dtype=complex)]
    amps, tot = {}, 0.0
    for tl in LAMBDAS:
        u3 = rs_spinor(pD, MD, tl)
        for s in range(2):
            ub = ubar(uspinor(pp, MN, s))
            for ip, e in enumerate(pol):
                a = sum(METRIC[n, n] * METRIC[m, m] * np.conj(e[m])
                        * (ub @ G[n, m] @ u3[n])
                        for n in range(4) for m in range(4))
                tot += abs(a) ** 2
                amps[(tl, s, ip)] = a
    return tot / 4.0 * k / (8 * np.pi * MD ** 2), amps, k


# The Breit-Wigner partial widths this diagnostic used to hard-code as its
# targets.  SOURCE: PDG, Review of Particle Physics, Delta(1232) 3/2+ listings,
# 2024 edition -- Gamma = 117 MeV with B(N gamma) = 0.55-0.65%, so
# Gamma(N gamma) = 0.66 MeV.  The PDG tabulates the branching ratio, not the
# radiative partial width.
#
# They are the right targets ONLY for a V9-style UFO, where hD, G1 and G2 are
# external and the widths are whatever they come out to be.  From V10 the
# widths are the INPUTS and the couplings are inverted from them, so the target
# is whatever the card says and the honest ratio is 1 -- see width_targets().
GAM_PI_BW, GAM_GAM_BW = 0.117, 0.00066


def rp(x):
    return float(x.real) if isinstance(x, complex) else float(x)


def width_targets(ns):
    """The widths this model should be compared against, and where they come from.

    V10 and later carry GamNPi/GamNGam as external inputs, so the vertex
    reproduces them by construction.  A V9-style UFO has neither, and the
    Breit-Wigner numbers are then the only available target.
    """
    if 'GamNPi' in ns and 'GamNGam' in ns:
        return rp(ns['GamNPi']), rp(ns['GamNGam']), 'card (V10+ inputs)'
    return GAM_PI_BW, GAM_GAM_BW, 'Breit-Wigner (PDG 2024, V9-style UFO)'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ufo', default='ChiPT_UFO_All')
    a = ap.parse_args()

    P, V = load_ufo(a.ufo)
    ns = parameter_namespace(P)
    ff = W.form_factors(ns, True)
    # From V10 hD, G1 and G2 are INTERNAL, so the UFO builds them with cmath and
    # they arrive here as complex with a zero imaginary part.  Without rp() the
    # very first print raises TypeError and the diagnostic cannot run at all on
    # the current model.
    MD, MN, fpi = rp(ns['MDelta']), rp(ns['MNucleon']), rp(ns['fPi'])
    hD = rp(ns['hD'])
    gam_pi_ref, gam_gam_ref, ref_src = width_targets(ns)

    print("UFO %s   hD = %.4f  MDelta = %.4f  MNucleon = %.6f  fPi = %.4f"
          % (a.ufo, hD, MD, MN, fpi))
    print("   width targets: Gamma(N pi) = %.3f MeV, Gamma(N gamma) = %.4f MeV"
          % (1e3 * gam_pi_ref, 1e3 * gam_gam_ref))
    print("   taken from %s" % ref_src)

    (sgn, dev), _ = check_projector(MD)
    print("\n1. Rarita-Schwinger machinery")
    print("   sum_lam u_a ubar_b  vs  rs_numerator :  sign %+d, max rel dev %.2e %s"
          % (sgn, dev, "(ok)" if dev < 1e-10 else "(MISMATCH)"))

    cal = calibrate_fstar()
    print("\n2. Which width convention?  conventional coupling at Gamma = 117 MeV")
    for lbl in ("averaged", "summed"):
        f, f2 = cal[lbl]
        print("   spin-%-9s f* = %.3f   f*^2/4pi = %.3f%s"
              % (lbl, f, f2, "   <- literature 2.13 / 0.36" if lbl == "averaged" else ""))

    print("\n3. Gamma(Delta -> N pi) from the UFO vertex")
    print("   (spin-SUMMED, the convention of Eq. B.7 and DeltaWidth.nb)")
    g0 = strong_width(V, ns, ff, 'Delta+', 'p', 'Pi0', ns['MPi0'])
    gp = strong_width(V, ns, ff, 'Delta+', 'n', 'Pi+', ns['MPiP'])
    tot = g0 + gp
    b7 = eq_B7(hD, MD, MN, ns['MPi0'], fpi)
    print("   Delta+ -> p pi0        %8.2f MeV" % (1e3 * g0))
    print("   Delta+ -> n pi+        %8.2f MeV   (isospin ratio %.3f, want 2)"
          % (1e3 * gp, g0 / gp))
    print("   total                  %8.2f MeV" % (1e3 * tot))
    print("   paper Eq. (B.7)        %8.2f MeV   ->  ratio %.4f"
          % (1e3 * b7, tot / b7))
    print("   param card WDeltaP     %8.2f MeV" % (1e3 * ns['WDeltaP']))
    print("   with the 1/(2J+1)=1/4 spin average instead: %.2f MeV (ratio %.4f)"
          % (1e3 * tot / 4, tot / 4 / b7))

    print("\n4. Effective C5A(0) of the gauged W-N-Delta transition")
    c5, rows, off = effective_C5A(V, ns, ff)
    if off:
        print("   isolated first: %s set to zero, their structures are not"
              % ", ".join(off))
        print("   proportional to g^{alpha mu} (see NON_G_COUPLINGS)")
    print("   projection onto g^{alpha mu} :  C5A(0)_eff = %.4f  (phase %+.1f deg)"
          % (abs(c5), np.angle(c5, deg=True)))
    print("   the phase is the i of the Feynman rule; only the modulus is C5A")
    signed = signed_ratios(rows)
    print("   component-by-component ratio  : min %+.4f  max %+.4f  (%d components)"
          % (min(signed), max(signed), len(signed)))
    if min(signed) < 0 < max(signed):
        print("   *** MIXED SIGN: the vertex still carries structures beyond")
        print("       g^{alpha mu}, so this projection is NOT a C5A. ***")
    else:
        pure = (max(signed) - min(signed)) < 0.05 * max(abs(x) for x in signed)
        print("   -> the epsilon structure is %s pure g^{alpha mu} at this point"
              % ("essentially" if pure else "NOT"))
    if off:
        # what the old, un-isolated projection reported -- kept visible so the
        # collapse stays legible rather than looking like a physics failure
        craw, rraw, _ = effective_C5A(V, ns, ff, isolate=False)
        sraw = signed_ratios(rraw)
        print("   without that isolation it reads %.4f, components %+.4f .. %+.4f"
              % (abs(craw), min(sraw), max(sraw)))
        print("   -- a cancellation between structures, not a small C5A")
    print("\n   phenomenological C5A(0) ~ 1.2 (CA5Norm in the param card)")
    print("   deficit in amplitude  %.2f     in Delta-pole rate  %.2f"
          % (1.2 / abs(c5), (1.2 / abs(c5)) ** 2))
    grad, amps, kg = radiative_width(V, ns, ff)
    a32 = max(abs(v) for kk, v in amps.items() if kk[0] == +3)
    a12 = max(abs(v) for kk, v in amps.items() if kk[0] == +1)
    print("\n5. Gamma(Delta+ -> p gamma) -- the test of g1/g2 ALONE")
    print("   model                  %8.4f MeV" % (1e3 * grad))
    print("   target                 %8.4f MeV   (%s)"
          % (1e3 * gam_gam_ref, ref_src))
    print("   ratio %.2f  ->  g too LARGE by %.2f in amplitude"
          % (grad / gam_gam_ref, np.sqrt(grad / gam_gam_ref)))
    print("   |A_3/2|/|A_1/2| = %.4f  (pure M1 -> sqrt(3) = %.4f), so the"
          % (a32 / a12, np.sqrt(3)))
    print("   extraction is M1-dominated as it should be")
    hshort = np.sqrt(gam_pi_ref / (tot / 4))
    glarge = np.sqrt(grad / gam_gam_ref)
    print("\n   THE TWO ERRORS COMPENSATE.  h short by %.2f, g large by %.2f,"
          % (hshort, glarge))
    print("   product g*h off by only %.2f -- which is exactly what a fit to"
          % (glarge / hshort))
    print("   photoproduction (which constrains g*h alone) would produce, and")
    print("   why Fig. 33 never caught either one.  The weak sector carries h")
    print("   TWICE and g not at all, so nothing compensates there.")

    # ---- the isospin convention, settled from the model's own numbers ----
    # The gauging puts the pion and the external axial source in the SAME
    # vielbein, so the model satisfies the off-diagonal Goldberger-Treiman
    # relation by construction: C5A(0) = f_pi f* / m_pi.  That makes GT a test
    # of the ISOSPIN BOOKKEEPING rather than of the physics -- run it both ways
    # and only the right convention comes out consistent.
    gam_phys = tot / 4                              # this model's true width
    # f* scales as sqrt(Gamma).  The literature value 2.13 is quoted at the
    # BREIT-WIGNER width, so the anchor of this scaling stays GAM_PI_BW even
    # when the model itself is parametrised at the pole.
    fstar_model = 2.13 * np.sqrt(gam_phys / GAM_PI_BW)
    c5_gt = 0.0924 * fstar_model / 0.1396           # f_pi f* / m_pi
    print("\n6. The isospin convention for C5A, settled internally")
    print("   physical width of this vertex      %8.2f MeV" % (1e3 * gam_phys))
    print("   -> its equivalent f*               %8.3f    (f* = 2.13 at 117 MeV)"
          % fstar_model)
    print("   -> GT predicts C5A(0) = f_pi f*/m_pi = %.4f" % c5_gt)
    for lbl, fac in (("as extracted (Delta++)", 1.0), ("divided by sqrt(3)", np.sqrt(3))):
        v = abs(c5) / fac
        print("      %-24s C5A(0) = %.4f   GT ratio %.3f%s"
              % (lbl, v, v / c5_gt, "   <- consistent" if abs(v / c5_gt - 1) < 0.1 else ""))
    print("   So the Delta++ channel carries sqrt(3) relative to the C5A that")
    print("   phenomenology quotes: the reduced value for THIS model is %.3f."
          % (abs(c5) / np.sqrt(3)))
    print("\n7. Everything in one place, all in AMPLITUDE")
    print("   h   short by %.2f   (strong width, %.2f vs %.2f MeV)"
          % (np.sqrt(gam_pi_ref / gam_phys), 1e3 * gam_phys, 1e3 * gam_pi_ref))
    print("   g   large by %.2f   (radiative width, %.2f vs %.2f MeV)"
          % (np.sqrt(grad / gam_gam_ref), 1e3 * grad, 1e3 * gam_gam_ref))
    print("   C5A short by %.2f   (reduced %.3f vs phenomenological 1.2)"
          % (1.2 / (abs(c5) / np.sqrt(3)), abs(c5) / np.sqrt(3)))
    print("   g*h off by   %.2f   -> photoproduction is blind to both"
          % (np.sqrt(grad / gam_gam_ref) / np.sqrt(gam_pi_ref / gam_phys)))


if __name__ == '__main__':
    main()

