#!/usr/bin/env python3
"""
formfactors.py -- the nucleon and N->Delta form factors, driven entirely by UFO
MODEL PARAMETERS, so that the Sherpa plugin (FormFactors.C) and the analytic
calculation (wprod_from_ufo.py) evaluate identical functions and both are
steered from the param card rather than from anything compiled in.

PARAMETERISATION, transliterated from Achilles/main:
    include/Achilles/FormFactor.hh   the classes
    src/Achilles/FormFactor.cc       Evaluate() and Fill()
    data/default/FormFactors.yml     the coefficients, which become the DEFAULTS
                                     of the UFO external parameters below
Achilles selects `vector: Kelly` and `axial: AxialZExpansion`; ArringtonHill
(the z-expansion for the VECTOR form factors) is ported too so the two can be
swapped by changing one parameter.

WHY THE PARAMETERS LIVE IN THE UFO.  Everything here reads out of block CHIPTFF
of the param card, alongside LambdaFF which is already there.  Sherpa's UFO
interface writes every external parameter into its ScalarConstants map under its
own name (MODEL/UFO/src/ufo_interface/model_writer.py, _write_external_param),
so the plugin gets them with MODEL::s_model->ScalarConstant("KEp1") and a fit
can be varied by editing param_ChiPT_UFO*.dat -- no recompilation, and no risk
of the C++ and the Python drifting apart because both read the same card.

THE MISSING-BLOCK TRAP.  Sherpa reads external parameters with
GetEntry<double>(block, index, 0.0), which silently returns ZERO when the entry
is absent.  A param card written before this block existed would therefore give
every form factor 0 and every cross section 0, with no error.  The constructor
below refuses a namespace with no CHIPTFF form-factor entries unless
allow_defaults is passed explicitly, and FormFactors.C must do the same.

ALMOST EVERYTHING THE WEAK VERTICES USE IS A RATIO normalised to 1 at Q^2 = 0
(the exceptions are the two new Pauli operators and FZ1p, both below).  That is
what lets this drop into the ChiPT model without disturbing anything already
validated:

  * the model's own g_A sets the strong pi-N coupling through the SAME chiral
    Lagrangian term as the axial current, so g_A must not be replaced.  The
    axial z-expansion has F_A(0) = -1.276384 -- 0.42% larger in magnitude than
    ga = 1.271 and opposite in sign convention.  F_A(Q^2)/F_A(0) cancels both,
    and the model keeps its normalisation while acquiring the fitted Q^2 shape.
    (The YAML's `gan1: 1.2694` belongs to AxialDipole, not to the z-expansion:
    the z-expansion's value at zero is a prediction of the fit, not an input.)
  * likewise C5A, where the ratio drops both CA5Norm and the sqrt(3/2) isospin
    factor MECAxialFormFactor folds in, leaving the model's own gauged N->Delta
    coupling untouched.

The two genuinely NEW operators -- weak magnetism on the W and on the Z, of
which the model has no point-like piece at all -- are the exception: they carry
absolute normalisation, and CVC fixes it from the electromagnetic F2's.

SIN^2(THETA_W) IS TAKEN AT Q -> 0, NOT FROM THE MODEL.  The UFO's sw comes from
the tree-level on-shell relation sw^2 = 1 - MW^2/MZ^2 with MW built out of Gf,
aEW and MZ, which gives 0.21215 -- an M_Z-scale quantity.  (Worth noting it is
not the MS-bar running value there either, which is 0.23122; the tree-level
on-shell number is lower than both.)  The neutral-current form factors are
evaluated at Q^2 of order a GeV^2 or less, where the right value is the low-Q
limit, parameter Sw2FF, default 0.23863.

This is not a cosmetic change.  The proton's neutral-current vector charge
1/2 - 2 sw^2 sits near a zero, so it drops from 0.0757 to 0.0227 -- a factor
0.30 -- and FZ1p(0) is that factor rather than 1.  The neutron is untouched:
its combination is (F1n - F1p)/2 - 2 sw^2 F1n and F1n(0) = 0, so it is -1/2 for
any mixing angle.  The axial neutral current is pure isovector and carries no
sw^2 at all, so FZA is unaffected.  The OVERALL normalisation g/(2 c_w) is left
to the model: it is fixed by G_F, and only the charge combinations carry the
sin^2(theta_W) sensitivity -- which is the standard treatment.

DEFAULTS PRESERVE PHOTOPRODUCTION EXACTLY.  MuP and MuN default to 2.792847 and
-1.913043, i.e. the kappa_p and kappa_n currently hard-coded in FormFactors.C,
NOT to Achilles' 2.79278 / -1.91315.  The two differ in the fifth decimal; using
the plugin's values means every Q^2 = 0 number, and so every Fig. 33 result, is
bit-identical to what is already published.  Set them to the Achilles values in
the param card if you would rather match Achilles.
"""

import math

# ---------------------------------------------------------------------------
# The UFO external parameters this module needs, with the values that go into
# ChiPT.fr as the FeynRules defaults.  Block CHIPTFF; LambdaFF is OrderBlock 1.
# Anything here can be overridden per run by editing the param card.
# ---------------------------------------------------------------------------
PARAMS = [
    # name        default        OrderBlock  description
    ("MuP",       2.792847,  2,  "proton magnetic moment (plugin kappa_p + 1)"),
    ("MuN",      -1.913043,  3,  "neutron magnetic moment (plugin kappa_n)"),
    ("KLamSq",    0.7174,    4,  "Kelly lambda^2 in Gen, GeV^2"),
    ("KEp1",     -0.24,      5,  "Kelly Gep numerator a1"),
    ("KEp2",     10.98,      6,  "Kelly Gep denominator b1"),
    ("KEp3",     12.82,      7,  "Kelly Gep denominator b2"),
    ("KEp4",     21.97,      8,  "Kelly Gep denominator b3"),
    ("KEn1",      1.70,      9,  "Kelly Gen A"),
    ("KEn2",      3.30,     10,  "Kelly Gen B"),
    ("KMp1",      0.12,     11,  "Kelly Gmp numerator a1"),
    ("KMp2",     10.97,     12,  "Kelly Gmp denominator b1"),
    ("KMp3",     18.86,     13,  "Kelly Gmp denominator b2"),
    ("KMp4",      6.55,     14,  "Kelly Gmp denominator b3"),
    ("KMn1",      2.33,     15,  "Kelly Gmn numerator a1"),
    ("KMn2",     14.72,     16,  "Kelly Gmn denominator b1"),
    ("KMn3",     24.20,     17,  "Kelly Gmn denominator b2"),
    ("KMn4",     84.1,      18,  "Kelly Gmn denominator b3"),
    ("AxTcut",    0.1753180641, 19, "axial z-expansion t_cut = 9 m_pi^2, GeV^2"),
    ("AxT0",     -0.28,     20,  "axial z-expansion t_0, GeV^2"),
    ("AxA0",     -0.759,    21,  "axial z-expansion a_0"),
    ("AxA1",      2.30,     22,  "axial z-expansion a_1"),
    ("AxA2",     -0.6,      23,  "axial z-expansion a_2"),
    ("AxA3",     -3.8,      24,  "axial z-expansion a_3"),
    ("AxA4",      2.3,      25,  "axial z-expansion a_4"),
    ("AxA5",      2.16,     26,  "axial z-expansion a_5"),
    ("AxA6",     -0.896,    27,  "axial z-expansion a_6"),
    ("AxA7",     -1.58,     28,  "axial z-expansion a_7"),
    ("AxA8",      0.823,    29,  "axial z-expansion a_8"),
    ("MADeltaSq", 1.1025,   30,  "N->Delta axial mass squared, GeV^2"),
    ("CA5Norm",   0.0,      31,  "C5A(0) in physical units; 0 means 'the model's own', sqrt(2/3) hD"),
    ("Sw2FF",     0.23863,  32,  "sin^2(theta_W) in the Q->0 limit, for the neutral-current charge combinations"),
    ("C4AHat",    0.28397656, 33, "C4AN/hD, the portable form of the Adler C4A calibration; C4AN itself is Internal and equals C4AHat*hD"),
    ("MRhoCT",    0.7758,   34,  "rho mass in the PCAC form factor on the axial contact term, GeV"),
    ("MV2ND",     0.71,     35,  "vector mass squared in the CVC N->Delta dipole, GeV^2"),
    ("PPNorm",    1.0,      37,  "pion-pole (PP) operator: 1 is the chiral value, 0 removes the diagram"),
    # Slot 36 held C6AN, which is now an Internal parameter equal to hD -- see
    # the note in ChiPT.fr.  Neither it nor C4AN belongs in the card any more:
    # both are tied to hD, and hD is derived from Gamma(Delta -> N pi), so a
    # card entry could only ever disagree with the model it came from.
]

DEFAULTS = {name: value for name, value, _, _ in PARAMS}

# Arrington-Hill is a 13-coefficient z-expansion per Sachs form factor: 52 more
# numbers is a lot of param-card clutter for an alternative that agrees with
# Kelly to ~1%, so it stays a compiled-in table, selected by VECTOR_MODEL.
ARRINGTON_HILL = dict(
    tcut=0.0779191396, t0=-0.7,
    Gep=[0.23916329807, -1.10985857441, 1.44438081306, 0.47956946560,
         -2.28689474187, 1.12663298498, 1.25061984354, -3.63102047159,
         4.08221702379, 0.50409734650, -5.08512046051, 3.96774254395,
         -0.98152907110],
    Gmp=[0.26414299414, -1.09530612212, 1.21855378178, 0.6611364935,
         -1.40567892503, -1.35641843888, 1.44702915534, 4.2356697359,
         -5.33404565341, -2.91630052096, 8.70740306757, -5.7069999438,
         1.28081437589],
    Gen=[0.04891998138, -0.06452505391, -0.24082589738, 0.3921087449,
         0.30044525860, -0.66188868718, -0.17563976969, 0.6246917245,
         -0.07768429937, -0.23600397526, 0.09040197347, 0.0, 0.0],
    Gmn=[0.25775832696, -1.07954064206, 1.18218381220, 0.7110150858,
         -1.34808093680, -1.66244402521, 2.62435442603, 1.7512344946,
         -4.92230087889, 3.19789272731, -0.71207238995, 0.0, 0.0],
)


def _zexpand(A, z):
    """Horner, exactly as Achilles' ZExpand."""
    r = 0.0
    for i in range(len(A) - 1, 0, -1):
        r += A[i]
        r *= z
    return r + A[0]


def _z(Q2, tcut, t0):
    a, b = math.sqrt(tcut + Q2), math.sqrt(tcut - t0)
    return (a - b) / (a + b)


class FormFactors:
    """Every coefficient comes from `ns`, a UFO parameter namespace.

    `ns` is what fig33_from_ufo.parameter_namespace() returns, so it also
    carries MNucleon and sw -- the neutral-current combinations need sin^2(th_W)
    and take it from the model rather than assuming a value.
    """

    def __init__(self, ns, vector_model="Kelly", allow_defaults=False):
        self.ns = ns
        self.vector_model = vector_model
        missing = [n for n, _, _, _ in PARAMS if n not in ns]
        if missing and not allow_defaults:
            raise KeyError(
                "UFO has no CHIPTFF form-factor parameters (%d missing, e.g. %s).\n"
                "Regenerate with CHIPT_FF=Weak (or All), or pass "
                "allow_defaults=True to fall back to the FeynRules defaults."
                % (len(missing), ", ".join(missing[:4])))
        # Internal UFO parameters come through complex even when they are real
        # (anything built with Sqrt does), so take the real part rather than
        # letting float() raise on a number that is real to machine precision.
        def _re(x):
            return float(x.real) if isinstance(x, complex) else float(x)
        self.p = {n: _re(ns.get(n, DEFAULTS[n])) for n, _, _, _ in PARAMS}
        self.used_defaults = bool(missing)
        MN = ns.get("MNucleon", 0.938272)
        self.MP2 = float(MN) ** 2
        # TWO DIFFERENT sin^2(theta_W), on purpose -- see the header.
        # sw2_model is what the model's own point-like Z couplings were built
        # from; sw2 is the low-Q value the physical charge combinations want.
        sw = ns.get("sw")
        self.sw2_model = float((sw ** 2).real if hasattr(sw ** 2, "real")
                               else sw ** 2) if sw is not None else 0.21215
        self.sw2 = self.p["Sw2FF"]
        self.FA0 = self.FA_raw(0.0)

    # ----------------------------------------------------------- vector part
    def _kelly(self, a1, b1, b2, b3, x):
        return (1 + a1 * x) / (1 + b1 * x + b2 * x * x + b3 * x ** 3)

    def sachs(self, Q2):
        """(Gep, Gen, Gmp, Gmn)."""
        p, tau = self.p, Q2 / 4 / self.MP2
        if self.vector_model == "Kelly":
            Gep = self._kelly(p["KEp1"], p["KEp2"], p["KEp3"], p["KEp4"], tau)
            Gen = (1.0 / (1 + Q2 / p["KLamSq"]) ** 2
                   * p["KEn1"] * tau / (1 + p["KEn2"] * tau))
            Gmp = p["MuP"] * self._kelly(p["KMp1"], p["KMp2"], p["KMp3"],
                                         p["KMp4"], tau)
            Gmn = p["MuN"] * self._kelly(p["KMn1"], p["KMn2"], p["KMn3"],
                                         p["KMn4"], tau)
            return Gep, Gen, Gmp, Gmn
        if self.vector_model == "ArringtonHill":
            # DISCREPANCY WITH ACHILLES, not a porting choice.  The tabulated
            # Arrington-Hill coefficients expand G_M/mu, not G_M: with these
            # numbers ZExpand gives Gmp(0) = Gmn(0) = 1.000000 exactly.
            # ArringtonHill::Evaluate assigns result.Gmp = ZExpand(...) with no
            # factor of mu -- it parses "Mu Proton"/"Mu Neutron" into muP/muN
            # and never uses them, unlike Kelly::Evaluate which does multiply.
            # As written that means mu_p = 1 and mu_n = +1, wrong in sign as
            # well as size, and F2p - F2n comes out NEGATIVE.  Restored here.
            # Kelly, the configured default, is unaffected.
            H = ARRINGTON_HILL
            z = _z(Q2, H["tcut"], H["t0"])
            return (_zexpand(H["Gep"], z), _zexpand(H["Gen"], z),
                    p["MuP"] * _zexpand(H["Gmp"], z),
                    p["MuN"] * _zexpand(H["Gmn"], z))
        raise ValueError("unknown vector model %r" % self.vector_model)

    def dirac_pauli(self, Q2):
        """(F1p, F1n, F2p, F2n) -- Achilles' Fill()."""
        Gep, Gen, Gmp, Gmn = self.sachs(Q2)
        tau = Q2 / 4 / self.MP2
        return ((Gep + tau * Gmp) / (1 + tau),
                (Gen + tau * Gmn) / (1 + tau),
                (Gmp - Gep) / (1 + tau),
                (Gmn - Gen) / (1 + tau))

    # ------------------------------------------------------------ axial part
    def FA_raw(self, Q2):
        """The z-expansion itself.  NEGATIVE, by Achilles' sign convention."""
        p = self.p
        A = [p["AxA%d" % i] for i in range(9)]
        return _zexpand(A, _z(Q2, p["AxTcut"], p["AxT0"]))

    def FA_ratio(self, Q2):
        return self.FA_raw(Q2) / self.FA0

    def C5A_model(self):
        """The model's own C5A(0), from the card, not compiled in.

        From V10 the pi-N-Delta coupling is DERIVED from Gamma(Delta -> N pi),
            hD = sqrt( 12 pi fPi^2 MD Gam / ( k^3 (E_N + MN) ) ),
        and the Adler decomposition gives C5A(0) = sqrt(2/3) hD exactly --
        measured to eight digits and independent of MDelta by
        tools/adler_ndelta.py.  Computing it here rather than storing 1.2411
        keeps this in step with FormFactors.C, which does the same arithmetic,
        and stops a change of width from silently rescaling C5A.
        """
        import math

        def g(name, dflt):
            v = self.ns.get(name, dflt)
            return float(v.real if isinstance(v, complex) else v)

        hd = g("hD", 0.0)
        if hd > 0.0:                      # External through V9, Internal in V10
            return math.sqrt(2.0 / 3.0) * hd
        mn, md = g("MNucleon", 0.938272), g("MDelta", 1.209)
        mpi = g("MPiP", 0.1395704)
        fpi, gam = g("fPi", 0.093), g("GamNPi", 0.117)
        a = md * md - mn * mn - mpi * mpi
        k = math.sqrt(a * a - 4.0 * mpi * mpi * mn * mn) / (2.0 * md)
        en = math.sqrt(k * k + mn * mn)
        hD = math.sqrt(12.0 * math.pi * fpi * fpi * md * gam
                       / (k ** 3 * (en + mn)))
        return math.sqrt(2.0 / 3.0) * hD

    def C5A_ratio(self, Q2):
        """C5A(Q^2)/C5A_model(0) -- so the vertex keeps its own normalisation
        unless CA5Norm asks for a different C5A(0).

        THE SCALE IS NOT 1.  Through V9 this returned the bare dipole and
        CA5Norm was dead here while FormFactors.C applied it, so the analytic
        engine and Sherpa quietly disagreed for any card that used the knob.
        """
        M2 = self.p["MADeltaSq"]
        norm = self.p["CA5Norm"]
        scale = norm / self.C5A_model() if norm > 0.0 else 1.0
        return scale / (1 + Q2 / M2) ** 2 / (1 + Q2 / 3 / M2)

    def FC6A(self, Q2):
        """The Delta's induced pseudoscalar, C6A, as it enters the vertex.

        PCAC ties it to C5A by  C6A = C5A MN^2/(Q^2 + mpi^2), and the operator
        in ChiPT.fr carries the two derivatives that supply the 1/MN^2, so what
        belongs here is C5A/(Q^2 + mpi^2) -- dimension 1/mass^2.

        The charged pion mass: the dominant use is the charged current.  The
        same symbol rides the Z (ChiVielbeinVWeak generates both), where the pi0
        would be marginally more correct; the difference is 3% of an already
        m_mu^2-suppressed term.
        """
        mpi = float(self.ns.get("MPiP", 0.1395704))
        return self.C5A_ratio(Q2) / (Q2 + mpi ** 2)

    def VND_ratio(self, Q2):
        """The CVC vector N->Delta dipole, 1 at Q^2 = 0.

        The standard C_i^V shape: a dipole in the nucleon vector mass with the
        extra 1/(1 + Q^2/4 M_V^2) pole.  This is the damping the model's vector
        N->Delta transition was missing entirely -- LWeakNDeltaV covariantises
        the photon vertex, whose own FgNDelta* form factors are identically 1,
        so nothing was suppressing the vector piece at large Q^2 and the Delta
        term ran away above ~1 GeV.  It is a ratio, so it multiplies G1 and G2
        without touching the Fig. 33 photoproduction fit at the photon point.
        """
        M2 = self.p["MV2ND"]
        return 1.0 / (1 + Q2 / M2) ** 2 / (1 + Q2 / (4 * M2))

    # ------------------------------------------- what the weak vertices need
    # The electromagnetic four, unchanged in role but now Q^2 dependent.
    def F1p(self, Q2): return self.dirac_pauli(Q2)[0]
    def F1n(self, Q2): return self.dirac_pauli(Q2)[1]
    def F2p(self, Q2): return self.dirac_pauli(Q2)[2]
    def F2n(self, Q2): return self.dirac_pauli(Q2)[3]

    # CVC: the charged-current vector form factors ARE the isovector
    # combinations of the electromagnetic ones.  F1V(0) = 1 already, so FW1 is
    # its own ratio; FW2 is absolute because the W has no point-like Pauli term.
    def FW1(self, Q2):
        F1p, F1n, _, _ = self.dirac_pauli(Q2)
        return F1p - F1n

    def FW2(self, Q2):
        _, _, F2p, F2n = self.dirac_pauli(Q2)
        return F2p - F2n

    def FWA(self, Q2):
        return self.FA_ratio(Q2)

    def FPP(self, Q2):
        """Induced pseudoscalar, as a RATIO to the axial vertex it sits beside.

        The nucleon axial current is

            ubar [ F_A gamma^mu gamma5  +  F_P q^mu gamma5 ] u

        and PCAC / the off-diagonal Goldberger-Treiman relation fixes

            F_P(Q^2) = 2 MN F_A(Q^2) / (Q^2 + mpi^2)

        with no free parameter.  ChiPT.fr writes the operator with the same
        prefactor and the same -ga as the axial term, so what belongs here is
        F_P/F_A times F_A's own ratio, i.e. exactly the expression above with
        FA_ratio in place of F_A.  Dimension is 1/mass, as it must be to pair
        with q^mu against a dimensionless gamma^mu coefficient.

        The CHARGED pion mass is the right one: this is the charged current.
        Contrast XPi/FpiNDelta, which follow Fig. 33 in using the neutral mass.
        """
        mpi = float(self.ns.get("MPiP", 0.1395704))
        return self.FA_ratio(Q2) / (Q2 + mpi ** 2)   # the 2 MN is in the coupling

    def FPPZ(self, Q2):
        """The neutral-current induced pseudoscalar.

        The NC axial current of the nucleon is pure isovector (no strangeness
        here), so it carries the SAME pion pole as the charged current and the
        same PCAC ratio -- only the mass differs, the pole being the pi0.
        """
        mpi = float(self.ns.get("MPi0", 0.1349768))
        return self.FA_ratio(Q2) / (Q2 + mpi ** 2)   # the 2 MN is in the coupling

    # Neutral current with no strangeness: J^Z = J^3 - 2 sw^2 J^EM, i.e.
    #   F_i^{Z,p} = (F_i^p - F_i^n)/2 - 2 sw^2 F_i^p
    #   F_i^{Z,n} = (F_i^n - F_i^p)/2 - 2 sw^2 F_i^n
    def _FZ(self, Q2, pauli):
        F1p, F1n, F2p, F2n = self.dirac_pauli(Q2)
        a, b = (F2p, F2n) if pauli else (F1p, F1n)
        s = self.sw2                       # low-Q value, NOT the model's
        return (0.5 * (a - b) - 2 * s * a, 0.5 * (b - a) - 2 * s * b)

    def FZ1p(self, Q2):
        """NOT 1 at Q^2 = 0, and that is the point.

        The denominator is the model's OWN point-like coupling, built from
        sw2_model; the numerator is the physical charge combination at the
        low-Q sin^2(theta_W).  Multiplying the vertex by this therefore does
        two jobs at once: it supplies the Q^2 dependence AND it corrects the
        proton's neutral-current vector charge from the model's on-shell value
        to the low-Q one.  That correction is a factor 0.30 -- (1/2 - 2 sw^2)
        is 0.0757 at sw^2 = 0.21215 and 0.0227 at 0.23863 -- because the
        proton's weak vector charge sits near the zero of that combination and
        so is hypersensitive to sin^2(theta_W).
        """
        return self._FZ(Q2, False)[0] / (0.5 - 2 * self.sw2_model)

    def FZ1n(self, Q2):
        """Exactly 1 at Q^2 = 0, for any sin^2(theta_W).

        The neutron's combination is (F1n - F1p)/2 - 2 sw^2 F1n, and F1n(0) = 0
        removes the sw^2 term outright, leaving -1/2 whatever the mixing angle is.
        Only the proton is affected by the shift -- a useful check that the two
        angles have been wired to the right places.
        """
        return self._FZ(Q2, False)[1] / (-0.5)

    def FZ2p(self, Q2):
        """Absolute, like FW2 -- the Z has no point-like Pauli term either."""
        return self._FZ(Q2, True)[0]

    def FZ2n(self, Q2):
        return self._FZ(Q2, True)[1]

    def FZA(self, Q2):
        """The NC axial current is pure isovector, so the CC ratio serves it."""
        return self.FA_ratio(Q2)

    def FZ1pi(self, Q2):
        """The pion side of the neutral-current background.

        Goes on the Z-pi-pi vertex and on the Kroll-Ruderman half of the Z
        contact term.  Same construction as FZ1p -- the physical isovector
        combination over the model's own point-like coupling -- and it exists
        for the same reason.  Conservation of the NC vector current in
        Z N -> pi N' needs the nucleon's isovector piece and the pion side to
        carry the SAME function, and

            g_p FZ1p - g_n FZ1n = F1V (1 - 2 Sw2FF)

        while the model's Z-pi-pi coupling was built with sw2_model.  The ratio
        below is that constant, 0.908 at the defaults; without it the neutral
        current background misses by 2-3% of the current at every Q^2, which is
        what tools/ward_background.py reports.

        The photon needs no analogue (its charges carry no mixing angle) and
        neither does the W, so FW1 stays on those.
        """
        return (self.FW1(Q2) * (1.0 - 2.0 * self.sw2)
                / (1.0 - 2.0 * self.sw2_model))

    def FPPpi(self, Q2):
        """The pion pole on the boson leg of the four-point W-N-N-pi vertex.

        This is the PP topology: the charged current converts to a virtual pion
        through the f_pi q^mu two-point mixing, the pion propagates, and it is
        absorbed on the nucleon line by the Weinberg-Tomozawa pi-pi-N-N vertex.
        The UFO has no two-point vertices, so the mixing and the propagator are
        folded into this form factor and the whole topology is carried by one
        effective four-point operator (LPPoleFF in ChiPT.fr) -- the same device
        LNNPPFF uses for the nucleon's own induced pseudoscalar.

        Dimension is 1/mass^2, which is the propagator; everything else in the
        normalisation lives in the coupling.  FW1 rides along because the vertex
        that absorbs the pion is the isovector VECTOR coupling of the nucleon,
        the same one the pion-in-flight term is dressed with -- and because it
        is 1 at Q^2 = 0 it cannot disturb the PCAC statement, which is a
        statement about the pole.
        """
        mpi = float(self.ns.get("MPiP", 0.1395704))
        return self.FW1(Q2) / (Q2 + mpi ** 2)

    def FPPZpi(self, Q2):
        """The neutral-current pion pole; the pi0 mass and the Z's isovector.

        The nucleon NC axial current is pure isovector here, so the same pole
        with the neutral pion in it, dressed with FZ1pi for the reason given
        there.
        """
        mpi = float(self.ns.get("MPi0", 0.1349768))
        return self.FZ1pi(Q2) / (Q2 + mpi ** 2)


def param_card_block():
    """The CHIPTFF entries, in param-card layout, for pasting or checking."""
    out = ["Block CHIPTFF "]
    for name, value, order, desc in PARAMS:
        out.append("  %2d %e # %s : %s" % (order, value, name, desc))
    return "\n".join(out)


def feynrules_block():
    """The M$Parameters entries to paste into ChiPT.fr."""
    out = []
    for name, value, order, desc in PARAMS:
        out.append("""  %s == {
    ParameterType    -> External,
    BlockName        -> CHIPTFF,
    OrderBlock       -> %d,
    Value            -> %s,
    InteractionOrder -> {QED, 0},
    Description      -> "%s.  Consumed by the generator's form factor plugin, not by any vertex."
  },""" % (name, order, repr(value), desc))
    return "\n".join(out)


# ------------------------------------------------------------------ self-test
def _check():
    import sys
    ok = True

    def chk(name, got, want, tol):
        nonlocal ok
        rel = abs(got - want) / abs(want) if want else abs(got)
        if rel > tol:
            ok = False
        print("  %-4s %-22s %12.8f  want %12.8f   rel %.2e"
              % ("ok " if rel <= tol else "FAIL", name, got, want, rel))

    # Read the real UFO so the parameter plumbing is exercised, not just the
    # defaults.  The current UFO predates block CHIPTFF's form-factor entries,
    # so allow_defaults is on; once it is regenerated this picks them up.
    ns = {}
    try:
        sys.argv = ["x"]
        from fig33_from_ufo import load_ufo, parameter_namespace
        P, _ = load_ufo("ChiPT_UFO_DeltaFF")
        ns = parameter_namespace(P)
        print("UFO ChiPT_UFO_DeltaFF loaded: MNucleon = %.6f, sw = %.6f"
              % (ns["MNucleon"], ns["sw"].real))
    except Exception as e:
        print("could not load the UFO (%s); using bare defaults" % e)

    ff = FormFactors(ns, allow_defaults=True)
    print("form-factor parameters from %s"
          % ("the FeynRules defaults (UFO not yet regenerated)"
             if ff.used_defaults else "the UFO param card"))
    print("sin^2(th_W): model (on-shell, tree) = %.5f   form factors (Q->0) = %.5f"
          % (ff.sw2_model, ff.sw2))

    print("\nQ^2 = 0 must reproduce the constants hard-coded in FormFactors.C:")
    F1p, F1n, F2p, F2n = ff.dirac_pauli(0.0)
    chk("F1p", F1p, 1.0, 1e-12)
    chk("F1n", F1n, 0.0, 1e-12)
    chk("F2p", F2p, 1.792847, 1e-12)
    chk("F2n", F2n, -1.913043, 1e-12)

    print("\nratios must be exactly 1 at Q^2 = 0:")
    for name, v in (("FW1", ff.FW1(0.0)), ("FWA", ff.FWA(0.0)),
                    ("FZ1n", ff.FZ1n(0.0)),
                    ("FZA", ff.FZA(0.0)), ("C5A", ff.C5A_ratio(0.0)),
                    ("FVND", ff.VND_ratio(0.0))):
        chk(name, v, 1.0, 1e-9)
    print("\nFZ1p(0) is deliberately NOT 1: it also carries the sin^2(th_W) shift")
    chk("FZ1p", ff.FZ1p(0.0),
        (0.5 - 2 * ff.sw2) / (0.5 - 2 * ff.sw2_model), 1e-12)

    print("\nabsolute normalisation of the new Pauli operators:")
    chk("FW2(0)=kp-kn", ff.FW2(0.0), 1.792847 + 1.913043, 1e-12)
    print("       FZ2p(0) = %+.6f   FZ2n(0) = %+.6f" % (ff.FZ2p(0.0), ff.FZ2n(0.0)))
    print("       FA(0) = %+.6f  (model ga = %s; ratio cancels sign and size)"
          % (ff.FA0, ns.get("ga", "n/a")))

    print("\nQ^2 dependence:")
    print("   Q^2     FW1     FW2      FWA     FZ1p    FZ1n     C5A    FVND")
    for q in (0.0, 0.2, 0.5, 1.0, 2.0):
        print("  %4.1f  %7.4f %7.4f  %7.4f  %6.4f  %6.4f  %6.4f  %6.4f"
              % (q, ff.FW1(q), ff.FW2(q), ff.FWA(q), ff.FZ1p(q), ff.FZ1n(q),
                 ff.C5A_ratio(q), ff.VND_ratio(q)))
    print("\n   induced pseudoscalar F_P (1/GeV), and F_P/F_A = 2MN/(Q^2+mpi^2):")
    for q in (0.0, 0.2, 0.5, 1.0, 2.0):
        r = 2 * float(ff.ns.get("MNucleon", 0.938272)) * ff.FPP(q) / ff.FWA(q)
        print("  %4.1f  F_P = %9.4f   F_P/F_A = %9.4f   check %9.4f"
              % (q, ff.FPP(q), r,
                 2 * float(ff.ns.get("MNucleon", 0.938272))
                 / (q + float(ff.ns.get("MPiP", 0.1395704)) ** 2)))

    ah = FormFactors(ns, vector_model="ArringtonHill", allow_defaults=True)
    print("\nvector model cross-check, Kelly vs ArringtonHill:")
    for q in (0.5, 1.0, 2.0):
        print("  Q^2=%.1f  FW1 %7.4f / %7.4f    FW2 %7.4f / %7.4f"
              % (q, ff.FW1(q), ah.FW1(q), ff.FW2(q), ah.FW2(q)))

    print("\nmissing-block guard:")
    try:
        FormFactors({})
        print("  FAIL  no exception raised for a UFO without CHIPTFF")
        ok = False
    except KeyError:
        print("  ok    refuses a namespace with no CHIPTFF form-factor entries")

    print("\n%s" % ("ALL CHECKS PASSED" if ok else "CHECKS FAILED"))
    return ok


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--feynrules":
        print(feynrules_block())
    elif len(sys.argv) > 1 and sys.argv[1] == "--paramcard":
        print(param_card_block())
    else:
        sys.exit(0 if _check() else 1)
