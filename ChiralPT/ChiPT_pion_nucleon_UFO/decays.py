# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Wed 3 Sep 2025 23:28:42


from object_library import all_decays, Decay
import particles as P


Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.A,P.Pi__plus__):'(ee**4*fPi**2*(-MPi**2 + MW**2))/(64.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.Pi0,P.Pi__plus__):'((-((ee**2*MPi**2)/sw**2) + (ee**2*MW**2)/(4.*sw**2))*cmath.sqrt(-4*MPi**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.p,P.n__tilde__):'(((ee**2*MNucleon**2)/sw**2 - (2*ee**2*ga**2*MNucleon**2)/sw**2 + (ee**2*MW**2)/(2.*sw**2) + (ee**2*ga**2*MW**2)/(2.*sw**2))*cmath.sqrt(-4*MNucleon**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.Pi__plus__,P.Z):'(((5*ee**4*fPi**2)/(8.*cw**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MW**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MZ**2) + (ee**4*fPi**2*MPi**4)/(16.*cw**2*MW**2*MZ**2) + (ee**4*fPi**2*MW**2)/(16.*cw**2*MZ**2) + (ee**4*fPi**2*MZ**2)/(16.*cw**2*MW**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MW)**3)'})

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
                                  (P.Pi__minus__,P.W__plus__):'(((5*ee**4*fPi**2)/(8.*cw**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MW**2) - (ee**4*fPi**2*MPi**2)/(8.*cw**2*MZ**2) + (ee**4*fPi**2*MPi**4)/(16.*cw**2*MW**2*MZ**2) + (ee**4*fPi**2*MW**2)/(16.*cw**2*MZ**2) + (ee**4*fPi**2*MZ**2)/(16.*cw**2*MW**2))*cmath.sqrt(MPi**4 - 2*MPi**2*MW**2 + MW**4 - 2*MPi**2*MZ**2 - 2*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_Pi0 = Decay(name = 'Decay_Pi0',
                  particle = P.Pi0,
                  partial_widths = {(P.n,P.n__tilde__):'(ga**2*MNucleon**2*MPi**2*cmath.sqrt(-4*MNucleon**2*MPi**2 + MPi**4))/(8.*fPi**2*cmath.pi*abs(MPi)**3)',
                                    (P.p,P.p__tilde__):'(ga**2*MNucleon**2*MPi**2*cmath.sqrt(-4*MNucleon**2*MPi**2 + MPi**4))/(8.*fPi**2*cmath.pi*abs(MPi)**3)'})

