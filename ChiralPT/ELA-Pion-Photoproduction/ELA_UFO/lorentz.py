# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Tue 28 Jul 2026 12:26:20


from __future__ import absolute_import
from .object_library import all_lorentz, Lorentz

from .function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   from . import form_factors as ForFac 
except ImportError:
   pass


FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,3)*Gamma(-1,2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,3)*Gamma5(-2,1)*Gamma(-1,2,-2)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = '-(P(-1,3)*Gamma(-1,2,-2)*Gamma(3,-2,1)) + P(-1,3)*Gamma(-1,-2,1)*Gamma(3,2,-2)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = '-(P(-1,3)*Gamma5(-2,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)) + P(-1,3)*Gamma5(-2,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)')

FRS1 = Lorentz(name = 'FRS1',
               spins = [ 2, 4, 1 ],
               structure = '-(Epsilon(2,-1,-2,-3)*P(-3,2)*P(-2,3)*Gamma(-1,2,1))')

FRS2 = Lorentz(name = 'FRS2',
               spins = [ 2, 4, 1 ],
               structure = '-(Epsilon(2,-1,-2,-3)*P(-3,2)*P(-2,3)*Gamma5(-4,1)*Gamma(-1,2,-4))')

FRV1 = Lorentz(name = 'FRV1',
               spins = [ 2, 4, 3 ],
               structure = 'Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,2)*Gamma5(2,1) - Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,3)*Gamma5(2,1)')

FRV2 = Lorentz(name = 'FRV2',
               spins = [ 2, 4, 3 ],
               structure = 'Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,2)*Identity(2,1) - Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,3)*Identity(2,1)')

FRV3 = Lorentz(name = 'FRV3',
               spins = [ 2, 4, 3 ],
               structure = 'P(2,3)*P(3,2)*Gamma5(2,1) - P(-1,2)*P(-1,3)*Gamma5(2,1)*Metric(2,3)')

FRV4 = Lorentz(name = 'FRV4',
               spins = [ 2, 4, 3 ],
               structure = 'P(2,3)*P(3,2)*Identity(2,1) - P(-1,2)*P(-1,3)*Identity(2,1)*Metric(2,3)')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)')

RFS1 = Lorentz(name = 'RFS1',
               spins = [ 4, 2, 1 ],
               structure = '-(Epsilon(1,-1,-2,-3)*P(-3,1)*P(-2,3)*Gamma(-1,2,1))')

RFS2 = Lorentz(name = 'RFS2',
               spins = [ 4, 2, 1 ],
               structure = '-(Epsilon(1,-1,-2,-3)*P(-3,1)*P(-2,3)*Gamma5(-4,1)*Gamma(-1,2,-4))')

RFV1 = Lorentz(name = 'RFV1',
               spins = [ 4, 2, 3 ],
               structure = 'Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,1)*Gamma5(2,1) - Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,3)*Gamma5(2,1)')

RFV2 = Lorentz(name = 'RFV2',
               spins = [ 4, 2, 3 ],
               structure = 'Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,1)*Identity(2,1) - Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,3)*Identity(2,1)')

RFV3 = Lorentz(name = 'RFV3',
               spins = [ 4, 2, 3 ],
               structure = 'P(1,3)*P(3,1)*Gamma5(2,1) - P(-1,1)*P(-1,3)*Gamma5(2,1)*Metric(1,3)')

RFV4 = Lorentz(name = 'RFV4',
               spins = [ 4, 2, 3 ],
               structure = 'P(1,3)*P(3,1)*Identity(2,1) - P(-1,1)*P(-1,3)*Identity(2,1)*Metric(1,3)')

FFVS1 = Lorentz(name = 'FFVS1',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

