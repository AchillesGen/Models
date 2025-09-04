# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Wed 3 Sep 2025 23:28:42


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

# Simple color structure instance
color_ones = Color()

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
                order = {'QED':0})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)/(4.*fPi**2)',
                order = {'QED':0})

GC_8 = Coupling(name = 'GC_8',
                value = '-(complex(0,1)/fPi**2)',
                order = {'QED':0})

GC_9 = Coupling(name = 'GC_9',
                value = '(-2*complex(0,1))/fPi**2',
                order = {'QED':0})

GC_10 = Coupling(name = 'GC_10',
                 value = '-0.5*complex(0,1)/(fPi**2*cmath.sqrt(2))',
                 order = {'QED':0})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)/(2.*fPi**2*cmath.sqrt(2))',
                 order = {'QED':0})

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
                 value = '(ee**2*complex(0,1))/(2.*fPi**2*sw**2)',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(ee**2*complex(0,1))/(fPi**2*sw**2)',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(3*ee**2*complex(0,1))/(2.*fPi**2*sw**2)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee*complex(0,1))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-0.5*(ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-0.125*(ee*complex(0,1))/(fPi**2*sw)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee*complex(0,1))/(8.*fPi**2*sw)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-0.25*(ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-0.5*(ee*complex(0,1))/(fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(ee*complex(0,1))/(2.*fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-0.25*ee/(fPi*sw)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = 'ee/(4.*fPi*sw)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'ee/(2.*fPi*sw)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'ee/(fPi*sw)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-0.5*ee/(fPi*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'ee/(2.*fPi*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(ee**2/(fPi*sw))',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-0.5*ee**2/(fPi*sw)',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = 'ee**2/(2.*fPi*sw)',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = 'ee**2/(fPi*sw)',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-0.5*(ee**2*fPi)/sw',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(ee**2*fPi)/(2.*sw)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-0.5*(ee*complex(0,1)*ga)/(sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-0.125*(ee*complex(0,1)*ga)/(fPi**2*sw)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee*complex(0,1)*ga)/(8.*fPi**2*sw)',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(ee*complex(0,1)*ga)/(4.*fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-0.5*(ee*complex(0,1)*ga)/(fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee*complex(0,1)*ga)/(2.*fPi**2*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-0.25*(ee*ga)/(fPi*sw)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee*ga)/(4.*fPi*sw)',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-0.5*(ee*ga)/(fPi*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(ee*ga)/(2.*fPi*sw*cmath.sqrt(2))',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-0.25*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(4.*cw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(cw*ee*complex(0,1))/(4.*sw) - (3*ee*complex(0,1)*sw)/(4.*cw)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(cw*ee*complex(0,1))/(4.*fPi**2*sw) - (ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-0.25*(cw*ee*complex(0,1))/(fPi**2*sw) + (ee*complex(0,1)*sw)/(4.*cw*fPi**2)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(cw*ee*complex(0,1))/(4.*fPi**2*sw*cmath.sqrt(2)) - (ee*complex(0,1)*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-0.5*(cw*ee)/(fPi*sw) - (ee*sw)/(2.*cw*fPi)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cw*ee)/(2.*fPi*sw) + (ee*sw)/(2.*cw*fPi)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-0.5*(cw*ee)/(fPi*sw*cmath.sqrt(2)) - (ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cw*ee)/(2.*fPi*sw*cmath.sqrt(2)) + (ee*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-0.25*(cw*ee*complex(0,1)*ga)/sw - (ee*complex(0,1)*ga*sw)/(4.*cw)',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cw*ee*complex(0,1)*ga)/(4.*sw) + (ee*complex(0,1)*ga*sw)/(4.*cw)',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-0.25*(cw*ee*complex(0,1)*ga)/(fPi**2*sw) - (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2)',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(cw*ee*complex(0,1)*ga)/(4.*fPi**2*sw) + (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2)',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '-0.25*(cw*ee*complex(0,1)*ga)/(fPi**2*sw*cmath.sqrt(2)) - (ee*complex(0,1)*ga*sw)/(4.*cw*fPi**2*cmath.sqrt(2))',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cw*ee*ga)/(2.*fPi*sw*cmath.sqrt(2)) - (ee*ga*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '-0.5*(cw*ee*ga)/(fPi*sw*cmath.sqrt(2)) + (ee*ga*sw)/(2.*cw*fPi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(ee**2*complex(0,1))/fPi**2 + (cw**2*ee**2*complex(0,1))/(2.*fPi**2*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2*fPi**2)',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(2*ee**2*complex(0,1))/fPi**2 + (cw**2*ee**2*complex(0,1))/(fPi**2*sw**2) + (ee**2*complex(0,1)*sw**2)/(cw**2*fPi**2)',
                 order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(3*ee**2*complex(0,1))/fPi**2 + (3*cw**2*ee**2*complex(0,1))/(2.*fPi**2*sw**2) + (3*ee**2*complex(0,1)*sw**2)/(2.*cw**2*fPi**2)',
                 order = {'QED':2})