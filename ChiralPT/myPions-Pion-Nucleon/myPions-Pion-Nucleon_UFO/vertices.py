# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Mon 6 Oct 2025 13:33:19


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_26})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_88})

V_3 = Vertex(name = 'V_3',
             particles = [ P.A, P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_4})

V_4 = Vertex(name = 'V_4',
             particles = [ P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS4 ],
             couplings = {(0,0):C.GC_9})

V_5 = Vertex(name = 'V_5',
             particles = [ P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VSS1 ],
             couplings = {(0,0):C.GC_1})

V_6 = Vertex(name = 'V_6',
             particles = [ P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS2 ],
             couplings = {(0,0):C.GC_8})

V_7 = Vertex(name = 'V_7',
             particles = [ P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS3 ],
             couplings = {(0,0):C.GC_9})

V_8 = Vertex(name = 'V_8',
             particles = [ P.p__tilde__, P.p, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_9 = Vertex(name = 'V_9',
             particles = [ P.n__tilde__, P.n, P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.FFVSS1 ],
             couplings = {(0,0):C.GC_13})

V_10 = Vertex(name = 'V_10',
              particles = [ P.n__tilde__, P.n, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_6})

V_11 = Vertex(name = 'V_11',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_91})

V_12 = Vertex(name = 'V_12',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_92})

V_13 = Vertex(name = 'V_13',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_93})

V_14 = Vertex(name = 'V_14',
              particles = [ P.p__tilde__, P.n, P.A, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_14})

V_15 = Vertex(name = 'V_15',
              particles = [ P.p__tilde__, P.n, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_10})

V_16 = Vertex(name = 'V_16',
              particles = [ P.n__tilde__, P.p, P.A, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_14})

V_17 = Vertex(name = 'V_17',
              particles = [ P.n__tilde__, P.p, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_11})

V_18 = Vertex(name = 'V_18',
              particles = [ P.p__tilde__, P.p, P.A, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_12})

V_19 = Vertex(name = 'V_19',
              particles = [ P.p__tilde__, P.p, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_7})

V_20 = Vertex(name = 'V_20',
              particles = [ P.A, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_53})

V_21 = Vertex(name = 'V_21',
              particles = [ P.A, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_36})

V_22 = Vertex(name = 'V_22',
              particles = [ P.A, P.W__minus__, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_49})

V_23 = Vertex(name = 'V_23',
              particles = [ P.A, P.W__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_48})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_32})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS3 ],
              couplings = {(0,0):C.GC_44})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1 ],
              couplings = {(0,0):C.GC_45})

V_27 = Vertex(name = 'V_27',
              particles = [ P.n__tilde__, P.p, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_54,(0,0):C.GC_33})

V_28 = Vertex(name = 'V_28',
              particles = [ P.n__tilde__, P.n, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_60,(0,0):C.GC_43})

V_29 = Vertex(name = 'V_29',
              particles = [ P.n__tilde__, P.n, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_56,(0,0):C.GC_37})

V_30 = Vertex(name = 'V_30',
              particles = [ P.p__tilde__, P.n, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_58,(0,0):C.GC_41})

V_31 = Vertex(name = 'V_31',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_62,(0,0):C.GC_47})

V_32 = Vertex(name = 'V_32',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_59,(0,0):C.GC_40})

V_33 = Vertex(name = 'V_33',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_57,(0,0):C.GC_39})

V_34 = Vertex(name = 'V_34',
              particles = [ P.p__tilde__, P.p, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_61,(0,0):C.GC_42})

V_35 = Vertex(name = 'V_35',
              particles = [ P.p__tilde__, P.p, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_55,(0,0):C.GC_38})

V_36 = Vertex(name = 'V_36',
              particles = [ P.A, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_52})

V_37 = Vertex(name = 'V_37',
              particles = [ P.A, P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_36})

V_38 = Vertex(name = 'V_38',
              particles = [ P.A, P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_50})

V_39 = Vertex(name = 'V_39',
              particles = [ P.A, P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_51})

V_40 = Vertex(name = 'V_40',
              particles = [ P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_31})

V_41 = Vertex(name = 'V_41',
              particles = [ P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS3 ],
              couplings = {(0,0):C.GC_44})

V_42 = Vertex(name = 'V_42',
              particles = [ P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_45})

V_43 = Vertex(name = 'V_43',
              particles = [ P.p__tilde__, P.n, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_54,(0,0):C.GC_33})

V_44 = Vertex(name = 'V_44',
              particles = [ P.n__tilde__, P.n, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_61,(0,0):C.GC_42})

V_45 = Vertex(name = 'V_45',
              particles = [ P.n__tilde__, P.n, P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_56,(0,0):C.GC_37})

V_46 = Vertex(name = 'V_46',
              particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_63,(0,0):C.GC_46})

V_47 = Vertex(name = 'V_47',
              particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_59,(0,0):C.GC_40})

V_48 = Vertex(name = 'V_48',
              particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_57,(0,0):C.GC_39})

V_49 = Vertex(name = 'V_49',
              particles = [ P.n__tilde__, P.p, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_58,(0,0):C.GC_41})

V_50 = Vertex(name = 'V_50',
              particles = [ P.p__tilde__, P.p, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_60,(0,0):C.GC_43})

V_51 = Vertex(name = 'V_51',
              particles = [ P.p__tilde__, P.p, P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_55,(0,0):C.GC_38})

V_52 = Vertex(name = 'V_52',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_27})

V_53 = Vertex(name = 'V_53',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_30})

V_54 = Vertex(name = 'V_54',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_28})

V_55 = Vertex(name = 'V_55',
              particles = [ P.W__minus__, P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_29})

V_56 = Vertex(name = 'V_56',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_89})

V_57 = Vertex(name = 'V_57',
              particles = [ P.A, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_69})

V_58 = Vertex(name = 'V_58',
              particles = [ P.Z, P.Pi0, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.VSSS5 ],
              couplings = {(0,0):C.GC_74})

V_59 = Vertex(name = 'V_59',
              particles = [ P.Z, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS2 ],
              couplings = {(0,0):C.GC_73})

V_60 = Vertex(name = 'V_60',
              particles = [ P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_66})

V_61 = Vertex(name = 'V_61',
              particles = [ P.n__tilde__, P.n, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_78,(0,0):C.GC_65})

V_62 = Vertex(name = 'V_62',
              particles = [ P.p__tilde__, P.p, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_77,(0,0):C.GC_68})

V_63 = Vertex(name = 'V_63',
              particles = [ P.n__tilde__, P.n, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_79,(0,0):C.GC_70})

V_64 = Vertex(name = 'V_64',
              particles = [ P.p__tilde__, P.n, P.Z, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_83,(0,0):C.GC_76})

V_65 = Vertex(name = 'V_65',
              particles = [ P.p__tilde__, P.n, P.Z, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_81,(0,0):C.GC_72})

V_66 = Vertex(name = 'V_66',
              particles = [ P.n__tilde__, P.p, P.Z, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_82,(0,0):C.GC_75})

V_67 = Vertex(name = 'V_67',
              particles = [ P.n__tilde__, P.p, P.Z, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_81,(0,0):C.GC_72})

V_68 = Vertex(name = 'V_68',
              particles = [ P.p__tilde__, P.p, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_80,(0,0):C.GC_71})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__minus__, P.Z, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_19})

V_70 = Vertex(name = 'V_70',
              particles = [ P.W__minus__, P.Z, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_5})

V_71 = Vertex(name = 'V_71',
              particles = [ P.W__minus__, P.Z, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_17})

V_72 = Vertex(name = 'V_72',
              particles = [ P.W__minus__, P.Z, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_18})

V_73 = Vertex(name = 'V_73',
              particles = [ P.W__plus__, P.Z, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_20})

V_74 = Vertex(name = 'V_74',
              particles = [ P.W__plus__, P.Z, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_5})

V_75 = Vertex(name = 'V_75',
              particles = [ P.W__plus__, P.Z, P.Pi0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_16})

V_76 = Vertex(name = 'V_76',
              particles = [ P.W__plus__, P.Z, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_15})

V_77 = Vertex(name = 'V_77',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_84})

V_78 = Vertex(name = 'V_78',
              particles = [ P.Z, P.Z, P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_87})

V_79 = Vertex(name = 'V_79',
              particles = [ P.Z, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_3})

V_80 = Vertex(name = 'V_80',
              particles = [ P.Z, P.Z, P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_85})

V_81 = Vertex(name = 'V_81',
              particles = [ P.Z, P.Z, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_86})

V_82 = Vertex(name = 'V_82',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_90})

V_83 = Vertex(name = 'V_83',
              particles = [ P.e__plus__, P.e__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_84 = Vertex(name = 'V_84',
              particles = [ P.mu__plus__, P.mu__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_85 = Vertex(name = 'V_85',
              particles = [ P.ta__plus__, P.ta__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_86 = Vertex(name = 'V_86',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_34})

V_87 = Vertex(name = 'V_87',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_34})

V_88 = Vertex(name = 'V_88',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_34})

V_89 = Vertex(name = 'V_89',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_34})

V_90 = Vertex(name = 'V_90',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_34})

V_91 = Vertex(name = 'V_91',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_34})

V_92 = Vertex(name = 'V_92',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_67})

V_93 = Vertex(name = 'V_93',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_67})

V_94 = Vertex(name = 'V_94',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_67})

V_95 = Vertex(name = 'V_95',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_64})

V_96 = Vertex(name = 'V_96',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_64})

V_97 = Vertex(name = 'V_97',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_64})

V_98 = Vertex(name = 'V_98',
              particles = [ P.n__tilde__, P.n, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_22})

V_99 = Vertex(name = 'V_99',
              particles = [ P.p__tilde__, P.n, P.A, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS2 ],
              couplings = {(0,0):C.GC_24})

V_100 = Vertex(name = 'V_100',
               particles = [ P.p__tilde__, P.n, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_23})

V_101 = Vertex(name = 'V_101',
               particles = [ P.n__tilde__, P.p, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_25})

V_102 = Vertex(name = 'V_102',
               particles = [ P.n__tilde__, P.p, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_23})

V_103 = Vertex(name = 'V_103',
               particles = [ P.p__tilde__, P.p, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_21})

