# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Wed 26 Nov 2025 10:10:30


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.5*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(ee*complex(0,1))/2.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(AD*ee*complex(0,1))',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = 'AD*ee*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-2*AD*ee*complex(0,1)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(-3*AD**2*ee*complex(0,1))/2.',
                order = {'QED':3})

GC_9 = Coupling(name = 'GC_9',
                value = '(3*AD**2*ee*complex(0,1))/2.',
                order = {'QED':3})

GC_10 = Coupling(name = 'GC_10',
                 value = '-3*AD**2*ee*complex(0,1)',
                 order = {'QED':3})

GC_11 = Coupling(name = 'GC_11',
                 value = '-2*ee**2*complex(0,1)',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '2*ee**2*complex(0,1)',
                 order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '(ee**2*complex(0,1))/(2.*cw)',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-0.125*complex(0,1)/fPi**2',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)/(8.*fPi**2)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-0.25*complex(0,1)/fPi**2',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)/(4.*fPi**2)',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(-3*complex(0,1))/(8.*fPi**2)',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(3*complex(0,1))/(8.*fPi**2)',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(complex(0,1)/fPi**2)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(-2*complex(0,1))/fPi**2',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-0.25*(complex(0,1)*cmath.sqrt(1.5))/fPi**2',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-0.5*complex(0,1)/(fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = 'complex(0,1)/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-0.25*(AD*complex(0,1))/fPi**2',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(AD*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(-3*AD*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(3*AD*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-0.5*(AD*complex(0,1)*cmath.sqrt(1.5))/fPi**2',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(AD*complex(0,1)*cmath.sqrt(1.5))/(2.*fPi**2)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-((AD*complex(0,1))/(fPi**2*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(AD*complex(0,1))/(fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(-3*AD**2*complex(0,1))/(8.*fPi**2)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(3*AD**2*complex(0,1))/(8.*fPi**2)',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(-9*AD**2*complex(0,1))/(8.*fPi**2)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(9*AD**2*complex(0,1))/(8.*fPi**2)',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(-3*AD**2*complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2)',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(3*AD**2*complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2)',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(-3*AD**2*complex(0,1))/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(3*AD**2*complex(0,1))/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-0.25*(ee*complex(0,1))/fPi**2',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ee*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-0.5*(ee*complex(0,1))/fPi**2',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(ee*complex(0,1))/(2.*fPi**2)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(-3*ee*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(3*ee*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-0.25*(ee*complex(0,1)*cmath.sqrt(1.5))/fPi**2',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-0.5*(ee*complex(0,1))/(fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee*complex(0,1))/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-0.5*(AD*ee*complex(0,1))/fPi**2',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(AD*ee*complex(0,1))/(2.*fPi**2)',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(-3*AD*ee*complex(0,1))/(2.*fPi**2)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(3*AD*ee*complex(0,1))/(2.*fPi**2)',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '-0.5*(AD*ee*complex(0,1)*cmath.sqrt(1.5))/fPi**2',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((AD*ee*complex(0,1))/(fPi**2*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(-3*AD**2*ee*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':3})

GC_58 = Coupling(name = 'GC_58',
                 value = '(3*AD**2*ee*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':3})

GC_59 = Coupling(name = 'GC_59',
                 value = '(-9*AD**2*ee*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':3})

GC_60 = Coupling(name = 'GC_60',
                 value = '(9*AD**2*ee*complex(0,1))/(4.*fPi**2)',
                 order = {'QED':3})

GC_61 = Coupling(name = 'GC_61',
                 value = '(-3*AD**2*ee*complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2)',
                 order = {'QED':3})

GC_62 = Coupling(name = 'GC_62',
                 value = '(-3*AD**2*ee*complex(0,1))/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'QED':3})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(ee**2/(cw*fPi))',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-0.5*ee**2/(cw*fPi)',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = 'ee**2/(2.*cw*fPi)',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = 'ee**2/(cw*fPi)',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-0.5*(ee**2*fPi)/cw',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee**2*fPi)/(2.*cw)',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-0.5*g1D/fPi',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-0.16666666666666666*g1D/fPi',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = 'g1D/(6.*fPi)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = 'g1D/(2.*fPi)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-0.3333333333333333*(g1D*cmath.sqrt(2))/fPi',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(g1D/(fPi*cmath.sqrt(6)))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-0.3333333333333333*(ee*g1D*cmath.sqrt(2))/fPi',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(ee*g1D*cmath.sqrt(2))/(3.*fPi)',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((ee*g1D)/(fPi*cmath.sqrt(6)))',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(ee*g1D)/(fPi*cmath.sqrt(6))',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-0.5*g2D/fPi',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-0.16666666666666666*g2D/fPi',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = 'g2D/(6.*fPi)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = 'g2D/(2.*fPi)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-0.3333333333333333*(g2D*cmath.sqrt(2))/fPi',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(g2D/(fPi*cmath.sqrt(6)))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-0.3333333333333333*(ee*g2D*cmath.sqrt(2))/fPi',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '(ee*g2D*cmath.sqrt(2))/(3.*fPi)',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((ee*g2D)/(fPi*cmath.sqrt(6)))',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ee*g2D)/(fPi*cmath.sqrt(6))',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '-0.5*g3D/fPi',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-0.16666666666666666*g3D/fPi',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = 'g3D/(6.*fPi)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'g3D/(2.*fPi)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(g3D*cmath.sqrt(2))/(3.*fPi)',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = 'g3D/(fPi*cmath.sqrt(6))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-0.3333333333333333*(ee*g3D*cmath.sqrt(2))/fPi',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*g3D*cmath.sqrt(2))/(3.*fPi)',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((ee*g3D)/(fPi*cmath.sqrt(6)))',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee*g3D)/(fPi*cmath.sqrt(6))',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '-0.5*ga/fPi',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = 'ga/(2.*fPi)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(ga/(fPi*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((ee*ga)/(fPi*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '(ee*ga)/(fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(gD/fPi)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = 'gD/fPi',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(gD*cmath.sqrt(0.6666666666666666))/fPi',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(gD/(fPi*cmath.sqrt(3)))',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = 'gD/(fPi*cmath.sqrt(3))',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((ee*gD)/fPi)',
                  order = {'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '(ee*gD)/fPi',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((ee*gD)/(fPi*cmath.sqrt(3)))',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '(ee*gD)/(fPi*cmath.sqrt(3))',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-6*complex(0,1)*lam',
                  order = {'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((complex(0,1)*gDGI)/(fPi*MDelta))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(complex(0,1)*gDGI)/(fPi*MDelta)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(complex(0,1)*gDGI*cmath.sqrt(0.6666666666666666))/(fPi*MDelta)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((complex(0,1)*gDGI)/(fPi*MDelta*cmath.sqrt(3)))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(complex(0,1)*gDGI)/(fPi*MDelta*cmath.sqrt(3))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((ee*complex(0,1)*gDGI)/(fPi*MDelta))',
                  order = {'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(ee*complex(0,1)*gDGI)/(fPi*MDelta)',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((ee*complex(0,1)*gDGI)/(fPi*MDelta*cmath.sqrt(3)))',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '(ee*complex(0,1)*gDGI)/(fPi*MDelta*cmath.sqrt(3))',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '(ee**2*complex(0,1))/(2.*fPi**2*sw**2)',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(ee**2*complex(0,1))/(fPi**2*sw**2)',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '(3*ee**2*complex(0,1))/(2.*fPi**2*sw**2)',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-0.5*(ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-0.25*(ee*complex(0,1)*cmath.sqrt(1.5))/sw',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-0.5*(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(ee*complex(0,1))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-0.5*(AD*ee*complex(0,1)*cmath.sqrt(1.5))/sw',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((AD*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(-3*AD**2*ee*complex(0,1)*cmath.sqrt(1.5))/(4.*sw)',
                  order = {'QED':3})

GC_136 = Coupling(name = 'GC_136',
                  value = '(-3*AD**2*ee*complex(0,1))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':3})

GC_137 = Coupling(name = 'GC_137',
                  value = '-0.5*(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-0.5*(ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-0.0625*(ee*complex(0,1))/(fPi**2*sw)',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(ee*complex(0,1))/(16.*fPi**2*sw)',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-0.125*(ee*complex(0,1))/(fPi**2*sw)',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(ee*complex(0,1))/(8.*fPi**2*sw)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(-3*ee*complex(0,1))/(16.*fPi**2*sw)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(3*ee*complex(0,1))/(16.*fPi**2*sw)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(ee*complex(0,1)*cmath.sqrt(1.5))/(8.*fPi**2*sw)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-0.25*(ee*complex(0,1)*cmath.sqrt(1.5))/(fPi**2*sw)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(ee*complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2*sw)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-0.25*(ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(ee*complex(0,1))/(4.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-0.5*(ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(ee*complex(0,1))/(2.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-0.125*(AD*ee*complex(0,1))/(fPi**2*sw)',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '(AD*ee*complex(0,1))/(8.*fPi**2*sw)',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '(-3*AD*ee*complex(0,1))/(8.*fPi**2*sw)',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '(3*AD*ee*complex(0,1))/(8.*fPi**2*sw)',
                  order = {'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '(AD*ee*complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2*sw)',
                  order = {'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '-0.5*(AD*ee*complex(0,1)*cmath.sqrt(1.5))/(fPi**2*sw)',
                  order = {'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '(AD*ee*complex(0,1)*cmath.sqrt(1.5))/(2.*fPi**2*sw)',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '(AD*ee*complex(0,1))/(2.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((AD*ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '(AD*ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '(-3*AD**2*ee*complex(0,1))/(16.*fPi**2*sw)',
                  order = {'QED':3})

GC_163 = Coupling(name = 'GC_163',
                  value = '(3*AD**2*ee*complex(0,1))/(16.*fPi**2*sw)',
                  order = {'QED':3})

GC_164 = Coupling(name = 'GC_164',
                  value = '(-9*AD**2*ee*complex(0,1))/(16.*fPi**2*sw)',
                  order = {'QED':3})

GC_165 = Coupling(name = 'GC_165',
                  value = '(9*AD**2*ee*complex(0,1))/(16.*fPi**2*sw)',
                  order = {'QED':3})

GC_166 = Coupling(name = 'GC_166',
                  value = '(3*AD**2*ee*complex(0,1)*cmath.sqrt(1.5))/(8.*fPi**2*sw)',
                  order = {'QED':3})

GC_167 = Coupling(name = 'GC_167',
                  value = '(-3*AD**2*ee*complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2*sw)',
                  order = {'QED':3})

GC_168 = Coupling(name = 'GC_168',
                  value = '(3*AD**2*ee*complex(0,1)*cmath.sqrt(1.5))/(4.*fPi**2*sw)',
                  order = {'QED':3})

GC_169 = Coupling(name = 'GC_169',
                  value = '(3*AD**2*ee*complex(0,1))/(4.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':3})

GC_170 = Coupling(name = 'GC_170',
                  value = '(-3*AD**2*ee*complex(0,1))/(2.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':3})

GC_171 = Coupling(name = 'GC_171',
                  value = '(3*AD**2*ee*complex(0,1))/(2.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':3})

GC_172 = Coupling(name = 'GC_172',
                  value = '(-3*ee)/(8.*fPi*sw)',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-0.25*ee/(fPi*sw)',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-0.125*ee/(fPi*sw)',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = 'ee/(8.*fPi*sw)',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = 'ee/(4.*fPi*sw)',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '(3*ee)/(8.*fPi*sw)',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = 'ee/(2.*fPi*sw)',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = 'ee/(fPi*sw)',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-0.25*(ee*cmath.sqrt(1.5))/(fPi*sw)',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(ee*cmath.sqrt(1.5))/(4.*fPi*sw)',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-0.5*ee/(fPi*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = 'ee/(2.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '(-3*AD*ee)/(4.*fPi*sw)',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '-0.25*(AD*ee)/(fPi*sw)',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '(AD*ee)/(4.*fPi*sw)',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(3*AD*ee)/(4.*fPi*sw)',
                  order = {'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '-0.5*(AD*ee*cmath.sqrt(1.5))/(fPi*sw)',
                  order = {'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(AD*ee*cmath.sqrt(1.5))/(2.*fPi*sw)',
                  order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((AD*ee)/(fPi*sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '(AD*ee)/(fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '(-9*AD**2*ee)/(8.*fPi*sw)',
                  order = {'QED':3})

GC_193 = Coupling(name = 'GC_193',
                  value = '(-3*AD**2*ee)/(8.*fPi*sw)',
                  order = {'QED':3})

GC_194 = Coupling(name = 'GC_194',
                  value = '(3*AD**2*ee)/(8.*fPi*sw)',
                  order = {'QED':3})

GC_195 = Coupling(name = 'GC_195',
                  value = '(9*AD**2*ee)/(8.*fPi*sw)',
                  order = {'QED':3})

GC_196 = Coupling(name = 'GC_196',
                  value = '(-3*AD**2*ee*cmath.sqrt(1.5))/(4.*fPi*sw)',
                  order = {'QED':3})

GC_197 = Coupling(name = 'GC_197',
                  value = '(3*AD**2*ee*cmath.sqrt(1.5))/(4.*fPi*sw)',
                  order = {'QED':3})

GC_198 = Coupling(name = 'GC_198',
                  value = '(-3*AD**2*ee)/(2.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':3})

GC_199 = Coupling(name = 'GC_199',
                  value = '(3*AD**2*ee)/(2.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':3})

GC_200 = Coupling(name = 'GC_200',
                  value = '-0.25*(cw*ee*cmath.sqrt(1.5))/(fPi*sw)',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(-3*AD**2*cw*ee)/(2.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':3})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(ee**2/(fPi*sw))',
                  order = {'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '-0.5*ee**2/(fPi*sw)',
                  order = {'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = 'ee**2/(2.*fPi*sw)',
                  order = {'QED':2})

GC_205 = Coupling(name = 'GC_205',
                  value = 'ee**2/(fPi*sw)',
                  order = {'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '-0.5*(ee**2*fPi)/sw',
                  order = {'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(ee**2*fPi)/(2.*sw)',
                  order = {'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(ee*complex(0,1)*g1D)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(ee*complex(0,1)*g1D)/(2.*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '-0.041666666666666664*(ee*complex(0,1)*g1D)/(fPi**2*sw)',
                  order = {'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(ee*complex(0,1)*g1D)/(24.*fPi**2*sw)',
                  order = {'QED':2})

GC_212 = Coupling(name = 'GC_212',
                  value = '-0.125*(ee*complex(0,1)*g1D)/(fPi**2*sw)',
                  order = {'QED':2})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ee*complex(0,1)*g1D)/(8.*fPi**2*sw)',
                  order = {'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '-0.16666666666666666*(ee*complex(0,1)*g1D)/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '-0.3333333333333333*(ee*complex(0,1)*g1D)/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee*complex(0,1)*g1D)/(3.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_217 = Coupling(name = 'GC_217',
                  value = '-0.25*(ee*complex(0,1)*g1D)/(fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '-0.5*(ee*complex(0,1)*g1D)/(fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '(ee*complex(0,1)*g1D)/(2.*fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '-0.25*(ee*g1D)/(fPi*sw)',
                  order = {'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '-0.08333333333333333*(ee*g1D)/(fPi*sw)',
                  order = {'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '(ee*g1D)/(12.*fPi*sw)',
                  order = {'QED':2})

GC_223 = Coupling(name = 'GC_223',
                  value = '(ee*g1D)/(4.*fPi*sw)',
                  order = {'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '-0.3333333333333333*(ee*g1D)/(fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_225 = Coupling(name = 'GC_225',
                  value = '(ee*g1D)/(3.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_226 = Coupling(name = 'GC_226',
                  value = '-0.5*(ee*g1D)/(fPi*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_227 = Coupling(name = 'GC_227',
                  value = '(ee*g1D)/(2.*fPi*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_228 = Coupling(name = 'GC_228',
                  value = '(ee*complex(0,1)*g2D)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_229 = Coupling(name = 'GC_229',
                  value = '(ee*complex(0,1)*g2D)/(2.*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_230 = Coupling(name = 'GC_230',
                  value = '-0.041666666666666664*(ee*complex(0,1)*g2D)/(fPi**2*sw)',
                  order = {'QED':2})

GC_231 = Coupling(name = 'GC_231',
                  value = '(ee*complex(0,1)*g2D)/(24.*fPi**2*sw)',
                  order = {'QED':2})

GC_232 = Coupling(name = 'GC_232',
                  value = '-0.125*(ee*complex(0,1)*g2D)/(fPi**2*sw)',
                  order = {'QED':2})

GC_233 = Coupling(name = 'GC_233',
                  value = '(ee*complex(0,1)*g2D)/(8.*fPi**2*sw)',
                  order = {'QED':2})

GC_234 = Coupling(name = 'GC_234',
                  value = '-0.16666666666666666*(ee*complex(0,1)*g2D)/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_235 = Coupling(name = 'GC_235',
                  value = '-0.3333333333333333*(ee*complex(0,1)*g2D)/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '(ee*complex(0,1)*g2D)/(3.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_237 = Coupling(name = 'GC_237',
                  value = '-0.25*(ee*complex(0,1)*g2D)/(fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_238 = Coupling(name = 'GC_238',
                  value = '-0.5*(ee*complex(0,1)*g2D)/(fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_239 = Coupling(name = 'GC_239',
                  value = '(ee*complex(0,1)*g2D)/(2.*fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_240 = Coupling(name = 'GC_240',
                  value = '-0.25*(ee*g2D)/(fPi*sw)',
                  order = {'QED':2})

GC_241 = Coupling(name = 'GC_241',
                  value = '-0.08333333333333333*(ee*g2D)/(fPi*sw)',
                  order = {'QED':2})

GC_242 = Coupling(name = 'GC_242',
                  value = '(ee*g2D)/(12.*fPi*sw)',
                  order = {'QED':2})

GC_243 = Coupling(name = 'GC_243',
                  value = '(ee*g2D)/(4.*fPi*sw)',
                  order = {'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '-0.3333333333333333*(ee*g2D)/(fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_245 = Coupling(name = 'GC_245',
                  value = '(ee*g2D)/(3.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_246 = Coupling(name = 'GC_246',
                  value = '-0.5*(ee*g2D)/(fPi*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_247 = Coupling(name = 'GC_247',
                  value = '(ee*g2D)/(2.*fPi*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '-0.3333333333333333*(ee*complex(0,1)*g3D)/(sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '-0.5*(ee*complex(0,1)*g3D)/(sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = '-0.041666666666666664*(ee*complex(0,1)*g3D)/(fPi**2*sw)',
                  order = {'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '(ee*complex(0,1)*g3D)/(24.*fPi**2*sw)',
                  order = {'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '-0.125*(ee*complex(0,1)*g3D)/(fPi**2*sw)',
                  order = {'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(ee*complex(0,1)*g3D)/(8.*fPi**2*sw)',
                  order = {'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '(ee*complex(0,1)*g3D)/(6.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '-0.3333333333333333*(ee*complex(0,1)*g3D)/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(ee*complex(0,1)*g3D)/(3.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(ee*complex(0,1)*g3D)/(4.*fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '-0.5*(ee*complex(0,1)*g3D)/(fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(ee*complex(0,1)*g3D)/(2.*fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '-0.25*(ee*g3D)/(fPi*sw)',
                  order = {'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '-0.08333333333333333*(ee*g3D)/(fPi*sw)',
                  order = {'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '(ee*g3D)/(12.*fPi*sw)',
                  order = {'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '(ee*g3D)/(4.*fPi*sw)',
                  order = {'QED':2})

GC_264 = Coupling(name = 'GC_264',
                  value = '-0.3333333333333333*(ee*g3D)/(fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_265 = Coupling(name = 'GC_265',
                  value = '(ee*g3D)/(3.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_266 = Coupling(name = 'GC_266',
                  value = '-0.5*(ee*g3D)/(fPi*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '(ee*g3D)/(2.*fPi*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_268 = Coupling(name = 'GC_268',
                  value = '-0.5*(ee*complex(0,1)*ga)/(sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '-0.125*(ee*complex(0,1)*ga)/(fPi**2*sw)',
                  order = {'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '(ee*complex(0,1)*ga)/(8.*fPi**2*sw)',
                  order = {'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '(ee*complex(0,1)*ga)/(4.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '-0.5*(ee*complex(0,1)*ga)/(fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(ee*complex(0,1)*ga)/(2.*fPi**2*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '-0.25*(ee*ga)/(fPi*sw)',
                  order = {'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '(ee*ga)/(4.*fPi*sw)',
                  order = {'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '-0.5*(ee*ga)/(fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '(ee*ga)/(2.*fPi*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '-0.5*(ee*complex(0,1)*gD)/sw',
                  order = {'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '(ee*complex(0,1)*gD)/(2.*sw)',
                  order = {'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '-0.5*(ee*complex(0,1)*gD)/(sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(ee*complex(0,1)*gD)/(2.*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '-0.25*(ee*complex(0,1)*gD)/(fPi**2*sw)',
                  order = {'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(ee*complex(0,1)*gD)/(4.*fPi**2*sw)',
                  order = {'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '-0.5*(ee*complex(0,1)*gD)/(fPi**2*sw)',
                  order = {'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '(ee*complex(0,1)*gD)/(2.*fPi**2*sw)',
                  order = {'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '-0.25*(ee*complex(0,1)*gD)/(fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '(ee*complex(0,1)*gD)/(4.*fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = '-0.5*(ee*complex(0,1)*gD)/(fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '(ee*complex(0,1)*gD)/(2.*fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '-0.5*(ee*complex(0,1)*gD)/(fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = '-0.5*(ee*gD)/(fPi*sw)',
                  order = {'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = '(ee*gD)/(2.*fPi*sw)',
                  order = {'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '-0.5*(ee*gD)/(fPi*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '(ee*gD)/(2.*fPi*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '-((ee*gD)/(fPi*sw*cmath.sqrt(6)))',
                  order = {'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '(ee*gD)/(fPi*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '-0.5*(ee*gDGI)/(MDelta*sw)',
                  order = {'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = '(ee*gDGI)/(2.*MDelta*sw)',
                  order = {'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '-0.5*(ee*gDGI)/(MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(ee*gDGI)/(2.*MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '-0.5*(ee*gDGI)/(fPi**2*MDelta*sw)',
                  order = {'QED':2})

GC_302 = Coupling(name = 'GC_302',
                  value = '-0.25*(ee*gDGI)/(fPi**2*MDelta*sw)',
                  order = {'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '(ee*gDGI)/(4.*fPi**2*MDelta*sw)',
                  order = {'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '(ee*gDGI)/(2.*fPi**2*MDelta*sw)',
                  order = {'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '-0.5*(ee*gDGI)/(fPi**2*MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '-0.25*(ee*gDGI)/(fPi**2*MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '(ee*gDGI)/(4.*fPi**2*MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '(ee*gDGI)/(2.*fPi**2*MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '-0.5*(ee*gDGI)/(fPi**2*MDelta*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_310 = Coupling(name = 'GC_310',
                  value = '-0.5*(ee*complex(0,1)*gDGI)/(fPi*MDelta*sw)',
                  order = {'QED':2})

GC_311 = Coupling(name = 'GC_311',
                  value = '(ee*complex(0,1)*gDGI)/(2.*fPi*MDelta*sw)',
                  order = {'QED':2})

GC_312 = Coupling(name = 'GC_312',
                  value = '-0.5*(ee*complex(0,1)*gDGI)/(fPi*MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '(ee*complex(0,1)*gDGI)/(2.*fPi*MDelta*sw*cmath.sqrt(3))',
                  order = {'QED':2})

GC_314 = Coupling(name = 'GC_314',
                  value = '-((ee*complex(0,1)*gDGI)/(fPi*MDelta*sw*cmath.sqrt(6)))',
                  order = {'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = '(ee*complex(0,1)*gDGI)/(fPi*MDelta*sw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '-0.25*(ee*sw*cmath.sqrt(1.5))/(cw*fPi)',
                  order = {'QED':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '(-3*AD**2*ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':3})

GC_319 = Coupling(name = 'GC_319',
                  value = '(3*cw*ee*complex(0,1))/(8.*sw) - (ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '(cw*ee*complex(0,1))/(8.*sw) + (ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '-0.25*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '-0.125*(cw*ee*complex(0,1))/sw + (3*ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '(-3*cw*ee*complex(0,1))/(8.*sw) + (5*ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '(cw*ee*complex(0,1))/(4.*sw) - (3*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'QED':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(3*AD*cw*ee*complex(0,1))/(4.*sw) - (AD*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '(AD*cw*ee*complex(0,1))/(4.*sw) + (AD*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'QED':2})

GC_329 = Coupling(name = 'GC_329',
                  value = '-0.25*(AD*cw*ee*complex(0,1))/sw + (3*AD*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '(-3*AD*cw*ee*complex(0,1))/(4.*sw) + (5*AD*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '(9*AD**2*cw*ee*complex(0,1))/(8.*sw) - (3*AD**2*ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':3})

GC_332 = Coupling(name = 'GC_332',
                  value = '(3*AD**2*cw*ee*complex(0,1))/(8.*sw) + (3*AD**2*ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':3})

GC_333 = Coupling(name = 'GC_333',
                  value = '(-3*AD**2*cw*ee*complex(0,1))/(8.*sw) + (9*AD**2*ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':3})

GC_334 = Coupling(name = 'GC_334',
                  value = '(-9*AD**2*cw*ee*complex(0,1))/(8.*sw) + (15*AD**2*ee*complex(0,1)*sw)/(8.*cw)',
                  order = {'QED':3})

GC_335 = Coupling(name = 'GC_335',
                  value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                  order = {'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(cw*ee*complex(0,1))/(8.*fPi**2*sw) - (ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '-0.125*(cw*ee*complex(0,1))/(fPi**2*sw) + (ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '(cw*ee*complex(0,1))/(4.*fPi**2*sw) - (ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                  order = {'QED':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '-0.25*(cw*ee*complex(0,1))/(fPi**2*sw) + (ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                  order = {'QED':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '(3*cw*ee*complex(0,1))/(8.*fPi**2*sw) - (3*ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '(-3*cw*ee*complex(0,1))/(8.*fPi**2*sw) + (3*ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '-0.125*(cw*ee*complex(0,1)*cmath.sqrt(1.5))/(fPi**2*sw) + (ee*complex(0,1)*sw*cmath.sqrt(1.5))/(8.*cw*fPi**2)',
                  order = {'QED':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(cw*ee*complex(0,1))/(4.*fPi**2*sw*cmath.sqrt(2)) - (ee*complex(0,1)*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '-0.25*(cw*ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '(AD*cw*ee*complex(0,1))/(4.*fPi**2*sw) - (AD*ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '-0.25*(AD*cw*ee*complex(0,1))/(fPi**2*sw) + (AD*ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '(3*AD*cw*ee*complex(0,1))/(4.*fPi**2*sw) - (3*AD*ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '(-3*AD*cw*ee*complex(0,1))/(4.*fPi**2*sw) + (3*AD*ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '-0.25*(AD*cw*ee*complex(0,1)*cmath.sqrt(1.5))/(fPi**2*sw) + (AD*ee*complex(0,1)*sw*cmath.sqrt(1.5))/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '-0.5*(AD*cw*ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2)) + (AD*ee*complex(0,1)*sw)/(2.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':2})

GC_351 = Coupling(name = 'GC_351',
                  value = '(3*AD**2*cw*ee*complex(0,1))/(8.*fPi**2*sw) - (3*AD**2*ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':3})

GC_352 = Coupling(name = 'GC_352',
                  value = '(-3*AD**2*cw*ee*complex(0,1))/(8.*fPi**2*sw) + (3*AD**2*ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':3})

GC_353 = Coupling(name = 'GC_353',
                  value = '(9*AD**2*cw*ee*complex(0,1))/(8.*fPi**2*sw) - (9*AD**2*ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':3})

GC_354 = Coupling(name = 'GC_354',
                  value = '(-9*AD**2*cw*ee*complex(0,1))/(8.*fPi**2*sw) + (9*AD**2*ee*complex(0,1)*sw)/(8.*cw*fPi**2)',
                  order = {'QED':3})

GC_355 = Coupling(name = 'GC_355',
                  value = '(-3*AD**2*cw*ee*complex(0,1)*cmath.sqrt(1.5))/(8.*fPi**2*sw) + (3*AD**2*ee*complex(0,1)*sw*cmath.sqrt(1.5))/(8.*cw*fPi**2)',
                  order = {'QED':3})

GC_356 = Coupling(name = 'GC_356',
                  value = '(-3*AD**2*cw*ee*complex(0,1))/(4.*fPi**2*sw*cmath.sqrt(2)) + (3*AD**2*ee*complex(0,1)*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':3})

GC_357 = Coupling(name = 'GC_357',
                  value = '-0.5*(cw*ee)/(fPi*sw) - (ee*sw)/(2.*cw*fPi)',
                  order = {'QED':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(cw*ee)/(2.*fPi*sw) + (ee*sw)/(2.*cw*fPi)',
                  order = {'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '-0.25*(cw*ee*cmath.sqrt(1.5))/(fPi*sw) - (ee*sw*cmath.sqrt(1.5))/(4.*cw*fPi)',
                  order = {'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(cw*ee*cmath.sqrt(1.5))/(4.*fPi*sw) + (ee*sw*cmath.sqrt(1.5))/(4.*cw*fPi)',
                  order = {'QED':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-0.5*(cw*ee)/(fPi*sw*cmath.sqrt(2)) - (ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cw*ee)/(2.*fPi*sw*cmath.sqrt(2)) + (ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '-0.5*(AD*cw*ee*cmath.sqrt(1.5))/(fPi*sw) - (AD*ee*sw*cmath.sqrt(1.5))/(2.*cw*fPi)',
                  order = {'QED':2})

GC_364 = Coupling(name = 'GC_364',
                  value = '(AD*cw*ee*cmath.sqrt(1.5))/(2.*fPi*sw) + (AD*ee*sw*cmath.sqrt(1.5))/(2.*cw*fPi)',
                  order = {'QED':2})

GC_365 = Coupling(name = 'GC_365',
                  value = '-((AD*cw*ee)/(fPi*sw*cmath.sqrt(2))) - (AD*ee*sw)/(cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_366 = Coupling(name = 'GC_366',
                  value = '(AD*cw*ee)/(fPi*sw*cmath.sqrt(2)) + (AD*ee*sw)/(cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_367 = Coupling(name = 'GC_367',
                  value = '(-3*AD**2*cw*ee*cmath.sqrt(1.5))/(4.*fPi*sw) - (3*AD**2*ee*sw*cmath.sqrt(1.5))/(4.*cw*fPi)',
                  order = {'QED':3})

GC_368 = Coupling(name = 'GC_368',
                  value = '(3*AD**2*cw*ee*cmath.sqrt(1.5))/(4.*fPi*sw) + (3*AD**2*ee*sw*cmath.sqrt(1.5))/(4.*cw*fPi)',
                  order = {'QED':3})

GC_369 = Coupling(name = 'GC_369',
                  value = '(3*AD**2*cw*ee)/(2.*fPi*sw*cmath.sqrt(2)) + (3*AD**2*ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':3})

GC_370 = Coupling(name = 'GC_370',
                  value = '-0.08333333333333333*(cw*ee*complex(0,1)*g1D)/sw - (ee*complex(0,1)*g1D*sw)/(12.*cw)',
                  order = {'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(cw*ee*complex(0,1)*g1D)/(12.*sw) + (ee*complex(0,1)*g1D*sw)/(12.*cw)',
                  order = {'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '-0.25*(cw*ee*complex(0,1)*g1D)/sw - (ee*complex(0,1)*g1D*sw)/(4.*cw)',
                  order = {'QED':2})

GC_373 = Coupling(name = 'GC_373',
                  value = '(cw*ee*complex(0,1)*g1D)/(4.*sw) + (ee*complex(0,1)*g1D*sw)/(4.*cw)',
                  order = {'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '-0.08333333333333333*(cw*ee*complex(0,1)*g1D)/(fPi**2*sw) - (ee*complex(0,1)*g1D*sw)/(12.*cw*fPi**2)',
                  order = {'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '(cw*ee*complex(0,1)*g1D)/(12.*fPi**2*sw) + (ee*complex(0,1)*g1D*sw)/(12.*cw*fPi**2)',
                  order = {'QED':2})

GC_376 = Coupling(name = 'GC_376',
                  value = '-0.25*(cw*ee*complex(0,1)*g1D)/(fPi**2*sw) - (ee*complex(0,1)*g1D*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_377 = Coupling(name = 'GC_377',
                  value = '(cw*ee*complex(0,1)*g1D)/(4.*fPi**2*sw) + (ee*complex(0,1)*g1D*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '(cw*ee*complex(0,1)*g1D)/(6.*fPi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*g1D*sw)/(6.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '(cw*ee*complex(0,1)*g1D)/(4.*fPi**2*sw*cmath.sqrt(6)) + (ee*complex(0,1)*g1D*sw)/(4.*cw*fPi**2*cmath.sqrt(6))',
                  order = {'QED':2})

GC_380 = Coupling(name = 'GC_380',
                  value = '(cw*ee*g1D)/(3.*fPi*sw*cmath.sqrt(2)) - (ee*g1D*sw)/(3.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_381 = Coupling(name = 'GC_381',
                  value = '-0.3333333333333333*(cw*ee*g1D)/(fPi*sw*cmath.sqrt(2)) + (ee*g1D*sw)/(3.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '(cw*ee*g1D)/(2.*fPi*sw*cmath.sqrt(6)) - (ee*g1D*sw)/(2.*cw*fPi*cmath.sqrt(6))',
                  order = {'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '-0.5*(cw*ee*g1D)/(fPi*sw*cmath.sqrt(6)) + (ee*g1D*sw)/(2.*cw*fPi*cmath.sqrt(6))',
                  order = {'QED':2})

GC_384 = Coupling(name = 'GC_384',
                  value = '-0.08333333333333333*(cw*ee*complex(0,1)*g2D)/sw - (ee*complex(0,1)*g2D*sw)/(12.*cw)',
                  order = {'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '(cw*ee*complex(0,1)*g2D)/(12.*sw) + (ee*complex(0,1)*g2D*sw)/(12.*cw)',
                  order = {'QED':2})

GC_386 = Coupling(name = 'GC_386',
                  value = '-0.25*(cw*ee*complex(0,1)*g2D)/sw - (ee*complex(0,1)*g2D*sw)/(4.*cw)',
                  order = {'QED':2})

GC_387 = Coupling(name = 'GC_387',
                  value = '(cw*ee*complex(0,1)*g2D)/(4.*sw) + (ee*complex(0,1)*g2D*sw)/(4.*cw)',
                  order = {'QED':2})

GC_388 = Coupling(name = 'GC_388',
                  value = '-0.08333333333333333*(cw*ee*complex(0,1)*g2D)/(fPi**2*sw) - (ee*complex(0,1)*g2D*sw)/(12.*cw*fPi**2)',
                  order = {'QED':2})

GC_389 = Coupling(name = 'GC_389',
                  value = '(cw*ee*complex(0,1)*g2D)/(12.*fPi**2*sw) + (ee*complex(0,1)*g2D*sw)/(12.*cw*fPi**2)',
                  order = {'QED':2})

GC_390 = Coupling(name = 'GC_390',
                  value = '-0.25*(cw*ee*complex(0,1)*g2D)/(fPi**2*sw) - (ee*complex(0,1)*g2D*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_391 = Coupling(name = 'GC_391',
                  value = '(cw*ee*complex(0,1)*g2D)/(4.*fPi**2*sw) + (ee*complex(0,1)*g2D*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_392 = Coupling(name = 'GC_392',
                  value = '(cw*ee*complex(0,1)*g2D)/(6.*fPi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*g2D*sw)/(6.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':2})

GC_393 = Coupling(name = 'GC_393',
                  value = '(cw*ee*complex(0,1)*g2D)/(4.*fPi**2*sw*cmath.sqrt(6)) + (ee*complex(0,1)*g2D*sw)/(4.*cw*fPi**2*cmath.sqrt(6))',
                  order = {'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '(cw*ee*g2D)/(3.*fPi*sw*cmath.sqrt(2)) - (ee*g2D*sw)/(3.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '-0.3333333333333333*(cw*ee*g2D)/(fPi*sw*cmath.sqrt(2)) + (ee*g2D*sw)/(3.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_396 = Coupling(name = 'GC_396',
                  value = '(cw*ee*g2D)/(2.*fPi*sw*cmath.sqrt(6)) - (ee*g2D*sw)/(2.*cw*fPi*cmath.sqrt(6))',
                  order = {'QED':2})

GC_397 = Coupling(name = 'GC_397',
                  value = '-0.5*(cw*ee*g2D)/(fPi*sw*cmath.sqrt(6)) + (ee*g2D*sw)/(2.*cw*fPi*cmath.sqrt(6))',
                  order = {'QED':2})

GC_398 = Coupling(name = 'GC_398',
                  value = '-0.08333333333333333*(cw*ee*complex(0,1)*g3D)/sw - (ee*complex(0,1)*g3D*sw)/(12.*cw)',
                  order = {'QED':2})

GC_399 = Coupling(name = 'GC_399',
                  value = '(cw*ee*complex(0,1)*g3D)/(12.*sw) + (ee*complex(0,1)*g3D*sw)/(12.*cw)',
                  order = {'QED':2})

GC_400 = Coupling(name = 'GC_400',
                  value = '-0.25*(cw*ee*complex(0,1)*g3D)/sw - (ee*complex(0,1)*g3D*sw)/(4.*cw)',
                  order = {'QED':2})

GC_401 = Coupling(name = 'GC_401',
                  value = '(cw*ee*complex(0,1)*g3D)/(4.*sw) + (ee*complex(0,1)*g3D*sw)/(4.*cw)',
                  order = {'QED':2})

GC_402 = Coupling(name = 'GC_402',
                  value = '-0.08333333333333333*(cw*ee*complex(0,1)*g3D)/(fPi**2*sw) - (ee*complex(0,1)*g3D*sw)/(12.*cw*fPi**2)',
                  order = {'QED':2})

GC_403 = Coupling(name = 'GC_403',
                  value = '(cw*ee*complex(0,1)*g3D)/(12.*fPi**2*sw) + (ee*complex(0,1)*g3D*sw)/(12.*cw*fPi**2)',
                  order = {'QED':2})

GC_404 = Coupling(name = 'GC_404',
                  value = '-0.25*(cw*ee*complex(0,1)*g3D)/(fPi**2*sw) - (ee*complex(0,1)*g3D*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_405 = Coupling(name = 'GC_405',
                  value = '(cw*ee*complex(0,1)*g3D)/(4.*fPi**2*sw) + (ee*complex(0,1)*g3D*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_406 = Coupling(name = 'GC_406',
                  value = '-0.16666666666666666*(cw*ee*complex(0,1)*g3D)/(fPi**2*sw*cmath.sqrt(2)) - (ee*complex(0,1)*g3D*sw)/(6.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':2})

GC_407 = Coupling(name = 'GC_407',
                  value = '-0.25*(cw*ee*complex(0,1)*g3D)/(fPi**2*sw*cmath.sqrt(6)) - (ee*complex(0,1)*g3D*sw)/(4.*cw*fPi**2*cmath.sqrt(6))',
                  order = {'QED':2})

GC_408 = Coupling(name = 'GC_408',
                  value = '(cw*ee*g3D)/(3.*fPi*sw*cmath.sqrt(2)) - (ee*g3D*sw)/(3.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_409 = Coupling(name = 'GC_409',
                  value = '-0.3333333333333333*(cw*ee*g3D)/(fPi*sw*cmath.sqrt(2)) + (ee*g3D*sw)/(3.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_410 = Coupling(name = 'GC_410',
                  value = '(cw*ee*g3D)/(2.*fPi*sw*cmath.sqrt(6)) - (ee*g3D*sw)/(2.*cw*fPi*cmath.sqrt(6))',
                  order = {'QED':2})

GC_411 = Coupling(name = 'GC_411',
                  value = '-0.5*(cw*ee*g3D)/(fPi*sw*cmath.sqrt(6)) + (ee*g3D*sw)/(2.*cw*fPi*cmath.sqrt(6))',
                  order = {'QED':2})

GC_412 = Coupling(name = 'GC_412',
                  value = '-0.25*(cw*ee*complex(0,1)*ga)/sw - (ee*complex(0,1)*ga*sw)/(4.*cw)',
                  order = {'QED':2})

GC_413 = Coupling(name = 'GC_413',
                  value = '(cw*ee*complex(0,1)*ga)/(4.*sw) + (ee*complex(0,1)*ga*sw)/(4.*cw)',
                  order = {'QED':2})

GC_414 = Coupling(name = 'GC_414',
                  value = '-0.25*(cw*ee*complex(0,1)*ga)/(fPi**2*sw) - (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_415 = Coupling(name = 'GC_415',
                  value = '(cw*ee*complex(0,1)*ga)/(4.*fPi**2*sw) + (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_416 = Coupling(name = 'GC_416',
                  value = '-0.25*(cw*ee*complex(0,1)*ga)/(fPi**2*sw*cmath.sqrt(2)) - (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                  order = {'QED':2})

GC_417 = Coupling(name = 'GC_417',
                  value = '(cw*ee*ga)/(2.*fPi*sw*cmath.sqrt(2)) - (ee*ga*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_418 = Coupling(name = 'GC_418',
                  value = '-0.5*(cw*ee*ga)/(fPi*sw*cmath.sqrt(2)) + (ee*ga*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_419 = Coupling(name = 'GC_419',
                  value = '-((cw*ee*complex(0,1)*gD)/(sw*cmath.sqrt(6))) - (ee*complex(0,1)*gD*sw)/(cw*cmath.sqrt(6))',
                  order = {'QED':2})

GC_420 = Coupling(name = 'GC_420',
                  value = '-0.25*(cw*ee*complex(0,1)*gD)/(fPi**2*sw) - (ee*complex(0,1)*gD*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '(cw*ee*complex(0,1)*gD)/(4.*fPi**2*sw) + (ee*complex(0,1)*gD*sw)/(4.*cw*fPi**2)',
                  order = {'QED':2})

GC_422 = Coupling(name = 'GC_422',
                  value = '-0.25*(cw*ee*complex(0,1)*gD)/(fPi**2*sw*cmath.sqrt(3)) - (ee*complex(0,1)*gD*sw)/(4.*cw*fPi**2*cmath.sqrt(3))',
                  order = {'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '(cw*ee*complex(0,1)*gD)/(4.*fPi**2*sw*cmath.sqrt(3)) + (ee*complex(0,1)*gD*sw)/(4.*cw*fPi**2*cmath.sqrt(3))',
                  order = {'QED':2})

GC_424 = Coupling(name = 'GC_424',
                  value = '(cw*ee*complex(0,1)*gD)/(fPi**2*sw*cmath.sqrt(6)) + (ee*complex(0,1)*gD*sw)/(cw*fPi**2*cmath.sqrt(6))',
                  order = {'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '(cw*ee*gD)/(2.*fPi*sw) - (ee*gD*sw)/(2.*cw*fPi)',
                  order = {'QED':2})

GC_426 = Coupling(name = 'GC_426',
                  value = '-0.5*(cw*ee*gD)/(fPi*sw) + (ee*gD*sw)/(2.*cw*fPi)',
                  order = {'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '(cw*ee*gD)/(2.*fPi*sw*cmath.sqrt(3)) - (ee*gD*sw)/(2.*cw*fPi*cmath.sqrt(3))',
                  order = {'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '-0.5*(cw*ee*gD)/(fPi*sw*cmath.sqrt(3)) + (ee*gD*sw)/(2.*cw*fPi*cmath.sqrt(3))',
                  order = {'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '-((cw*ee*gDGI)/(MDelta*sw*cmath.sqrt(6))) - (ee*gDGI*sw)/(cw*MDelta*cmath.sqrt(6))',
                  order = {'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '-0.25*(cw*ee*gDGI)/(fPi**2*MDelta*sw) - (ee*gDGI*sw)/(4.*cw*fPi**2*MDelta)',
                  order = {'QED':2})

GC_431 = Coupling(name = 'GC_431',
                  value = '(cw*ee*gDGI)/(4.*fPi**2*MDelta*sw) + (ee*gDGI*sw)/(4.*cw*fPi**2*MDelta)',
                  order = {'QED':2})

GC_432 = Coupling(name = 'GC_432',
                  value = '-0.25*(cw*ee*gDGI)/(fPi**2*MDelta*sw*cmath.sqrt(3)) - (ee*gDGI*sw)/(4.*cw*fPi**2*MDelta*cmath.sqrt(3))',
                  order = {'QED':2})

GC_433 = Coupling(name = 'GC_433',
                  value = '(cw*ee*gDGI)/(4.*fPi**2*MDelta*sw*cmath.sqrt(3)) + (ee*gDGI*sw)/(4.*cw*fPi**2*MDelta*cmath.sqrt(3))',
                  order = {'QED':2})

GC_434 = Coupling(name = 'GC_434',
                  value = '(cw*ee*gDGI)/(fPi**2*MDelta*sw*cmath.sqrt(6)) + (ee*gDGI*sw)/(cw*fPi**2*MDelta*cmath.sqrt(6))',
                  order = {'QED':2})

GC_435 = Coupling(name = 'GC_435',
                  value = '(cw*ee*complex(0,1)*gDGI)/(2.*fPi*MDelta*sw) - (ee*complex(0,1)*gDGI*sw)/(2.*cw*fPi*MDelta)',
                  order = {'QED':2})

GC_436 = Coupling(name = 'GC_436',
                  value = '-0.5*(cw*ee*complex(0,1)*gDGI)/(fPi*MDelta*sw) + (ee*complex(0,1)*gDGI*sw)/(2.*cw*fPi*MDelta)',
                  order = {'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '(cw*ee*complex(0,1)*gDGI)/(2.*fPi*MDelta*sw*cmath.sqrt(3)) - (ee*complex(0,1)*gDGI*sw)/(2.*cw*fPi*MDelta*cmath.sqrt(3))',
                  order = {'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '-0.5*(cw*ee*complex(0,1)*gDGI)/(fPi*MDelta*sw*cmath.sqrt(3)) + (ee*complex(0,1)*gDGI*sw)/(2.*cw*fPi*MDelta*cmath.sqrt(3))',
                  order = {'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '(ee**2*complex(0,1))/fPi**2 + (cw**2*ee**2*complex(0,1))/(2.*fPi**2*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2*fPi**2)',
                  order = {'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '(2*ee**2*complex(0,1))/fPi**2 + (cw**2*ee**2*complex(0,1))/(fPi**2*sw**2) + (ee**2*complex(0,1)*sw**2)/(cw**2*fPi**2)',
                  order = {'QED':2})

GC_442 = Coupling(name = 'GC_442',
                  value = '(3*ee**2*complex(0,1))/fPi**2 + (3*cw**2*ee**2*complex(0,1))/(2.*fPi**2*sw**2) + (3*ee**2*complex(0,1)*sw**2)/(2.*cw**2*fPi**2)',
                  order = {'QED':2})

GC_443 = Coupling(name = 'GC_443',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '-((gD*ztilde)/fPi)',
                  order = {'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '(gD*ztilde)/fPi',
                  order = {'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '(gD*ztilde*cmath.sqrt(0.6666666666666666))/fPi',
                  order = {'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '-((gD*ztilde)/(fPi*cmath.sqrt(3)))',
                  order = {'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '(gD*ztilde)/(fPi*cmath.sqrt(3))',
                  order = {'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '-((ee*gD*ztilde)/fPi)',
                  order = {'QED':3})

GC_455 = Coupling(name = 'GC_455',
                  value = '(ee*gD*ztilde)/fPi',
                  order = {'QED':3})

GC_456 = Coupling(name = 'GC_456',
                  value = '-((ee*gD*ztilde)/(fPi*cmath.sqrt(3)))',
                  order = {'QED':3})

GC_457 = Coupling(name = 'GC_457',
                  value = '(ee*gD*ztilde)/(fPi*cmath.sqrt(3))',
                  order = {'QED':3})

GC_458 = Coupling(name = 'GC_458',
                  value = '-0.5*(ee*complex(0,1)*gD*ztilde)/sw',
                  order = {'QED':3})

GC_459 = Coupling(name = 'GC_459',
                  value = '(ee*complex(0,1)*gD*ztilde)/(2.*sw)',
                  order = {'QED':3})

GC_460 = Coupling(name = 'GC_460',
                  value = '-0.5*(ee*complex(0,1)*gD*ztilde)/(sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_461 = Coupling(name = 'GC_461',
                  value = '(ee*complex(0,1)*gD*ztilde)/(2.*sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_462 = Coupling(name = 'GC_462',
                  value = '-0.25*(ee*complex(0,1)*gD*ztilde)/(fPi**2*sw)',
                  order = {'QED':3})

GC_463 = Coupling(name = 'GC_463',
                  value = '(ee*complex(0,1)*gD*ztilde)/(4.*fPi**2*sw)',
                  order = {'QED':3})

GC_464 = Coupling(name = 'GC_464',
                  value = '-0.5*(ee*complex(0,1)*gD*ztilde)/(fPi**2*sw)',
                  order = {'QED':3})

GC_465 = Coupling(name = 'GC_465',
                  value = '(ee*complex(0,1)*gD*ztilde)/(2.*fPi**2*sw)',
                  order = {'QED':3})

GC_466 = Coupling(name = 'GC_466',
                  value = '-0.25*(ee*complex(0,1)*gD*ztilde)/(fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_467 = Coupling(name = 'GC_467',
                  value = '(ee*complex(0,1)*gD*ztilde)/(4.*fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_468 = Coupling(name = 'GC_468',
                  value = '-0.5*(ee*complex(0,1)*gD*ztilde)/(fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_469 = Coupling(name = 'GC_469',
                  value = '(ee*complex(0,1)*gD*ztilde)/(2.*fPi**2*sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_470 = Coupling(name = 'GC_470',
                  value = '-0.5*(ee*complex(0,1)*gD*ztilde)/(fPi**2*sw*cmath.sqrt(6))',
                  order = {'QED':3})

GC_471 = Coupling(name = 'GC_471',
                  value = '-0.5*(ee*gD*ztilde)/(fPi*sw)',
                  order = {'QED':3})

GC_472 = Coupling(name = 'GC_472',
                  value = '(ee*gD*ztilde)/(2.*fPi*sw)',
                  order = {'QED':3})

GC_473 = Coupling(name = 'GC_473',
                  value = '-0.5*(ee*gD*ztilde)/(fPi*sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_474 = Coupling(name = 'GC_474',
                  value = '(ee*gD*ztilde)/(2.*fPi*sw*cmath.sqrt(3))',
                  order = {'QED':3})

GC_475 = Coupling(name = 'GC_475',
                  value = '-((ee*gD*ztilde)/(fPi*sw*cmath.sqrt(6)))',
                  order = {'QED':3})

GC_476 = Coupling(name = 'GC_476',
                  value = '(ee*gD*ztilde)/(fPi*sw*cmath.sqrt(6))',
                  order = {'QED':3})

GC_477 = Coupling(name = 'GC_477',
                  value = '-((cw*ee*complex(0,1)*gD*ztilde)/(sw*cmath.sqrt(6))) - (ee*complex(0,1)*gD*sw*ztilde)/(cw*cmath.sqrt(6))',
                  order = {'QED':3})

GC_478 = Coupling(name = 'GC_478',
                  value = '-0.25*(cw*ee*complex(0,1)*gD*ztilde)/(fPi**2*sw) - (ee*complex(0,1)*gD*sw*ztilde)/(4.*cw*fPi**2)',
                  order = {'QED':3})

GC_479 = Coupling(name = 'GC_479',
                  value = '(cw*ee*complex(0,1)*gD*ztilde)/(4.*fPi**2*sw) + (ee*complex(0,1)*gD*sw*ztilde)/(4.*cw*fPi**2)',
                  order = {'QED':3})

GC_480 = Coupling(name = 'GC_480',
                  value = '-0.25*(cw*ee*complex(0,1)*gD*ztilde)/(fPi**2*sw*cmath.sqrt(3)) - (ee*complex(0,1)*gD*sw*ztilde)/(4.*cw*fPi**2*cmath.sqrt(3))',
                  order = {'QED':3})

GC_481 = Coupling(name = 'GC_481',
                  value = '(cw*ee*complex(0,1)*gD*ztilde)/(4.*fPi**2*sw*cmath.sqrt(3)) + (ee*complex(0,1)*gD*sw*ztilde)/(4.*cw*fPi**2*cmath.sqrt(3))',
                  order = {'QED':3})

GC_482 = Coupling(name = 'GC_482',
                  value = '(cw*ee*complex(0,1)*gD*ztilde)/(fPi**2*sw*cmath.sqrt(6)) + (ee*complex(0,1)*gD*sw*ztilde)/(cw*fPi**2*cmath.sqrt(6))',
                  order = {'QED':3})

GC_483 = Coupling(name = 'GC_483',
                  value = '(cw*ee*gD*ztilde)/(2.*fPi*sw) - (ee*gD*sw*ztilde)/(2.*cw*fPi)',
                  order = {'QED':3})

GC_484 = Coupling(name = 'GC_484',
                  value = '-0.5*(cw*ee*gD*ztilde)/(fPi*sw) + (ee*gD*sw*ztilde)/(2.*cw*fPi)',
                  order = {'QED':3})

GC_485 = Coupling(name = 'GC_485',
                  value = '(cw*ee*gD*ztilde)/(2.*fPi*sw*cmath.sqrt(3)) - (ee*gD*sw*ztilde)/(2.*cw*fPi*cmath.sqrt(3))',
                  order = {'QED':3})

GC_486 = Coupling(name = 'GC_486',
                  value = '-0.5*(cw*ee*gD*ztilde)/(fPi*sw*cmath.sqrt(3)) + (ee*gD*sw*ztilde)/(2.*cw*fPi*cmath.sqrt(3))',
                  order = {'QED':3})

