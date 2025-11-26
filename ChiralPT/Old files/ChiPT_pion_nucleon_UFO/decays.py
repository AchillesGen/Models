# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Fri 5 Sep 2025 16:14:08


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.e__minus__,P.e__plus__):'((-4*Me**2*ye**2 + MH**2*ye**2)*cmath.sqrt(-4*Me**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((MH**2*ym**2 - 4*MMU**2*ym**2)*cmath.sqrt(MH**4 - 4*MH**2*MMU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.A,P.Pi__plus__):'(ee**4*fPi**2*(-MPi**2 + MW**2))/(64.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.Pi0,P.Pi__plus__):'((-((ee**2*MPi**2)/sw**2) + (ee**2*MW**2)/(4.*sw**2))*cmath.sqrt(-4*MPi**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.p,P.n__tilde__):'(((ee**2*MNucleon**2)/sw**2 - (2*ee**2*ga**2*MNucleon**2)/sw**2 + (ee**2*MW**2)/(2.*sw**2) + (ee**2*ga**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MNucleon**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi__plus__,P.Z):'(((5*ee**4*fPi**2)/(8.*cw**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MW**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MZ**2) + (ee**4*fPi**2*MPi**4)/(16.*cw**2*MW**2*MZ**2) + (ee**4*fPi**2*MW**2)/(16.*cw**2*MZ**2) + (ee**4*fPi**2*MZ**2)/(16.*cw**2*MW**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'((-Me**2 + MW**2)*(-0.5*(ee**2*Me**2)/sw**2 - (ee**2*Me**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MMU**2 + MW**2)*(-0.5*(ee**2*MMU**2)/sw**2 - (ee**2*MMU**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Pi__plus__ = Decay(name = 'Decay_Pi__plus__',
                         particle = P.Pi__plus__,
                         partial_widths = {(P.A,P.W__plus__):'(3*ee**4*fPi**2*(MPi**2 - MW**2))/(64.*cmath.pi*sw**2*abs(MPi)**3)',
                                           (P.W__plus__,P.Z):'(((5*ee**4*fPi**2)/(8.*cw**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MW**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MZ**2) + (ee**4*fPi**2*MPi**4)/(16.*cw**2*MW**2*MZ**2) + (ee**4*fPi**2*MW**2)/(16.*cw**2*MZ**2) + (ee**4*fPi**2*MZ**2)/(16.*cw**2*MW**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(16.*cmath.pi*abs(MPi)**3)',
                                           (P.p,P.n__tilde__):'(ga**2*MNucleon**2*MPi**2*cmath.sqrt(-4*MNucleon**2*MPi**2 + MPi**4))/(4.*fPi**2*cmath.pi*abs(MPi)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.Pi__minus__,P.Pi__plus__):'((2*ee**2*MPi**2 - (ee**2*MZ**2)/2. - (cw**2*ee**2*MPi**2)/sw**2 + (cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MPi**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/(4.*cw**2))*cmath.sqrt(-4*MPi**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.n,P.n__tilde__):'((ee**2*MNucleon**2 - 2*ee**2*ga**2*MNucleon**2 + (ee**2*MZ**2)/2. + (ee**2*ga**2*MZ**2)/2. + (cw**2*ee**2*MNucleon**2)/(2.*sw**2) - (cw**2*ee**2*ga**2*MNucleon**2)/sw**2 + (cw**2*ee**2*MZ**2)/(4.*sw**2) + (cw**2*ee**2*ga**2*MZ**2)/(4.*sw**2) + (ee**2*MNucleon**2*sw**2)/(2.*cw**2) - (ee**2*ga**2*MNucleon**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/(4.*cw**2) + (ee**2*ga**2*MZ**2*sw**2)/(4.*cw**2))*cmath.sqrt(-4*MNucleon**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.p,P.p__tilde__):'((-3*ee**2*MNucleon**2 - 2*ee**2*ga**2*MNucleon**2 - (3*ee**2*MZ**2)/2. + (ee**2*ga**2*MZ**2)/2. + (cw**2*ee**2*MNucleon**2)/(2.*sw**2) - (cw**2*ee**2*ga**2*MNucleon**2)/sw**2 + (cw**2*ee**2*MZ**2)/(4.*sw**2) + (cw**2*ee**2*ga**2*MZ**2)/(4.*sw**2) + (9*ee**2*MNucleon**2*sw**2)/(2.*cw**2) - (ee**2*ga**2*MNucleon**2*sw**2)/cw**2 + (9*ee**2*MZ**2*sw**2)/(4.*cw**2) + (ee**2*ga**2*MZ**2*sw**2)/(4.*cw**2))*cmath.sqrt(-4*MNucleon**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi__plus__,P.W__minus__):'(((5*ee**4*fPi**2)/(8.*cw**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MW**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MZ**2) + (ee**4*fPi**2*MPi**4)/(16.*cw**2*MW**2*MZ**2) + (ee**4*fPi**2*MW**2)/(16.*cw**2*MZ**2) + (ee**4*fPi**2*MZ**2)/(16.*cw**2*MW**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Pi__minus__,P.W__plus__):'(((5*ee**4*fPi**2)/(8.*cw**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MW**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MZ**2) + (ee**4*fPi**2*MPi**4)/(16.*cw**2*MW**2*MZ**2) + (ee**4*fPi**2*MW**2)/(16.*cw**2*MZ**2) + (ee**4*fPi**2*MZ**2)/(16.*cw**2*MW**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'((-5*ee**2*Me**2 - ee**2*MZ**2 - (cw**2*ee**2*Me**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*Me**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*Me**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MMU**2 - ee**2*MZ**2 - (cw**2*ee**2*MMU**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MMU**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MMU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_e__minus__ = Decay(name = 'Decay_e__minus__',
                         particle = P.e__minus__,
                         partial_widths = {(P.W__minus__,P.ve):'((Me**2 - MW**2)*((ee**2*Me**2)/(2.*sw**2) + (ee**2*Me**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Me)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.W__minus__,P.vm):'((MMU**2 - MW**2)*((ee**2*MMU**2)/(2.*sw**2) + (ee**2*MMU**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MMU)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_Pi0 = Decay(name = 'Decay_Pi0',
                  particle = P.Pi0,
                  partial_widths = {(P.n,P.n__tilde__):'(ga**2*MNucleon**2*MPi**2*cmath.sqrt(-4*MNucleon**2*MPi**2 + MPi**4))/(8.*fPi**2*cmath.pi*abs(MPi)**3)',
                                    (P.p,P.p__tilde__):'(ga**2*MNucleon**2*MPi**2*cmath.sqrt(-4*MNucleon**2*MPi**2 + MPi**4))/(8.*fPi**2*cmath.pi*abs(MPi)**3)'})

