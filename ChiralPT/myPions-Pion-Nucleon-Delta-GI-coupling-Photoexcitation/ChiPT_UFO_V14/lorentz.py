# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Mon 12 Oct 2026 12:30:26


from __future__ import absolute_import
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
               structure = '(F1n(-P(-1,3)**2))*Gamma(3,2,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = '(F1p(-P(-1,3)**2))*Gamma(3,2,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = '(FW1(-P(-9,3)**2))*Gamma(3,2,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = '(FW1(-P(-9,3)**2))*Gamma(3,2,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = '(FZ1n(-P(-9,3)**2))*Gamma(3,2,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = '(FZ1p(-P(-9,3)**2))*Gamma(3,2,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = '(FWA(-P(-9,3)**2))*Gamma5(-1,1)*Gamma(3,2,-1)')

FFV9 = Lorentz(name = 'FFV9',
               spins = [ 2, 2, 3 ],
               structure = '(FWA(-P(-9,3)**2))*Gamma5(-1,1)*Gamma(3,2,-1)')

FFV10 = Lorentz(name = 'FFV10',
                spins = [ 2, 2, 3 ],
                structure = '(FZA(-P(-9,3)**2))*Gamma5(-1,1)*Gamma(3,2,-1)')

FFV11 = Lorentz(name = 'FFV11',
                spins = [ 2, 2, 3 ],
                structure = '(FZA(-P(-9,3)**2))*Gamma5(-1,1)*Gamma(3,2,-1)')

FFV12 = Lorentz(name = 'FFV12',
                spins = [ 2, 2, 3 ],
                structure = '(FPP(-P(-9,3)**2))*P(-1,3)*P(3,3)*Gamma5(-2,1)*Gamma(-1,2,-2)')

FFV13 = Lorentz(name = 'FFV13',
                spins = [ 2, 2, 3 ],
                structure = '(FPP(-P(-9,3)**2))*P(-1,3)*P(3,3)*Gamma5(-2,1)*Gamma(-1,2,-2)')

FFV14 = Lorentz(name = 'FFV14',
                spins = [ 2, 2, 3 ],
                structure = '(FPPZ(-P(-9,3)**2))*P(-1,3)*P(3,3)*Gamma5(-2,1)*Gamma(-1,2,-2)')

FFV15 = Lorentz(name = 'FFV15',
                spins = [ 2, 2, 3 ],
                structure = '(FPPZ(-P(-9,3)**2))*P(-1,3)*P(3,3)*Gamma5(-2,1)*Gamma(-1,2,-2)')

FFV16 = Lorentz(name = 'FFV16',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV17 = Lorentz(name = 'FFV17',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV18 = Lorentz(name = 'FFV18',
                spins = [ 2, 2, 3 ],
                structure = '(F2n(-P(-1,3)**2))*P(-1,3)*Sigma(3,-1,2,1)')

FFV19 = Lorentz(name = 'FFV19',
                spins = [ 2, 2, 3 ],
                structure = '(F2p(-P(-1,3)**2))*P(-1,3)*Sigma(3,-1,2,1)')

FFV20 = Lorentz(name = 'FFV20',
                spins = [ 2, 2, 3 ],
                structure = '(FW2(-P(-9,3)**2))*P(-1,3)*Sigma(3,-1,2,1)')

FFV21 = Lorentz(name = 'FFV21',
                spins = [ 2, 2, 3 ],
                structure = '(FW2(-P(-9,3)**2))*P(-1,3)*Sigma(3,-1,2,1)')

FFV22 = Lorentz(name = 'FFV22',
                spins = [ 2, 2, 3 ],
                structure = '(FZ2n(-P(-9,3)**2))*P(-1,3)*Sigma(3,-1,2,1)')

FFV23 = Lorentz(name = 'FFV23',
                spins = [ 2, 2, 3 ],
                structure = '(FZ2p(-P(-9,3)**2))*P(-1,3)*Sigma(3,-1,2,1)')

FRS1 = Lorentz(name = 'FRS1',
               spins = [ 2, 4, 1 ],
               structure = '-((FpiNDelta(P(-9,2)**2))*Epsilon(2,-1,-2,-3)*P(-2,2)*P(-1,3)*Gamma5(-4,1)*Gamma(-3,2,-4))')

FRV1 = Lorentz(name = 'FRV1',
               spins = [ 2, 4, 3 ],
               structure = '-((FCA5(-P(-9,3)**2))*Epsilon(2,3,-1,-2)*P(-1,2)*Gamma5(-3,1)*Gamma(-2,2,-3))')

FRV2 = Lorentz(name = 'FRV2',
               spins = [ 2, 4, 3 ],
               structure = '-((FC6A(-P(-9,3)**2))*Epsilon(2,-1,-2,-3)*P(-3,3)*P(-1,2)*P(3,3)*Gamma5(-4,1)*Gamma(-2,2,-4))')

FRV3 = Lorentz(name = 'FRV3',
               spins = [ 2, 4, 3 ],
               structure = '-2*(FVND(-P(-9,3)**2))*Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,2)*Identity(2,1)')

FRV4 = Lorentz(name = 'FRV4',
               spins = [ 2, 4, 3 ],
               structure = '(FVND(-P(-9,3)**2))*(P(2,3)*P(3,2)*Gamma5(2,1) - P(-1,2)*P(-1,3)*Gamma5(2,1)*Metric(2,3))')

FRV5 = Lorentz(name = 'FRV5',
               spins = [ 2, 4, 3 ],
               structure = '(FCA5(-P(-9,3)**2))*(P(2,3)*P(3,2)*Identity(2,1) - P(-1,2)*P(-1,3)*Identity(2,1)*Metric(2,3))')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = '(FW1(-P(-9,1)**2))*(P(1,2) - P(1,3))')

VSS2 = Lorentz(name = 'VSS2',
               spins = [ 3, 1, 1 ],
               structure = '(FZ1pi(-P(-9,1)**2))*(P(1,2) - P(1,3))')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

RFS1 = Lorentz(name = 'RFS1',
               spins = [ 4, 2, 1 ],
               structure = '-((FpiNDelta(P(-9,1)**2))*Epsilon(1,-1,-2,-3)*P(-2,1)*P(-1,3)*Gamma5(-4,1)*Gamma(-3,2,-4))')

RFV1 = Lorentz(name = 'RFV1',
               spins = [ 4, 2, 3 ],
               structure = '-((FCA5(-P(-9,3)**2))*Epsilon(1,3,-1,-2)*P(-1,1)*Gamma5(-3,1)*Gamma(-2,2,-3))')

RFV2 = Lorentz(name = 'RFV2',
               spins = [ 4, 2, 3 ],
               structure = '-((FC6A(-P(-9,3)**2))*Epsilon(1,-1,-2,-3)*P(-3,3)*P(-1,1)*P(3,3)*Gamma5(-4,1)*Gamma(-2,2,-4))')

RFV3 = Lorentz(name = 'RFV3',
               spins = [ 4, 2, 3 ],
               structure = '-2*(FVND(-P(-9,3)**2))*Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,1)*Identity(2,1)')

RFV4 = Lorentz(name = 'RFV4',
               spins = [ 4, 2, 3 ],
               structure = '(FVND(-P(-9,3)**2))*(P(1,3)*P(3,1)*Gamma5(2,1) - P(-1,1)*P(-1,3)*Gamma5(2,1)*Metric(1,3))')

RFV5 = Lorentz(name = 'RFV5',
               spins = [ 4, 2, 3 ],
               structure = '(FCA5(-P(-9,3)**2))*(P(1,3)*P(3,1)*Identity(2,1) - P(-1,1)*P(-1,3)*Identity(2,1)*Metric(1,3))')

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
                structure = '(FrhoCT(-P(-9,3)**2))*Gamma(3,2,1)')

FFVS2 = Lorentz(name = 'FFVS2',
                spins = [ 2, 2, 3, 1 ],
                structure = '(FW1(-P(-9,3)**2))*Gamma5(-1,1)*Gamma(3,2,-1)')

FFVS3 = Lorentz(name = 'FFVS3',
                spins = [ 2, 2, 3, 1 ],
                structure = '(FZ1pi(-P(-9,3)**2))*Gamma5(-1,1)*Gamma(3,2,-1)')

FFVS4 = Lorentz(name = 'FFVS4',
                spins = [ 2, 2, 3, 1 ],
                structure = '(FPPpi(-P(-9,3)**2))*(P(-1,3)*P(3,3)*Gamma(-1,2,1) - P(-1,4)*P(3,3)*Gamma(-1,2,1))')

FFVS5 = Lorentz(name = 'FFVS5',
                spins = [ 2, 2, 3, 1 ],
                structure = '(FPPZpi(-P(-9,3)**2))*(P(-1,3)*P(3,3)*Gamma(-1,2,1) - P(-1,4)*P(3,3)*Gamma(-1,2,1))')

FRVS1 = Lorentz(name = 'FRVS1',
                spins = [ 2, 4, 3, 1 ],
                structure = '-((FpiNDelta(P(-9,2)**2))*Epsilon(2,3,-1,-2)*P(-1,2)*Gamma5(-3,1)*Gamma(-2,2,-3))')

VSSS1 = Lorentz(name = 'VSSS1',
                spins = [ 3, 1, 1, 1 ],
                structure = '(FW1(-P(-9,1)**2))*P(1,2)')

VSSS2 = Lorentz(name = 'VSSS2',
                spins = [ 3, 1, 1, 1 ],
                structure = '(FW1(-P(-9,1)**2))*P(1,4)')

VSSS3 = Lorentz(name = 'VSSS3',
                spins = [ 3, 1, 1, 1 ],
                structure = '(FW1(-P(-9,1)**2))*(P(1,2) + P(1,3) - P(1,4))')

VSSS4 = Lorentz(name = 'VSSS4',
                spins = [ 3, 1, 1, 1 ],
                structure = '(FZ1pi(-P(-9,1)**2))*(P(1,2) - P(1,3) - P(1,4))')

VSSS5 = Lorentz(name = 'VSSS5',
                spins = [ 3, 1, 1, 1 ],
                structure = '(FZ1pi(-P(-9,1)**2))*(P(1,2) + P(1,3) + P(1,4))')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

RFVS1 = Lorentz(name = 'RFVS1',
                spins = [ 4, 2, 3, 1 ],
                structure = '-((FpiNDelta(P(-9,1)**2))*Epsilon(1,3,-1,-2)*P(-1,1)*Gamma5(-3,1)*Gamma(-2,2,-3))')

RRSS1 = Lorentz(name = 'RRSS1',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3)')

RRSS2 = Lorentz(name = 'RRSS2',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(2,3)*Gamma(1,2,1) - P(2,4)*Gamma(1,2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) + P(1,3)*Gamma(2,2,1) - P(1,4)*Gamma(2,2,1)')

RRSS3 = Lorentz(name = 'RRSS3',
                spins = [ 4, 4, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(1,-2,1)*Gamma(2,2,-3) + 2*P(-1,3)*Gamma(-1,2,1)*Metric(1,2) - 2*P(-1,4)*Gamma(-1,2,1)*Metric(1,2)')

RRVS1 = Lorentz(name = 'RRVS1',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1)')

RRVS2 = Lorentz(name = 'RRVS2',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(1,-2,-1)*Gamma(2,2,-3)*Gamma(3,-3,-2)')

RRVS3 = Lorentz(name = 'RRVS3',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(3,2,1)*Metric(1,2)')

RRVS4 = Lorentz(name = 'RRVS4',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(3,2,-1)*Metric(1,2)')

RRVS5 = Lorentz(name = 'RRVS5',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + 2*Gamma(3,2,1)*Metric(1,2)')

RRVS6 = Lorentz(name = 'RRVS6',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma(1,-1,1)*Gamma(2,2,-2)*Gamma(3,-2,-1) + Gamma(2,2,1)*Metric(1,3) + Gamma(1,2,1)*Metric(2,3)')

RRVS7 = Lorentz(name = 'RRVS7',
                spins = [ 4, 4, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(2,2,-1)*Metric(1,3) + Gamma5(-1,1)*Gamma(1,2,-1)*Metric(2,3)')

