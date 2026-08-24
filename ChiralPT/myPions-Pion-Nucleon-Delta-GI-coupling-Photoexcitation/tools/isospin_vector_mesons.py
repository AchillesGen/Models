"""Isospin decomposition: does the vector-meson exchange enter the CC channels
with the pi0-like (destructive) or pi+-like (constructive) weight?

An isovector current J^b producing pion a off a nucleon has only two isospin
structures:

    T^{ab} = delta^{ab} A(+)  +  i eps^{abc} tau^c A(-)

and an ISOSCALAR current has only one,  T^a = tau^a A(0).

Where the mesons sit follows from their own quantum numbers:
  omega  isoscalar, so the gamma-pi-omega vertex needs the ISOVECTOR photon and
         carries delta^{ab}; omega-N-N is isoscalar (no tau).   -> pure A(+)
  rho    isovector; isovector photon gives eps^{abc}, rho-N-N gives tau^c
                                                                -> pure A(-)
         isoscalar photon gives delta, rho-N-N gives tau^a      -> pure A(0)

A(0) has NO charged-current analogue (the W has no isoscalar piece), so the rho
piece that lives in A(0) drops out of the weak sector while the A(-) piece does
not.  That is the correction to what I said earlier.
"""
import numpy as np, itertools

tau=[np.array([[0,1],[1,0]],dtype=complex),
     np.array([[0,-1j],[1j,0]],dtype=complex),
     np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
eps=np.zeros((3,3,3));
for i,j,k in itertools.permutations(range(3)):
    eps[i,j,k]=np.sign(np.linalg.det(np.eye(3)[[i,j,k]]))

# Cartesian polarisation vectors for the pion charge states (Condon-Shortley)
e={'+': -(np.array([1,1j,0]))/np.sqrt(2),
   '0':  np.array([0,0,1],dtype=complex),
   '-':  (np.array([1,-1j,0]))/np.sqrt(2)}
# current: photon = Cartesian 3 ; CC raising = spherical +1 component
cur={'EM': np.array([0,0,1],dtype=complex),
     'CC': -(np.array([1,1j,0]))/np.sqrt(2)}
p=np.array([1,0],dtype=complex); n=np.array([0,1],dtype=complex)
N={'p':p,'n':n}

def amp(pion, current, Ni, Nf):
    """coefficients of (A+, A-, A0) for <Nf pion| J_current |Ni>"""
    ea=np.conj(e[pion]); cb=cur[current]
    Ap=sum(ea[a]*cb[a] for a in range(3))                       # delta^{ab}
    Am=sum(1j*eps[a,b,c]*ea[a]*cb[b]*(np.conj(N[Nf])@tau[c]@N[Ni])
           for a in range(3) for b in range(3) for c in range(3))
    A0=sum(ea[a]*(np.conj(N[Nf])@tau[a]@N[Ni]) for a in range(3)) \
       if current=='EM' else 0.0                                 # isoscalar: EM only
    ov=np.conj(N[Nf])@N[Ni]
    return Ap*ov, Am, A0

print("PHOTOPRODUCTION            A(+) [omega]      A(-) [rho_iv]     A(0) [rho_is]")
photo=[('pi0 p','0','EM','p','p'),('pi0 n','0','EM','n','n'),
       ('pi+ n','+','EM','p','n'),('pi- p','-','EM','n','p')]
for lbl,pi,cu,i,f in photo:
    a,b,c=amp(pi,cu,i,f)
    print("  %-8s        %14s %18s %16s"%(lbl,f"{a:+.4g}",f"{b:+.4g}",f"{c:+.4g}"))

print("\nCHARGED CURRENT (W+ raising)   A(+) [omega]      A(-) [rho_iv]     A(0)")
cc=[('p -> p pi+  (ppip)','+','CC','p','p'),
    ('n -> p pi0  (ppi0)','0','CC','n','p'),
    ('n -> n pi+  (npip)','+','CC','n','n')]
for lbl,pi,cu,i,f in cc:
    a,b,c=amp(pi,cu,i,f)
    print("  %-20s %10s %18s %16s"%(lbl,f"{a:+.4g}",f"{b:+.4g}",f"{c:+.4g}"))
