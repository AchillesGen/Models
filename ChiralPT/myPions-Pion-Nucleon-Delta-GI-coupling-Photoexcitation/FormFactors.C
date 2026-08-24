// Form factor implementations for ChiPT_UFO_DeltaFF (CHIPT_FF=All).
//
// Sherpa-generate-model does NOT write this file; it is added by hand and
// registered in CMakeLists.txt.  Each Lorentz calculator that carries a form
// factor looks its ID up through FF_Getter and multiplies the whole current by
// FF(arg), with arg evaluated from the UFO Value string:
//
//   F1p, F1n, F2p, F2n      arg = -P(boson)^2 = Q^2
//   FgNDeltaPG1/PG2/NG1/NG2 arg = -P(boson)^2 = Q^2
//   FW1, FW2, FWA           arg = Q^2   charged-current nucleon form factors
//   FZ1p, FZ1n, FZ2p,
//   FZ2n, FZA               arg = Q^2   neutral-current nucleon form factors
//   FCA5                    arg = Q^2   N -> Delta axial, C5A(Q^2)/C5A(0)
//   FVND                    arg = Q^2   N -> Delta VECTOR, the CVC dipole
//   FPP                     arg = Q^2   induced pseudoscalar, F_P/F_A ratio
//   FPPZ                    arg = Q^2   the same for the neutral current (pi0)
//   FC6A                    arg = Q^2   Delta induced pseudoscalar, 1/mass^2
//   FpiNDelta               arg = +P(Delta)^2  = the Delta leg's INVARIANT MASS
//                                                SQUARED, not Q^2
//
// FpiNDelta = sqrt(X_pi(s)) is the Fig. 33 damping of the resonance,
// nucl-th/0509020v2 Eqs. (44)-(47), rewritten as a function of the Delta leg's
// own p^2.  That is exact for the s-channel Delta -- X_pi(u) = 0 everywhere in
// the physical region of gamma N -> pi N -- and switches the u-channel Delta
// off, which Fig. 33 instead damps by sqrt(X_pi(s)).  See DELTA_FORM_FACTORS.md
// for the size of that (1-2% at the peak, 9-17% at 0.6 GeV) and for what is
// still missing (the energy-dependent width, which is a propagator, not a form
// factor).
//
// The four gamma-N-Delta form factors MULTIPLY the fitted couplings G1 = 6.061
// and G2 = 2.414, so 1 reproduces Fig. 33 exactly.  They are separate functions
// because the magnetic (G1) and electric (G2) N -> Delta transition form
// factors are independent, and so are the proton and neutron ones.
//
// ---------------------------------------------------------------------------
// EVERYTHING BELOW IS DRIVEN BY THE PARAM CARD, NOT COMPILED IN.  Every
// coefficient is read from block CHIPTFF through MODEL::s_model->ScalarConstant,
// which is where Sherpa's UFO interface puts each external parameter under its
// own name (MODEL/UFO/src/ufo_interface/model_writer.py, _write_external_param).
// So a fit can be varied by editing param_ChiPT_UFO*.dat with no recompilation,
// and this file and the analytic cross-check formfactors.py evaluate the same
// numbers because they read the same card.  The Python side is the reference
// implementation; this is a transliteration of it.
//
// THE MISSING-BLOCK TRAP.  Sherpa reads external parameters with a default of
// 0.0 when the entry is absent, so a param card written before block CHIPTFF
// existed would silently give every form factor zero and every cross section
// zero.  Params::Get below throws instead.
//
// WHICH ARE RATIOS AND WHICH ARE NOT.  FW1, FWA, FZ1n, FZA, FCA5 and FVND are 1 at
// Q^2 = 0 and multiply a coupling the model already has, so they change nothing
// at the photon point.  FZ1p is NOT 1 there: it also carries the shift of
// sin^2(theta_W) from the model's tree-level on-shell value to the Q -> 0 one,
// a factor 0.30, because the proton's weak vector charge 1/2 - 2 sw^2 sits near
// a zero.  FW2, FZ2p and FZ2n are absolute: the model has no point-like weak
// magnetism at all, so those operators are new and carry their own
// normalisation, which CVC fixes from the electromagnetic F2's.

#include "ATOOLS/Org/Message.H"
#include "METOOLS/Explicit/Form_Factor.H"
#include "METOOLS/Explicit/Vertex_Key.H"
#include "METOOLS/Explicit/Current.H"
#include "METOOLS/Explicit/Vertex.H"
#include "MODEL/Main/Model_Base.H"

#include "ATOOLS/Org/Exception.H"

#include <cmath>

using namespace ATOOLS;
using namespace METOOLS;

namespace {

  // Masses in GeV, as in param_ChiPT_UFO_DeltaFF.dat.
  constexpr double MN = 0.938272, MPi = 0.1349768, MD = 1.209;

  // ---- param-card access ---------------------------------------------------
  struct Params {
    static double Get(const std::string &name) {
      const auto &c = MODEL::s_model->ScalarConstants();
      auto it = c.find(name);
      if (it == c.end() || it->second == 0.0)
        THROW(fatal_error, "CHIPTFF parameter '" + name + "' missing or zero in "
              "the param card.  Regenerate the UFO with CHIPT_FF=Weak (or All) "
              "and rewrite param_ChiPT_UFO*.dat -- Sherpa defaults absent "
              "entries to 0, which would silently zero the cross section.");
      return it->second;
    }
    static double Opt(const std::string &name, double dflt) {
      const auto &c = MODEL::s_model->ScalarConstants();
      auto it = c.find(name);
      return it == c.end() ? dflt : it->second;
    }
    // The MODEL's OWN sin^2(theta_W), which is NOT Sw2FF.  Sherpa's UFO
    // interface computes csin2_thetaW = 1 - MW^2/MZ^2 from the particle masses
    // (MODEL/UFO/UFO_Model.C) and stores it among the complex constants; the
    // UFO's internal 'sw' is only a local in the generated model and never
    // reaches the constants map, so this is the way to get it.
    static double Sw2Model() {
      return MODEL::s_model->ComplexConstant("csin2_thetaW").real();
    }
  };

  // ---- Kelly vector form factors, coefficients from block CHIPTFF -----------
  // Achilles/main data/default/FormFactors.yml, class Kelly in
  // src/Achilles/FormFactor.cc.  Sachs -> Dirac/Pauli is Achilles' Fill().
  inline double KellyRatio(double a1, double b1, double b2, double b3, double x) {
    return (1 + a1 * x) / (1 + b1 * x + b2 * x * x + b3 * x * x * x);
  }

  void Sachs(double Q2, double &Gep, double &Gen, double &Gmp, double &Gmn) {
    const double tau = Q2 / (4 * MN * MN);
    Gep = KellyRatio(Params::Get("KEp1"), Params::Get("KEp2"),
                     Params::Get("KEp3"), Params::Get("KEp4"), tau);
    Gen = 1.0 / std::pow(1 + Q2 / Params::Get("KLamSq"), 2)
          * Params::Get("KEn1") * tau / (1 + Params::Get("KEn2") * tau);
    Gmp = Params::Get("MuP") * KellyRatio(Params::Get("KMp1"), Params::Get("KMp2"),
                                          Params::Get("KMp3"), Params::Get("KMp4"), tau);
    Gmn = Params::Get("MuN") * KellyRatio(Params::Get("KMn1"), Params::Get("KMn2"),
                                          Params::Get("KMn3"), Params::Get("KMn4"), tau);
  }

  void DiracPauli(double Q2, double &F1p, double &F1n, double &F2p, double &F2n) {
    double Gep, Gen, Gmp, Gmn;
    Sachs(Q2, Gep, Gen, Gmp, Gmn);
    const double tau = Q2 / (4 * MN * MN);
    F1p = (Gep + tau * Gmp) / (1 + tau);
    F1n = (Gen + tau * Gmn) / (1 + tau);
    F2p = (Gmp - Gep) / (1 + tau);
    F2n = (Gmn - Gen) / (1 + tau);
  }

  // ---- axial z-expansion ----------------------------------------------------
  // Achilles class AxialZExpansion.  FA(0) comes out NEGATIVE by its sign
  // convention and 0.42% larger in magnitude than the model's ga; the RATIO
  // FA(Q^2)/FA(0) cancels both, so the model keeps its own g_A -- which it must,
  // because ga sets the strong pi-N coupling through the same chiral Lagrangian
  // term as the axial current.
  double FA_raw(double Q2) {
    const double tcut = Params::Get("AxTcut"), t0 = Params::Get("AxT0");
    const double z = (std::sqrt(tcut + Q2) - std::sqrt(tcut - t0))
                   / (std::sqrt(tcut + Q2) + std::sqrt(tcut - t0));
    double a[9] = {Params::Get("AxA0"), Params::Get("AxA1"), Params::Get("AxA2"),
                   Params::Get("AxA3"), Params::Get("AxA4"), Params::Get("AxA5"),
                   Params::Get("AxA6"), Params::Get("AxA7"), Params::Get("AxA8")};
    double r = 0;                       // Horner, as Achilles' ZExpand
    for (int i = 8; i > 0; --i) { r += a[i]; r *= z; }
    return r + a[0];
  }
  double FA_ratio(double Q2) { return FA_raw(Q2) / FA_raw(0.0); }

  // ---- N -> Delta axial, C5A(Q^2)/C5A(0) ------------------------------------
  // Achilles MECAxialFormFactor's shape; ca5norm and its sqrt(3/2) cancel in the
  // ratio, so the model's own gauged N -> Delta coupling is left alone.
  // rho-dominance factor on the axial half of the contact term.  The
  // references pair it with the pion-pole (PP) diagram so that PCAC survives;
  // this model has NO PP term -- it would come from the two-point W-pi mixing,
  // which FeynRules does not export to a UFO -- so PCAC is NOT restored the way
  // CVC now is.  Left as a documented limitation, not a claim.
  double FrhoCT(double Q2) {
    const double m2 = std::pow(Params::Get("MRhoCT"), 2);
    return m2 / (m2 + Q2);          // t = -Q^2 for the spacelike exchange
  }

  double C5A_ratio(double Q2) {
    const double M2 = Params::Get("MADeltaSq");
    return 1.0 / std::pow(1 + Q2 / M2, 2) / (1 + Q2 / (3 * M2));
  }

  // The CVC vector N -> Delta dipole, 1 at Q^2 = 0.  The standard C_i^V shape:
  // a dipole in the nucleon vector mass with the extra 1/(1 + Q^2/4 M_V^2)
  // pole.  LWeakNDeltaV covariantises the model's PHOTON N -> Delta vertex,
  // whose own FgNDelta* form factors are identically 1, so before this was
  // added nothing damped the vector transition at large Q^2 and the Delta term
  // ran away above ~1 GeV.  Being a ratio it multiplies G1 and G2 without
  // moving the Fig. 33 photoproduction fit at the photon point.
  // Induced pseudoscalar, as a ratio to the axial vertex it sits beside:
  //     F_P(Q^2) = 2 MN F_A(Q^2) / (Q^2 + mpi^2)
  // PCAC / off-diagonal Goldberger-Treiman, no free parameter.  ChiPT.fr writes
  // the operator with the same prefactor and the same -ga as the axial term, so
  // only the ratio belongs here.  MPiC is the CHARGED pion -- this is the
  // charged current -- unlike MPi above, which follows Fig. 33's neutral mass.
  double FPP(double Q2) {
    constexpr double MPiC = 0.1395704;
    return FA_ratio(Q2) / (Q2 + MPiC * MPiC);   // the 2 MN is in the coupling
  }

  // Neutral-current induced pseudoscalar.  The NC axial current is pure
  // isovector, so the same pole and the same PCAC ratio -- only the mass
  // differs, the pole being the pi0.  MPi is already the neutral one.
  double FPPZ(double Q2) {
    return FA_ratio(Q2) / (Q2 + MPi * MPi);   // the 2 MN is in the coupling
  }

  // The Delta's induced pseudoscalar.  PCAC ties C6A to C5A by
  //     C6A = C5A MN^2 / (Q^2 + mpi^2)
  // and the operator in ChiPT.fr carries two derivatives of the source, which
  // supply the 1/MN^2, so only C5A/(Q^2+mpi^2) belongs here.  Dimension is
  // 1/mass^2.  Charged pion mass, as in formfactors.py.
  double FC6A(double Q2) {
    constexpr double MPiC = 0.1395704;
    return C5A_ratio(Q2) / (Q2 + MPiC * MPiC);
  }

  double VND_ratio(double Q2) {
    const double M2 = Params::Get("MV2ND");
    return 1.0 / std::pow(1 + Q2 / M2, 2) / (1 + Q2 / (4 * M2));
  }

  // ---- the neutral-current charge combinations ------------------------------
  // No strangeness: J^Z = J^3 - 2 sw^2 J^EM, i.e.
  //   F_i^{Z,p} = (F_i^p - F_i^n)/2 - 2 sw^2 F_i^p ,  and p <-> n for the other.
  // sw^2 is Sw2FF, the Q -> 0 value, NOT the model's tree-level on-shell one.
  void FZ(double Q2, bool pauli, double &Zp, double &Zn) {
    double F1p, F1n, F2p, F2n;
    DiracPauli(Q2, F1p, F1n, F2p, F2n);
    const double a = pauli ? F2p : F1p, b = pauli ? F2n : F1n;
    const double s = Params::Get("Sw2FF");
    Zp = 0.5 * (a - b) - 2 * s * a;
    Zn = 0.5 * (b - a) - 2 * s * b;
  }

  // pi-N cm momentum at invariant mass squared l.
  double KPiN(double l) {
    const double a = l - MN * MN - MPi * MPi;
    const double r = a * a - 4.0 * MPi * MPi * MN * MN;
    return (r <= 0.0 || l <= 0.0) ? 0.0 : std::sqrt(r) / (2.0 * std::sqrt(l));
  }

  // X_pi(s), Eqs. (44)-(47).  Zero below the pi-N threshold, 1 at s = M_Delta^2.
  double XPi(double s) {
    if(s < (MN + MPi) * (MN + MPi)) return 0.0;
    const double r = KPiN(s) / KPiN(MD * MD);
    return 2.0 * r * r * r / (1.0 + std::pow(r, 5));
  }

}

class FormFactorInterface : public METOOLS::Form_Factor {
  private:
    std::string m_id;

  public:
    FormFactorInterface(const Vertex_Key &key, const std::string &id) : Form_Factor(id, key), m_id(id) {}

    // arg is Q^2 for the electromagnetic form factors and p_Delta^2 for FpiNDelta.
    double FF(double arg) const override {
        // arg is Q^2 for everything except FpiNDelta, which gets p_Delta^2.
        if(m_id == "F1p" || m_id == "F1n" || m_id == "F2p" || m_id == "F2n") {
            double F1p, F1n, F2p, F2n;
            DiracPauli(arg, F1p, F1n, F2p, F2n);
            if(m_id == "F1p") return F1p;
            if(m_id == "F1n") return F1n;
            if(m_id == "F2p") return F2p;
            return F2n;
        }

        // charged current.  CVC: the vector ones ARE the isovector combinations
        // of the electromagnetic ones, so no new parameters.  FW1(0) = 1 already,
        // hence it is its own ratio; FW2 is absolute.
        if(m_id == "FW1" || m_id == "FW2") {
            double F1p, F1n, F2p, F2n;
            DiracPauli(arg, F1p, F1n, F2p, F2n);
            return m_id == "FW1" ? F1p - F1n : F2p - F2n;
        }
        if(m_id == "FWA") return FA_ratio(arg);

        // neutral current
        if(m_id == "FZ1p" || m_id == "FZ1n") {
            double Zp, Zn; FZ(arg, false, Zp, Zn);
            // TWO DIFFERENT MIXING ANGLES, on purpose.  The numerator is the
            // physical charge combination at the low-Q value (inside FZ, via
            // Sw2FF); the denominator is the model's OWN point-like coupling,
            // which was built from csin2_thetaW.  So multiplying the vertex by
            // this does two jobs: it supplies the Q^2 dependence AND corrects
            // sin^2(theta_W).  Hence FZ1p(0) = 0.30, not 1.  FZ1n IS 1 at
            // Q^2 = 0 for any angle, because F1n(0) = 0 removes the sw^2 term --
            // which is the check that the two angles are wired to the right
            // places.
            return m_id == "FZ1p" ? Zp / (0.5 - 2 * Params::Sw2Model())
                                  : Zn / (-0.5);
        }
        if(m_id == "FZ2p" || m_id == "FZ2n") {
            double Zp, Zn; FZ(arg, true, Zp, Zn);
            return m_id == "FZ2p" ? Zp : Zn;
        }
        if(m_id == "FZA") return FA_ratio(arg);   // NC axial is pure isovector

        if(m_id == "FCA5") return C5A_ratio(arg);
        if(m_id == "FVND") return VND_ratio(arg);
        if(m_id == "FPP") return FPP(arg);
        if(m_id == "FPPZ") return FPPZ(arg);
        if(m_id == "FC6A") return FC6A(arg);
        if(m_id == "FrhoCT") return FrhoCT(arg);

        if(m_id == "FpiNDelta") return std::sqrt(XPi(arg));

        if(m_id == "FgNDeltaPG1") return 1;
        if(m_id == "FgNDeltaPG2") return 1;
        if(m_id == "FgNDeltaNG1") return 1;
        if(m_id == "FgNDeltaNG2") return 1;

        THROW(fatal_error, "Form factor not implemented '" + m_id + "'");
    }
};


#define FORM_FACTOR_IMPLEMENTATION(NAME)                                                         \
    namespace achilles {                                                                         \
    class NAME : public Getter_Function<Form_Factor, Vertex_Key, std::less<std::string> > {      \
        static NAME s_initializer;                                                               \
                                                                                                 \
      protected:                                                                                 \
        void PrintInfo(std::ostream &str, const size_t) const {                                  \
            str << #NAME;                                                                        \
        }                                                                                        \
        Object_Type *operator()(const Parameter_Type &args) const {                              \
            return new FormFactorInterface(args, #NAME);                                         \
        }                                                                                        \
                                                                                                 \
      public:                                                                                    \
        NAME(const std::string &name)                                                            \
            : ATOOLS::Getter_Function<Form_Factor, Vertex_Key, std::less<std::string> >(name) {} \
    };                                                                                           \
    NAME NAME::s_initializer(#NAME);                                                             \
    }

FORM_FACTOR_IMPLEMENTATION(F1p)
FORM_FACTOR_IMPLEMENTATION(F1n)
FORM_FACTOR_IMPLEMENTATION(F2p)
FORM_FACTOR_IMPLEMENTATION(F2n)
FORM_FACTOR_IMPLEMENTATION(FpiNDelta)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaPG1)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaPG2)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaNG1)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaNG2)
FORM_FACTOR_IMPLEMENTATION(FW1)
FORM_FACTOR_IMPLEMENTATION(FW2)
FORM_FACTOR_IMPLEMENTATION(FWA)
FORM_FACTOR_IMPLEMENTATION(FZ1p)
FORM_FACTOR_IMPLEMENTATION(FZ1n)
FORM_FACTOR_IMPLEMENTATION(FZ2p)
FORM_FACTOR_IMPLEMENTATION(FZ2n)
FORM_FACTOR_IMPLEMENTATION(FZA)
FORM_FACTOR_IMPLEMENTATION(FCA5)
FORM_FACTOR_IMPLEMENTATION(FVND)
FORM_FACTOR_IMPLEMENTATION(FPP)
FORM_FACTOR_IMPLEMENTATION(FPPZ)
FORM_FACTOR_IMPLEMENTATION(FC6A)
FORM_FACTOR_IMPLEMENTATION(FrhoCT)

#undef FORM_FACTOR_IMPLEMENTATION
