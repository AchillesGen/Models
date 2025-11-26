# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Wed 26 Nov 2025 10:42:35


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


SSS2 = Lorentz(name = 'SSS2',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,3)*Gamma5(-2,1)*Gamma(-1,2,-2)')

FFS4 = Lorentz(name = 'FFS4',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FRS4 = Lorentz(name = 'FRS4',
               spins = [ 2, 4, 1 ],
               structure = '-2*Epsilon(2,-1,-2,-3)*P(-3,2)*P(-2,3)*Gamma5(-4,1)*Gamma(-1,2,-4)')

FRS5 = Lorentz(name = 'FRS5',
               spins = [ 2, 4, 1 ],
               structure = 'P(-1,3)*Gamma(-1,-2,1)*Gamma(2,2,-2)')

FRS6 = Lorentz(name = 'FRS6',
               spins = [ 2, 4, 1 ],
               structure = 'P(2,3)*Identity(2,1)')

FRV4 = Lorentz(name = 'FRV4',
               spins = [ 2, 4, 3 ],
               structure = 'Gamma(2,2,-1)*Gamma(3,-1,1)')

FRV5 = Lorentz(name = 'FRV5',
               spins = [ 2, 4, 3 ],
               structure = '-2*Epsilon(2,3,-1,-2)*P(-2,2)*Gamma5(-3,1)*Gamma(-1,2,-3)')

FRV6 = Lorentz(name = 'FRV6',
               spins = [ 2, 4, 3 ],
               structure = 'Identity(2,1)*Metric(2,3)')

VSS2 = Lorentz(name = 'VSS2',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

RFS4 = Lorentz(name = 'RFS4',
               spins = [ 4, 2, 1 ],
               structure = 'P(-1,3)*Gamma(-1,2,-2)*Gamma(1,-2,1)')

RFS5 = Lorentz(name = 'RFS5',
               spins = [ 4, 2, 1 ],
               structure = '-2*Epsilon(1,-1,-2,-3)*P(-3,1)*P(-2,3)*Gamma5(-4,1)*Gamma(-1,2,-4)')

RFS6 = Lorentz(name = 'RFS6',
               spins = [ 4, 2, 1 ],
               structure = 'P(1,3)*Identity(2,1)')

RFV4 = Lorentz(name = 'RFV4',
               spins = [ 4, 2, 3 ],
               structure = 'Gamma(1,-1,1)*Gamma(3,2,-1)')

RFV5 = Lorentz(name = 'RFV5',
               spins = [ 4, 2, 3 ],
               structure = '-2*Epsilon(1,3,-1,-2)*P(-2,1)*Gamma5(-3,1)*Gamma(-1,2,-3)')

RFV6 = Lorentz(name = 'RFV6',
               spins = [ 4, 2, 3 ],
               structure = 'Identity(2,1)*Metric(1,3)')

RRS4 = Lorentz(name = 'RRS4',
               spins = [ 4, 4, 1 ],
               structure = 'P(2,3)*Gamma5(-1,1)*Gamma(1,2,-1) + P(1,3)*Gamma5(-1,1)*Gamma(2,2,-1)')

RRS5 = Lorentz(name = 'RRS5',
               spins = [ 4, 4, 1 ],
               structure = 'P(-1,3)*Gamma5(-2,1)*Gamma(-1,-4,-3)*Gamma(1,-3,-2)*Gamma(2,2,-4)')

RRS6 = Lorentz(name = 'RRS6',
               spins = [ 4, 4, 1 ],
               structure = 'P(-1,3)*Gamma5(-2,1)*Gamma(-1,2,-2)*Metric(1,2)')

RRV8 = Lorentz(name = 'RRV8',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1)')

RRV9 = Lorentz(name = 'RRV9',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(1,-2,-1)*Gamma(2,2,-3)*Gamma(3,-3,-2)')

RRV10 = Lorentz(name = 'RRV10',
                spins = [ 4, 4, 3 ],
                structure = 'Gamma5(-1,1)*Gamma(3,2,-1)*Metric(1,2)')

RRV11 = Lorentz(name = 'RRV11',
                spins = [ 4, 4, 3 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + 2*Gamma(3,2,1)*Metric(1,2)')

RRV12 = Lorentz(name = 'RRV12',
                spins = [ 4, 4, 3 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + Gamma(2,2,1)*Metric(1,3) + Gamma(1,2,1)*Metric(2,3)')

RRV13 = Lorentz(name = 'RRV13',
                spins = [ 4, 4, 3 ],
                structure = 'Gamma5(-1,1)*Gamma(2,2,-1)*Metric(1,3) + Gamma5(-1,1)*Gamma(1,2,-1)*Metric(2,3)')

SSSS5 = Lorentz(name = 'SSSS5',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

SSSS6 = Lorentz(name = 'SSSS6',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4)')

SSSS7 = Lorentz(name = 'SSSS7',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,2) + (P(-1,1)*P(-1,3))/2. + (P(-1,2)*P(-1,3))/2. + (P(-1,1)*P(-1,4))/2. + (P(-1,2)*P(-1,4))/2. + P(-1,3)*P(-1,4)')

SSSS8 = Lorentz(name = 'SSSS8',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4) + P(-1,3)*P(-1,4)')

FFSS2 = Lorentz(name = 'FFSS2',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,2,1) - P(-1,4)*Gamma(-1,2,1)')

FFVS3 = Lorentz(name = 'FFVS3',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma(3,2,1)')

FFVS4 = Lorentz(name = 'FFVS4',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FRVS4 = Lorentz(name = 'FRVS4',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Gamma(2,2,-1)*Gamma(3,-1,1)')

FRVS5 = Lorentz(name = 'FRVS5',
                spins = [ 2, 4, 3, 1 ],
                structure = '-2*Epsilon(2,3,-1,-2)*P(-2,2)*Gamma5(-3,1)*Gamma(-1,2,-3)')

FRVS6 = Lorentz(name = 'FRVS6',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Identity(2,1)*Metric(2,3)')

VSSS6 = Lorentz(name = 'VSSS6',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2)')

VSSS7 = Lorentz(name = 'VSSS7',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2) - P(1,3) - P(1,4)')

VSSS8 = Lorentz(name = 'VSSS8',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2) + P(1,3) - P(1,4)')

VSSS9 = Lorentz(name = 'VSSS9',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,4)')

VSSS10 = Lorentz(name = 'VSSS10',
                 spins = [ 3, 1, 1, 1 ],
                 structure = 'P(1,2) + P(1,3) + P(1,4)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

RFVS4 = Lorentz(name = 'RFVS4',
                spins = [ 4, 2, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(3,2,-1)')

RFVS5 = Lorentz(name = 'RFVS5',
                spins = [ 4, 2, 3, 1 ],
                structure = '-2*Epsilon(1,3,-1,-2)*P(-2,1)*Gamma5(-3,1)*Gamma(-1,2,-3)')

RFVS6 = Lorentz(name = 'RFVS6',
                spins = [ 4, 2, 3, 1 ],
                structure = 'Identity(2,1)*Metric(1,3)')

RRSS5 = Lorentz(name = 'RRSS5',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3)')

RRSS6 = Lorentz(name = 'RRSS6',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(2,3)*Gamma(1,2,1) - P(2,4)*Gamma(1,2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) + P(1,3)*Gamma(2,2,1) - P(1,4)*Gamma(2,2,1)')

RRSS7 = Lorentz(name = 'RRSS7',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) + 2*P(-1,3)*Gamma(-1,2,1)*Metric(1,2) - 2*P(-1,4)*Gamma(-1,2,1)*Metric(1,2)')

RRVS9 = Lorentz(name = 'RRVS9',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1)')

RRVS10 = Lorentz(name = 'RRVS10',
                 spins = [ 4, 4, 3, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(1,-2,-1)*Gamma(2,2,-3)*Gamma(3,-3,-2)')

RRVS11 = Lorentz(name = 'RRVS11',
                 spins = [ 4, 4, 3, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(3,2,-1)*Metric(1,2)')

RRVS12 = Lorentz(name = 'RRVS12',
                 spins = [ 4, 4, 3, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + 2*Gamma(3,2,1)*Metric(1,2)')

RRVS13 = Lorentz(name = 'RRVS13',
                 spins = [ 4, 4, 3, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + Gamma(2,2,1)*Metric(1,3) + Gamma(1,2,1)*Metric(2,3)')

RRVS14 = Lorentz(name = 'RRVS14',
                 spins = [ 4, 4, 3, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(2,2,-1)*Metric(1,3) + Gamma5(-1,1)*Gamma(1,2,-1)*Metric(2,3)')

FFVSS3 = Lorentz(name = 'FFVSS3',
                 spins = [ 2, 2, 3, 1, 1 ],
                 structure = 'Gamma(3,2,1)')

FFVSS4 = Lorentz(name = 'FFVSS4',
                 spins = [ 2, 2, 3, 1, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FRVSS4 = Lorentz(name = 'FRVSS4',
                 spins = [ 2, 4, 3, 1, 1 ],
                 structure = 'Gamma(2,2,-1)*Gamma(3,-1,1)')

FRVSS5 = Lorentz(name = 'FRVSS5',
                 spins = [ 2, 4, 3, 1, 1 ],
                 structure = '-2*Epsilon(2,3,-1,-2)*P(-2,2)*Gamma5(-3,1)*Gamma(-1,2,-3)')

FRVSS6 = Lorentz(name = 'FRVSS6',
                 spins = [ 2, 4, 3, 1, 1 ],
                 structure = 'Identity(2,1)*Metric(2,3)')

VVSSS2 = Lorentz(name = 'VVSSS2',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'Metric(1,2)')

RFVSS4 = Lorentz(name = 'RFVSS4',
                 spins = [ 4, 2, 3, 1, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(3,2,-1)')

RFVSS5 = Lorentz(name = 'RFVSS5',
                 spins = [ 4, 2, 3, 1, 1 ],
                 structure = '-2*Epsilon(1,3,-1,-2)*P(-2,1)*Gamma5(-3,1)*Gamma(-1,2,-3)')

RFVSS6 = Lorentz(name = 'RFVSS6',
                 spins = [ 4, 2, 3, 1, 1 ],
                 structure = 'Identity(2,1)*Metric(1,3)')

RRVSS7 = Lorentz(name = 'RRVSS7',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1)')

RRVSS8 = Lorentz(name = 'RRVSS8',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(1,-2,-1)*Gamma(2,2,-3)*Gamma(3,-3,-2)')

RRVSS9 = Lorentz(name = 'RRVSS9',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(3,2,-1)*Metric(1,2)')

RRVSS10 = Lorentz(name = 'RRVSS10',
                  spins = [ 4, 4, 3, 1, 1 ],
                  structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + 2*Gamma(3,2,1)*Metric(1,2)')

RRVSS11 = Lorentz(name = 'RRVSS11',
                  spins = [ 4, 4, 3, 1, 1 ],
                  structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + Gamma(2,2,1)*Metric(1,3) + Gamma(1,2,1)*Metric(2,3)')

RRVSS12 = Lorentz(name = 'RRVSS12',
                  spins = [ 4, 4, 3, 1, 1 ],
                  structure = 'Gamma5(-1,1)*Gamma(2,2,-1)*Metric(1,3) + Gamma5(-1,1)*Gamma(1,2,-1)*Metric(2,3)')

VVSSSS2 = Lorentz(name = 'VVSSSS2',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'Metric(1,2)')

