# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Mon 12 Oct 2026 12:30:26


from __future__ import absolute_import
from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_80})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_175})

V_3 = Vertex(name = 'V_3',
             particles = [ P.A, P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_12})

V_4 = Vertex(name = 'V_4',
             particles = [ P.Pi0, P.Pi0, P.Pi0, P.Pi0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS4 ],
             couplings = {(0,0):C.GC_20})

V_5 = Vertex(name = 'V_5',
             particles = [ P.A, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VSS1 ],
             couplings = {(0,0):C.GC_3})

V_6 = Vertex(name = 'V_6',
             particles = [ P.Pi0, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS2 ],
             couplings = {(0,0):C.GC_19})

V_7 = Vertex(name = 'V_7',
             particles = [ P.Pi__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS3 ],
             couplings = {(0,0):C.GC_20})

V_8 = Vertex(name = 'V_8',
             particles = [ P.n__tilde__, P.n, P.A ],
             color = [ '1' ],
             lorentz = [ L.FFV18, L.FFV2 ],
             couplings = {(0,1):C.GC_4,(0,0):C.GC_90})

V_9 = Vertex(name = 'V_9',
             particles = [ P.n__tilde__, P.n, P.W__minus__, P.Pi__plus__ ],
             color = [ '1' ],
             lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4 ],
             couplings = {(0,1):C.GC_256,(0,0):C.GC_201,(0,2):C.GC_285})

V_10 = Vertex(name = 'V_10',
              particles = [ P.n__tilde__, P.n, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4 ],
              couplings = {(0,1):C.GC_257,(0,0):C.GC_198,(0,2):C.GC_284})

V_11 = Vertex(name = 'V_11',
              particles = [ P.p__tilde__, P.n, P.W__plus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4 ],
              couplings = {(0,1):C.GC_259,(0,0):C.GC_205,(0,2):C.GC_286})

V_12 = Vertex(name = 'V_12',
              particles = [ P.p__tilde__, P.n, P.Z, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS3, L.FFVS5 ],
              couplings = {(0,1):C.GC_161,(0,0):C.GC_135,(0,2):C.GC_173})

V_13 = Vertex(name = 'V_13',
              particles = [ P.n__tilde__, P.p, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4 ],
              couplings = {(0,1):C.GC_258,(0,0):C.GC_206,(0,2):C.GC_287})

V_14 = Vertex(name = 'V_14',
              particles = [ P.n__tilde__, P.p, P.Z, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS3, L.FFVS5 ],
              couplings = {(0,1):C.GC_160,(0,0):C.GC_132,(0,2):C.GC_172})

V_15 = Vertex(name = 'V_15',
              particles = [ P.p__tilde__, P.p, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV19, L.FFV3 ],
              couplings = {(0,1):C.GC_4,(0,0):C.GC_90})

V_16 = Vertex(name = 'V_16',
              particles = [ P.p__tilde__, P.p, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4 ],
              couplings = {(0,1):C.GC_257,(0,0):C.GC_198,(0,2):C.GC_284})

V_17 = Vertex(name = 'V_17',
              particles = [ P.p__tilde__, P.p, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4 ],
              couplings = {(0,1):C.GC_256,(0,0):C.GC_201,(0,2):C.GC_285})

V_18 = Vertex(name = 'V_18',
              particles = [ P.Delta0__tilde__, P.Delta0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_26,(0,2):C.GC_14,(0,0):C.GC_34})

V_19 = Vertex(name = 'V_19',
              particles = [ P.Delta__minus____tilde__, P.Delta0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_29,(0,2):C.GC_21,(0,0):C.GC_37})

V_20 = Vertex(name = 'V_20',
              particles = [ P.Delta0__tilde__, P.Delta__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_30,(0,2):C.GC_22,(0,0):C.GC_38})

V_21 = Vertex(name = 'V_21',
              particles = [ P.Delta__minus____tilde__, P.Delta__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV4, L.RRV5 ],
              couplings = {(0,1):C.GC_2,(0,2):C.GC_6,(0,0):C.GC_9})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Delta__minus____tilde__, P.Delta__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_28,(0,2):C.GC_18,(0,0):C.GC_36})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Delta__plus____tilde__, P.Delta0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_32,(0,2):C.GC_24,(0,0):C.GC_40})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Delta0__tilde__, P.Delta__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_31,(0,2):C.GC_23,(0,0):C.GC_39})

V_25 = Vertex(name = 'V_25',
              particles = [ P.Delta__plus____tilde__, P.Delta__plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV4, L.RRV5 ],
              couplings = {(0,1):C.GC_1,(0,2):C.GC_5,(0,0):C.GC_8})

V_26 = Vertex(name = 'V_26',
              particles = [ P.Delta__plus____tilde__, P.Delta__plus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_25,(0,0):C.GC_33,(0,2):C.GC_13})

V_27 = Vertex(name = 'V_27',
              particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_30,(0,2):C.GC_22,(0,0):C.GC_38})

V_28 = Vertex(name = 'V_28',
              particles = [ P.Delta__plus____tilde__, P.Delta__plus____plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_29,(0,2):C.GC_21,(0,0):C.GC_37})

V_29 = Vertex(name = 'V_29',
              particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus____plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV4, L.RRV5 ],
              couplings = {(0,1):C.GC_3,(0,2):C.GC_7,(0,0):C.GC_10})

V_30 = Vertex(name = 'V_30',
              particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus____plus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRSS1, L.RRSS2, L.RRSS3 ],
              couplings = {(0,1):C.GC_27,(0,2):C.GC_17,(0,0):C.GC_35})

V_31 = Vertex(name = 'V_31',
              particles = [ P.n__tilde__, P.Delta__plus__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV2, L.FRV3, L.FRV4, L.FRV5 ],
              couplings = {(0,3):C.GC_267,(0,0):C.GC_275,(0,1):C.GC_271,(0,2):C.GC_263,(0,4):C.GC_192})

V_32 = Vertex(name = 'V_32',
              particles = [ P.n__tilde__, P.Delta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV2, L.FRV3, L.FRV4, L.FRV5 ],
              couplings = {(0,3):C.GC_264,(0,0):C.GC_272,(0,1):C.GC_268,(0,2):C.GC_260,(0,4):C.GC_191})

V_33 = Vertex(name = 'V_33',
              particles = [ P.n__tilde__, P.Delta0, P.A ],
              color = [ '1' ],
              lorentz = [ L.FRV3, L.FRV4 ],
              couplings = {(0,1):C.GC_78,(0,0):C.GC_76})

V_34 = Vertex(name = 'V_34',
              particles = [ P.n__tilde__, P.Delta0, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV2, L.FRV3, L.FRV4, L.FRV5 ],
              couplings = {(0,3):C.GC_165,(0,0):C.GC_112,(0,1):C.GC_111,(0,2):C.GC_163,(0,4):C.GC_93})

V_35 = Vertex(name = 'V_35',
              particles = [ P.Delta__minus____tilde__, P.n, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV2, L.RFV3, L.RFV4, L.RFV5 ],
              couplings = {(0,3):C.GC_265,(0,0):C.GC_272,(0,1):C.GC_268,(0,2):C.GC_261,(0,4):C.GC_191})

V_36 = Vertex(name = 'V_36',
              particles = [ P.Delta__plus____tilde__, P.n, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV2, L.RFV3, L.RFV4, L.RFV5 ],
              couplings = {(0,3):C.GC_266,(0,0):C.GC_275,(0,1):C.GC_271,(0,2):C.GC_262,(0,4):C.GC_192})

V_37 = Vertex(name = 'V_37',
              particles = [ P.Delta0__tilde__, P.n, P.Z ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV2, L.RFV3, L.RFV4, L.RFV5 ],
              couplings = {(0,3):C.GC_164,(0,0):C.GC_112,(0,1):C.GC_111,(0,2):C.GC_162,(0,4):C.GC_93})

V_38 = Vertex(name = 'V_38',
              particles = [ P.Delta0__tilde__, P.n, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV3, L.RFV4 ],
              couplings = {(0,1):C.GC_79,(0,0):C.GC_77})

V_39 = Vertex(name = 'V_39',
              particles = [ P.n__tilde__, P.n, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_15})

V_40 = Vertex(name = 'V_40',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_288})

V_41 = Vertex(name = 'V_41',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_289})

V_42 = Vertex(name = 'V_42',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_290})

V_43 = Vertex(name = 'V_43',
              particles = [ P.p__tilde__, P.Delta__plus____plus__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV2, L.FRV3, L.FRV4, L.FRV5 ],
              couplings = {(0,3):C.GC_265,(0,0):C.GC_273,(0,1):C.GC_269,(0,2):C.GC_261,(0,4):C.GC_190})

V_44 = Vertex(name = 'V_44',
              particles = [ P.p__tilde__, P.Delta0, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV2, L.FRV3, L.FRV4, L.FRV5 ],
              couplings = {(0,3):C.GC_266,(0,0):C.GC_274,(0,1):C.GC_270,(0,2):C.GC_262,(0,4):C.GC_193})

V_45 = Vertex(name = 'V_45',
              particles = [ P.p__tilde__, P.Delta__plus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FRV3, L.FRV4 ],
              couplings = {(0,1):C.GC_78,(0,0):C.GC_76})

V_46 = Vertex(name = 'V_46',
              particles = [ P.p__tilde__, P.Delta__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FRV1, L.FRV2, L.FRV3, L.FRV4, L.FRV5 ],
              couplings = {(0,3):C.GC_165,(0,0):C.GC_112,(0,1):C.GC_111,(0,2):C.GC_163,(0,4):C.GC_93})

V_47 = Vertex(name = 'V_47',
              particles = [ P.p__tilde__, P.n, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_23})

V_48 = Vertex(name = 'V_48',
              particles = [ P.Delta0__tilde__, P.p, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV2, L.RFV3, L.RFV4, L.RFV5 ],
              couplings = {(0,3):C.GC_267,(0,0):C.GC_274,(0,1):C.GC_270,(0,2):C.GC_263,(0,4):C.GC_193})

V_49 = Vertex(name = 'V_49',
              particles = [ P.Delta__plus____plus____tilde__, P.p, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV2, L.RFV3, L.RFV4, L.RFV5 ],
              couplings = {(0,3):C.GC_264,(0,0):C.GC_273,(0,1):C.GC_269,(0,2):C.GC_260,(0,4):C.GC_190})

V_50 = Vertex(name = 'V_50',
              particles = [ P.Delta__plus____tilde__, P.p, P.Z ],
              color = [ '1' ],
              lorentz = [ L.RFV1, L.RFV2, L.RFV3, L.RFV4, L.RFV5 ],
              couplings = {(0,3):C.GC_164,(0,0):C.GC_112,(0,1):C.GC_111,(0,2):C.GC_162,(0,4):C.GC_93})

V_51 = Vertex(name = 'V_51',
              particles = [ P.Delta__plus____tilde__, P.p, P.A ],
              color = [ '1' ],
              lorentz = [ L.RFV3, L.RFV4 ],
              couplings = {(0,1):C.GC_79,(0,0):C.GC_77})

V_52 = Vertex(name = 'V_52',
              particles = [ P.n__tilde__, P.p, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_24})

V_53 = Vertex(name = 'V_53',
              particles = [ P.p__tilde__, P.p, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_16})

V_54 = Vertex(name = 'V_54',
              particles = [ P.p__tilde__, P.n, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV13, L.FFV21, L.FFV5, L.FFV9 ],
              couplings = {(0,3):C.GC_255,(0,2):C.GC_185,(0,1):C.GC_282,(0,0):C.GC_283})

V_55 = Vertex(name = 'V_55',
              particles = [ P.n__tilde__, P.n, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV10, L.FFV14, L.FFV22, L.FFV6 ],
              couplings = {(0,0):C.GC_159,(0,3):C.GC_116,(0,2):C.GC_113,(0,1):C.GC_171})

V_56 = Vertex(name = 'V_56',
              particles = [ P.n__tilde__, P.p, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV12, L.FFV20, L.FFV4, L.FFV8 ],
              couplings = {(0,3):C.GC_255,(0,2):C.GC_185,(0,1):C.GC_282,(0,0):C.GC_283})

V_57 = Vertex(name = 'V_57',
              particles = [ P.p__tilde__, P.p, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV11, L.FFV15, L.FFV23, L.FFV7 ],
              couplings = {(0,0):C.GC_158,(0,3):C.GC_120,(0,2):C.GC_113,(0,1):C.GC_170})

V_58 = Vertex(name = 'V_58',
              particles = [ P.A, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_223})

V_59 = Vertex(name = 'V_59',
              particles = [ P.A, P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_194})

V_60 = Vertex(name = 'V_60',
              particles = [ P.W__minus__, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_182})

V_61 = Vertex(name = 'V_61',
              particles = [ P.W__minus__, P.Pi0, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS3 ],
              couplings = {(0,0):C.GC_196})

V_62 = Vertex(name = 'V_62',
              particles = [ P.W__minus__, P.Pi__minus__, P.Pi__plus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS1 ],
              couplings = {(0,0):C.GC_195})

V_63 = Vertex(name = 'V_63',
              particles = [ P.Delta0__tilde__, P.Delta0, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_200,(0,4):C.GC_209,(0,0):C.GC_217,(0,1):C.GC_249,(0,2):C.GC_228,(0,5):C.GC_238})

V_64 = Vertex(name = 'V_64',
              particles = [ P.Delta__minus____tilde__, P.Delta0, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_183,(0,4):C.GC_186,(0,0):C.GC_188,(0,1):C.GC_246,(0,2):C.GC_226,(0,5):C.GC_236})

V_65 = Vertex(name = 'V_65',
              particles = [ P.Delta__minus____tilde__, P.Delta0, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_204,(0,4):C.GC_212,(0,0):C.GC_220,(0,1):C.GC_254,(0,2):C.GC_233,(0,5):C.GC_243})

V_66 = Vertex(name = 'V_66',
              particles = [ P.Delta__minus____tilde__, P.Delta__minus__, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_202,(0,4):C.GC_210,(0,0):C.GC_218,(0,1):C.GC_250,(0,2):C.GC_227,(0,5):C.GC_237})

V_67 = Vertex(name = 'V_67',
              particles = [ P.Delta0__tilde__, P.Delta__plus__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_184,(0,4):C.GC_187,(0,0):C.GC_189,(0,1):C.GC_245,(0,2):C.GC_225,(0,5):C.GC_235})

V_68 = Vertex(name = 'V_68',
              particles = [ P.Delta0__tilde__, P.Delta__plus__, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_206,(0,4):C.GC_214,(0,0):C.GC_222,(0,1):C.GC_252,(0,2):C.GC_231,(0,5):C.GC_241})

V_69 = Vertex(name = 'V_69',
              particles = [ P.Delta__plus____tilde__, P.Delta__plus__, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_199,(0,4):C.GC_208,(0,0):C.GC_216,(0,1):C.GC_248,(0,2):C.GC_229,(0,5):C.GC_239})

V_70 = Vertex(name = 'V_70',
              particles = [ P.Delta__plus____tilde__, P.Delta__plus____plus__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_183,(0,4):C.GC_186,(0,0):C.GC_188,(0,1):C.GC_246,(0,2):C.GC_226,(0,5):C.GC_236})

V_71 = Vertex(name = 'V_71',
              particles = [ P.Delta__plus____tilde__, P.Delta__plus____plus__, P.W__minus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_204,(0,4):C.GC_212,(0,0):C.GC_220,(0,1):C.GC_254,(0,2):C.GC_233,(0,5):C.GC_243})

V_72 = Vertex(name = 'V_72',
              particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus____plus__, P.W__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,4):C.GC_207,(0,0):C.GC_215,(0,1):C.GC_247,(0,3):C.GC_197,(0,2):C.GC_230,(0,5):C.GC_240})

V_73 = Vertex(name = 'V_73',
              particles = [ P.A, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_224})

V_74 = Vertex(name = 'V_74',
              particles = [ P.A, P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_194})

V_75 = Vertex(name = 'V_75',
              particles = [ P.W__plus__, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_181})

V_76 = Vertex(name = 'V_76',
              particles = [ P.W__plus__, P.Pi0, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS3 ],
              couplings = {(0,0):C.GC_196})

V_77 = Vertex(name = 'V_77',
              particles = [ P.W__plus__, P.Pi__minus__, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS2 ],
              couplings = {(0,0):C.GC_195})

V_78 = Vertex(name = 'V_78',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_91})

V_79 = Vertex(name = 'V_79',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_176})

V_80 = Vertex(name = 'V_80',
              particles = [ P.Delta0__tilde__, P.Delta0, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_199,(0,4):C.GC_208,(0,0):C.GC_216,(0,1):C.GC_248,(0,2):C.GC_229,(0,5):C.GC_239})

V_81 = Vertex(name = 'V_81',
              particles = [ P.Delta0__tilde__, P.Delta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_183,(0,4):C.GC_186,(0,0):C.GC_188,(0,1):C.GC_246,(0,2):C.GC_226,(0,5):C.GC_236})

V_82 = Vertex(name = 'V_82',
              particles = [ P.Delta0__tilde__, P.Delta__minus__, P.W__plus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_203,(0,4):C.GC_211,(0,0):C.GC_219,(0,1):C.GC_253,(0,2):C.GC_234,(0,5):C.GC_244})

V_83 = Vertex(name = 'V_83',
              particles = [ P.Delta__minus____tilde__, P.Delta__minus__, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_197,(0,4):C.GC_207,(0,0):C.GC_215,(0,1):C.GC_247,(0,2):C.GC_230,(0,5):C.GC_240})

V_84 = Vertex(name = 'V_84',
              particles = [ P.Delta__plus____tilde__, P.Delta0, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_184,(0,4):C.GC_187,(0,0):C.GC_189,(0,1):C.GC_245,(0,2):C.GC_225,(0,5):C.GC_235})

V_85 = Vertex(name = 'V_85',
              particles = [ P.Delta__plus____tilde__, P.Delta0, P.W__plus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_205,(0,4):C.GC_213,(0,0):C.GC_221,(0,1):C.GC_251,(0,2):C.GC_232,(0,5):C.GC_242})

V_86 = Vertex(name = 'V_86',
              particles = [ P.Delta__plus____tilde__, P.Delta__plus__, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_200,(0,4):C.GC_209,(0,0):C.GC_217,(0,1):C.GC_249,(0,2):C.GC_228,(0,5):C.GC_238})

V_87 = Vertex(name = 'V_87',
              particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
              couplings = {(0,3):C.GC_183,(0,4):C.GC_186,(0,0):C.GC_188,(0,1):C.GC_246,(0,2):C.GC_226,(0,5):C.GC_236})

V_88 = Vertex(name = 'V_88',
              particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus__, P.W__plus__, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,4):C.GC_211,(0,0):C.GC_219,(0,3):C.GC_203,(0,1):C.GC_253,(0,2):C.GC_234,(0,5):C.GC_244})

V_89 = Vertex(name = 'V_89',
              particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus____plus__, P.W__plus__, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
              couplings = {(0,3):C.GC_202,(0,4):C.GC_210,(0,0):C.GC_218,(0,1):C.GC_250,(0,2):C.GC_227,(0,5):C.GC_237})

V_90 = Vertex(name = 'V_90',
              particles = [ P.A, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_131})

V_91 = Vertex(name = 'V_91',
              particles = [ P.Z, P.Pi0, P.Pi0, P.Pi0 ],
              color = [ '1' ],
              lorentz = [ L.VSSS5 ],
              couplings = {(0,0):C.GC_95})

V_92 = Vertex(name = 'V_92',
              particles = [ P.Z, P.Pi0, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSSS4 ],
              couplings = {(0,0):C.GC_96})

V_93 = Vertex(name = 'V_93',
              particles = [ P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_122})

V_94 = Vertex(name = 'V_94',
              particles = [ P.W__minus__, P.Z, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_180})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__minus__, P.Z, P.Pi0, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_178})

V_96 = Vertex(name = 'V_96',
              particles = [ P.W__plus__, P.Z, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_179})

V_97 = Vertex(name = 'V_97',
              particles = [ P.W__plus__, P.Z, P.Pi0, P.Pi__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_178})

V_98 = Vertex(name = 'V_98',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_174})

V_99 = Vertex(name = 'V_99',
              particles = [ P.Z, P.Z, P.Pi__minus__, P.Pi__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_11})

V_100 = Vertex(name = 'V_100',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_177})

V_101 = Vertex(name = 'V_101',
               particles = [ P.Delta0__tilde__, P.Delta0, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_115,(0,4):C.GC_123,(0,0):C.GC_127,(0,1):C.GC_108,(0,2):C.GC_99,(0,5):C.GC_103})

V_102 = Vertex(name = 'V_102',
               particles = [ P.Delta__minus____tilde__, P.Delta0, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
               couplings = {(0,0):C.GC_142,(0,3):C.GC_136,(0,4):C.GC_140,(0,1):C.GC_157,(0,2):C.GC_148,(0,5):C.GC_152})

V_103 = Vertex(name = 'V_103',
               particles = [ P.Delta0__tilde__, P.Delta__minus__, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
               couplings = {(0,0):C.GC_143,(0,3):C.GC_137,(0,4):C.GC_141,(0,1):C.GC_156,(0,2):C.GC_149,(0,5):C.GC_153})

V_104 = Vertex(name = 'V_104',
               particles = [ P.Delta__minus____tilde__, P.Delta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,4):C.GC_124,(0,0):C.GC_128,(0,3):C.GC_117,(0,1):C.GC_110,(0,2):C.GC_101,(0,5):C.GC_105})

V_105 = Vertex(name = 'V_105',
               particles = [ P.Delta__plus____tilde__, P.Delta0, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS1, L.RRVS2, L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
               couplings = {(0,0):C.GC_145,(0,4):C.GC_134,(0,5):C.GC_139,(0,1):C.GC_154,(0,3):C.GC_147,(0,6):C.GC_151,(0,2):C.GC_98})

V_106 = Vertex(name = 'V_106',
               particles = [ P.Delta0__tilde__, P.Delta__plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS1, L.RRVS2, L.RRVS3, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
               couplings = {(0,0):C.GC_144,(0,4):C.GC_133,(0,5):C.GC_138,(0,1):C.GC_155,(0,3):C.GC_146,(0,6):C.GC_150,(0,2):C.GC_97})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Delta__plus____tilde__, P.Delta__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_118,(0,4):C.GC_125,(0,0):C.GC_129,(0,1):C.GC_107,(0,2):C.GC_100,(0,5):C.GC_104})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus__, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
               couplings = {(0,0):C.GC_143,(0,3):C.GC_137,(0,4):C.GC_141,(0,1):C.GC_156,(0,2):C.GC_149,(0,5):C.GC_153})

V_109 = Vertex(name = 'V_109',
               particles = [ P.Delta__plus____tilde__, P.Delta__plus____plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS1, L.RRVS2, L.RRVS4, L.RRVS5, L.RRVS6, L.RRVS7 ],
               couplings = {(0,0):C.GC_142,(0,3):C.GC_136,(0,4):C.GC_140,(0,1):C.GC_157,(0,2):C.GC_148,(0,5):C.GC_152})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus____plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RRV1, L.RRV2, L.RRV3, L.RRV4, L.RRV5, L.RRV6 ],
               couplings = {(0,3):C.GC_121,(0,4):C.GC_126,(0,0):C.GC_130,(0,1):C.GC_109,(0,2):C.GC_102,(0,5):C.GC_106})

V_111 = Vertex(name = 'V_111',
               particles = [ P.e__plus__, P.e__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_112 = Vertex(name = 'V_112',
               particles = [ P.mu__plus__, P.mu__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_113 = Vertex(name = 'V_113',
               particles = [ P.ta__plus__, P.ta__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_114 = Vertex(name = 'V_114',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_92})

V_115 = Vertex(name = 'V_115',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_92})

V_116 = Vertex(name = 'V_116',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_92})

V_117 = Vertex(name = 'V_117',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_92})

V_118 = Vertex(name = 'V_118',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_92})

V_119 = Vertex(name = 'V_119',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_92})

V_120 = Vertex(name = 'V_120',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_119})

V_121 = Vertex(name = 'V_121',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_119})

V_122 = Vertex(name = 'V_122',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV16 ],
               couplings = {(0,0):C.GC_119})

V_123 = Vertex(name = 'V_123',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV16, L.FFV17 ],
               couplings = {(0,0):C.GC_94,(0,1):C.GC_114})

V_124 = Vertex(name = 'V_124',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV16, L.FFV17 ],
               couplings = {(0,0):C.GC_94,(0,1):C.GC_114})

V_125 = Vertex(name = 'V_125',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV16, L.FFV17 ],
               couplings = {(0,0):C.GC_94,(0,1):C.GC_114})

V_126 = Vertex(name = 'V_126',
               particles = [ P.p__tilde__, P.n, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_74})

V_127 = Vertex(name = 'V_127',
               particles = [ P.n__tilde__, P.p, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_75})

V_128 = Vertex(name = 'V_128',
               particles = [ P.n__tilde__, P.n, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_72})

V_129 = Vertex(name = 'V_129',
               particles = [ P.p__tilde__, P.n, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_73})

V_130 = Vertex(name = 'V_130',
               particles = [ P.n__tilde__, P.p, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_73})

V_131 = Vertex(name = 'V_131',
               particles = [ P.p__tilde__, P.p, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_71})

V_132 = Vertex(name = 'V_132',
               particles = [ P.Delta0__tilde__, P.Delta0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_53,(0,1):C.GC_62,(0,2):C.GC_43})

V_133 = Vertex(name = 'V_133',
               particles = [ P.Delta__minus____tilde__, P.Delta0, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS2, L.RRVS4, L.RRVS7 ],
               couplings = {(0,0):C.GC_69,(0,1):C.GC_50,(0,2):C.GC_60})

V_134 = Vertex(name = 'V_134',
               particles = [ P.Delta__minus____tilde__, P.Delta0, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_56,(0,1):C.GC_66,(0,2):C.GC_46})

V_135 = Vertex(name = 'V_135',
               particles = [ P.Delta0__tilde__, P.Delta__minus__, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS2, L.RRVS4, L.RRVS7 ],
               couplings = {(0,0):C.GC_70,(0,1):C.GC_49,(0,2):C.GC_59})

V_136 = Vertex(name = 'V_136',
               particles = [ P.Delta0__tilde__, P.Delta__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_56,(0,1):C.GC_66,(0,2):C.GC_46})

V_137 = Vertex(name = 'V_137',
               particles = [ P.Delta__minus____tilde__, P.Delta__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_54,(0,1):C.GC_61,(0,2):C.GC_44})

V_138 = Vertex(name = 'V_138',
               particles = [ P.Delta__plus____tilde__, P.Delta0, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS2, L.RRVS4, L.RRVS7 ],
               couplings = {(0,0):C.GC_68,(0,1):C.GC_47,(0,2):C.GC_57})

V_139 = Vertex(name = 'V_139',
               particles = [ P.Delta__plus____tilde__, P.Delta0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_55,(0,1):C.GC_65,(0,2):C.GC_45})

V_140 = Vertex(name = 'V_140',
               particles = [ P.Delta0__tilde__, P.Delta__plus__, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS2, L.RRVS4, L.RRVS7 ],
               couplings = {(0,0):C.GC_67,(0,1):C.GC_48,(0,2):C.GC_58})

V_141 = Vertex(name = 'V_141',
               particles = [ P.Delta0__tilde__, P.Delta__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_55,(0,1):C.GC_65,(0,2):C.GC_45})

V_142 = Vertex(name = 'V_142',
               particles = [ P.Delta__plus____tilde__, P.Delta__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_52,(0,1):C.GC_63,(0,2):C.GC_42})

V_143 = Vertex(name = 'V_143',
               particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus__, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS2, L.RRVS4, L.RRVS7 ],
               couplings = {(0,0):C.GC_70,(0,1):C.GC_49,(0,2):C.GC_59})

V_144 = Vertex(name = 'V_144',
               particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_56,(0,1):C.GC_66,(0,2):C.GC_46})

V_145 = Vertex(name = 'V_145',
               particles = [ P.Delta__plus____tilde__, P.Delta__plus____plus__, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRVS2, L.RRVS4, L.RRVS7 ],
               couplings = {(0,0):C.GC_69,(0,1):C.GC_50,(0,2):C.GC_60})

V_146 = Vertex(name = 'V_146',
               particles = [ P.Delta__plus____tilde__, P.Delta__plus____plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_56,(0,1):C.GC_66,(0,2):C.GC_46})

V_147 = Vertex(name = 'V_147',
               particles = [ P.Delta__plus____plus____tilde__, P.Delta__plus____plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RRS1, L.RRS2, L.RRS3 ],
               couplings = {(0,0):C.GC_51,(0,1):C.GC_64,(0,2):C.GC_41})

V_148 = Vertex(name = 'V_148',
               particles = [ P.Delta0__tilde__, P.n, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFS1 ],
               couplings = {(0,0):C.GC_83})

V_149 = Vertex(name = 'V_149',
               particles = [ P.Delta0__tilde__, P.n, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_280})

V_150 = Vertex(name = 'V_150',
               particles = [ P.Delta0__tilde__, P.n, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_281})

V_151 = Vertex(name = 'V_151',
               particles = [ P.Delta__plus____tilde__, P.p, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFS1 ],
               couplings = {(0,0):C.GC_83})

V_152 = Vertex(name = 'V_152',
               particles = [ P.Delta__plus____tilde__, P.p, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_280})

V_153 = Vertex(name = 'V_153',
               particles = [ P.Delta__plus____tilde__, P.p, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_281})

V_154 = Vertex(name = 'V_154',
               particles = [ P.Delta__minus____tilde__, P.n, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_86})

V_155 = Vertex(name = 'V_155',
               particles = [ P.Delta__minus____tilde__, P.n, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFS1 ],
               couplings = {(0,0):C.GC_82})

V_156 = Vertex(name = 'V_156',
               particles = [ P.Delta__plus____tilde__, P.n, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_88})

V_157 = Vertex(name = 'V_157',
               particles = [ P.Delta__plus____tilde__, P.n, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFS1 ],
               couplings = {(0,0):C.GC_84})

V_158 = Vertex(name = 'V_158',
               particles = [ P.Delta__minus____tilde__, P.n, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_277})

V_159 = Vertex(name = 'V_159',
               particles = [ P.Delta__plus____tilde__, P.n, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_279})

V_160 = Vertex(name = 'V_160',
               particles = [ P.Delta__minus____tilde__, P.n, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_167})

V_161 = Vertex(name = 'V_161',
               particles = [ P.Delta__plus____tilde__, P.n, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_169})

V_162 = Vertex(name = 'V_162',
               particles = [ P.Delta0__tilde__, P.p, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_88})

V_163 = Vertex(name = 'V_163',
               particles = [ P.Delta0__tilde__, P.p, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFS1 ],
               couplings = {(0,0):C.GC_85})

V_164 = Vertex(name = 'V_164',
               particles = [ P.Delta__plus____plus____tilde__, P.p, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_86})

V_165 = Vertex(name = 'V_165',
               particles = [ P.Delta__plus____plus____tilde__, P.p, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFS1 ],
               couplings = {(0,0):C.GC_81})

V_166 = Vertex(name = 'V_166',
               particles = [ P.Delta0__tilde__, P.p, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_279})

V_167 = Vertex(name = 'V_167',
               particles = [ P.Delta__plus____plus____tilde__, P.p, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_277})

V_168 = Vertex(name = 'V_168',
               particles = [ P.Delta0__tilde__, P.p, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_169})

V_169 = Vertex(name = 'V_169',
               particles = [ P.Delta__plus____plus____tilde__, P.p, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RFVS1 ],
               couplings = {(0,0):C.GC_167})

V_170 = Vertex(name = 'V_170',
               particles = [ P.n__tilde__, P.Delta0, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRS1 ],
               couplings = {(0,0):C.GC_83})

V_171 = Vertex(name = 'V_171',
               particles = [ P.n__tilde__, P.Delta__minus__, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_87})

V_172 = Vertex(name = 'V_172',
               particles = [ P.n__tilde__, P.Delta__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRS1 ],
               couplings = {(0,0):C.GC_82})

V_173 = Vertex(name = 'V_173',
               particles = [ P.n__tilde__, P.Delta__plus__, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_89})

V_174 = Vertex(name = 'V_174',
               particles = [ P.n__tilde__, P.Delta__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRS1 ],
               couplings = {(0,0):C.GC_84})

V_175 = Vertex(name = 'V_175',
               particles = [ P.p__tilde__, P.Delta0, P.A, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_89})

V_176 = Vertex(name = 'V_176',
               particles = [ P.p__tilde__, P.Delta0, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRS1 ],
               couplings = {(0,0):C.GC_85})

V_177 = Vertex(name = 'V_177',
               particles = [ P.p__tilde__, P.Delta__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRS1 ],
               couplings = {(0,0):C.GC_83})

V_178 = Vertex(name = 'V_178',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.A, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_87})

V_179 = Vertex(name = 'V_179',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRS1 ],
               couplings = {(0,0):C.GC_81})

V_180 = Vertex(name = 'V_180',
               particles = [ P.n__tilde__, P.Delta0, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_280})

V_181 = Vertex(name = 'V_181',
               particles = [ P.n__tilde__, P.Delta__plus__, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_278})

V_182 = Vertex(name = 'V_182',
               particles = [ P.p__tilde__, P.Delta__plus__, P.W__minus__, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_280})

V_183 = Vertex(name = 'V_183',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.W__minus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_276})

V_184 = Vertex(name = 'V_184',
               particles = [ P.n__tilde__, P.Delta0, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_281})

V_185 = Vertex(name = 'V_185',
               particles = [ P.n__tilde__, P.Delta__minus__, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_276})

V_186 = Vertex(name = 'V_186',
               particles = [ P.p__tilde__, P.Delta0, P.W__plus__, P.Pi0 ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_278})

V_187 = Vertex(name = 'V_187',
               particles = [ P.p__tilde__, P.Delta__plus__, P.W__plus__, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_281})

V_188 = Vertex(name = 'V_188',
               particles = [ P.n__tilde__, P.Delta__minus__, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_166})

V_189 = Vertex(name = 'V_189',
               particles = [ P.n__tilde__, P.Delta__plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_168})

V_190 = Vertex(name = 'V_190',
               particles = [ P.p__tilde__, P.Delta0, P.Z, P.Pi__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_168})

V_191 = Vertex(name = 'V_191',
               particles = [ P.p__tilde__, P.Delta__plus____plus__, P.Z, P.Pi__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FRVS1 ],
               couplings = {(0,0):C.GC_166})

