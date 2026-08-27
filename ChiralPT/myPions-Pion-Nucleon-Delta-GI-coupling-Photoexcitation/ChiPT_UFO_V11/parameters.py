# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Wed 26 Aug 2026 18:42:05


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
AD = Parameter(name = 'AD',
               nature = 'external',
               type = 'real',
               value = -1,
               texname = '\\text{AD}',
               lhablock = 'CHIPTDELTA',
               lhacode = [ 1 ])

gD = Parameter(name = 'gD',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{gD}',
               lhablock = 'CHIPTDELTA',
               lhacode = [ 2 ])

g1D = Parameter(name = 'g1D',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{g1D}',
                lhablock = 'CHIPTDELTA',
                lhacode = [ 3 ])

GamNPi = Parameter(name = 'GamNPi',
                   nature = 'external',
                   type = 'real',
                   value = 0.117,
                   texname = '\\text{GamNPi}',
                   lhablock = 'CHIPTDELTA',
                   lhacode = [ 4 ])

GamNGam = Parameter(name = 'GamNGam',
                    nature = 'external',
                    type = 'real',
                    value = 0.00066,
                    texname = '\\text{GamNGam}',
                    lhablock = 'CHIPTDELTA',
                    lhacode = [ 5 ])

G2overG1 = Parameter(name = 'G2overG1',
                     nature = 'external',
                     type = 'real',
                     value = 0.3982841,
                     texname = '\\text{G2overG1}',
                     lhablock = 'CHIPTDELTA',
                     lhacode = [ 6 ])

LambdaFF = Parameter(name = 'LambdaFF',
                     nature = 'external',
                     type = 'real',
                     value = 1.121,
                     texname = '\\text{LambdaFF}',
                     lhablock = 'CHIPTFF',
                     lhacode = [ 1 ])

MuP = Parameter(name = 'MuP',
                nature = 'external',
                type = 'real',
                value = 2.792847,
                texname = '\\text{MuP}',
                lhablock = 'CHIPTFF',
                lhacode = [ 2 ])

MuN = Parameter(name = 'MuN',
                nature = 'external',
                type = 'real',
                value = -1.913043,
                texname = '\\text{MuN}',
                lhablock = 'CHIPTFF',
                lhacode = [ 3 ])

KLamSq = Parameter(name = 'KLamSq',
                   nature = 'external',
                   type = 'real',
                   value = 0.7174,
                   texname = '\\text{KLamSq}',
                   lhablock = 'CHIPTFF',
                   lhacode = [ 4 ])

KEp1 = Parameter(name = 'KEp1',
                 nature = 'external',
                 type = 'real',
                 value = -0.24,
                 texname = '\\text{KEp1}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 5 ])

KEp2 = Parameter(name = 'KEp2',
                 nature = 'external',
                 type = 'real',
                 value = 10.98,
                 texname = '\\text{KEp2}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 6 ])

KEp3 = Parameter(name = 'KEp3',
                 nature = 'external',
                 type = 'real',
                 value = 12.82,
                 texname = '\\text{KEp3}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 7 ])

KEp4 = Parameter(name = 'KEp4',
                 nature = 'external',
                 type = 'real',
                 value = 21.97,
                 texname = '\\text{KEp4}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 8 ])

KEn1 = Parameter(name = 'KEn1',
                 nature = 'external',
                 type = 'real',
                 value = 1.7,
                 texname = '\\text{KEn1}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 9 ])

KEn2 = Parameter(name = 'KEn2',
                 nature = 'external',
                 type = 'real',
                 value = 3.3,
                 texname = '\\text{KEn2}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 10 ])

KMp1 = Parameter(name = 'KMp1',
                 nature = 'external',
                 type = 'real',
                 value = 0.12,
                 texname = '\\text{KMp1}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 11 ])

KMp2 = Parameter(name = 'KMp2',
                 nature = 'external',
                 type = 'real',
                 value = 10.97,
                 texname = '\\text{KMp2}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 12 ])

KMp3 = Parameter(name = 'KMp3',
                 nature = 'external',
                 type = 'real',
                 value = 18.86,
                 texname = '\\text{KMp3}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 13 ])

KMp4 = Parameter(name = 'KMp4',
                 nature = 'external',
                 type = 'real',
                 value = 6.55,
                 texname = '\\text{KMp4}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 14 ])

KMn1 = Parameter(name = 'KMn1',
                 nature = 'external',
                 type = 'real',
                 value = 2.33,
                 texname = '\\text{KMn1}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 15 ])

KMn2 = Parameter(name = 'KMn2',
                 nature = 'external',
                 type = 'real',
                 value = 14.72,
                 texname = '\\text{KMn2}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 16 ])

KMn3 = Parameter(name = 'KMn3',
                 nature = 'external',
                 type = 'real',
                 value = 24.2,
                 texname = '\\text{KMn3}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 17 ])

KMn4 = Parameter(name = 'KMn4',
                 nature = 'external',
                 type = 'real',
                 value = 84.1,
                 texname = '\\text{KMn4}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 18 ])

AxTcut = Parameter(name = 'AxTcut',
                   nature = 'external',
                   type = 'real',
                   value = 0.1753180641,
                   texname = '\\text{AxTcut}',
                   lhablock = 'CHIPTFF',
                   lhacode = [ 19 ])

AxT0 = Parameter(name = 'AxT0',
                 nature = 'external',
                 type = 'real',
                 value = -0.28,
                 texname = '\\text{AxT0}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 20 ])

AxA0 = Parameter(name = 'AxA0',
                 nature = 'external',
                 type = 'real',
                 value = -0.759,
                 texname = '\\text{AxA0}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 21 ])

AxA1 = Parameter(name = 'AxA1',
                 nature = 'external',
                 type = 'real',
                 value = 2.3,
                 texname = '\\text{AxA1}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 22 ])

AxA2 = Parameter(name = 'AxA2',
                 nature = 'external',
                 type = 'real',
                 value = -0.6,
                 texname = '\\text{AxA2}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 23 ])

AxA3 = Parameter(name = 'AxA3',
                 nature = 'external',
                 type = 'real',
                 value = -3.8,
                 texname = '\\text{AxA3}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 24 ])

AxA4 = Parameter(name = 'AxA4',
                 nature = 'external',
                 type = 'real',
                 value = 2.3,
                 texname = '\\text{AxA4}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 25 ])

AxA5 = Parameter(name = 'AxA5',
                 nature = 'external',
                 type = 'real',
                 value = 2.16,
                 texname = '\\text{AxA5}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 26 ])

AxA6 = Parameter(name = 'AxA6',
                 nature = 'external',
                 type = 'real',
                 value = -0.896,
                 texname = '\\text{AxA6}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 27 ])

AxA7 = Parameter(name = 'AxA7',
                 nature = 'external',
                 type = 'real',
                 value = -1.58,
                 texname = '\\text{AxA7}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 28 ])

AxA8 = Parameter(name = 'AxA8',
                 nature = 'external',
                 type = 'real',
                 value = 0.823,
                 texname = '\\text{AxA8}',
                 lhablock = 'CHIPTFF',
                 lhacode = [ 29 ])

MADeltaSq = Parameter(name = 'MADeltaSq',
                      nature = 'external',
                      type = 'real',
                      value = 1.1025,
                      texname = '\\text{MADeltaSq}',
                      lhablock = 'CHIPTFF',
                      lhacode = [ 30 ])

CA5Norm = Parameter(name = 'CA5Norm',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{CA5Norm}',
                    lhablock = 'CHIPTFF',
                    lhacode = [ 31 ])

Sw2FF = Parameter(name = 'Sw2FF',
                  nature = 'external',
                  type = 'real',
                  value = 0.23863,
                  texname = '\\text{Sw2FF}',
                  lhablock = 'CHIPTFF',
                  lhacode = [ 32 ])

C4AHat = Parameter(name = 'C4AHat',
                   nature = 'external',
                   type = 'real',
                   value = 0.28397656,
                   texname = '\\text{C4AHat}',
                   lhablock = 'CHIPTFF',
                   lhacode = [ 33 ])

MRhoCT = Parameter(name = 'MRhoCT',
                   nature = 'external',
                   type = 'real',
                   value = 0.7758,
                   texname = '\\text{MRhoCT}',
                   lhablock = 'CHIPTFF',
                   lhacode = [ 34 ])

MV2ND = Parameter(name = 'MV2ND',
                  nature = 'external',
                  type = 'real',
                  value = 0.71,
                  texname = '\\text{MV2ND}',
                  lhablock = 'CHIPTFF',
                  lhacode = [ 35 ])

PPNorm = Parameter(name = 'PPNorm',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{PPNorm}',
                   lhablock = 'CHIPTFF',
                   lhacode = [ 37 ])

fPi = Parameter(name = 'fPi',
                nature = 'external',
                type = 'real',
                value = 0.093,
                texname = '\\text{fPi}',
                lhablock = 'CHIPTPION',
                lhacode = [ 1 ])

ga = Parameter(name = 'ga',
               nature = 'external',
               type = 'real',
               value = 1.271,
               texname = '\\text{ga}',
               lhablock = 'CHIPTPION',
               lhacode = [ 2 ])

cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 137.035999,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MNucleon = Parameter(name = 'MNucleon',
                     nature = 'external',
                     type = 'real',
                     value = 0.938272,
                     texname = '\\text{MNucleon}',
                     lhablock = 'MASS',
                     lhacode = [ 2112 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MPi0 = Parameter(name = 'MPi0',
                 nature = 'external',
                 type = 'real',
                 value = 0.1349768,
                 texname = '\\text{MPi0}',
                 lhablock = 'MASS',
                 lhacode = [ 111 ])

MPiP = Parameter(name = 'MPiP',
                 nature = 'external',
                 type = 'real',
                 value = 0.1395704,
                 texname = '\\text{MPiP}',
                 lhablock = 'MASS',
                 lhacode = [ 211 ])

MEta = Parameter(name = 'MEta',
                 nature = 'external',
                 type = 'real',
                 value = 0.547862,
                 texname = '\\text{MEta}',
                 lhablock = 'MASS',
                 lhacode = [ 221 ])

MK0 = Parameter(name = 'MK0',
                nature = 'external',
                type = 'real',
                value = 0.497611,
                texname = '\\text{MK0}',
                lhablock = 'MASS',
                lhacode = [ 311 ])

MKp = Parameter(name = 'MKp',
                nature = 'external',
                type = 'real',
                value = 0.493677,
                texname = '\\text{MKp}',
                lhablock = 'MASS',
                lhacode = [ 321 ])

MDelta = Parameter(name = 'MDelta',
                   nature = 'external',
                   type = 'real',
                   value = 1.209,
                   texname = '\\text{MDelta}',
                   lhablock = 'MASS',
                   lhacode = [ 1114 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WPi0 = Parameter(name = 'WPi0',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WPi0}',
                 lhablock = 'DECAY',
                 lhacode = [ 111 ])

WPiP = Parameter(name = 'WPiP',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WPiP}',
                 lhablock = 'DECAY',
                 lhacode = [ 211 ])

WEta = Parameter(name = 'WEta',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{WEta}',
                 lhablock = 'DECAY',
                 lhacode = [ 221 ])

WK0 = Parameter(name = 'WK0',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{WK0}',
                lhablock = 'DECAY',
                lhacode = [ 311 ])

WKp = Parameter(name = 'WKp',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{WKp}',
                lhablock = 'DECAY',
                lhacode = [ 321 ])

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

WDelta0 = Parameter(name = 'WDelta0',
                    nature = 'external',
                    type = 'real',
                    value = 0.102,
                    texname = '\\text{WDelta0}',
                    lhablock = 'DECAY',
                    lhacode = [ 2114 ])

WDeltaM = Parameter(name = 'WDeltaM',
                    nature = 'external',
                    type = 'real',
                    value = 0.102,
                    texname = '\\text{WDeltaM}',
                    lhablock = 'DECAY',
                    lhacode = [ 1114 ])

MPi = Parameter(name = 'MPi',
                nature = 'internal',
                type = 'real',
                value = 'MPi0',
                texname = '\\text{MPi}')

g2D = Parameter(name = 'g2D',
                nature = 'internal',
                type = 'real',
                value = 'AD*g1D',
                texname = '\\text{g2D}')

g3D = Parameter(name = 'g3D',
                nature = 'internal',
                type = 'real',
                value = '((-1 - 2*AD - 3*AD**2)*g1D)/2.',
                texname = '\\text{g3D}')

kPiDelta = Parameter(name = 'kPiDelta',
                     nature = 'internal',
                     type = 'real',
                     value = 'cmath.sqrt(-4*MNucleon**2*MPiP**2 + (MDelta**2 - MNucleon**2 - MPiP**2)**2)/(2.*MDelta)',
                     texname = '\\text{kPiDelta}')

kGamDelta = Parameter(name = 'kGamDelta',
                      nature = 'internal',
                      type = 'real',
                      value = '(MDelta**2 - MNucleon**2)/(2.*MDelta)',
                      texname = '\\text{kGamDelta}')

ztilde = Parameter(name = 'ztilde',
                   nature = 'internal',
                   type = 'real',
                   value = '(1 + 3*AD)/2.',
                   texname = '\\text{ztilde}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

Vud = Parameter(name = 'Vud',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(cabi)',
                texname = 'V_{\\text{ud}}')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

hD = Parameter(name = 'hD',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(3*cmath.pi)*cmath.sqrt((fPi**2*GamNPi*MDelta)/(kPiDelta**3*(MNucleon + cmath.sqrt(kPiDelta**2 + MNucleon**2))))',
               texname = '\\text{hD}')

xEMDelta = Parameter(name = 'xEMDelta',
                     nature = 'internal',
                     type = 'real',
                     value = 'kGamDelta/(MNucleon + (MDelta**2 + MNucleon**2)/(2.*MDelta))',
                     texname = '\\text{xEMDelta}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

C4AN = Parameter(name = 'C4AN',
                 nature = 'internal',
                 type = 'real',
                 value = 'C4AHat*hD',
                 texname = '\\text{C4AN}')

C6AN = Parameter(name = 'C6AN',
                 nature = 'internal',
                 type = 'real',
                 value = 'hD',
                 texname = '\\text{C6AN}')

G1 = Parameter(name = 'G1',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(2*cmath.pi)*cmath.sqrt((GamNGam*MNucleon**2)/(ee**2*kGamDelta**3*(1 + G2overG1*xEMDelta + G2overG1**2*xEMDelta**2)))',
               texname = '\\text{G1}')

Kappa = Parameter(name = 'Kappa',
                  nature = 'internal',
                  type = 'real',
                  value = '(3*ee)/(2.*MNucleon*(MDelta + MNucleon))',
                  texname = '\\text{Kappa}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

G2 = Parameter(name = 'G2',
               nature = 'internal',
               type = 'real',
               value = 'G1*G2overG1',
               texname = '\\text{G2}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

g2 = Parameter(name = 'g2',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

