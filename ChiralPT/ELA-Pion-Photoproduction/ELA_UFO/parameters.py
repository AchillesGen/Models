# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Tue 28 Jul 2026 12:26:20


from __future__ import absolute_import

from .object_library import all_parameters, Parameter


from .function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
fpiN = Parameter(name = 'fpiN',
                 nature = 'external',
                 type = 'real',
                 value = 0.9701623,
                 texname = 'f_{\\text{$\\pi $N}}',
                 lhablock = 'ELABORN',
                 lhacode = [ 1 ])

F1V = Parameter(name = 'F1V',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{F1V}',
                lhablock = 'ELABORN',
                lhacode = [ 2 ])

F1SV = Parameter(name = 'F1SV',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{F1SV}',
                 lhablock = 'ELABORN',
                 lhacode = [ 3 ])

F2V = Parameter(name = 'F2V',
                nature = 'external',
                type = 'real',
                value = 3.7,
                texname = '\\text{F2V}',
                lhablock = 'ELABORN',
                lhacode = [ 4 ])

F2SV = Parameter(name = 'F2SV',
                 nature = 'external',
                 type = 'real',
                 value = -0.0324324,
                 texname = '\\text{F2SV}',
                 lhablock = 'ELABORN',
                 lhacode = [ 5 ])

hN1520 = Parameter(name = 'hN1520',
                   nature = 'external',
                   type = 'real',
                   value = 0.56,
                   texname = '\\text{hN1520}',
                   lhablock = 'ELAD13',
                   lhacode = [ 1 ])

g1pN1520 = Parameter(name = 'g1pN1520',
                     nature = 'external',
                     type = 'real',
                     value = -5.753,
                     texname = '\\text{g1pN1520}',
                     lhablock = 'ELAD13',
                     lhacode = [ 2 ])

g1nN1520 = Parameter(name = 'g1nN1520',
                     nature = 'external',
                     type = 'real',
                     value = 1.217,
                     texname = '\\text{g1nN1520}',
                     lhablock = 'ELAD13',
                     lhacode = [ 3 ])

g2pN1520 = Parameter(name = 'g2pN1520',
                     nature = 'external',
                     type = 'real',
                     value = -0.861,
                     texname = '\\text{g2pN1520}',
                     lhablock = 'ELAD13',
                     lhacode = [ 4 ])

g2nN1520 = Parameter(name = 'g2nN1520',
                     nature = 'external',
                     type = 'real',
                     value = 1.462,
                     texname = '\\text{g2nN1520}',
                     lhablock = 'ELAD13',
                     lhacode = [ 5 ])

hD1700 = Parameter(name = 'hD1700',
                   nature = 'external',
                   type = 'real',
                   value = 0.285,
                   texname = '\\text{hD1700}',
                   lhablock = 'ELAD33',
                   lhacode = [ 1 ])

g1D1700 = Parameter(name = 'g1D1700',
                    nature = 'external',
                    type = 'real',
                    value = -3.513,
                    texname = '\\text{g1D1700}',
                    lhablock = 'ELAD33',
                    lhacode = [ 2 ])

g2D1700 = Parameter(name = 'g2D1700',
                    nature = 'external',
                    type = 'real',
                    value = 1.871,
                    texname = '\\text{g2D1700}',
                    lhablock = 'ELAD33',
                    lhacode = [ 3 ])

LambdaFF = Parameter(name = 'LambdaFF',
                     nature = 'external',
                     type = 'real',
                     value = 1.121,
                     texname = '\\text{LambdaFF}',
                     lhablock = 'ELAFF',
                     lhacode = [ 1 ])

mpiScale = Parameter(name = 'mpiScale',
                     nature = 'external',
                     type = 'real',
                     value = 0.1395673,
                     texname = '\\text{mpiScale}',
                     lhablock = 'ELAMASS',
                     lhacode = [ 1 ])

fpi = Parameter(name = 'fpi',
                nature = 'external',
                type = 'real',
                value = 0.0923,
                texname = 'f_{\\pi }',
                lhablock = 'ELAMASS',
                lhacode = [ 2 ])

hN1440 = Parameter(name = 'hN1440',
                   nature = 'external',
                   type = 'real',
                   value = 0.213,
                   texname = '\\text{hN1440}',
                   lhablock = 'ELAP11',
                   lhacode = [ 1 ])

gpN1440 = Parameter(name = 'gpN1440',
                    nature = 'external',
                    type = 'real',
                    value = 0.255,
                    texname = '\\text{gpN1440}',
                    lhablock = 'ELAP11',
                    lhacode = [ 2 ])

gnN1440 = Parameter(name = 'gnN1440',
                    nature = 'external',
                    type = 'real',
                    value = -0.125,
                    texname = '\\text{gnN1440}',
                    lhablock = 'ELAP11',
                    lhacode = [ 3 ])

hDelta = Parameter(name = 'hDelta',
                   nature = 'external',
                   type = 'real',
                   value = 0.764,
                   texname = '\\text{hDelta}',
                   lhablock = 'ELAP33',
                   lhacode = [ 1 ])

g1Delta = Parameter(name = 'g1Delta',
                    nature = 'external',
                    type = 'real',
                    value = 6.061,
                    texname = '\\text{g1Delta}',
                    lhablock = 'ELAP33',
                    lhacode = [ 2 ])

g2Delta = Parameter(name = 'g2Delta',
                    nature = 'external',
                    type = 'real',
                    value = 2.414,
                    texname = '\\text{g2Delta}',
                    lhablock = 'ELAP33',
                    lhacode = [ 3 ])

hN1535 = Parameter(name = 'hN1535',
                   nature = 'external',
                   type = 'real',
                   value = 0.132,
                   texname = '\\text{hN1535}',
                   lhablock = 'ELAS11A',
                   lhacode = [ 1 ])

gpN1535 = Parameter(name = 'gpN1535',
                    nature = 'external',
                    type = 'real',
                    value = 0.219,
                    texname = '\\text{gpN1535}',
                    lhablock = 'ELAS11A',
                    lhacode = [ 2 ])

gnN1535 = Parameter(name = 'gnN1535',
                    nature = 'external',
                    type = 'real',
                    value = -0.102,
                    texname = '\\text{gnN1535}',
                    lhablock = 'ELAS11A',
                    lhacode = [ 3 ])

hN1650 = Parameter(name = 'hN1650',
                   nature = 'external',
                   type = 'real',
                   value = 0.102,
                   texname = '\\text{hN1650}',
                   lhablock = 'ELAS11B',
                   lhacode = [ 1 ])

gpN1650 = Parameter(name = 'gpN1650',
                    nature = 'external',
                    type = 'real',
                    value = 0.113,
                    texname = '\\text{gpN1650}',
                    lhablock = 'ELAS11B',
                    lhacode = [ 2 ])

gnN1650 = Parameter(name = 'gnN1650',
                    nature = 'external',
                    type = 'real',
                    value = 0.018,
                    texname = '\\text{gnN1650}',
                    lhablock = 'ELAS11B',
                    lhacode = [ 3 ])

hD1620 = Parameter(name = 'hD1620',
                   nature = 'external',
                   type = 'real',
                   value = 0.133,
                   texname = '\\text{hD1620}',
                   lhablock = 'ELAS31',
                   lhacode = [ 1 ])

gD1620 = Parameter(name = 'gD1620',
                   nature = 'external',
                   type = 'real',
                   value = -0.154,
                   texname = '\\text{gD1620}',
                   lhablock = 'ELAS31',
                   lhacode = [ 2 ])

FRhoNN = Parameter(name = 'FRhoNN',
                   nature = 'external',
                   type = 'real',
                   value = 2.6,
                   texname = '\\text{FRhoNN}',
                   lhablock = 'ELAVMESON',
                   lhacode = [ 1 ])

KRho = Parameter(name = 'KRho',
                 nature = 'external',
                 type = 'real',
                 value = 6.3,
                 texname = '\\text{KRho}',
                 lhablock = 'ELAVMESON',
                 lhacode = [ 2 ])

FOmNN = Parameter(name = 'FOmNN',
                  nature = 'external',
                  type = 'real',
                  value = 21.11,
                  texname = '\\text{FOmNN}',
                  lhablock = 'ELAVMESON',
                  lhacode = [ 3 ])

KOm = Parameter(name = 'KOm',
                nature = 'external',
                type = 'real',
                value = -0.17,
                texname = '\\text{KOm}',
                lhablock = 'ELAVMESON',
                lhacode = [ 4 ])

GRho0PiGam = Parameter(name = 'GRho0PiGam',
                       nature = 'external',
                       type = 'real',
                       value = 0.1161,
                       texname = '\\text{GRho0PiGam}',
                       lhablock = 'ELAVMESON',
                       lhacode = [ 5 ])

GRhoCPiGam = Parameter(name = 'GRhoCPiGam',
                       nature = 'external',
                       type = 'real',
                       value = 0.0906,
                       texname = '\\text{GRhoCPiGam}',
                       lhablock = 'ELAVMESON',
                       lhacode = [ 6 ])

GOmPiGam = Parameter(name = 'GOmPiGam',
                     nature = 'external',
                     type = 'real',
                     value = 0.2804,
                     texname = '\\text{GOmPiGam}',
                     lhablock = 'ELAVMESON',
                     lhacode = [ 7 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 137.035999,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

MOm = Parameter(name = 'MOm',
                nature = 'external',
                type = 'real',
                value = 0.78257,
                texname = '\\text{MOm}',
                lhablock = 'MASS',
                lhacode = [ 223 ])

MRho0 = Parameter(name = 'MRho0',
                  nature = 'external',
                  type = 'real',
                  value = 0.7685,
                  texname = '\\text{MRho0}',
                  lhablock = 'MASS',
                  lhacode = [ 113 ])

MRhoP = Parameter(name = 'MRhoP',
                  nature = 'external',
                  type = 'real',
                  value = 0.7665,
                  texname = '\\text{MRhoP}',
                  lhablock = 'MASS',
                  lhacode = [ 213 ])

MPi0 = Parameter(name = 'MPi0',
                 nature = 'external',
                 type = 'real',
                 value = 0.1349766,
                 texname = '\\text{MPi0}',
                 lhablock = 'MASS',
                 lhacode = [ 111 ])

MPiC = Parameter(name = 'MPiC',
                 nature = 'external',
                 type = 'real',
                 value = 0.1395673,
                 texname = '\\text{MPiC}',
                 lhablock = 'MASS',
                 lhacode = [ 211 ])

MN = Parameter(name = 'MN',
               nature = 'external',
               type = 'real',
               value = 0.9389175,
               texname = '\\text{MN}',
               lhablock = 'MASS',
               lhacode = [ 2112 ])

MN1440 = Parameter(name = 'MN1440',
                   nature = 'external',
                   type = 'real',
                   value = 1.385,
                   texname = '\\text{MN1440}',
                   lhablock = 'MASS',
                   lhacode = [ 12112 ])

MN1535 = Parameter(name = 'MN1535',
                   nature = 'external',
                   type = 'real',
                   value = 1.495,
                   texname = '\\text{MN1535}',
                   lhablock = 'MASS',
                   lhacode = [ 22112 ])

MN1650 = Parameter(name = 'MN1650',
                   nature = 'external',
                   type = 'real',
                   value = 1.68,
                   texname = '\\text{MN1650}',
                   lhablock = 'MASS',
                   lhacode = [ 32112 ])

MD1620 = Parameter(name = 'MD1620',
                   nature = 'external',
                   type = 'real',
                   value = 1.59,
                   texname = '\\text{MD1620}',
                   lhablock = 'MASS',
                   lhacode = [ 1112 ])

MDelta = Parameter(name = 'MDelta',
                   nature = 'external',
                   type = 'real',
                   value = 1.209,
                   texname = '\\text{MDelta}',
                   lhablock = 'MASS',
                   lhacode = [ 1114 ])

MN1520 = Parameter(name = 'MN1520',
                   nature = 'external',
                   type = 'real',
                   value = 1.505,
                   texname = '\\text{MN1520}',
                   lhablock = 'MASS',
                   lhacode = [ 1214 ])

MD1700 = Parameter(name = 'MD1700',
                   nature = 'external',
                   type = 'real',
                   value = 1.62,
                   texname = '\\text{MD1700}',
                   lhablock = 'MASS',
                   lhacode = [ 11114 ])

WOm = Parameter(name = 'WOm',
                nature = 'external',
                type = 'real',
                value = 0.00849,
                texname = '\\text{WOm}',
                lhablock = 'DECAY',
                lhacode = [ 223 ])

WRho0 = Parameter(name = 'WRho0',
                  nature = 'external',
                  type = 'real',
                  value = 0.1502,
                  texname = '\\text{WRho0}',
                  lhablock = 'DECAY',
                  lhacode = [ 113 ])

WRhoP = Parameter(name = 'WRhoP',
                  nature = 'external',
                  type = 'real',
                  value = 0.1492,
                  texname = '\\text{WRhoP}',
                  lhablock = 'DECAY',
                  lhacode = [ 213 ])

WN1440p = Parameter(name = 'WN1440p',
                    nature = 'external',
                    type = 'real',
                    value = 0.16,
                    texname = '\\text{WN1440p}',
                    lhablock = 'DECAY',
                    lhacode = [ 12212 ])

WN1440n = Parameter(name = 'WN1440n',
                    nature = 'external',
                    type = 'real',
                    value = 0.16,
                    texname = '\\text{WN1440n}',
                    lhablock = 'DECAY',
                    lhacode = [ 12112 ])

WN1535p = Parameter(name = 'WN1535p',
                    nature = 'external',
                    type = 'real',
                    value = 0.25,
                    texname = '\\text{WN1535p}',
                    lhablock = 'DECAY',
                    lhacode = [ 22212 ])

WN1535n = Parameter(name = 'WN1535n',
                    nature = 'external',
                    type = 'real',
                    value = 0.25,
                    texname = '\\text{WN1535n}',
                    lhablock = 'DECAY',
                    lhacode = [ 22112 ])

WN1650p = Parameter(name = 'WN1650p',
                    nature = 'external',
                    type = 'real',
                    value = 0.15,
                    texname = '\\text{WN1650p}',
                    lhablock = 'DECAY',
                    lhacode = [ 32212 ])

WN1650n = Parameter(name = 'WN1650n',
                    nature = 'external',
                    type = 'real',
                    value = 0.15,
                    texname = '\\text{WN1650n}',
                    lhablock = 'DECAY',
                    lhacode = [ 32112 ])

WD1620PP = Parameter(name = 'WD1620PP',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{WD1620PP}',
                     lhablock = 'DECAY',
                     lhacode = [ 2222 ])

WD1620P = Parameter(name = 'WD1620P',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{WD1620P}',
                    lhablock = 'DECAY',
                    lhacode = [ 2122 ])

WD1620Z = Parameter(name = 'WD1620Z',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{WD1620Z}',
                    lhablock = 'DECAY',
                    lhacode = [ 1212 ])

WD1620M = Parameter(name = 'WD1620M',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{WD1620M}',
                    lhablock = 'DECAY',
                    lhacode = [ 1112 ])

WDeltaPP = Parameter(name = 'WDeltaPP',
                     nature = 'external',
                     type = 'real',
                     value = 0.102,
                     texname = '\\text{WDeltaPP}',
                     lhablock = 'DECAY',
                     lhacode = [ 2224 ])

WDeltaP = Parameter(name = 'WDeltaP',
                    nature = 'external',
                    type = 'real',
                    value = 0.102,
                    texname = '\\text{WDeltaP}',
                    lhablock = 'DECAY',
                    lhacode = [ 2214 ])

WDeltaZ = Parameter(name = 'WDeltaZ',
                    nature = 'external',
                    type = 'real',
                    value = 0.102,
                    texname = '\\text{WDeltaZ}',
                    lhablock = 'DECAY',
                    lhacode = [ 2114 ])

WDeltaM = Parameter(name = 'WDeltaM',
                    nature = 'external',
                    type = 'real',
                    value = 0.102,
                    texname = '\\text{WDeltaM}',
                    lhablock = 'DECAY',
                    lhacode = [ 1114 ])

WN1520p = Parameter(name = 'WN1520p',
                    nature = 'external',
                    type = 'real',
                    value = 0.11,
                    texname = '\\text{WN1520p}',
                    lhablock = 'DECAY',
                    lhacode = [ 2124 ])

WN1520n = Parameter(name = 'WN1520n',
                    nature = 'external',
                    type = 'real',
                    value = 0.11,
                    texname = '\\text{WN1520n}',
                    lhablock = 'DECAY',
                    lhacode = [ 1214 ])

WD1700PP = Parameter(name = 'WD1700PP',
                     nature = 'external',
                     type = 'real',
                     value = 0.25,
                     texname = '\\text{WD1700PP}',
                     lhablock = 'DECAY',
                     lhacode = [ 12224 ])

WD1700P = Parameter(name = 'WD1700P',
                    nature = 'external',
                    type = 'real',
                    value = 0.25,
                    texname = '\\text{WD1700P}',
                    lhablock = 'DECAY',
                    lhacode = [ 12214 ])

WD1700Z = Parameter(name = 'WD1700Z',
                    nature = 'external',
                    type = 'real',
                    value = 0.25,
                    texname = '\\text{WD1700Z}',
                    lhablock = 'DECAY',
                    lhacode = [ 12114 ])

WD1700M = Parameter(name = 'WD1700M',
                    nature = 'external',
                    type = 'real',
                    value = 0.25,
                    texname = '\\text{WD1700M}',
                    lhablock = 'DECAY',
                    lhacode = [ 11114 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

GEDelta = Parameter(name = 'GEDelta',
                    nature = 'internal',
                    type = 'real',
                    value = '-0.5*(g2Delta*(MDelta - MN))/(MDelta + MN)',
                    texname = '\\text{GEDelta}')

GMDelta = Parameter(name = 'GMDelta',
                    nature = 'internal',
                    type = 'real',
                    value = 'g1Delta + (g2Delta*(MDelta - MN))/(2.*(MDelta + MN))',
                    texname = '\\text{GMDelta}')

gSN1440 = Parameter(name = 'gSN1440',
                    nature = 'internal',
                    type = 'real',
                    value = 'gnN1440 + gpN1440',
                    texname = '\\text{gSN1440}')

gVN1440 = Parameter(name = 'gVN1440',
                    nature = 'internal',
                    type = 'real',
                    value = '-gnN1440 + gpN1440',
                    texname = '\\text{gVN1440}')

gSN1535 = Parameter(name = 'gSN1535',
                    nature = 'internal',
                    type = 'real',
                    value = 'gnN1535 + gpN1535',
                    texname = '\\text{gSN1535}')

gVN1535 = Parameter(name = 'gVN1535',
                    nature = 'internal',
                    type = 'real',
                    value = '-gnN1535 + gpN1535',
                    texname = '\\text{gVN1535}')

gSN1650 = Parameter(name = 'gSN1650',
                    nature = 'internal',
                    type = 'real',
                    value = 'gnN1650 + gpN1650',
                    texname = '\\text{gSN1650}')

gVN1650 = Parameter(name = 'gVN1650',
                    nature = 'internal',
                    type = 'real',
                    value = '-gnN1650 + gpN1650',
                    texname = '\\text{gVN1650}')

g1SN1520 = Parameter(name = 'g1SN1520',
                     nature = 'internal',
                     type = 'real',
                     value = 'g1nN1520 + g1pN1520',
                     texname = '\\text{g1SN1520}')

g1VN1520 = Parameter(name = 'g1VN1520',
                     nature = 'internal',
                     type = 'real',
                     value = '-g1nN1520 + g1pN1520',
                     texname = '\\text{g1VN1520}')

g2SN1520 = Parameter(name = 'g2SN1520',
                     nature = 'internal',
                     type = 'real',
                     value = 'g2nN1520 + g2pN1520',
                     texname = '\\text{g2SN1520}')

g2VN1520 = Parameter(name = 'g2VN1520',
                     nature = 'internal',
                     type = 'real',
                     value = '-g2nN1520 + g2pN1520',
                     texname = '\\text{g2VN1520}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

