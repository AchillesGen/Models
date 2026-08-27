#!/usr/bin/env python3
"""PCAC on the CC single-pion current, against the model's own pi N amplitude.

Adler's relation ties the divergence of the axial current to the pion-nucleon
amplitude.  With PCAC, d_mu A^mu = f_pi mpi^2 phi_pi, and the pion field creates
the off-shell pion whose propagator times the pi N amplitude gives the matrix
element, so

    | q_mu <pi N'| A^mu |N> |  =  f_pi mpi^2 |T(pi* N -> pi N')| / (Q^2 + mpi^2)

with T the pi N amplitude at the SAME kinematics and the incoming pion off shell
at q^2 = -Q^2.  Nothing here is fitted: T is built from the model's own strong
vertices, which tools/pin_scattering.py validates against the unitarity limit.

CONTRACTING q INTO THE FULL CURRENT IS ENOUGH.  q_mu V^mu = 0 is already
verified to 1e-16 by tools/ward_background.py, so contracting q into the full
W+ N -> pi N' current leaves the axial piece alone and nothing has to be split
by hand.

WHAT IT MEASURES, and what it does NOT.  Measured on ChiPT_UFO_V9,
W+ p -> pi+ p, the ratio came out

      Q^2     W=1.209   W=1.300
     0.01      0.317     0.456
     0.05      0.328     0.630
     0.20      0.506     1.179
     0.50      0.737     1.616

and on V10, after the induced-pseudoscalar sign was fixed, 0.314 / 0.292 /
0.228 / 0.141 on the peak -- the same shortfall at Q^2 -> 0 and a cleaner,
monotonic fall away from it (V9's rise came from the wrong-sign F_P inflating
|q.H|, not from anything getting better).

THIS SHORTFALL IS NOT THE MISSING PION POLE, and an earlier version of this
docstring said it was.  The pole contributes

    q_mu [ f_pi q^mu/(q^2 - mpi^2) T ]  =  f_pi Q^2/(Q^2 + mpi^2) T

to the divergence -- it carries a factor q^2 and therefore VANISHES at
Q^2 -> 0, which is exactly where the deficit is largest.  Its job is the
opposite one: at large Q^2 it SUBTRACTS from the pole-free f_pi T and leaves
the f_pi mpi^2/(Q^2+mpi^2) T that PCAC asks for.  Adding it (ChiPT_UFO_V11,
LPPoleFF) moves the Q^2 -> 0 number by 0.1%, as it must.

So what the Q^2 -> 0 ratio measures is the Adler consistency of the pole-FREE
current against the model's own pi-N amplitude, and 0.31 says those two are
not consistent.  Two things could produce that and this script cannot separate
them: the current could be short, or T_piN below could be too large -- note it
is evaluated with the incoming pion OFF SHELL at q^2 = -Q^2, which is a
model-dependent continuation, and that the s-channel Delta dominates it.
Treat the number as a diagnostic, not as a measurement of a missing diagram.

Usage:  python3 tools/pcac_1pi.py
"""
import os
import sys

ROOT='/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/myPions-Pion-Nucleon-Delta-GI-coupling-Photoexcitation'
sys.path.insert(0,ROOT); os.chdir(ROOT); sys.path.insert(0,ROOT+'/tools')
import numpy as np
from fig33_from_ufo import (build, uspinor, ubar, prop_fermion, rs_numerator,
                            dot, METRIC, kmom, load_ufo, parameter_namespace)
from wprod_from_ufo import hadronic_current, form_factors
import importlib
MODEL = os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V9')
VM = importlib.import_module(MODEL + '.vertices')
P, Vmod = load_ufo(MODEL); ns = parameter_namespace(P)
ff = form_factors(ns, True)
V = Vmod.all_vertices
VMOD = Vmod
MN=ns['MNucleon']; MD=ns['MDelta']; mpi=ns['MPiP']; fpi=float(ns['fPi'])
GD=float(ns['WDeltaP'])
def vtx(names):
    w=sorted(names); return [v for v in V if sorted(p.name for p in v.particles)==w][0]

def T_piN(qin, p, kout, pp):
    """pi+*(qin) p -> pi+(kout) p, incoming pion OFF SHELL at qin^2."""
    vs=p+qin; vu=p-kout
    M=np.zeros((4,4),dtype=complex)
    Vp=build(vtx(['p~','Delta++','Pi-']), {'p~':-p,'Delta++':vs,'Pi-':-qin}, ns, ff)
    Vd=build(vtx(['Delta++~','p','Pi+']), {'Delta++~':-vs,'p':pp,'Pi+':kout}, ns, ff)
    N=rs_numerator(vs,MD); den=dot(vs,vs)-MD**2+1j*MD*GD
    for a in range(4):
        for b in range(4):
            M+=METRIC[a,a]*METRIC[b,b]*Vd[a]@(1j*N[a,b]/den)@Vp[b]
    Ve=build(vtx(['p~','n','Pi+']), {'p~':-p,'n':vu,'Pi+':kout}, ns, ff)
    Va=build(vtx(['n~','p','Pi-']), {'n~':-vu,'p':pp,'Pi-':-qin}, ns, ff)
    M+=Va@prop_fermion(vu,MN)@Ve
    Ve=build(vtx(['p~','Delta0','Pi+']), {'p~':-p,'Delta0':vu,'Pi+':kout}, ns, ff)
    Va=build(vtx(['Delta0~','p','Pi-']), {'Delta0~':-vu,'p':pp,'Pi-':-qin}, ns, ff)
    N=rs_numerator(vu,MD); den=dot(vu,vu)-MD**2+1j*MD*GD
    for a in range(4):
        for b in range(4):
            M+=METRIC[a,a]*METRIC[b,b]*Va[a]@(1j*N[a,b]/den)@Ve[b]
    M+=build(vtx(['p~','p','Pi-','Pi+']), {'p~':-p,'p':pp,'Pi-':-qin,'Pi+':kout}, ns, ff)
    return M

def norm(M,p,pp):
    return np.sqrt(sum(abs(ubar(uspinor(pp,MN,s2)) @ M @ uspinor(p,MN,s1))**2
                       for s1 in range(2) for s2 in range(2)))

G=np.diag(METRIC).real
print("PCAC on the CC1pi current:  |q.H| vs  f_pi mpi^2 |T_piN| / (Q^2+mpi^2)")
print("W+ p -> pi+ p, and the SAME kinematics for pi+* p -> pi+ p\n")
print("  %7s %7s %13s %13s %9s" % ("Q^2","W","|q.H|","PCAC pred","ratio"))
for W in (1.209, 1.30):
    for Q2 in (0.01, 0.05, 0.2, 0.5):
        # W+(q) p(P) -> pi+(k) p(pp) in the hadronic cms
        q0=(W**2-MN**2-Q2)/(2*W); qz=np.sqrt(q0**2+Q2)
        q=np.array([q0,0,0,qz],dtype=complex)
        Pp=np.array([W-q0,0,0,-qz],dtype=complex)
        kk=kmom(W**2,mpi,MN); th=0.7
        k=np.array([np.sqrt(kk**2+mpi**2),kk*np.sin(th),0,kk*np.cos(th)],dtype=complex)
        pp=np.array([W-k[0].real,-kk*np.sin(th),0,-kk*np.cos(th)],dtype=complex)
        opt=dict(born=True,delta=True,dwidth=True,wwidth=True)
        H=hadronic_current('ppip', q, Pp, k, pp, VMOD, ns, ff, opt)
        C=sum(G[m]*q[m]*H[m] for m in range(4))
        T=T_piN(q,Pp,k,pp)
        num=norm(C,Pp,pp)
        den=fpi*mpi**2/(Q2+mpi**2)*norm(T,Pp,pp)
        print("  %7.3f %7.3f %13.5g %13.5g %9.4f" % (Q2,W,num,den,num/den))
