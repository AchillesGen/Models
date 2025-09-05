# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Fri 5 Sep 2025 16:14:08


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# Color algebra definitions (REQUIRED by MG5 even for U(1) models)
import cmath

# Identity color factor (for singlets)
def one(color):
    return 1

# Color matrix class (MG5 expects this)
class Color(object):
    pass

# Color basis definition (crucial for ALOHA)
color_basis = ['1']

# Color matrix definitions (even for trivial case)
color_matrices = {
    'Identity': {
        (0,0): 1
    }
}

GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_4 = Coupling(name = 'GC_4',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-0.25*complex(0,1)/fPi**2',
                order = {'1':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)/(4.*fPi**2)',
                order = {'1':1})

GC_8 = Coupling(name = 'GC_8',
                value = '-(complex(0,1)/fPi**2)',
                order = {'1':1})

GC_9 = Coupling(name = 'GC_9',
                value = '(-2*complex(0,1))/fPi**2',
                order = {'1':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-0.5*complex(0,1)/(fPi**2*cmath.sqrt(2))',
                 order = {'1':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'1':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-0.5*(ee*complex(0,1))/fPi**2',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(ee*complex(0,1))/(2.*fPi**2)',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(ee*complex(0,1))/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(ee**2/(cw*fPi))',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-0.5*ee**2/(cw*fPi)',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = 'ee**2/(2.*cw*fPi)',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = 'ee**2/(cw*fPi)',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-0.5*(ee**2*fPi)/cw',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(ee**2*fPi)/(2.*cw)',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-0.5*ga/fPi',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = 'ga/(2.*fPi)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(ga/(fPi*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-((ee*ga)/(fPi*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(ee*ga)/(fPi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(ee**2*complex(0,1))/(2.*fPi**2*sw**2)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(ee**2*complex(0,1))/(fPi**2*sw**2)',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(3*ee**2*complex(0,1))/(2.*fPi**2*sw**2)',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ee*complex(0,1))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-0.5*(ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-0.125*(ee*complex(0,1))/(fPi**2*sw)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(ee*complex(0,1))/(8.*fPi**2*sw)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-0.25*(ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-0.5*(ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(ee*complex(0,1))/(2.*fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-0.25*ee/(fPi*sw)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'ee/(4.*fPi*sw)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = 'ee/(2.*fPi*sw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = 'ee/(fPi*sw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-0.5*ee/(fPi*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = 'ee/(2.*fPi*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(ee**2/(fPi*sw))',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '-0.5*ee**2/(fPi*sw)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = 'ee**2/(2.*fPi*sw)',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = 'ee**2/(fPi*sw)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-0.5*(ee**2*fPi)/sw',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(ee**2*fPi)/(2.*sw)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-0.5*(ee*complex(0,1)*ga)/(sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '-0.125*(ee*complex(0,1)*ga)/(fPi**2*sw)',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee*complex(0,1)*ga)/(8.*fPi**2*sw)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee*complex(0,1)*ga)/(4.*fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-0.5*(ee*complex(0,1)*ga)/(fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(ee*complex(0,1)*ga)/(2.*fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-0.25*(ee*ga)/(fPi*sw)',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(ee*ga)/(4.*fPi*sw)',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-0.5*(ee*ga)/(fPi*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(ee*ga)/(2.*fPi*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-0.25*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(4.*cw)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cw*ee*complex(0,1))/(4.*sw) - (3*ee*complex(0,1)*sw)/(4.*cw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cw*ee*complex(0,1))/(4.*fPi**2*sw) - (ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-0.25*(cw*ee*complex(0,1))/(fPi**2*sw) + (ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cw*ee*complex(0,1))/(4.*fPi**2*sw*cmath.sqrt(2)) - (ee*complex(0,1)*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-0.5*(cw*ee)/(fPi*sw) - (ee*sw)/(2.*cw*fPi)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(cw*ee)/(2.*fPi*sw) + (ee*sw)/(2.*cw*fPi)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-0.5*(cw*ee)/(fPi*sw*cmath.sqrt(2)) - (ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cw*ee)/(2.*fPi*sw*cmath.sqrt(2)) + (ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-0.25*(cw*ee*complex(0,1)*ga)/sw - (ee*complex(0,1)*ga*sw)/(4.*cw)',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(cw*ee*complex(0,1)*ga)/(4.*sw) + (ee*complex(0,1)*ga*sw)/(4.*cw)',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-0.25*(cw*ee*complex(0,1)*ga)/(fPi**2*sw) - (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2)',
                 order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(cw*ee*complex(0,1)*ga)/(4.*fPi**2*sw) + (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2)',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '-0.25*(cw*ee*complex(0,1)*ga)/(fPi**2*sw*cmath.sqrt(2)) - (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(cw*ee*ga)/(2.*fPi*sw*cmath.sqrt(2)) - (ee*ga*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-0.5*(cw*ee*ga)/(fPi*sw*cmath.sqrt(2)) + (ee*ga*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(ee**2*complex(0,1))/fPi**2 + (cw**2*ee**2*complex(0,1))/(2.*fPi**2*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2*fPi**2)',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '(2*ee**2*complex(0,1))/fPi**2 + (cw**2*ee**2*complex(0,1))/(fPi**2*sw**2) + (ee**2*complex(0,1)*sw**2)/(cw**2*fPi**2)',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(3*ee**2*complex(0,1))/fPi**2 + (3*cw**2*ee**2*complex(0,1))/(2.*fPi**2*sw**2) + (3*ee**2*complex(0,1)*sw**2)/(2.*cw**2*fPi**2)',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

