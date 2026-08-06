# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Tue 28 Jul 2026 12:26:20


from __future__ import absolute_import
from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.A, P.pi__minus__, P.pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VSS1 ],
             couplings = {(0,0):C.GC_1})

V_2 = Vertex(name = 'V_2',
             particles = [ P.n__tilde__, P.N15350, P.pi0 ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_16})

V_3 = Vertex(name = 'V_3',
             particles = [ P.n__tilde__, P.N1535__plus__, P.pi__minus__ ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_18})

V_4 = Vertex(name = 'V_4',
             particles = [ P.n__tilde__, P.N16500, P.pi0 ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_19})

V_5 = Vertex(name = 'V_5',
             particles = [ P.n__tilde__, P.N1650__plus__, P.pi__minus__ ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_21})

V_6 = Vertex(name = 'V_6',
             particles = [ P.n__tilde__, P.Delta16200, P.pi0 ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_10})

V_7 = Vertex(name = 'V_7',
             particles = [ P.n__tilde__, P.Delta1620__minus__, P.pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_8})

V_8 = Vertex(name = 'V_8',
             particles = [ P.n__tilde__, P.Delta1620__plus__, P.pi__minus__ ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_12})

V_9 = Vertex(name = 'V_9',
             particles = [ P.n__tilde__, P.Delta0, P.A ],
             color = [ '1' ],
             lorentz = [ L.FRV2, L.FRV3 ],
             couplings = {(0,1):C.GC_55,(0,0):C.GC_52})

V_10 = Vertex(name = 'V_10',
              particles = [ P.n__tilde__, P.N15200, P.A ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV4 ],
              couplings = {(0,0):C.GC_60,(0,1):C.GC_61})

V_11 = Vertex(name = 'V_11',
              particles = [ P.n__tilde__, P.N15200, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_57})

V_12 = Vertex(name = 'V_12',
              particles = [ P.n__tilde__, P.N1520__plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_58})

V_13 = Vertex(name = 'V_13',
              particles = [ P.n__tilde__, P.Delta17000, P.A ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV4 ],
              couplings = {(0,0):C.GC_50,(0,1):C.GC_51})

V_14 = Vertex(name = 'V_14',
              particles = [ P.n__tilde__, P.Delta1700__minus__, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_23})

V_15 = Vertex(name = 'V_15',
              particles = [ P.n__tilde__, P.Delta1700__plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_25})

V_16 = Vertex(name = 'V_16',
              particles = [ P.n__tilde__, P.Delta17000, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_24})

V_17 = Vertex(name = 'V_17',
              particles = [ P.Delta17000__tilde__, P.n, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV4 ],
              couplings = {(0,0):C.GC_50,(0,1):C.GC_51})

V_18 = Vertex(name = 'V_18',
              particles = [ P.N15200__tilde__, P.n, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV4 ],
              couplings = {(0,0):C.GC_60,(0,1):C.GC_61})

V_19 = Vertex(name = 'V_19',
              particles = [ P.Delta0__tilde__, P.n, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV2, L.RFV3 ],
              couplings = {(0,1):C.GC_54,(0,0):C.GC_53})

V_20 = Vertex(name = 'V_20',
              particles = [ P.Delta16200__tilde__, P.n, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_10})

V_21 = Vertex(name = 'V_21',
              particles = [ P.Delta1620__minus____tilde__, P.n, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_8})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Delta1620__plus____tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_12})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Delta1700__minus____tilde__, P.n, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_23})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Delta1700__plus____tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_25})

V_25 = Vertex(name = 'V_25',
              particles = [ P.Delta17000__tilde__, P.n, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_24})

V_26 = Vertex(name = 'V_26',
              particles = [ P.N15200__tilde__, P.n, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_57})

V_27 = Vertex(name = 'V_27',
              particles = [ P.N1520__plus____tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_58})

V_28 = Vertex(name = 'V_28',
              particles = [ P.N15350__tilde__, P.n, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_16})

V_29 = Vertex(name = 'V_29',
              particles = [ P.N1535__plus____tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_18})

V_30 = Vertex(name = 'V_30',
              particles = [ P.N16500__tilde__, P.n, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_31 = Vertex(name = 'V_31',
              particles = [ P.N1650__plus____tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_21})

V_32 = Vertex(name = 'V_32',
              particles = [ P.n__tilde__, P.n, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,0):C.GC_3,(0,1):C.GC_33})

V_33 = Vertex(name = 'V_33',
              particles = [ P.n__tilde__, P.n, P.omega ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,0):C.GC_4,(0,1):C.GC_46})

V_34 = Vertex(name = 'V_34',
              particles = [ P.A, P.omega, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_68})

V_35 = Vertex(name = 'V_35',
              particles = [ P.p__tilde__, P.N15350, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_18})

V_36 = Vertex(name = 'V_36',
              particles = [ P.p__tilde__, P.N1535__plus__, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_17})

V_37 = Vertex(name = 'V_37',
              particles = [ P.p__tilde__, P.N16500, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_21})

V_38 = Vertex(name = 'V_38',
              particles = [ P.p__tilde__, P.N1650__plus__, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_20})

V_39 = Vertex(name = 'V_39',
              particles = [ P.p__tilde__, P.Delta1620__plus__, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_10})

V_40 = Vertex(name = 'V_40',
              particles = [ P.p__tilde__, P.Delta16200, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_11})

V_41 = Vertex(name = 'V_41',
              particles = [ P.p__tilde__, P.Delta1620__plus____plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_9})

V_42 = Vertex(name = 'V_42',
              particles = [ P.p__tilde__, P.Delta__plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FRV2, L.FRV3 ],
              couplings = {(0,1):C.GC_55,(0,0):C.GC_52})

V_43 = Vertex(name = 'V_43',
              particles = [ P.p__tilde__, P.N1520__plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV4 ],
              couplings = {(0,0):C.GC_59,(0,1):C.GC_62})

V_44 = Vertex(name = 'V_44',
              particles = [ P.p__tilde__, P.N15200, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_58})

V_45 = Vertex(name = 'V_45',
              particles = [ P.p__tilde__, P.N1520__plus__, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_56})

V_46 = Vertex(name = 'V_46',
              particles = [ P.p__tilde__, P.Delta1700__plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV4 ],
              couplings = {(0,0):C.GC_50,(0,1):C.GC_51})

V_47 = Vertex(name = 'V_47',
              particles = [ P.p__tilde__, P.Delta1700__plus__, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_24})

V_48 = Vertex(name = 'V_48',
              particles = [ P.p__tilde__, P.Delta1700__plus____plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_22})

V_49 = Vertex(name = 'V_49',
              particles = [ P.p__tilde__, P.Delta17000, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1 ],
              couplings = {(0,0):C.GC_26})

V_50 = Vertex(name = 'V_50',
              particles = [ P.Delta1700__plus____tilde__, P.p, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV4 ],
              couplings = {(0,0):C.GC_50,(0,1):C.GC_51})

V_51 = Vertex(name = 'V_51',
              particles = [ P.N1520__plus____tilde__, P.p, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV4 ],
              couplings = {(0,0):C.GC_59,(0,1):C.GC_62})

V_52 = Vertex(name = 'V_52',
              particles = [ P.Delta__plus____tilde__, P.p, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV2, L.RFV3 ],
              couplings = {(0,1):C.GC_54,(0,0):C.GC_53})

V_53 = Vertex(name = 'V_53',
              particles = [ P.Delta1620__plus____tilde__, P.p, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_10})

V_54 = Vertex(name = 'V_54',
              particles = [ P.Delta16200__tilde__, P.p, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_11})

V_55 = Vertex(name = 'V_55',
              particles = [ P.Delta1620__plus____plus____tilde__, P.p, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_9})

V_56 = Vertex(name = 'V_56',
              particles = [ P.Delta1700__plus____tilde__, P.p, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_24})

V_57 = Vertex(name = 'V_57',
              particles = [ P.Delta1700__plus____plus____tilde__, P.p, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_22})

V_58 = Vertex(name = 'V_58',
              particles = [ P.Delta17000__tilde__, P.p, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_26})

V_59 = Vertex(name = 'V_59',
              particles = [ P.N15200__tilde__, P.p, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_58})

V_60 = Vertex(name = 'V_60',
              particles = [ P.N1520__plus____tilde__, P.p, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.RFS1 ],
              couplings = {(0,0):C.GC_56})

V_61 = Vertex(name = 'V_61',
              particles = [ P.N15350__tilde__, P.p, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_18})

V_62 = Vertex(name = 'V_62',
              particles = [ P.N1535__plus____tilde__, P.p, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_17})

V_63 = Vertex(name = 'V_63',
              particles = [ P.N16500__tilde__, P.p, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_21})

V_64 = Vertex(name = 'V_64',
              particles = [ P.N1650__plus____tilde__, P.p, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_20})

V_65 = Vertex(name = 'V_65',
              particles = [ P.p__tilde__, P.p, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,0):C.GC_2,(0,1):C.GC_32})

V_66 = Vertex(name = 'V_66',
              particles = [ P.p__tilde__, P.p, P.omega ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,0):C.GC_4,(0,1):C.GC_46})

V_67 = Vertex(name = 'V_67',
              particles = [ P.n__tilde__, P.n, P.rho0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,0):C.GC_6,(0,1):C.GC_48})

V_68 = Vertex(name = 'V_68',
              particles = [ P.p__tilde__, P.p, P.rho0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,0):C.GC_5,(0,1):C.GC_47})

V_69 = Vertex(name = 'V_69',
              particles = [ P.A, P.rho0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_69})

V_70 = Vertex(name = 'V_70',
              particles = [ P.n__tilde__, P.p, P.rho__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_49,(0,0):C.GC_7})

V_71 = Vertex(name = 'V_71',
              particles = [ P.A, P.rho__minus__, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_70})

V_72 = Vertex(name = 'V_72',
              particles = [ P.p__tilde__, P.n, P.rho__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_49,(0,0):C.GC_7})

V_73 = Vertex(name = 'V_73',
              particles = [ P.A, P.rho__plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_70})

V_74 = Vertex(name = 'V_74',
              particles = [ P.n__tilde__, P.N14400, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_13})

V_75 = Vertex(name = 'V_75',
              particles = [ P.n__tilde__, P.N1440__plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_15})

V_76 = Vertex(name = 'V_76',
              particles = [ P.p__tilde__, P.N14400, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_15})

V_77 = Vertex(name = 'V_77',
              particles = [ P.p__tilde__, P.N1440__plus__, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_14})

V_78 = Vertex(name = 'V_78',
              particles = [ P.N14400__tilde__, P.n, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_13})

V_79 = Vertex(name = 'V_79',
              particles = [ P.N1440__plus____tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_15})

V_80 = Vertex(name = 'V_80',
              particles = [ P.n__tilde__, P.n, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_64})

V_81 = Vertex(name = 'V_81',
              particles = [ P.p__tilde__, P.n, P.A, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1 ],
              couplings = {(0,0):C.GC_67})

V_82 = Vertex(name = 'V_82',
              particles = [ P.p__tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_65})

V_83 = Vertex(name = 'V_83',
              particles = [ P.N14400__tilde__, P.p, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_15})

V_84 = Vertex(name = 'V_84',
              particles = [ P.N1440__plus____tilde__, P.p, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_14})

V_85 = Vertex(name = 'V_85',
              particles = [ P.n__tilde__, P.p, P.A, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1 ],
              couplings = {(0,0):C.GC_66})

V_86 = Vertex(name = 'V_86',
              particles = [ P.n__tilde__, P.p, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_65})

V_87 = Vertex(name = 'V_87',
              particles = [ P.p__tilde__, P.p, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_63})

V_88 = Vertex(name = 'V_88',
              particles = [ P.n__tilde__, P.N14400, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_34})

V_89 = Vertex(name = 'V_89',
              particles = [ P.p__tilde__, P.N1440__plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_90 = Vertex(name = 'V_90',
              particles = [ P.N14400__tilde__, P.n, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_34})

V_91 = Vertex(name = 'V_91',
              particles = [ P.N1440__plus____tilde__, P.p, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_92 = Vertex(name = 'V_92',
              particles = [ P.n__tilde__, P.Delta__minus__, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS2 ],
              couplings = {(0,0):C.GC_28})

V_93 = Vertex(name = 'V_93',
              particles = [ P.n__tilde__, P.Delta__plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS2 ],
              couplings = {(0,0):C.GC_30})

V_94 = Vertex(name = 'V_94',
              particles = [ P.n__tilde__, P.Delta0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS2 ],
              couplings = {(0,0):C.GC_29})

V_95 = Vertex(name = 'V_95',
              particles = [ P.p__tilde__, P.Delta__plus__, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS2 ],
              couplings = {(0,0):C.GC_29})

V_96 = Vertex(name = 'V_96',
              particles = [ P.p__tilde__, P.Delta__plus____plus__, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS2 ],
              couplings = {(0,0):C.GC_27})

V_97 = Vertex(name = 'V_97',
              particles = [ P.p__tilde__, P.Delta0, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS2 ],
              couplings = {(0,0):C.GC_31})

V_98 = Vertex(name = 'V_98',
              particles = [ P.Delta__minus____tilde__, P.n, P.pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS2 ],
              couplings = {(0,0):C.GC_28})

V_99 = Vertex(name = 'V_99',
              particles = [ P.Delta__plus____tilde__, P.n, P.pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS2 ],
              couplings = {(0,0):C.GC_30})

V_100 = Vertex(name = 'V_100',
               particles = [ P.Delta0__tilde__, P.n, P.pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFS2 ],
               couplings = {(0,0):C.GC_29})

V_101 = Vertex(name = 'V_101',
               particles = [ P.Delta__plus____tilde__, P.p, P.pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFS2 ],
               couplings = {(0,0):C.GC_29})

V_102 = Vertex(name = 'V_102',
               particles = [ P.Delta__plus____plus____tilde__, P.p, P.pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFS2 ],
               couplings = {(0,0):C.GC_27})

V_103 = Vertex(name = 'V_103',
               particles = [ P.Delta0__tilde__, P.p, P.pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFS2 ],
               couplings = {(0,0):C.GC_31})

V_104 = Vertex(name = 'V_104',
               particles = [ P.n__tilde__, P.N15350, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_37})

V_105 = Vertex(name = 'V_105',
               particles = [ P.p__tilde__, P.N1535__plus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_39})

V_106 = Vertex(name = 'V_106',
               particles = [ P.n__tilde__, P.N16500, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_41})

V_107 = Vertex(name = 'V_107',
               particles = [ P.p__tilde__, P.N1650__plus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_43})

V_108 = Vertex(name = 'V_108',
               particles = [ P.n__tilde__, P.Delta16200, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_44})

V_109 = Vertex(name = 'V_109',
               particles = [ P.p__tilde__, P.Delta1620__plus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_44})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Delta16200__tilde__, P.n, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_45})

V_111 = Vertex(name = 'V_111',
               particles = [ P.N15350__tilde__, P.n, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_38})

V_112 = Vertex(name = 'V_112',
               particles = [ P.N16500__tilde__, P.n, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_42})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Delta1620__plus____tilde__, P.p, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_45})

V_114 = Vertex(name = 'V_114',
               particles = [ P.N1535__plus____tilde__, P.p, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_36})

V_115 = Vertex(name = 'V_115',
               particles = [ P.N1650__plus____tilde__, P.p, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_40})

