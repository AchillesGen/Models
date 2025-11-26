# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Tue 7 Oct 2025 19:50:49


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

A = Particle(pdg_code = 22,
             name = 'A',
             antiname = 'A',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'A',
             antitexname = 'A',
             charge = 0,
             BaryonNumber = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             BaryonNumber = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     BaryonNumber = 0,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               BaryonNumber = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               BaryonNumber = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                BaryonNumber = 0,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                BaryonNumber = 0,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              BaryonNumber = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              BaryonNumber = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              BaryonNumber = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      BaryonNumber = 0,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       BaryonNumber = 0,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       BaryonNumber = 0,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

p = Particle(pdg_code = 2212,
             name = 'p',
             antiname = 'p~',
             spin = 2,
             color = 1,
             mass = Param.MNucleon,
             width = Param.ZERO,
             texname = 'p',
             antitexname = 'p~',
             charge = 1,
             BaryonNumber = 1,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 1)

p__tilde__ = p.anti()

n = Particle(pdg_code = 2112,
             name = 'n',
             antiname = 'n~',
             spin = 2,
             color = 1,
             mass = Param.MNucleon,
             width = Param.ZERO,
             texname = 'n',
             antitexname = 'n~',
             charge = 0,
             BaryonNumber = 1,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 1)

n__tilde__ = n.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             BaryonNumber = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              BaryonNumber = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     BaryonNumber = 0,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Pi0 = Particle(pdg_code = 111,
               name = 'Pi0',
               antiname = 'Pi0',
               spin = 1,
               color = 1,
               mass = Param.MPi,
               width = Param.WPi,
               texname = 'Pi0',
               antitexname = 'Pi0',
               charge = 0,
               BaryonNumber = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

Pi__plus__ = Particle(pdg_code = 211,
                      name = 'Pi+',
                      antiname = 'Pi-',
                      spin = 1,
                      color = 1,
                      mass = Param.MPi,
                      width = Param.WPi,
                      texname = 'Pi+',
                      antitexname = 'Pi-',
                      charge = 1,
                      BaryonNumber = 0,
                      GhostNumber = 0,
                      LeptonNumber = 0,
                      Y = 0)

Pi__minus__ = Pi__plus__.anti()

Eta = Particle(pdg_code = 221,
               name = 'Eta',
               antiname = 'Eta',
               spin = 1,
               color = 1,
               mass = Param.MEta,
               width = Param.WEta,
               texname = 'Eta',
               antitexname = 'Eta',
               charge = 0,
               BaryonNumber = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

K0 = Particle(pdg_code = 311,
              name = 'K0',
              antiname = 'K0~',
              spin = 1,
              color = 1,
              mass = Param.MK0,
              width = Param.WK0,
              texname = 'K0',
              antitexname = 'K0~',
              charge = 0,
              BaryonNumber = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

K0__tilde__ = K0.anti()

K__plus__ = Particle(pdg_code = 321,
                     name = 'K+',
                     antiname = 'K-',
                     spin = 1,
                     color = 1,
                     mass = Param.MKp,
                     width = Param.WKp,
                     texname = 'K+',
                     antitexname = 'K-',
                     charge = 1,
                     BaryonNumber = 0,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

K__minus__ = K__plus__.anti()

Delta__plus____plus__ = Particle(pdg_code = 2224,
                                 name = 'Delta++',
                                 antiname = 'Delta--Bar',
                                 spin = 4,
                                 color = 1,
                                 mass = Param.MDelta,
                                 width = Param.WDelta,
                                 texname = 'Delta++',
                                 antitexname = 'Delta--Bar',
                                 charge = 2,
                                 BaryonNumber = 1,
                                 GhostNumber = 0,
                                 LeptonNumber = 0,
                                 Y = 1)

Delta__minus____minus__Bar = Delta__plus____plus__.anti()

Delta__plus__ = Particle(pdg_code = 2214,
                         name = 'Delta+',
                         antiname = 'Delta-Bar',
                         spin = 4,
                         color = 1,
                         mass = Param.MDelta,
                         width = Param.WDelta,
                         texname = 'Delta+',
                         antitexname = 'Delta-Bar',
                         charge = 1,
                         BaryonNumber = 1,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 1)

Delta__minus__Bar = Delta__plus__.anti()

Delta0 = Particle(pdg_code = 2114,
                  name = 'Delta0',
                  antiname = 'Delta0Bar',
                  spin = 4,
                  color = 1,
                  mass = Param.MDelta,
                  width = Param.WDelta,
                  texname = 'Delta0',
                  antitexname = 'Delta0Bar',
                  charge = 0,
                  BaryonNumber = 1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 1)

Delta0Bar = Delta0.anti()

Delta__minus__ = Particle(pdg_code = 1114,
                          name = 'Delta-',
                          antiname = 'Delta-bar',
                          spin = 4,
                          color = 1,
                          mass = Param.MDelta,
                          width = Param.WDelta,
                          texname = 'Delta-',
                          antitexname = 'Delta-bar',
                          charge = -1,
                          BaryonNumber = 1,
                          GhostNumber = 0,
                          LeptonNumber = 0,
                          Y = 1)

Delta__minus__bar = Delta__minus__.anti()

