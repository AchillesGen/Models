# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Wed 3 Sep 2025 23:28:42


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.A, P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVSS2 ],
             couplings = {(0,0):C.GC_4})

V_2 = Vertex(name = 'V_2',
             particles = [ P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS6 ],
             couplings = {(0,0):C.GC_9})

V_3 = Vertex(name = 'V_3',
             particles = [ P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VSS2 ],
             couplings = {(0,0):C.GC_1})

V_4 = Vertex(name = 'V_4',
             particles = [ P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS4 ],
             couplings = {(0,0):C.GC_8})

V_5 = Vertex(name = 'V_5',
             particles = [ P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS5 ],
             couplings = {(0,0):C.GC_9})

V_6 = Vertex(name = 'V_6',
             particles = [ P.p__tilde__, P.p, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV3 ],
             couplings = {(0,0):C.GC_2})

V_7 = Vertex(name = 'V_7',
             particles = [ P.n__tilde__, P.n, P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.FFVSS3 ],
             couplings = {(0,0):C.GC_13})

V_8 = Vertex(name = 'V_8',
             particles = [ P.n__tilde__, P.n, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.FFSS2 ],
             couplings = {(0,0):C.GC_6})

V_9 = Vertex(name = 'V_9',
             particles = [ P.p__tilde__, P.n, P.A, P.Pi0, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.FFVSS3 ],
             couplings = {(0,0):C.GC_14})

V_10 = Vertex(name = 'V_10',
              particles = [ P.p__tilde__, P.n, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_10})

V_11 = Vertex(name = 'V_11',
              particles = [ P.n__tilde__, P.p, P.A, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3 ],
              couplings = {(0,0):C.GC_14})

V_12 = Vertex(name = 'V_12',
              particles = [ P.n__tilde__, P.p, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_11})

V_13 = Vertex(name = 'V_13',
              particles = [ P.p__tilde__, P.p, P.A, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3 ],
              couplings = {(0,0):C.GC_12})

V_14 = Vertex(name = 'V_14',
              particles = [ P.p__tilde__, P.p, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_7})

V_15 = Vertex(name = 'V_15',
              particles = [ P.A, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_49})

V_16 = Vertex(name = 'V_16',
              particles = [ P.A, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_32})

V_17 = Vertex(name = 'V_17',
              particles = [ P.A, P.W__minus__, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_45})

V_18 = Vertex(name = 'V_18',
              particles = [ P.A, P.W__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_44})

V_19 = Vertex(name = 'V_19',
              particles = [ P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_30})

V_20 = Vertex(name = 'V_20',
              particles = [ P.W__minus__, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS8 ],
              couplings = {(0,0):C.GC_40})

V_21 = Vertex(name = 'V_21',
              particles = [ P.W__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS6 ],
              couplings = {(0,0):C.GC_41})

V_22 = Vertex(name = 'V_22',
              particles = [ P.n__tilde__, P.p, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_50,(0,0):C.GC_31})

V_23 = Vertex(name = 'V_23',
              particles = [ P.n__tilde__, P.n, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_56,(0,0):C.GC_39})

V_24 = Vertex(name = 'V_24',
              particles = [ P.n__tilde__, P.n, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_52,(0,0):C.GC_33})

V_25 = Vertex(name = 'V_25',
              particles = [ P.p__tilde__, P.n, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_54,(0,0):C.GC_37})

V_26 = Vertex(name = 'V_26',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_58,(0,0):C.GC_43})

V_27 = Vertex(name = 'V_27',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_55,(0,0):C.GC_36})

V_28 = Vertex(name = 'V_28',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_53,(0,0):C.GC_35})

V_29 = Vertex(name = 'V_29',
              particles = [ P.p__tilde__, P.p, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_57,(0,0):C.GC_38})

V_30 = Vertex(name = 'V_30',
              particles = [ P.p__tilde__, P.p, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_51,(0,0):C.GC_34})

V_31 = Vertex(name = 'V_31',
              particles = [ P.A, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_48})

V_32 = Vertex(name = 'V_32',
              particles = [ P.A, P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_32})

V_33 = Vertex(name = 'V_33',
              particles = [ P.A, P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_46})

V_34 = Vertex(name = 'V_34',
              particles = [ P.A, P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_47})

V_35 = Vertex(name = 'V_35',
              particles = [ P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_29})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS8 ],
              couplings = {(0,0):C.GC_40})

V_37 = Vertex(name = 'V_37',
              particles = [ P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS9 ],
              couplings = {(0,0):C.GC_41})

V_38 = Vertex(name = 'V_38',
              particles = [ P.p__tilde__, P.n, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_50,(0,0):C.GC_31})

V_39 = Vertex(name = 'V_39',
              particles = [ P.n__tilde__, P.n, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_57,(0,0):C.GC_38})

V_40 = Vertex(name = 'V_40',
              particles = [ P.n__tilde__, P.n, P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_52,(0,0):C.GC_33})

V_41 = Vertex(name = 'V_41',
              particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_59,(0,0):C.GC_42})

V_42 = Vertex(name = 'V_42',
              particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_55,(0,0):C.GC_36})

V_43 = Vertex(name = 'V_43',
              particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_53,(0,0):C.GC_35})

V_44 = Vertex(name = 'V_44',
              particles = [ P.n__tilde__, P.p, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_54,(0,0):C.GC_37})

V_45 = Vertex(name = 'V_45',
              particles = [ P.p__tilde__, P.p, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_56,(0,0):C.GC_39})

V_46 = Vertex(name = 'V_46',
              particles = [ P.p__tilde__, P.p, P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_51,(0,0):C.GC_34})

V_47 = Vertex(name = 'V_47',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS2 ],
              couplings = {(0,0):C.GC_28})

V_48 = Vertex(name = 'V_48',
              particles = [ P.W__minus__, P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS2 ],
              couplings = {(0,0):C.GC_26})

V_49 = Vertex(name = 'V_49',
              particles = [ P.W__minus__, P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS2 ],
              couplings = {(0,0):C.GC_27})

V_50 = Vertex(name = 'V_50',
              particles = [ P.A, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_63})

V_51 = Vertex(name = 'V_51',
              particles = [ P.Z, P.Pi0, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.VSSS10 ],
              couplings = {(0,0):C.GC_68})

V_52 = Vertex(name = 'V_52',
              particles = [ P.Z, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS7 ],
              couplings = {(0,0):C.GC_67})

V_53 = Vertex(name = 'V_53',
              particles = [ P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_61})

V_54 = Vertex(name = 'V_54',
              particles = [ P.n__tilde__, P.n, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_72,(0,0):C.GC_60})

V_55 = Vertex(name = 'V_55',
              particles = [ P.p__tilde__, P.p, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_71,(0,0):C.GC_62})

V_56 = Vertex(name = 'V_56',
              particles = [ P.n__tilde__, P.n, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_73,(0,0):C.GC_64})

V_57 = Vertex(name = 'V_57',
              particles = [ P.p__tilde__, P.n, P.Z, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_77,(0,0):C.GC_70})

V_58 = Vertex(name = 'V_58',
              particles = [ P.p__tilde__, P.n, P.Z, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_75,(0,0):C.GC_66})

V_59 = Vertex(name = 'V_59',
              particles = [ P.n__tilde__, P.p, P.Z, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS3, L.FFVS4 ],
              couplings = {(0,1):C.GC_76,(0,0):C.GC_69})

V_60 = Vertex(name = 'V_60',
              particles = [ P.n__tilde__, P.p, P.Z, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_75,(0,0):C.GC_66})

V_61 = Vertex(name = 'V_61',
              particles = [ P.p__tilde__, P.p, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS3, L.FFVSS4 ],
              couplings = {(0,1):C.GC_74,(0,0):C.GC_65})

V_62 = Vertex(name = 'V_62',
              particles = [ P.W__minus__, P.Z, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_19})

V_63 = Vertex(name = 'V_63',
              particles = [ P.W__minus__, P.Z, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_5})

V_64 = Vertex(name = 'V_64',
              particles = [ P.W__minus__, P.Z, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_17})

V_65 = Vertex(name = 'V_65',
              particles = [ P.W__minus__, P.Z, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_18})

V_66 = Vertex(name = 'V_66',
              particles = [ P.W__plus__, P.Z, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_20})

V_67 = Vertex(name = 'V_67',
              particles = [ P.W__plus__, P.Z, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_5})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__plus__, P.Z, P.Pi0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_16})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__plus__, P.Z, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2 ],
              couplings = {(0,0):C.GC_15})

V_70 = Vertex(name = 'V_70',
              particles = [ P.Z, P.Z, P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS2 ],
              couplings = {(0,0):C.GC_80})

V_71 = Vertex(name = 'V_71',
              particles = [ P.Z, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_3})

V_72 = Vertex(name = 'V_72',
              particles = [ P.Z, P.Z, P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS2 ],
              couplings = {(0,0):C.GC_78})

V_73 = Vertex(name = 'V_73',
              particles = [ P.Z, P.Z, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS2 ],
              couplings = {(0,0):C.GC_79})

V_74 = Vertex(name = 'V_74',
              particles = [ P.n__tilde__, P.n, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_22})

V_75 = Vertex(name = 'V_75',
              particles = [ P.p__tilde__, P.n, P.A, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS4 ],
              couplings = {(0,0):C.GC_24})

V_76 = Vertex(name = 'V_76',
              particles = [ P.p__tilde__, P.n, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_23})

V_77 = Vertex(name = 'V_77',
              particles = [ P.n__tilde__, P.p, P.A, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS4 ],
              couplings = {(0,0):C.GC_25})

V_78 = Vertex(name = 'V_78',
              particles = [ P.n__tilde__, P.p, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_23})

V_79 = Vertex(name = 'V_79',
              particles = [ P.p__tilde__, P.p, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_21})

