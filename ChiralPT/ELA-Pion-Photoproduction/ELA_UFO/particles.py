# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Tue 28 Jul 2026 12:26:20


from __future__ import division
from __future__ import absolute_import
from .object_library import all_particles, Particle
from . import parameters as Param

from . import propagators as Prop

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
             BaryonNumber = 0)

omega = Particle(pdg_code = 223,
                 name = 'omega',
                 antiname = 'omega',
                 spin = 3,
                 color = 1,
                 mass = Param.MOm,
                 width = Param.WOm,
                 texname = 'omega',
                 antitexname = 'omega',
                 charge = 0,
                 BaryonNumber = 0)

rho0 = Particle(pdg_code = 113,
                name = 'rho0',
                antiname = 'rho0',
                spin = 3,
                color = 1,
                mass = Param.MRho0,
                width = Param.WRho0,
                texname = 'rho0',
                antitexname = 'rho0',
                charge = 0,
                BaryonNumber = 0)

rho__plus__ = Particle(pdg_code = 213,
                       name = 'rho+',
                       antiname = 'rho-',
                       spin = 3,
                       color = 1,
                       mass = Param.MRhoP,
                       width = Param.WRhoP,
                       texname = 'rho+',
                       antitexname = 'rho-',
                       charge = 1,
                       BaryonNumber = 0)

rho__minus__ = rho__plus__.anti()

pi0 = Particle(pdg_code = 111,
               name = 'pi0',
               antiname = 'pi0',
               spin = 1,
               color = 1,
               mass = Param.MPi0,
               width = Param.ZERO,
               texname = 'pi0',
               antitexname = 'pi0',
               charge = 0,
               BaryonNumber = 0)

pi__plus__ = Particle(pdg_code = 211,
                      name = 'pi+',
                      antiname = 'pi-',
                      spin = 1,
                      color = 1,
                      mass = Param.MPiC,
                      width = Param.ZERO,
                      texname = 'pi+',
                      antitexname = 'pi-',
                      charge = 1,
                      BaryonNumber = 0)

pi__minus__ = pi__plus__.anti()

p = Particle(pdg_code = 2212,
             name = 'p',
             antiname = 'p~',
             spin = 2,
             color = 1,
             mass = Param.MN,
             width = Param.ZERO,
             texname = 'p',
             antitexname = 'p~',
             charge = 1,
             BaryonNumber = 1)

p__tilde__ = p.anti()

n = Particle(pdg_code = 2112,
             name = 'n',
             antiname = 'n~',
             spin = 2,
             color = 1,
             mass = Param.MN,
             width = Param.ZERO,
             texname = 'n',
             antitexname = 'n~',
             charge = 0,
             BaryonNumber = 1)

n__tilde__ = n.anti()

N1440__plus__ = Particle(pdg_code = 12212,
                         name = 'N1440+',
                         antiname = 'N1440+~',
                         spin = 2,
                         color = 1,
                         mass = Param.MN1440,
                         width = Param.WN1440p,
                         texname = 'N1440+',
                         antitexname = 'N1440+~',
                         charge = 1,
                         BaryonNumber = 1)

N1440__plus____tilde__ = N1440__plus__.anti()

N14400 = Particle(pdg_code = 12112,
                  name = 'N14400',
                  antiname = 'N14400~',
                  spin = 2,
                  color = 1,
                  mass = Param.MN1440,
                  width = Param.WN1440n,
                  texname = 'N14400',
                  antitexname = 'N14400~',
                  charge = 0,
                  BaryonNumber = 1)

N14400__tilde__ = N14400.anti()

N1535__plus__ = Particle(pdg_code = 22212,
                         name = 'N1535+',
                         antiname = 'N1535+~',
                         spin = 2,
                         color = 1,
                         mass = Param.MN1535,
                         width = Param.WN1535p,
                         texname = 'N1535+',
                         antitexname = 'N1535+~',
                         charge = 1,
                         BaryonNumber = 1)

N1535__plus____tilde__ = N1535__plus__.anti()

N15350 = Particle(pdg_code = 22112,
                  name = 'N15350',
                  antiname = 'N15350~',
                  spin = 2,
                  color = 1,
                  mass = Param.MN1535,
                  width = Param.WN1535n,
                  texname = 'N15350',
                  antitexname = 'N15350~',
                  charge = 0,
                  BaryonNumber = 1)

N15350__tilde__ = N15350.anti()

N1650__plus__ = Particle(pdg_code = 32212,
                         name = 'N1650+',
                         antiname = 'N1650+~',
                         spin = 2,
                         color = 1,
                         mass = Param.MN1650,
                         width = Param.WN1650p,
                         texname = 'N1650+',
                         antitexname = 'N1650+~',
                         charge = 1,
                         BaryonNumber = 1)

N1650__plus____tilde__ = N1650__plus__.anti()

N16500 = Particle(pdg_code = 32112,
                  name = 'N16500',
                  antiname = 'N16500~',
                  spin = 2,
                  color = 1,
                  mass = Param.MN1650,
                  width = Param.WN1650n,
                  texname = 'N16500',
                  antitexname = 'N16500~',
                  charge = 0,
                  BaryonNumber = 1)

N16500__tilde__ = N16500.anti()

Delta1620__plus____plus__ = Particle(pdg_code = 2222,
                                     name = 'Delta1620++',
                                     antiname = 'Delta1620++~',
                                     spin = 2,
                                     color = 1,
                                     mass = Param.MD1620,
                                     width = Param.WD1620PP,
                                     texname = 'Delta1620++',
                                     antitexname = 'Delta1620++~',
                                     charge = 2,
                                     BaryonNumber = 1)

Delta1620__plus____plus____tilde__ = Delta1620__plus____plus__.anti()

Delta1620__plus__ = Particle(pdg_code = 2122,
                             name = 'Delta1620+',
                             antiname = 'Delta1620+~',
                             spin = 2,
                             color = 1,
                             mass = Param.MD1620,
                             width = Param.WD1620P,
                             texname = 'Delta1620+',
                             antitexname = 'Delta1620+~',
                             charge = 1,
                             BaryonNumber = 1)

Delta1620__plus____tilde__ = Delta1620__plus__.anti()

Delta16200 = Particle(pdg_code = 1212,
                      name = 'Delta16200',
                      antiname = 'Delta16200~',
                      spin = 2,
                      color = 1,
                      mass = Param.MD1620,
                      width = Param.WD1620Z,
                      texname = 'Delta16200',
                      antitexname = 'Delta16200~',
                      charge = 0,
                      BaryonNumber = 1)

Delta16200__tilde__ = Delta16200.anti()

Delta1620__minus__ = Particle(pdg_code = 1112,
                              name = 'Delta1620-',
                              antiname = 'Delta1620-~',
                              spin = 2,
                              color = 1,
                              mass = Param.MD1620,
                              width = Param.WD1620M,
                              texname = 'Delta1620-',
                              antitexname = 'Delta1620-~',
                              charge = -1,
                              BaryonNumber = 1)

Delta1620__minus____tilde__ = Delta1620__minus__.anti()

Delta__plus____plus__ = Particle(pdg_code = 2224,
                                 name = 'Delta++',
                                 antiname = 'Delta++~',
                                 spin = 4,
                                 color = 1,
                                 mass = Param.MDelta,
                                 width = Param.WDeltaPP,
                                 texname = 'Delta++',
                                 antitexname = 'Delta++~',
                                 charge = 2,
                                 BaryonNumber = 1)

Delta__plus____plus____tilde__ = Delta__plus____plus__.anti()

Delta__plus__ = Particle(pdg_code = 2214,
                         name = 'Delta+',
                         antiname = 'Delta+~',
                         spin = 4,
                         color = 1,
                         mass = Param.MDelta,
                         width = Param.WDeltaP,
                         texname = 'Delta+',
                         antitexname = 'Delta+~',
                         charge = 1,
                         BaryonNumber = 1)

Delta__plus____tilde__ = Delta__plus__.anti()

Delta0 = Particle(pdg_code = 2114,
                  name = 'Delta0',
                  antiname = 'Delta0~',
                  spin = 4,
                  color = 1,
                  mass = Param.MDelta,
                  width = Param.WDeltaZ,
                  texname = 'Delta0',
                  antitexname = 'Delta0~',
                  charge = 0,
                  BaryonNumber = 1)

Delta0__tilde__ = Delta0.anti()

Delta__minus__ = Particle(pdg_code = 1114,
                          name = 'Delta-',
                          antiname = 'Delta-~',
                          spin = 4,
                          color = 1,
                          mass = Param.MDelta,
                          width = Param.WDeltaM,
                          texname = 'Delta-',
                          antitexname = 'Delta-~',
                          charge = -1,
                          BaryonNumber = 1)

Delta__minus____tilde__ = Delta__minus__.anti()

N1520__plus__ = Particle(pdg_code = 2124,
                         name = 'N1520+',
                         antiname = 'N1520+~',
                         spin = 4,
                         color = 1,
                         mass = Param.MN1520,
                         width = Param.WN1520p,
                         texname = 'N1520+',
                         antitexname = 'N1520+~',
                         charge = 1,
                         BaryonNumber = 1)

N1520__plus____tilde__ = N1520__plus__.anti()

N15200 = Particle(pdg_code = 1214,
                  name = 'N15200',
                  antiname = 'N15200~',
                  spin = 4,
                  color = 1,
                  mass = Param.MN1520,
                  width = Param.WN1520n,
                  texname = 'N15200',
                  antitexname = 'N15200~',
                  charge = 0,
                  BaryonNumber = 1)

N15200__tilde__ = N15200.anti()

Delta1700__plus____plus__ = Particle(pdg_code = 12224,
                                     name = 'Delta1700++',
                                     antiname = 'Delta1700++~',
                                     spin = 4,
                                     color = 1,
                                     mass = Param.MD1700,
                                     width = Param.WD1700PP,
                                     texname = 'Delta1700++',
                                     antitexname = 'Delta1700++~',
                                     charge = 2,
                                     BaryonNumber = 1)

Delta1700__plus____plus____tilde__ = Delta1700__plus____plus__.anti()

Delta1700__plus__ = Particle(pdg_code = 12214,
                             name = 'Delta1700+',
                             antiname = 'Delta1700+~',
                             spin = 4,
                             color = 1,
                             mass = Param.MD1700,
                             width = Param.WD1700P,
                             texname = 'Delta1700+',
                             antitexname = 'Delta1700+~',
                             charge = 1,
                             BaryonNumber = 1)

Delta1700__plus____tilde__ = Delta1700__plus__.anti()

Delta17000 = Particle(pdg_code = 12114,
                      name = 'Delta17000',
                      antiname = 'Delta17000~',
                      spin = 4,
                      color = 1,
                      mass = Param.MD1700,
                      width = Param.WD1700Z,
                      texname = 'Delta17000',
                      antitexname = 'Delta17000~',
                      charge = 0,
                      BaryonNumber = 1)

Delta17000__tilde__ = Delta17000.anti()

Delta1700__minus__ = Particle(pdg_code = 11114,
                              name = 'Delta1700-',
                              antiname = 'Delta1700-~',
                              spin = 4,
                              color = 1,
                              mass = Param.MD1700,
                              width = Param.WD1700M,
                              texname = 'Delta1700-',
                              antitexname = 'Delta1700-~',
                              charge = -1,
                              BaryonNumber = 1)

Delta1700__minus____tilde__ = Delta1700__minus__.anti()

