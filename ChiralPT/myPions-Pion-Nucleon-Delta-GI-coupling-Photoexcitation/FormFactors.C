// Form factor implementations for ChiPT_UFO_DeltaFF (CHIPT_FF=All).
//
// Sherpa-generate-model does NOT write this file; it is added by hand and
// registered in CMakeLists.txt.  Each Lorentz calculator that carries a form
// factor looks its ID up through FF_Getter and multiplies the whole current by
// FF(arg), with arg evaluated from the UFO Value string:
//
//   F1p, F1n, F2p, F2n      arg = -P(photon)^2 = Q^2
//   FgNDeltaPG1/PG2/NG1/NG2 arg = -P(photon)^2 = Q^2
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
        if(m_id == "F1p") return 1;
        if(m_id == "F1n") return 0;
        if(m_id == "F2p") return 1.792847;
        if(m_id == "F2n") return -1.913043;

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

#undef FORM_FACTOR_IMPLEMENTATION
