# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Wed 29 Oct 2025 00:14:05


from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_122})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_443})

V_3 = Vertex(name = 'V_3',
             particles = [ P.A, P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_12})

V_4 = Vertex(name = 'V_4',
             particles = [ P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS4 ],
             couplings = {(0,0):C.GC_21})

V_5 = Vertex(name = 'V_5',
             particles = [ P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VSS1 ],
             couplings = {(0,0):C.GC_3})

V_6 = Vertex(name = 'V_6',
             particles = [ P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS2 ],
             couplings = {(0,0):C.GC_20})

V_7 = Vertex(name = 'V_7',
             particles = [ P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS3 ],
             couplings = {(0,0):C.GC_21})

V_8 = Vertex(name = 'V_8',
             particles = [ P.p__tilde__, P.p, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_9 = Vertex(name = 'V_9',
             particles = [ P.Delta0Bar, P.Delta0, P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
             couplings = {(0,1):C.GC_42,(0,2):C.GC_51,(0,0):C.GC_57})

V_10 = Vertex(name = 'V_10',
              particles = [ P.Delta0Bar, P.Delta0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_27,(0,2):C.GC_15,(0,0):C.GC_35})

V_11 = Vertex(name = 'V_11',
              particles = [ P.Delta__minus__bar, P.Delta0, P.A, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_48,(0,2):C.GC_55,(0,0):C.GC_61})

V_12 = Vertex(name = 'V_12',
              particles = [ P.Delta__minus__bar, P.Delta0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_30,(0,2):C.GC_22,(0,0):C.GC_38})

V_13 = Vertex(name = 'V_13',
              particles = [ P.Delta0Bar, P.Delta__minus__, P.A, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_48,(0,2):C.GC_55,(0,0):C.GC_61})

V_14 = Vertex(name = 'V_14',
              particles = [ P.Delta0Bar, P.Delta__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_31,(0,2):C.GC_23,(0,0):C.GC_39})

V_15 = Vertex(name = 'V_15',
              particles = [ P.Delta__minus__bar, P.Delta__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV4, L.RRV5 ],
              couplings = {(0,1):C.GC_2,(0,2):C.GC_6,(0,0):C.GC_9})

V_16 = Vertex(name = 'V_16',
              particles = [ P.Delta__minus__bar, P.Delta__minus__, P.A, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_46,(0,2):C.GC_53,(0,0):C.GC_59})

V_17 = Vertex(name = 'V_17',
              particles = [ P.Delta__minus__bar, P.Delta__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_29,(0,2):C.GC_19,(0,0):C.GC_37})

V_18 = Vertex(name = 'V_18',
              particles = [ P.Delta__minus__Bar, P.Delta0, P.A, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_49,(0,2):C.GC_56,(0,0):C.GC_62})

V_19 = Vertex(name = 'V_19',
              particles = [ P.Delta__minus__Bar, P.Delta0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_33,(0,0):C.GC_41,(0,2):C.GC_25})

V_20 = Vertex(name = 'V_20',
              particles = [ P.Delta0Bar, P.Delta__plus__, P.A, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_49,(0,2):C.GC_56,(0,0):C.GC_62})

V_21 = Vertex(name = 'V_21',
              particles = [ P.Delta0Bar, P.Delta__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_32,(0,2):C.GC_24,(0,0):C.GC_40})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV4, L.RRV5 ],
              couplings = {(0,1):C.GC_1,(0,2):C.GC_5,(0,0):C.GC_8})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.A, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_43,(0,2):C.GC_52,(0,0):C.GC_58})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_26,(0,2):C.GC_14,(0,0):C.GC_34})

V_25 = Vertex(name = 'V_25',
              particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.A, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_48,(0,2):C.GC_55,(0,0):C.GC_61})

V_26 = Vertex(name = 'V_26',
              particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_31,(0,2):C.GC_23,(0,0):C.GC_39})

V_27 = Vertex(name = 'V_27',
              particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.A, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_48,(0,2):C.GC_55,(0,0):C.GC_61})

V_28 = Vertex(name = 'V_28',
              particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_30,(0,2):C.GC_22,(0,0):C.GC_38})

V_29 = Vertex(name = 'V_29',
              particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV4, L.RRV5 ],
              couplings = {(0,1):C.GC_3,(0,2):C.GC_7,(0,0):C.GC_10})

V_30 = Vertex(name = 'V_30',
              particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.A, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS5, L.RRVSS6 ],
              couplings = {(0,1):C.GC_47,(0,2):C.GC_54,(0,0):C.GC_60})

V_31 = Vertex(name = 'V_31',
              particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS2, L.RRSS3, L.RRSS4 ],
              couplings = {(0,1):C.GC_28,(0,2):C.GC_18,(0,0):C.GC_36})

V_32 = Vertex(name = 'V_32',
              particles = [ P.n__tilde__, P.Delta0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS1, L.FRS2, L.FRS3 ],
              couplings = {(0,0):C.GC_115,(0,2):C.GC_106,(0,1):C.GC_451})

V_33 = Vertex(name = 'V_33',
              particles = [ P.n__tilde__, P.Delta__minus__, P.A, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
              couplings = {(0,1):C.GC_118,(0,0):C.GC_455,(0,2):C.GC_110})

V_34 = Vertex(name = 'V_34',
              particles = [ P.n__tilde__, P.Delta__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1, L.FRS2, L.FRS3 ],
              couplings = {(0,0):C.GC_114,(0,2):C.GC_105,(0,1):C.GC_450})

V_35 = Vertex(name = 'V_35',
              particles = [ P.n__tilde__, P.Delta__plus__, P.A, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
              couplings = {(0,1):C.GC_120,(0,0):C.GC_457,(0,2):C.GC_112})

V_36 = Vertex(name = 'V_36',
              particles = [ P.n__tilde__, P.Delta__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1, L.FRS2, L.FRS3 ],
              couplings = {(0,0):C.GC_116,(0,2):C.GC_107,(0,1):C.GC_452})

V_37 = Vertex(name = 'V_37',
              particles = [ P.Delta__minus__bar, P.n, P.A, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
              couplings = {(0,1):C.GC_119,(0,0):C.GC_454,(0,2):C.GC_109})

V_38 = Vertex(name = 'V_38',
              particles = [ P.Delta__minus__bar, P.n, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1, L.RFS2, L.RFS3 ],
              couplings = {(0,1):C.GC_114,(0,2):C.GC_105,(0,0):C.GC_450})

V_39 = Vertex(name = 'V_39',
              particles = [ P.Delta__minus__Bar, P.n, P.A, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
              couplings = {(0,1):C.GC_121,(0,0):C.GC_456,(0,2):C.GC_111})

V_40 = Vertex(name = 'V_40',
              particles = [ P.Delta__minus__Bar, P.n, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1, L.RFS2, L.RFS3 ],
              couplings = {(0,1):C.GC_116,(0,2):C.GC_107,(0,0):C.GC_452})

V_41 = Vertex(name = 'V_41',
              particles = [ P.Delta0Bar, P.n, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RFS1, L.RFS2, L.RFS3 ],
              couplings = {(0,1):C.GC_115,(0,2):C.GC_106,(0,0):C.GC_451})

V_42 = Vertex(name = 'V_42',
              particles = [ P.n__tilde__, P.n, P.A, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_45})

V_43 = Vertex(name = 'V_43',
              particles = [ P.n__tilde__, P.n, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_16})

V_44 = Vertex(name = 'V_44',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_446})

V_45 = Vertex(name = 'V_45',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_447})

V_46 = Vertex(name = 'V_46',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_448})

V_47 = Vertex(name = 'V_47',
              particles = [ P.p__tilde__, P.Delta0, P.A, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
              couplings = {(0,1):C.GC_120,(0,0):C.GC_457,(0,2):C.GC_112})

V_48 = Vertex(name = 'V_48',
              particles = [ P.p__tilde__, P.Delta0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1, L.FRS2, L.FRS3 ],
              couplings = {(0,0):C.GC_117,(0,2):C.GC_108,(0,1):C.GC_453})

V_49 = Vertex(name = 'V_49',
              particles = [ P.p__tilde__, P.Delta__plus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FRS1, L.FRS2, L.FRS3 ],
              couplings = {(0,0):C.GC_115,(0,2):C.GC_106,(0,1):C.GC_451})

V_50 = Vertex(name = 'V_50',
              particles = [ P.p__tilde__, P.Delta__plus____plus__, P.A, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
              couplings = {(0,1):C.GC_118,(0,0):C.GC_455,(0,2):C.GC_110})

V_51 = Vertex(name = 'V_51',
              particles = [ P.p__tilde__, P.Delta__plus____plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRS1, L.FRS2, L.FRS3 ],
              couplings = {(0,0):C.GC_113,(0,2):C.GC_104,(0,1):C.GC_449})

V_52 = Vertex(name = 'V_52',
              particles = [ P.p__tilde__, P.n, P.A, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_50})

V_53 = Vertex(name = 'V_53',
              particles = [ P.p__tilde__, P.n, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_24})

V_54 = Vertex(name = 'V_54',
              particles = [ P.Delta0Bar, P.p, P.A, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
              couplings = {(0,1):C.GC_121,(0,0):C.GC_456,(0,2):C.GC_111})

V_55 = Vertex(name = 'V_55',
              particles = [ P.Delta0Bar, P.p, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1, L.RFS2, L.RFS3 ],
              couplings = {(0,1):C.GC_117,(0,2):C.GC_108,(0,0):C.GC_453})

V_56 = Vertex(name = 'V_56',
              particles = [ P.Delta__minus____minus__Bar, P.p, P.A, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
              couplings = {(0,1):C.GC_119,(0,0):C.GC_454,(0,2):C.GC_109})

V_57 = Vertex(name = 'V_57',
              particles = [ P.Delta__minus____minus__Bar, P.p, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFS1, L.RFS2, L.RFS3 ],
              couplings = {(0,1):C.GC_113,(0,2):C.GC_104,(0,0):C.GC_449})

V_58 = Vertex(name = 'V_58',
              particles = [ P.Delta__minus__Bar, P.p, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RFS1, L.RFS2, L.RFS3 ],
              couplings = {(0,1):C.GC_115,(0,2):C.GC_106,(0,0):C.GC_451})

V_59 = Vertex(name = 'V_59',
              particles = [ P.n__tilde__, P.p, P.A, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_50})

V_60 = Vertex(name = 'V_60',
              particles = [ P.n__tilde__, P.p, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_25})

V_61 = Vertex(name = 'V_61',
              particles = [ P.p__tilde__, P.p, P.A, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_44})

V_62 = Vertex(name = 'V_62',
              particles = [ P.p__tilde__, P.p, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_17})

V_63 = Vertex(name = 'V_63',
              particles = [ P.A, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_207})

V_64 = Vertex(name = 'V_64',
              particles = [ P.A, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_138})

V_65 = Vertex(name = 'V_65',
              particles = [ P.A, P.W__minus__, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_203})

V_66 = Vertex(name = 'V_66',
              particles = [ P.A, P.W__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_202})

V_67 = Vertex(name = 'V_67',
              particles = [ P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_128})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__minus__, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS3 ],
              couplings = {(0,0):C.GC_179})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1 ],
              couplings = {(0,0):C.GC_180})

V_70 = Vertex(name = 'V_70',
              particles = [ P.n__tilde__, P.p, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_268,(0,0):C.GC_131})

V_71 = Vertex(name = 'V_71',
              particles = [ P.n__tilde__, P.n, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_274,(0,0):C.GC_177})

V_72 = Vertex(name = 'V_72',
              particles = [ P.n__tilde__, P.n, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_270,(0,0):C.GC_141})

V_73 = Vertex(name = 'V_73',
              particles = [ P.p__tilde__, P.n, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_272,(0,0):C.GC_151})

V_74 = Vertex(name = 'V_74',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_276,(0,0):C.GC_184})

V_75 = Vertex(name = 'V_75',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_273,(0,0):C.GC_150})

V_76 = Vertex(name = 'V_76',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_271,(0,0):C.GC_148})

V_77 = Vertex(name = 'V_77',
              particles = [ P.p__tilde__, P.p, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2 ],
              couplings = {(0,1):C.GC_275,(0,0):C.GC_174})

V_78 = Vertex(name = 'V_78',
              particles = [ P.p__tilde__, P.p, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,1):C.GC_269,(0,0):C.GC_142})

V_79 = Vertex(name = 'V_79',
              particles = [ P.Delta0Bar, P.Delta0, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
              couplings = {(0,3):C.GC_176,(0,4):C.GC_187,(0,0):C.GC_195,(0,1):C.GC_262,(0,2):C.GC_221,(0,5):C.GC_241})

V_80 = Vertex(name = 'V_80',
              particles = [ P.Delta0Bar, P.Delta0, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_140,(0,4):C.GC_153,(0,0):C.GC_163,(0,1):C.GC_251,(0,2):C.GC_210,(0,5):C.GC_230})

V_81 = Vertex(name = 'V_81',
              particles = [ P.Delta__minus__bar, P.Delta0, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_129,(0,4):C.GC_133,(0,0):C.GC_135,(0,1):C.GC_249,(0,2):C.GC_209,(0,5):C.GC_229})

V_82 = Vertex(name = 'V_82',
              particles = [ P.Delta__minus__bar, P.Delta0, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
              couplings = {(0,3):C.GC_182,(0,4):C.GC_190,(0,0):C.GC_198,(0,1):C.GC_267,(0,2):C.GC_226,(0,5):C.GC_246})

V_83 = Vertex(name = 'V_83',
              particles = [ P.Delta__minus__bar, P.Delta0, P.W__minus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_147,(0,4):C.GC_158,(0,0):C.GC_168,(0,1):C.GC_259,(0,2):C.GC_218,(0,5):C.GC_238})

V_84 = Vertex(name = 'V_84',
              particles = [ P.Delta__minus__bar, P.Delta0, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_145,(0,4):C.GC_156,(0,0):C.GC_166,(0,1):C.GC_257,(0,2):C.GC_217,(0,5):C.GC_237})

V_85 = Vertex(name = 'V_85',
              particles = [ P.Delta0Bar, P.Delta__minus__, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_146,(0,4):C.GC_157,(0,0):C.GC_167,(0,1):C.GC_258,(0,2):C.GC_219,(0,5):C.GC_239})

V_86 = Vertex(name = 'V_86',
              particles = [ P.Delta__minus__bar, P.Delta__minus__, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
              couplings = {(0,4):C.GC_188,(0,0):C.GC_196,(0,1):C.GC_263,(0,3):C.GC_178,(0,2):C.GC_220,(0,5):C.GC_240})

V_87 = Vertex(name = 'V_87',
              particles = [ P.Delta__minus__bar, P.Delta__minus__, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_144,(0,4):C.GC_155,(0,0):C.GC_165,(0,1):C.GC_253,(0,2):C.GC_212,(0,5):C.GC_232})

V_88 = Vertex(name = 'V_88',
              particles = [ P.Delta__minus__Bar, P.Delta0, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_150,(0,4):C.GC_160,(0,0):C.GC_170,(0,1):C.GC_255,(0,2):C.GC_216,(0,5):C.GC_236})

V_89 = Vertex(name = 'V_89',
              particles = [ P.Delta0Bar, P.Delta__plus__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_130,(0,4):C.GC_134,(0,0):C.GC_136,(0,1):C.GC_248,(0,2):C.GC_208,(0,5):C.GC_228})

V_90 = Vertex(name = 'V_90',
              particles = [ P.Delta0Bar, P.Delta__plus__, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
              couplings = {(0,3):C.GC_184,(0,4):C.GC_192,(0,0):C.GC_200,(0,1):C.GC_265,(0,2):C.GC_224,(0,5):C.GC_244})

V_91 = Vertex(name = 'V_91',
              particles = [ P.Delta0Bar, P.Delta__plus__, P.W__minus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_151,(0,4):C.GC_161,(0,0):C.GC_171,(0,1):C.GC_256,(0,2):C.GC_215,(0,5):C.GC_235})

V_92 = Vertex(name = 'V_92',
              particles = [ P.Delta0Bar, P.Delta__plus__, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_149,(0,4):C.GC_159,(0,0):C.GC_169,(0,1):C.GC_254,(0,2):C.GC_214,(0,5):C.GC_234})

V_93 = Vertex(name = 'V_93',
              particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
              couplings = {(0,3):C.GC_175,(0,4):C.GC_186,(0,0):C.GC_194,(0,1):C.GC_261,(0,2):C.GC_222,(0,5):C.GC_242})

V_94 = Vertex(name = 'V_94',
              particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_139,(0,4):C.GC_152,(0,0):C.GC_162,(0,1):C.GC_250,(0,2):C.GC_211,(0,5):C.GC_231})

V_95 = Vertex(name = 'V_95',
              particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_146,(0,4):C.GC_157,(0,0):C.GC_167,(0,1):C.GC_258,(0,2):C.GC_219,(0,5):C.GC_239})

V_96 = Vertex(name = 'V_96',
              particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_129,(0,4):C.GC_133,(0,0):C.GC_135,(0,1):C.GC_249,(0,2):C.GC_209,(0,5):C.GC_229})

V_97 = Vertex(name = 'V_97',
              particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
              couplings = {(0,3):C.GC_182,(0,4):C.GC_190,(0,0):C.GC_198,(0,1):C.GC_267,(0,2):C.GC_226,(0,5):C.GC_246})

V_98 = Vertex(name = 'V_98',
              particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.W__minus__, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_147,(0,4):C.GC_158,(0,0):C.GC_168,(0,1):C.GC_259,(0,2):C.GC_218,(0,5):C.GC_238})

V_99 = Vertex(name = 'V_99',
              particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
              couplings = {(0,3):C.GC_145,(0,4):C.GC_156,(0,0):C.GC_166,(0,1):C.GC_257,(0,2):C.GC_217,(0,5):C.GC_237})

V_100 = Vertex(name = 'V_100',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_173,(0,4):C.GC_185,(0,0):C.GC_193,(0,1):C.GC_260,(0,2):C.GC_223,(0,5):C.GC_243})

V_101 = Vertex(name = 'V_101',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.W__minus__, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_143,(0,4):C.GC_154,(0,0):C.GC_164,(0,1):C.GC_252,(0,2):C.GC_213,(0,5):C.GC_233})

V_102 = Vertex(name = 'V_102',
               particles = [ P.n__tilde__, P.Delta0, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_315,(0,0):C.GC_475,(0,2):C.GC_295})

V_103 = Vertex(name = 'V_103',
               particles = [ P.n__tilde__, P.Delta0, P.W__minus__, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_104 = Vertex(name = 'V_104',
               particles = [ P.n__tilde__, P.Delta__minus__, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_301,(0,0):C.GC_464,(0,2):C.GC_284})

V_105 = Vertex(name = 'V_105',
               particles = [ P.n__tilde__, P.Delta__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRV1, L.FRV2, L.FRV3 ],
               couplings = {(0,1):C.GC_300,(0,0):C.GC_461,(0,2):C.GC_281})

V_106 = Vertex(name = 'V_106',
               particles = [ P.n__tilde__, P.Delta__plus__, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_313,(0,0):C.GC_473,(0,2):C.GC_293})

V_107 = Vertex(name = 'V_107',
               particles = [ P.n__tilde__, P.Delta__plus__, P.W__minus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_305,(0,0):C.GC_468,(0,2):C.GC_288})

V_108 = Vertex(name = 'V_108',
               particles = [ P.n__tilde__, P.Delta__plus__, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_306,(0,0):C.GC_466,(0,2):C.GC_286})

V_109 = Vertex(name = 'V_109',
               particles = [ P.Delta__minus__bar, P.n, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFV1, L.RFV2, L.RFV3 ],
               couplings = {(0,1):C.GC_297,(0,0):C.GC_458,(0,2):C.GC_278})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Delta__minus__bar, P.n, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_310,(0,0):C.GC_472,(0,2):C.GC_292})

V_111 = Vertex(name = 'V_111',
               particles = [ P.Delta__minus__bar, P.n, P.W__minus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_304,(0,0):C.GC_465,(0,2):C.GC_285})

V_112 = Vertex(name = 'V_112',
               particles = [ P.Delta__minus__bar, P.n, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_303,(0,0):C.GC_463,(0,2):C.GC_283})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Delta__minus__Bar, P.n, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_308,(0,0):C.GC_469,(0,2):C.GC_289})

V_114 = Vertex(name = 'V_114',
               particles = [ P.Delta0Bar, P.n, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_315,(0,0):C.GC_475,(0,2):C.GC_295})

V_115 = Vertex(name = 'V_115',
               particles = [ P.Delta0Bar, P.n, P.W__minus__, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_116 = Vertex(name = 'V_116',
               particles = [ P.p__tilde__, P.Delta0, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_305,(0,0):C.GC_468,(0,2):C.GC_288})

V_117 = Vertex(name = 'V_117',
               particles = [ P.p__tilde__, P.Delta__plus__, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_315,(0,0):C.GC_475,(0,2):C.GC_295})

V_118 = Vertex(name = 'V_118',
               particles = [ P.p__tilde__, P.Delta__plus__, P.W__minus__, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_119 = Vertex(name = 'V_119',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRV1, L.FRV2, L.FRV3 ],
               couplings = {(0,1):C.GC_298,(0,0):C.GC_459,(0,2):C.GC_279})

V_120 = Vertex(name = 'V_120',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_311,(0,0):C.GC_471,(0,2):C.GC_291})

V_121 = Vertex(name = 'V_121',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.W__minus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_301,(0,0):C.GC_464,(0,2):C.GC_284})

V_122 = Vertex(name = 'V_122',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_302,(0,0):C.GC_462,(0,2):C.GC_282})

V_123 = Vertex(name = 'V_123',
               particles = [ P.Delta0Bar, P.p, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFV1, L.RFV2, L.RFV3 ],
               couplings = {(0,1):C.GC_299,(0,0):C.GC_460,(0,2):C.GC_280})

V_124 = Vertex(name = 'V_124',
               particles = [ P.Delta0Bar, P.p, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_312,(0,0):C.GC_474,(0,2):C.GC_294})

V_125 = Vertex(name = 'V_125',
               particles = [ P.Delta0Bar, P.p, P.W__minus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_308,(0,0):C.GC_469,(0,2):C.GC_289})

V_126 = Vertex(name = 'V_126',
               particles = [ P.Delta0Bar, P.p, P.W__minus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_307,(0,0):C.GC_467,(0,2):C.GC_287})

V_127 = Vertex(name = 'V_127',
               particles = [ P.Delta__minus____minus__Bar, P.p, P.W__minus__, P.Pi__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_304,(0,0):C.GC_465,(0,2):C.GC_285})

V_128 = Vertex(name = 'V_128',
               particles = [ P.Delta__minus__Bar, P.p, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_315,(0,0):C.GC_475,(0,2):C.GC_295})

V_129 = Vertex(name = 'V_129',
               particles = [ P.Delta__minus__Bar, P.p, P.W__minus__, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_130 = Vertex(name = 'V_130',
               particles = [ P.A, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_206})

V_131 = Vertex(name = 'V_131',
               particles = [ P.A, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_138})

V_132 = Vertex(name = 'V_132',
               particles = [ P.A, P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_204})

V_133 = Vertex(name = 'V_133',
               particles = [ P.A, P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_205})

V_134 = Vertex(name = 'V_134',
               particles = [ P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_127})

V_135 = Vertex(name = 'V_135',
               particles = [ P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS3 ],
               couplings = {(0,0):C.GC_179})

V_136 = Vertex(name = 'V_136',
               particles = [ P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS4 ],
               couplings = {(0,0):C.GC_180})

V_137 = Vertex(name = 'V_137',
               particles = [ P.p__tilde__, P.n, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_268,(0,0):C.GC_131})

V_138 = Vertex(name = 'V_138',
               particles = [ P.n__tilde__, P.n, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_275,(0,0):C.GC_174})

V_139 = Vertex(name = 'V_139',
               particles = [ P.n__tilde__, P.n, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_270,(0,0):C.GC_141})

V_140 = Vertex(name = 'V_140',
               particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_277,(0,0):C.GC_183})

V_141 = Vertex(name = 'V_141',
               particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_273,(0,0):C.GC_150})

V_142 = Vertex(name = 'V_142',
               particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_271,(0,0):C.GC_148})

V_143 = Vertex(name = 'V_143',
               particles = [ P.n__tilde__, P.p, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_272,(0,0):C.GC_151})

V_144 = Vertex(name = 'V_144',
               particles = [ P.p__tilde__, P.p, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_274,(0,0):C.GC_177})

V_145 = Vertex(name = 'V_145',
               particles = [ P.p__tilde__, P.p, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_269,(0,0):C.GC_142})

V_146 = Vertex(name = 'V_146',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_123})

V_147 = Vertex(name = 'V_147',
               particles = [ P.W__minus__, P.W__plus__, P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_126})

V_148 = Vertex(name = 'V_148',
               particles = [ P.W__minus__, P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_124})

V_149 = Vertex(name = 'V_149',
               particles = [ P.W__minus__, P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_125})

V_150 = Vertex(name = 'V_150',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_444})

V_151 = Vertex(name = 'V_151',
               particles = [ P.Delta0Bar, P.Delta0, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_175,(0,4):C.GC_186,(0,0):C.GC_194,(0,1):C.GC_261,(0,2):C.GC_222,(0,5):C.GC_242})

V_152 = Vertex(name = 'V_152',
               particles = [ P.Delta0Bar, P.Delta0, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_140,(0,4):C.GC_153,(0,0):C.GC_163,(0,1):C.GC_251,(0,2):C.GC_210,(0,5):C.GC_230})

V_153 = Vertex(name = 'V_153',
               particles = [ P.Delta__minus__bar, P.Delta0, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_146,(0,4):C.GC_157,(0,0):C.GC_167,(0,1):C.GC_258,(0,2):C.GC_219,(0,5):C.GC_239})

V_154 = Vertex(name = 'V_154',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_129,(0,4):C.GC_133,(0,0):C.GC_135,(0,1):C.GC_249,(0,2):C.GC_209,(0,5):C.GC_229})

V_155 = Vertex(name = 'V_155',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_181,(0,4):C.GC_189,(0,0):C.GC_197,(0,1):C.GC_266,(0,2):C.GC_227,(0,5):C.GC_247})

V_156 = Vertex(name = 'V_156',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_147,(0,4):C.GC_158,(0,0):C.GC_168,(0,1):C.GC_259,(0,2):C.GC_218,(0,5):C.GC_238})

V_157 = Vertex(name = 'V_157',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_145,(0,4):C.GC_156,(0,0):C.GC_166,(0,1):C.GC_257,(0,2):C.GC_217,(0,5):C.GC_237})

V_158 = Vertex(name = 'V_158',
               particles = [ P.Delta__minus__bar, P.Delta__minus__, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_173,(0,4):C.GC_185,(0,0):C.GC_193,(0,1):C.GC_260,(0,2):C.GC_223,(0,5):C.GC_243})

V_159 = Vertex(name = 'V_159',
               particles = [ P.Delta__minus__bar, P.Delta__minus__, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_144,(0,4):C.GC_155,(0,0):C.GC_165,(0,1):C.GC_253,(0,2):C.GC_212,(0,5):C.GC_232})

V_160 = Vertex(name = 'V_160',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_130,(0,4):C.GC_134,(0,0):C.GC_136,(0,1):C.GC_248,(0,2):C.GC_208,(0,5):C.GC_228})

V_161 = Vertex(name = 'V_161',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_183,(0,4):C.GC_191,(0,0):C.GC_199,(0,1):C.GC_264,(0,2):C.GC_225,(0,5):C.GC_245})

V_162 = Vertex(name = 'V_162',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_151,(0,4):C.GC_161,(0,0):C.GC_171,(0,1):C.GC_256,(0,2):C.GC_215,(0,5):C.GC_235})

V_163 = Vertex(name = 'V_163',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_149,(0,4):C.GC_159,(0,0):C.GC_169,(0,1):C.GC_254,(0,2):C.GC_214,(0,5):C.GC_234})

V_164 = Vertex(name = 'V_164',
               particles = [ P.Delta0Bar, P.Delta__plus__, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,4):C.GC_160,(0,0):C.GC_170,(0,1):C.GC_255,(0,3):C.GC_150,(0,2):C.GC_216,(0,5):C.GC_236})

V_165 = Vertex(name = 'V_165',
               particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_176,(0,4):C.GC_187,(0,0):C.GC_195,(0,1):C.GC_262,(0,2):C.GC_221,(0,5):C.GC_241})

V_166 = Vertex(name = 'V_166',
               particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_139,(0,4):C.GC_152,(0,0):C.GC_162,(0,1):C.GC_250,(0,2):C.GC_211,(0,5):C.GC_231})

V_167 = Vertex(name = 'V_167',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_129,(0,4):C.GC_133,(0,0):C.GC_135,(0,1):C.GC_249,(0,2):C.GC_209,(0,5):C.GC_229})

V_168 = Vertex(name = 'V_168',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_181,(0,4):C.GC_189,(0,0):C.GC_197,(0,1):C.GC_266,(0,2):C.GC_227,(0,5):C.GC_247})

V_169 = Vertex(name = 'V_169',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_147,(0,4):C.GC_158,(0,0):C.GC_168,(0,1):C.GC_259,(0,2):C.GC_218,(0,5):C.GC_238})

V_170 = Vertex(name = 'V_170',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_145,(0,4):C.GC_156,(0,0):C.GC_166,(0,1):C.GC_257,(0,2):C.GC_217,(0,5):C.GC_237})

V_171 = Vertex(name = 'V_171',
               particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_146,(0,4):C.GC_157,(0,0):C.GC_167,(0,1):C.GC_258,(0,2):C.GC_219,(0,5):C.GC_239})

V_172 = Vertex(name = 'V_172',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_178,(0,4):C.GC_188,(0,0):C.GC_196,(0,1):C.GC_263,(0,2):C.GC_220,(0,5):C.GC_240})

V_173 = Vertex(name = 'V_173',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_143,(0,4):C.GC_154,(0,0):C.GC_164,(0,1):C.GC_252,(0,2):C.GC_213,(0,5):C.GC_233})

V_174 = Vertex(name = 'V_174',
               particles = [ P.n__tilde__, P.Delta0, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_314,(0,0):C.GC_476,(0,2):C.GC_296})

V_175 = Vertex(name = 'V_175',
               particles = [ P.n__tilde__, P.Delta0, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_176 = Vertex(name = 'V_176',
               particles = [ P.n__tilde__, P.Delta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRV1, L.FRV2, L.FRV3 ],
               couplings = {(0,1):C.GC_297,(0,0):C.GC_458,(0,2):C.GC_278})

V_177 = Vertex(name = 'V_177',
               particles = [ P.n__tilde__, P.Delta__minus__, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_311,(0,0):C.GC_471,(0,2):C.GC_291})

V_178 = Vertex(name = 'V_178',
               particles = [ P.n__tilde__, P.Delta__minus__, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_304,(0,0):C.GC_465,(0,2):C.GC_285})

V_179 = Vertex(name = 'V_179',
               particles = [ P.n__tilde__, P.Delta__minus__, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_303,(0,0):C.GC_463,(0,2):C.GC_283})

V_180 = Vertex(name = 'V_180',
               particles = [ P.n__tilde__, P.Delta__plus__, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_308,(0,0):C.GC_469,(0,2):C.GC_289})

V_181 = Vertex(name = 'V_181',
               particles = [ P.Delta__minus__bar, P.n, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_301,(0,0):C.GC_464,(0,2):C.GC_284})

V_182 = Vertex(name = 'V_182',
               particles = [ P.Delta__minus__Bar, P.n, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFV1, L.RFV2, L.RFV3 ],
               couplings = {(0,1):C.GC_300,(0,0):C.GC_461,(0,2):C.GC_281})

V_183 = Vertex(name = 'V_183',
               particles = [ P.Delta__minus__Bar, P.n, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_312,(0,0):C.GC_474,(0,2):C.GC_294})

V_184 = Vertex(name = 'V_184',
               particles = [ P.Delta__minus__Bar, P.n, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_305,(0,0):C.GC_468,(0,2):C.GC_288})

V_185 = Vertex(name = 'V_185',
               particles = [ P.Delta__minus__Bar, P.n, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_306,(0,0):C.GC_466,(0,2):C.GC_286})

V_186 = Vertex(name = 'V_186',
               particles = [ P.Delta0Bar, P.n, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_314,(0,0):C.GC_476,(0,2):C.GC_296})

V_187 = Vertex(name = 'V_187',
               particles = [ P.Delta0Bar, P.n, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_188 = Vertex(name = 'V_188',
               particles = [ P.p__tilde__, P.Delta0, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRV1, L.FRV2, L.FRV3 ],
               couplings = {(0,1):C.GC_299,(0,0):C.GC_460,(0,2):C.GC_280})

V_189 = Vertex(name = 'V_189',
               particles = [ P.p__tilde__, P.Delta0, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_313,(0,0):C.GC_473,(0,2):C.GC_293})

V_190 = Vertex(name = 'V_190',
               particles = [ P.p__tilde__, P.Delta0, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_308,(0,0):C.GC_469,(0,2):C.GC_289})

V_191 = Vertex(name = 'V_191',
               particles = [ P.p__tilde__, P.Delta0, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_307,(0,0):C.GC_467,(0,2):C.GC_287})

V_192 = Vertex(name = 'V_192',
               particles = [ P.p__tilde__, P.Delta__plus__, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_314,(0,0):C.GC_476,(0,2):C.GC_296})

V_193 = Vertex(name = 'V_193',
               particles = [ P.p__tilde__, P.Delta__plus__, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_194 = Vertex(name = 'V_194',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_304,(0,0):C.GC_465,(0,2):C.GC_285})

V_195 = Vertex(name = 'V_195',
               particles = [ P.Delta0Bar, P.p, P.W__plus__, P.Pi__minus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_305,(0,0):C.GC_468,(0,2):C.GC_288})

V_196 = Vertex(name = 'V_196',
               particles = [ P.Delta__minus____minus__Bar, P.p, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFV1, L.RFV2, L.RFV3 ],
               couplings = {(0,1):C.GC_298,(0,0):C.GC_459,(0,2):C.GC_279})

V_197 = Vertex(name = 'V_197',
               particles = [ P.Delta__minus____minus__Bar, P.p, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_310,(0,0):C.GC_472,(0,2):C.GC_292})

V_198 = Vertex(name = 'V_198',
               particles = [ P.Delta__minus____minus__Bar, P.p, P.W__plus__, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_301,(0,0):C.GC_464,(0,2):C.GC_284})

V_199 = Vertex(name = 'V_199',
               particles = [ P.Delta__minus____minus__Bar, P.p, P.W__plus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_302,(0,0):C.GC_462,(0,2):C.GC_282})

V_200 = Vertex(name = 'V_200',
               particles = [ P.Delta__minus__Bar, P.p, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_314,(0,0):C.GC_476,(0,2):C.GC_296})

V_201 = Vertex(name = 'V_201',
               particles = [ P.Delta__minus__Bar, P.p, P.W__plus__, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_309,(0,0):C.GC_470,(0,2):C.GC_290})

V_202 = Vertex(name = 'V_202',
               particles = [ P.A, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_335})

V_203 = Vertex(name = 'V_203',
               particles = [ P.Z, P.Pi0, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.VSSS5 ],
               couplings = {(0,0):C.GC_358})

V_204 = Vertex(name = 'V_204',
               particles = [ P.Z, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSSS2 ],
               couplings = {(0,0):C.GC_357})

V_205 = Vertex(name = 'V_205',
               particles = [ P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_323})

V_206 = Vertex(name = 'V_206',
               particles = [ P.n__tilde__, P.n, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_413,(0,0):C.GC_321})

V_207 = Vertex(name = 'V_207',
               particles = [ P.p__tilde__, P.p, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_412,(0,0):C.GC_326})

V_208 = Vertex(name = 'V_208',
               particles = [ P.n__tilde__, P.n, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_414,(0,0):C.GC_338})

V_209 = Vertex(name = 'V_209',
               particles = [ P.p__tilde__, P.n, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_418,(0,0):C.GC_362})

V_210 = Vertex(name = 'V_210',
               particles = [ P.p__tilde__, P.n, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_416,(0,0):C.GC_343})

V_211 = Vertex(name = 'V_211',
               particles = [ P.n__tilde__, P.p, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_417,(0,0):C.GC_361})

V_212 = Vertex(name = 'V_212',
               particles = [ P.n__tilde__, P.p, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_416,(0,0):C.GC_343})

V_213 = Vertex(name = 'V_213',
               particles = [ P.p__tilde__, P.p, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_415,(0,0):C.GC_339})

V_214 = Vertex(name = 'V_214',
               particles = [ P.W__minus__, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_67})

V_215 = Vertex(name = 'V_215',
               particles = [ P.W__minus__, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_216 = Vertex(name = 'V_216',
               particles = [ P.W__minus__, P.Z, P.Pi0, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_65})

V_217 = Vertex(name = 'V_217',
               particles = [ P.W__minus__, P.Z, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_66})

V_218 = Vertex(name = 'V_218',
               particles = [ P.W__plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_68})

V_219 = Vertex(name = 'V_219',
               particles = [ P.W__plus__, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_220 = Vertex(name = 'V_220',
               particles = [ P.W__plus__, P.Z, P.Pi0, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_64})

V_221 = Vertex(name = 'V_221',
               particles = [ P.W__plus__, P.Z, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_63})

V_222 = Vertex(name = 'V_222',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_439})

V_223 = Vertex(name = 'V_223',
               particles = [ P.Z, P.Z, P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_442})

V_224 = Vertex(name = 'V_224',
               particles = [ P.Z, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_11})

V_225 = Vertex(name = 'V_225',
               particles = [ P.Z, P.Z, P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_440})

V_226 = Vertex(name = 'V_226',
               particles = [ P.Z, P.Z, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_441})

V_227 = Vertex(name = 'V_227',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_445})

V_228 = Vertex(name = 'V_228',
               particles = [ P.Delta0Bar, P.Delta0, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_320,(0,4):C.GC_328,(0,0):C.GC_332,(0,1):C.GC_399,(0,2):C.GC_370,(0,5):C.GC_384})

V_229 = Vertex(name = 'V_229',
               particles = [ P.Delta0Bar, P.Delta0, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_337,(0,4):C.GC_346,(0,0):C.GC_352,(0,1):C.GC_402,(0,2):C.GC_375,(0,5):C.GC_389})

V_230 = Vertex(name = 'V_230',
               particles = [ P.Delta__minus__bar, P.Delta0, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_359,(0,4):C.GC_363,(0,0):C.GC_367,(0,1):C.GC_411,(0,2):C.GC_382,(0,5):C.GC_396})

V_231 = Vertex(name = 'V_231',
               particles = [ P.Delta__minus__bar, P.Delta0, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS4, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_172,(0,5):C.GC_349,(0,0):C.GC_355,(0,4):C.GC_317,(0,1):C.GC_407,(0,2):C.GC_379,(0,6):C.GC_393})

V_232 = Vertex(name = 'V_232',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_360,(0,4):C.GC_364,(0,0):C.GC_368,(0,1):C.GC_410,(0,2):C.GC_383,(0,5):C.GC_397})

V_233 = Vertex(name = 'V_233',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_342,(0,4):C.GC_349,(0,0):C.GC_355,(0,1):C.GC_407,(0,2):C.GC_379,(0,5):C.GC_393})

V_234 = Vertex(name = 'V_234',
               particles = [ P.Delta__minus__bar, P.Delta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_319,(0,4):C.GC_327,(0,0):C.GC_331,(0,1):C.GC_401,(0,2):C.GC_372,(0,5):C.GC_386})

V_235 = Vertex(name = 'V_235',
               particles = [ P.Delta__minus__bar, P.Delta__minus__, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_341,(0,4):C.GC_348,(0,0):C.GC_354,(0,1):C.GC_404,(0,2):C.GC_377,(0,5):C.GC_391})

V_236 = Vertex(name = 'V_236',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_362,(0,4):C.GC_366,(0,0):C.GC_369,(0,1):C.GC_408,(0,2):C.GC_381,(0,5):C.GC_395})

V_237 = Vertex(name = 'V_237',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_344,(0,4):C.GC_350,(0,0):C.GC_356,(0,1):C.GC_406,(0,2):C.GC_378,(0,5):C.GC_392})

V_238 = Vertex(name = 'V_238',
               particles = [ P.Delta0Bar, P.Delta__plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS1, L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,0):C.GC_318,(0,2):C.GC_409,(0,4):C.GC_361,(0,5):C.GC_365,(0,1):C.GC_201,(0,3):C.GC_380,(0,6):C.GC_394})

V_239 = Vertex(name = 'V_239',
               particles = [ P.Delta0Bar, P.Delta__plus__, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_344,(0,4):C.GC_350,(0,0):C.GC_356,(0,1):C.GC_406,(0,2):C.GC_378,(0,5):C.GC_392})

V_240 = Vertex(name = 'V_240',
               particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_322,(0,4):C.GC_329,(0,0):C.GC_333,(0,1):C.GC_398,(0,2):C.GC_371,(0,5):C.GC_385})

V_241 = Vertex(name = 'V_241',
               particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_336,(0,4):C.GC_345,(0,0):C.GC_351,(0,1):C.GC_403,(0,2):C.GC_374,(0,5):C.GC_388})

V_242 = Vertex(name = 'V_242',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_360,(0,4):C.GC_364,(0,0):C.GC_368,(0,1):C.GC_410,(0,2):C.GC_383,(0,5):C.GC_397})

V_243 = Vertex(name = 'V_243',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_342,(0,4):C.GC_349,(0,0):C.GC_355,(0,1):C.GC_407,(0,2):C.GC_379,(0,5):C.GC_393})

V_244 = Vertex(name = 'V_244',
               particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7, L.RRVS8 ],
               couplings = {(0,3):C.GC_359,(0,4):C.GC_363,(0,0):C.GC_367,(0,1):C.GC_411,(0,2):C.GC_382,(0,5):C.GC_396})

V_245 = Vertex(name = 'V_245',
               particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_342,(0,4):C.GC_349,(0,0):C.GC_355,(0,1):C.GC_407,(0,2):C.GC_379,(0,5):C.GC_393})

V_246 = Vertex(name = 'V_246',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_325,(0,4):C.GC_330,(0,0):C.GC_334,(0,1):C.GC_400,(0,2):C.GC_373,(0,5):C.GC_387})

V_247 = Vertex(name = 'V_247',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVSS1, L.RRVSS2, L.RRVSS3, L.RRVSS5, L.RRVSS6, L.RRVSS7 ],
               couplings = {(0,3):C.GC_340,(0,4):C.GC_347,(0,0):C.GC_353,(0,1):C.GC_405,(0,2):C.GC_376,(0,5):C.GC_390})

V_248 = Vertex(name = 'V_248',
               particles = [ P.n__tilde__, P.Delta0, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FRV1, L.FRV2, L.FRV3 ],
               couplings = {(0,1):C.GC_429,(0,0):C.GC_477,(0,2):C.GC_419})

V_249 = Vertex(name = 'V_249',
               particles = [ P.n__tilde__, P.Delta0, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_434,(0,0):C.GC_482,(0,2):C.GC_424})

V_250 = Vertex(name = 'V_250',
               particles = [ P.n__tilde__, P.Delta__minus__, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_436,(0,0):C.GC_483,(0,2):C.GC_425})

V_251 = Vertex(name = 'V_251',
               particles = [ P.n__tilde__, P.Delta__minus__, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_430,(0,0):C.GC_478,(0,2):C.GC_420})

V_252 = Vertex(name = 'V_252',
               particles = [ P.n__tilde__, P.Delta__plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_438,(0,0):C.GC_485,(0,2):C.GC_427})

V_253 = Vertex(name = 'V_253',
               particles = [ P.n__tilde__, P.Delta__plus__, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_433,(0,0):C.GC_481,(0,2):C.GC_423})

V_254 = Vertex(name = 'V_254',
               particles = [ P.Delta__minus__bar, P.n, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_435,(0,0):C.GC_484,(0,2):C.GC_426})

V_255 = Vertex(name = 'V_255',
               particles = [ P.Delta__minus__bar, P.n, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_430,(0,0):C.GC_478,(0,2):C.GC_420})

V_256 = Vertex(name = 'V_256',
               particles = [ P.Delta__minus__Bar, P.n, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_437,(0,0):C.GC_486,(0,2):C.GC_428})

V_257 = Vertex(name = 'V_257',
               particles = [ P.Delta__minus__Bar, P.n, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_433,(0,0):C.GC_481,(0,2):C.GC_423})

V_258 = Vertex(name = 'V_258',
               particles = [ P.Delta0Bar, P.n, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RFV1, L.RFV2, L.RFV3 ],
               couplings = {(0,1):C.GC_429,(0,0):C.GC_477,(0,2):C.GC_419})

V_259 = Vertex(name = 'V_259',
               particles = [ P.Delta0Bar, P.n, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_434,(0,0):C.GC_482,(0,2):C.GC_424})

V_260 = Vertex(name = 'V_260',
               particles = [ P.p__tilde__, P.Delta0, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_438,(0,0):C.GC_485,(0,2):C.GC_427})

V_261 = Vertex(name = 'V_261',
               particles = [ P.p__tilde__, P.Delta0, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_432,(0,0):C.GC_480,(0,2):C.GC_422})

V_262 = Vertex(name = 'V_262',
               particles = [ P.p__tilde__, P.Delta__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FRV1, L.FRV2, L.FRV3 ],
               couplings = {(0,1):C.GC_429,(0,0):C.GC_477,(0,2):C.GC_419})

V_263 = Vertex(name = 'V_263',
               particles = [ P.p__tilde__, P.Delta__plus__, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_434,(0,0):C.GC_482,(0,2):C.GC_424})

V_264 = Vertex(name = 'V_264',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1, L.FRVS2, L.FRVS3 ],
               couplings = {(0,1):C.GC_436,(0,0):C.GC_483,(0,2):C.GC_425})

V_265 = Vertex(name = 'V_265',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVSS1, L.FRVSS2, L.FRVSS3 ],
               couplings = {(0,1):C.GC_431,(0,0):C.GC_479,(0,2):C.GC_421})

V_266 = Vertex(name = 'V_266',
               particles = [ P.Delta0Bar, P.p, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_437,(0,0):C.GC_486,(0,2):C.GC_428})

V_267 = Vertex(name = 'V_267',
               particles = [ P.Delta0Bar, P.p, P.Z, P.Pi0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_432,(0,0):C.GC_480,(0,2):C.GC_422})

V_268 = Vertex(name = 'V_268',
               particles = [ P.Delta__minus____minus__Bar, P.p, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1, L.RFVS2, L.RFVS3 ],
               couplings = {(0,1):C.GC_435,(0,0):C.GC_484,(0,2):C.GC_426})

V_269 = Vertex(name = 'V_269',
               particles = [ P.Delta__minus____minus__Bar, P.p, P.Z, P.Pi0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_431,(0,0):C.GC_479,(0,2):C.GC_421})

V_270 = Vertex(name = 'V_270',
               particles = [ P.Delta__minus__Bar, P.p, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RFV1, L.RFV2, L.RFV3 ],
               couplings = {(0,1):C.GC_429,(0,0):C.GC_477,(0,2):C.GC_419})

V_271 = Vertex(name = 'V_271',
               particles = [ P.Delta__minus__Bar, P.p, P.Z, P.Pi__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVSS1, L.RFVSS2, L.RFVSS3 ],
               couplings = {(0,1):C.GC_434,(0,0):C.GC_482,(0,2):C.GC_424})

V_272 = Vertex(name = 'V_272',
               particles = [ P.e__plus__, P.e__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_273 = Vertex(name = 'V_273',
               particles = [ P.mu__plus__, P.mu__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_274 = Vertex(name = 'V_274',
               particles = [ P.ta__plus__, P.ta__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_275 = Vertex(name = 'V_275',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_132})

V_276 = Vertex(name = 'V_276',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_132})

V_277 = Vertex(name = 'V_277',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_132})

V_278 = Vertex(name = 'V_278',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_132})

V_279 = Vertex(name = 'V_279',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_132})

V_280 = Vertex(name = 'V_280',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_132})

V_281 = Vertex(name = 'V_281',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_324})

V_282 = Vertex(name = 'V_282',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_324})

V_283 = Vertex(name = 'V_283',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_324})

V_284 = Vertex(name = 'V_284',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_316})

V_285 = Vertex(name = 'V_285',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_316})

V_286 = Vertex(name = 'V_286',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_316})

V_287 = Vertex(name = 'V_287',
               particles = [ P.n__tilde__, P.n, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_100})

V_288 = Vertex(name = 'V_288',
               particles = [ P.p__tilde__, P.n, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_102})

V_289 = Vertex(name = 'V_289',
               particles = [ P.p__tilde__, P.n, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_101})

V_290 = Vertex(name = 'V_290',
               particles = [ P.n__tilde__, P.p, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_103})

V_291 = Vertex(name = 'V_291',
               particles = [ P.n__tilde__, P.p, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_101})

V_292 = Vertex(name = 'V_292',
               particles = [ P.p__tilde__, P.p, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_99})

V_293 = Vertex(name = 'V_293',
               particles = [ P.Delta0Bar, P.Delta0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_81,(0,1):C.GC_90,(0,2):C.GC_71})

V_294 = Vertex(name = 'V_294',
               particles = [ P.Delta__minus__bar, P.Delta0, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS4, L.RRVS5, L.RRVS8 ],
               couplings = {(0,0):C.GC_97,(0,1):C.GC_78,(0,2):C.GC_88})

V_295 = Vertex(name = 'V_295',
               particles = [ P.Delta__minus__bar, P.Delta0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_94,(0,2):C.GC_74})

V_296 = Vertex(name = 'V_296',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS4, L.RRVS5, L.RRVS8 ],
               couplings = {(0,0):C.GC_98,(0,1):C.GC_77,(0,2):C.GC_87})

V_297 = Vertex(name = 'V_297',
               particles = [ P.Delta0Bar, P.Delta__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_94,(0,2):C.GC_74})

V_298 = Vertex(name = 'V_298',
               particles = [ P.Delta__minus__bar, P.Delta__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_82,(0,1):C.GC_89,(0,2):C.GC_72})

V_299 = Vertex(name = 'V_299',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS4, L.RRVS5, L.RRVS8 ],
               couplings = {(0,0):C.GC_96,(0,1):C.GC_75,(0,2):C.GC_85})

V_300 = Vertex(name = 'V_300',
               particles = [ P.Delta__minus__Bar, P.Delta0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_83,(0,1):C.GC_93,(0,2):C.GC_73})

V_301 = Vertex(name = 'V_301',
               particles = [ P.Delta0Bar, P.Delta__plus__, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS4, L.RRVS5, L.RRVS8 ],
               couplings = {(0,0):C.GC_95,(0,1):C.GC_76,(0,2):C.GC_86})

V_302 = Vertex(name = 'V_302',
               particles = [ P.Delta0Bar, P.Delta__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_83,(0,1):C.GC_93,(0,2):C.GC_73})

V_303 = Vertex(name = 'V_303',
               particles = [ P.Delta__minus__Bar, P.Delta__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_80,(0,1):C.GC_91,(0,2):C.GC_70})

V_304 = Vertex(name = 'V_304',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS4, L.RRVS5, L.RRVS8 ],
               couplings = {(0,0):C.GC_98,(0,1):C.GC_77,(0,2):C.GC_87})

V_305 = Vertex(name = 'V_305',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_94,(0,2):C.GC_74})

V_306 = Vertex(name = 'V_306',
               particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS2, L.RRVS5, L.RRVS8 ],
               couplings = {(0,0):C.GC_97,(0,1):C.GC_78,(0,2):C.GC_88})

V_307 = Vertex(name = 'V_307',
               particles = [ P.Delta__minus__Bar, P.Delta__plus____plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_94,(0,2):C.GC_74})

V_308 = Vertex(name = 'V_308',
               particles = [ P.Delta__minus____minus__Bar, P.Delta__plus____plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_79,(0,1):C.GC_92,(0,2):C.GC_69})

