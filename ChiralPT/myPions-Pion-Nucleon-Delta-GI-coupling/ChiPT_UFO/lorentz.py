# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Wed 29 Oct 2025 00:14:05


from .object_library import all_lorentz, Lorentz

from .function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   from . import form_factors as ForFac 
except ImportError:
   pass


SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,3)*Gamma5(-2,1)*Gamma(-1,2,-2)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FRS1 = Lorentz(name = 'FRS1',
               spins = [ 2, 4, 1 ],
               structure = '-2*Epsilon(2,-1,-2,-3)*P(-3,2)*P(-2,3)*Gamma5(-4,1)*Gamma(-1,2,-4)*FDeltaDipole(P(-5,2)**2)')

FRS2 = Lorentz(name = 'FRS2',
               spins = [ 2, 4, 1 ],
               structure = 'P(-1,3)*Gamma(-1,-2,1)*Gamma(2,2,-2)*FDeltaDipole(P(-5,2)**2)')

FRS3 = Lorentz(name = 'FRS3',
               spins = [ 2, 4, 1 ],
               structure = 'P(2,3)*Identity(2,1)*FDeltaDipole(P(-5,2)**2)')

FRV1 = Lorentz(name = 'FRV1',
               spins = [ 2, 4, 3 ],
               structure = 'Gamma(2,2,-1)*Gamma(3,-1,1)')

FRV2 = Lorentz(name = 'FRV2',
               spins = [ 2, 4, 3 ],
               structure = '-2*Epsilon(2,3,-1,-2)*P(-2,2)*Gamma5(-3,1)*Gamma(-1,2,-3)')

FRV3 = Lorentz(name = 'FRV3',
               spins = [ 2, 4, 3 ],
               structure = 'Identity(2,1)*Metric(2,3)')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

RFS1 = Lorentz(name = 'RFS1',
               spins = [ 4, 2, 1 ],
               structure = 'P(-1,3)*Gamma(-1,2,-2)*Gamma(1,-2,1)*FDeltaDipole(P(-5,1)**2)')

RFS2 = Lorentz(name = 'RFS2',
               spins = [ 4, 2, 1 ],
               structure = '-2*Epsilon(1,-1,-2,-3)*P(-3,1)*P(-2,3)*Gamma5(-4,1)*Gamma(-1,2,-4)*FDeltaDipole(P(-5,1)**2)')

RFS3 = Lorentz(name = 'RFS3',
               spins = [ 4, 2, 1 ],
               structure = 'P(1,3)*Identity(2,1)*FDeltaDipole(P(-5,1)**2)')

RFV1 = Lorentz(name = 'RFV1',
               spins = [ 4, 2, 3 ],
               structure = 'Gamma(1,-1,1)*Gamma(3,2,-1)')

RFV2 = Lorentz(name = 'RFV2',
               spins = [ 4, 2, 3 ],
               structure = '-2*Epsilon(1,3,-1,-2)*P(-2,1)*Gamma5(-3,1)*Gamma(-1,2,-3)')

RFV3 = Lorentz(name = 'RFV3',
               spins = [ 4, 2, 3 ],
               structure = 'Identity(2,1)*Metric(1,3)')

RRS1 = Lorentz(name = 'RRS1',
               spins = [ 4, 4, 1 ],
               structure = 'P(2,3)*Gamma5(-1,1)*Gamma(1,2,-1) + P(1,3)*Gamma5(-1,1)*Gamma(2,2,-1)')

RRS2 = Lorentz(name = 'RRS2',
               spins = [ 4, 4, 1 ],
               structure = 'P(-1,3)*Gamma5(-2,1)*Gamma(-1,-4,-3)*Gamma(1,-3,-2)*Gamma(2,2,-4)')

RRS3 = Lorentz(name = 'RRS3',
               spins = [ 4, 4, 1 ],
               structure = 'P(-1,3)*Gamma5(-2,1)*Gamma(-1,2,-2)*Metric(1,2)')

RRV1 = Lorentz(name = 'RRV1',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1)')

RRV2 = Lorentz(name = 'RRV2',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(1,-2,-1)*Gamma(2,2,-3)*Gamma(3,-3,-2)')

RRV3 = Lorentz(name = 'RRV3',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(3,2,-1)*Metric(1,2)')

RRV4 = Lorentz(name = 'RRV4',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + 2*Gamma(3,2,1)*Metric(1,2)')

RRV5 = Lorentz(name = 'RRV5',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + Gamma(2,2,1)*Metric(1,3) + Gamma(1,2,1)*Metric(2,3)')

RRV6 = Lorentz(name = 'RRV6',
               spins = [ 4, 4, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(2,2,-1)*Metric(1,3) + Gamma5(-1,1)*Gamma(1,2,-1)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

SSSS2 = Lorentz(name = 'SSSS2',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4)')

SSSS3 = Lorentz(name = 'SSSS3',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,2) + (P(-1,1)*P(-1,3))/2. + (P(-1,2)*P(-1,3))/2. + (P(-1,1)*P(-1,4))/2. + (P(-1,2)*P(-1,4))/2. + P(-1,3)*P(-1,4)')

SSSS4 = Lorentz(name = 'SSSS4',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4) + P(-1,3)*P(-1,4)')

FFSS1 = Lorentz(name = 'FFSS1',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,2,1) - P(-1,4)*Gamma(-1,2,1)')

FFVS1 = Lorentz(name = 'FFVS1',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma(3,2,1)')

FFVS2 = Lorentz(name = 'FFVS2',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FRVS1 = Lorentz(name = 'FRVS1',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Gamma(2,2,-1)*Gamma(3,-1,1)')

FRVS2 = Lorentz(name = 'FRVS2',
                spins = [ 2, 4, 3, 1 ],
                structure = '-2*Epsilon(2,3,-1,-2)*P(-2,2)*Gamma5(-3,1)*Gamma(-1,2,-3)')

FRVS3 = Lorentz(name = 'FRVS3',
                spins = [ 2, 4, 3, 1 ],
                structure = 'Identity(2,1)*Metric(2,3)')

VSSS1 = Lorentz(name = 'VSSS1',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2)')

VSSS2 = Lorentz(name = 'VSSS2',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2) - P(1,3) - P(1,4)')

VSSS3 = Lorentz(name = 'VSSS3',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2) + P(1,3) - P(1,4)')

VSSS4 = Lorentz(name = 'VSSS4',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,4)')

VSSS5 = Lorentz(name = 'VSSS5',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2) + P(1,3) + P(1,4)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

RFVS1 = Lorentz(name = 'RFVS1',
                spins = [ 4, 2, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(3,2,-1)')

RFVS2 = Lorentz(name = 'RFVS2',
                spins = [ 4, 2, 3, 1 ],
                structure = '-2*Epsilon(1,3,-1,-2)*P(-2,1)*Gamma5(-3,1)*Gamma(-1,2,-3)')

RFVS3 = Lorentz(name = 'RFVS3',
                spins = [ 4, 2, 3, 1 ],
                structure = 'Identity(2,1)*Metric(1,3)')

RRSS1 = Lorentz(name = 'RRSS1',
                spins = [ 4, 4, 1, 1 ],
                structure = '-(P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3)) + P(-1,3)*Gamma(-1,-2,-3)*Gamma(1,-3,1)*Gamma(2,2,-2)')

RRSS2 = Lorentz(name = 'RRSS2',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3)')

RRSS3 = Lorentz(name = 'RRSS3',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(2,3)*Gamma(1,2,1) - P(2,4)*Gamma(1,2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) + P(1,3)*Gamma(2,2,1) - P(1,4)*Gamma(2,2,1)')

RRSS4 = Lorentz(name = 'RRSS4',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) + 2*P(-1,3)*Gamma(-1,2,1)*Metric(1,2) - 2*P(-1,4)*Gamma(-1,2,1)*Metric(1,2)')

RRVS1 = Lorentz(name = 'RRVS1',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-2,1)*Gamma(2,2,-1)*Gamma(3,-1,-2)')

RRVS2 = Lorentz(name = 'RRVS2',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma5(-2,1)*Gamma(1,-3,-2)*Gamma(2,2,-1)*Gamma(3,-1,-3)')

RRVS3 = Lorentz(name = 'RRVS3',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1)')

RRVS4 = Lorentz(name = 'RRVS4',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(1,-2,-1)*Gamma(2,2,-3)*Gamma(3,-3,-2)')

RRVS5 = Lorentz(name = 'RRVS5',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(3,2,-1)*Metric(1,2)')

RRVS6 = Lorentz(name = 'RRVS6',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + 2*Gamma(3,2,1)*Metric(1,2)')

RRVS7 = Lorentz(name = 'RRVS7',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + Gamma(2,2,1)*Metric(1,3) + Gamma(1,2,1)*Metric(2,3)')

RRVS8 = Lorentz(name = 'RRVS8',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(2,2,-1)*Metric(1,3) + Gamma5(-1,1)*Gamma(1,2,-1)*Metric(2,3)')

FFVSS1 = Lorentz(name = 'FFVSS1',
                 spins = [ 2, 2, 3, 1, 1 ],
                 structure = 'Gamma(3,2,1)')

FFVSS2 = Lorentz(name = 'FFVSS2',
                 spins = [ 2, 2, 3, 1, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FRVSS1 = Lorentz(name = 'FRVSS1',
                 spins = [ 2, 4, 3, 1, 1 ],
                 structure = 'Gamma(2,2,-1)*Gamma(3,-1,1)')

FRVSS2 = Lorentz(name = 'FRVSS2',
                 spins = [ 2, 4, 3, 1, 1 ],
                 structure = '-2*Epsilon(2,3,-1,-2)*P(-2,2)*Gamma5(-3,1)*Gamma(-1,2,-3)')

FRVSS3 = Lorentz(name = 'FRVSS3',
                 spins = [ 2, 4, 3, 1, 1 ],
                 structure = 'Identity(2,1)*Metric(2,3)')

VVSSS1 = Lorentz(name = 'VVSSS1',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'Metric(1,2)')

RFVSS1 = Lorentz(name = 'RFVSS1',
                 spins = [ 4, 2, 3, 1, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(3,2,-1)')

RFVSS2 = Lorentz(name = 'RFVSS2',
                 spins = [ 4, 2, 3, 1, 1 ],
                 structure = '-2*Epsilon(1,3,-1,-2)*P(-2,1)*Gamma5(-3,1)*Gamma(-1,2,-3)')

RFVSS3 = Lorentz(name = 'RFVSS3',
                 spins = [ 4, 2, 3, 1, 1 ],
                 structure = 'Identity(2,1)*Metric(1,3)')

RRVSS1 = Lorentz(name = 'RRVSS1',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1)')

RRVSS2 = Lorentz(name = 'RRVSS2',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(1,-2,-1)*Gamma(2,2,-3)*Gamma(3,-3,-2)')

RRVSS3 = Lorentz(name = 'RRVSS3',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(3,2,-1)*Metric(1,2)')

RRVSS4 = Lorentz(name = 'RRVSS4',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma(1,-2,1)*Gamma(2,2,-1)*Gamma(3,-1,-2) + 2*Gamma(3,2,1)*Metric(1,2)')

RRVSS5 = Lorentz(name = 'RRVSS5',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + 2*Gamma(3,2,1)*Metric(1,2)')

RRVSS6 = Lorentz(name = 'RRVSS6',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + Gamma(2,2,1)*Metric(1,3) + Gamma(1,2,1)*Metric(2,3)')

RRVSS7 = Lorentz(name = 'RRVSS7',
                 spins = [ 4, 4, 3, 1, 1 ],
                 structure = 'Gamma5(-1,1)*Gamma(2,2,-1)*Metric(1,3) + Gamma5(-1,1)*Gamma(1,2,-1)*Metric(2,3)')

VVSSSS1 = Lorentz(name = 'VVSSSS1',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'Metric(1,2)')

