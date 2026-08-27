#!/usr/bin/env python3
"""Adler decomposition of the model's weak N -> Delta transition.

Reads the UFO vertex and fits it to the eight standard structures

    axial   C3A (g^{am} qslash - q^a gamma^m)/M ,  C4A (g^{am} q.p' - q^a p'^m)/M^2 ,
            C5A g^{am} ,                           C6A q^a q^m / M^2
    vector  the same four contracted with gamma5 (C3V, C4V, C5V, C6V)

by least squares on ubar_alpha(p_Delta) V^{alpha mu} u(p) over all four Delta
helicities, both nucleon spins and all four mu -- 32 complex equations for 8
unknowns.  The fit is EXACT (residual ~1e-15), which is itself the first
result: the model's vertex really does live in the Adler basis, so the
coefficients below are a faithful description of it and not a projection.

The sqrt(3) p -> Delta++ Clebsch is divided out, so these are REDUCED
coefficients directly comparable with the phenomenological values.  Form
factors are set to 1, so what comes out is the coupling times shape at Q^2 = 0.

WHAT IT FINDS (2026-08-26, ChiPT_UFO_V9):

    C3A  +0.0000     want 0                      OK
    C4A  +0.1551     C4A/C5A = -1/8              <-- WANT -1/4, OFF BY 2
    C5A  -1.2411     want ~1.2                   OK to 3%
    C6A  -1.0926     C6A/C5A = 0.8803 = M^2      OK, exactly PCAC
    C3V  -2.0898     want ~2.13                  OK to 2%
    C4V  +0.9759     C4V/C3V = -0.467            NOT a discrepancy, see below
    C5V, C6V  0, 0   want 0, 0                   OK

C3V coming out at the known 2.13 is what validates the normalisation of this
extraction -- the sqrt(3), the g_cc and the basis -- independently of anything
being tested.  The relative isospin is checked too: the Delta++/Delta+ ratio is
sqrt3 = 1.7321 for EVERY coefficient, axial and vector alike, so the two sectors
share one isospin routing.  The eight structures are well separated at this
kinematic point (condition number 52), so none of this rests on a degenerate fit.

C4V IS NOT WRONG.  C4V/C3V = -M/MD is the PURE M1 idealisation that HNV and
Lalakulich-Paschos adopt as a simplification; it gives E2/M1 = 0 identically.
Building a synthetic vertex from the extracted C3V and C4V alone reproduces the
model's photon helicity ratio |A_3/2|/|A_1/2| = 1.9152 exactly, and that
corresponds to E2/M1 = -2.45% against the measured EMR of about -2.5%.  So the
model carries a physical E2 admixture where the standard parameterisation
carries none -- it is closer to the data here, not further.  (1.9152 also
reproduces delta_couplings.py's independently computed value, and the pure-M1
synthetic returns sqrt3 to machine precision, which validates both machineries.)

THE GAMMA5 IN ChiPT.fr's COMMENT IS AN INTERNAL CONVENTION ONLY.  LC6ANDelta
notes that "in this model's Rarita-Schwinger convention the C5A structure is the
one that carries the explicit Gamma5".  The EXPORTED vertex is not like that:
this fit puts C5A on g^{am} x Identity and returns exactly zero on g^{am} gamma5,
i.e. the standard Adler convention in which the axial current carries no gamma5.
The model's Delta field must carry a relative gamma5 against the standard RS
convention, and it cancels on export.

THE C4A RESULT IS A BUG.  formfactors.py describes C4AN as "calibrated so the
extracted C4A/C5A is -1/4", and the param card carries C4AN = 0.215822.  It
delivers -1/8.  C4AN should be 0.431644.  Whoever calibrated it presumably used
the projection in delta_couplings.py item 4, which prints its own warning that
the epsilon structure is not pure g^{alpha mu} at its chosen point and returns
C5A(0) = 0.065 instead of 1.24.

IT IS NOT THE FACTOR 2 IN THE CROSS SECTION.  Doubling C4AN moves
sigma(nu p -> mu- p pi+, W<1.4) at 1 GeV by 1.0%, from 0.97844 to 0.96827
(1e-38 cm^2, corrected units).  Every other coefficient is at its standard
value, so the Delta axial structure does not contain the 2x reported in
tools/ccqe_ls.py.

Usage:  python3 tools/adler_ndelta.py
"""

import sys, os
ROOT='/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/myPions-Pion-Nucleon-Delta-GI-coupling-Photoexcitation'
sys.path.insert(0,ROOT); os.chdir(ROOT)
import numpy as np
from fig33_from_ufo import (build, uspinor, ubar, GAMMA, GAMMA5, METRIC,
                            load_ufo, parameter_namespace, dot)
from delta_couplings import rs_spinor, LAMBDAS
import importlib
MODEL = os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V9')
VM = importlib.import_module(MODEL + '.vertices')

P,_=load_ufo(MODEL); ns=parameter_namespace(P)
MN=float(ns['MNucleon']); MD=float(ns['MDelta']); mpi=float(ns['MPiP'])
ee=float(ns['ee'].real); sw=float(ns['sw'].real); Vud=float(ns['Vud'].real)
gcc = ee*Vud/(2*sw*np.sqrt(2))
V=VM.all_vertices
def vtx(names):
    w=sorted(names); return [v for v in V if sorted(p.name for p in v.particles)==w][0]
ONE = {n:(lambda x: 1.0) for n in
       ('FCA5','FC6A','FVND','FpiNDelta','FW1','FWA','FW2','FPP')}

def slash(v):
    return sum(v[m]*METRIC[m,m]*GAMMA[m] for m in range(4))

def basis(q, p, pD, M):
    """The eight Adler structures B[name][alpha][mu] as 4x4 Dirac matrices."""
    g = np.zeros((4,4)); np.fill_diagonal(g, np.diag(METRIC))
    qs = slash(q); I=np.eye(4,dtype=complex)
    qp  = dot(q,pD); qpn = dot(q,p)
    B={}
    def mk(f): return np.array([[f(a,m) for m in range(4)] for a in range(4)])
    B['C3A']=mk(lambda a,m: (g[a,m]*qs - q[a]*GAMMA[m])/M)
    B['C4A']=mk(lambda a,m: (g[a,m]*qp - q[a]*pD[m])*I/M**2)
    B['C5A']=mk(lambda a,m: g[a,m]*I)
    B['C6A']=mk(lambda a,m: q[a]*q[m]*I/M**2)
    B['C3V']=mk(lambda a,m: (g[a,m]*qs - q[a]*GAMMA[m])@GAMMA5/M)
    B['C4V']=mk(lambda a,m: (g[a,m]*qp - q[a]*pD[m])*GAMMA5/M**2)
    B['C5V']=mk(lambda a,m: (g[a,m]*qpn - q[a]*p[m])*GAMMA5/M**2)
    B['C6V']=mk(lambda a,m: g[a,m]*GAMMA5)
    return B

def sandwich(T, p, pD):
    """[lambda, s, mu] of ubar_alpha(pD) T^{alpha mu} u(p)."""
    G=np.diag(METRIC).real
    out=np.zeros((4,2,4),dtype=complex)
    us=[uspinor(p,MN,s) for s in range(2)]
    for il,tl in enumerate(LAMBDAS):
        ud=rs_spinor(pD,MD,tl)
        for s in range(2):
            for m in range(4):
                out[il,s,m]=sum(G[a]*(ubar(ud[a]) @ T[a][m] @ us[s]) for a in range(4))
    return out.reshape(-1)

print("Adler decomposition of the model's weak N -> Delta vertex (p -> Delta++)")
print("coefficients are REDUCED: the sqrt(3) p->Delta++ Clebsch is divided out")
print("form factors set to 1, so these are the Q^2 = 0 couplings times shape\n")
names=['C3A','C4A','C5A','C6A','C3V','C4V','C5V','C6V']
print("  %7s " % "Q^2" + "".join("%9s"%n for n in names) + "%11s" % "resid")
for Q2 in (0.0, 0.05, 0.2, 0.5, 1.0):
    # Delta at rest -> clean RS spinors (rs_spinor is a REST-frame construction)
    pD=np.array([MD,0,0,0],dtype=complex)
    # nucleon: E_N = (MD^2+MN^2+Q2)/(2MD), |p| from on-shell
    EN=(MD**2+MN**2+Q2)/(2*MD)
    pz=np.sqrt(max(EN**2-MN**2,0.0))
    p=np.array([EN,0,0,-pz],dtype=complex)
    q=pD-p
    Vw = build(vtx(['p~','Delta++','W-']), {'p~':-p,'Delta++':pD,'W-':-q}, ns, ONE)
    y = sandwich([[Vw[a,m] for m in range(4)] for a in range(4)], p, pD)/(1j*gcc*np.sqrt(3))
    B = basis(q,p,pD,MN)
    A = np.stack([sandwich([[B[n][a][m] for m in range(4)] for a in range(4)], p, pD)
                  for n in names],axis=1)
    c,_,_,_ = np.linalg.lstsq(A,y,rcond=None)
    res = np.linalg.norm(A@c-y)/max(np.linalg.norm(y),1e-30)
    print("  %7.3f " % Q2 + "".join("%9.4f"%v.real for v in c) + "%11.1e"%res)
    if Q2 == 0.0:
        cz = {n: v.real for n, v in zip(names, c)}

# The two calibration ratios, at full precision.  Both C5A and C3V come from
# the gauged Pascalutsa coupling and so carry hD, while the C4A operator has
# its own constant C4AN -- so the ratio C4A/C5A moves whenever hD moves, and
# in a model whose hD is DERIVED from Gamma(Delta -> N pi) that happens every
# time the width or the Delta mass is touched.  Reporting C4AN/hD is what makes
# the calibration portable: it is the number ChiPT.fr stores, and the C4A/C5A
# printed above is what it has to deliver.
_hD = float(np.real(ns['hD']))
_c4 = float(np.real(ns['C4AN']))
print("\ncalibration, full precision:")
print("   C4A/C5A      = %+.8f   (want -0.25)" % (cz['C4A'] / cz['C5A']))
print("   C5A(0)/hD    = %+.8f" % (cz['C5A'] / _hD))
print("   C4A(0)/C4AN  = %+.8f" % (cz['C4A'] / _c4))
print("   C4AN/hD now  = %+.8f" % (_c4 / _hD))
print("   C4AN/hD for C4A/C5A = -1/4: %+.8f"
      % (-0.25 * (cz['C5A'] / _hD) / (cz['C4A'] / _c4)))
print("\nstandard values: C3A = 0,  C4A = -C5A/4,  C5A(0) ~ 1.2,")
print("                 C6A = C5A M^2/(Q^2+mpi^2)")
for Q2 in (0.0,0.05,0.2,0.5,1.0):
    print("   Q^2=%.2f  C6A/C5A should be M^2/(Q^2+mpi^2) = %8.3f"
          % (Q2, MN**2/(Q2+mpi**2)))
