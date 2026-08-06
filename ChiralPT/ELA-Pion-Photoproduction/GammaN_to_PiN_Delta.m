(* ****************************************************************************** *)
(*  gamma p -> pi0 p through the Delta(1232), s- and u-channel, constant width.   *)
(*                                                                                *)
(*  The vertices are transcribed from the generated UFO (ELA_UFO), NOT from the    *)
(*  paper's appendix, so this calculation validates the exported model             *)
(*  end-to-end.  The transcription is recorded vertex by vertex below.            *)
(*                                                                                *)
(*  Kinematics follow Fernandez-Ramirez Eqs. (1)-(3), where -- note -- q is the    *)
(*  PHOTON momentum and k is the PION momentum:                                    *)
(*        s = (p+q)^2 = (pp+k)^2,  u = (pp-q)^2 = (p-k)^2,  t = (k-q)^2           *)
(*                                                                                *)
(*  Constant width Gamma_0 here, i.e. NOT the energy-dependent Gamma(s,u) of       *)
(*  Eqs. (44)-(47), and no Davidson-Workman form factors.  Baseline only.          *)
(* ****************************************************************************** *)

$HistoryLength = 0;
$FeynCalcStartupMessages = False;
<< FeynCalc`
Print["[fc] FeynCalc ", $FeynCalcVersion, " loaded."];

SCRATCH = "/tmp/claude-1000/-home-isaacson-Documents-Projects-NeutrinoGenerator-AchillesModels-ChiralPT/b586773b-aaff-4198-8d38-80cf72faa02e/scratchpad";

(* ------------------------------------------------------------- kinematics ---- *)
(* p incoming N, q incoming photon, k outgoing pion, pp outgoing N; p+q = pp+k.   *)
FCClearScalarProducts[];
SP[p, p]   = MN^2;
SP[pp, pp] = MN^2;
SP[q, q]   = 0;
SP[k, k]   = mpi^2;
SP[p, q]   = (ss - MN^2)/2;
SP[pp, k]  = (ss - MN^2)/2;
SP[k, q]   = (mpi^2 - tt)/2;
SP[p, pp]  = MN^2 - tt/2;
SP[p, k]   = (MN^2 + mpi^2 - uu)/2;
SP[pp, q]  = (MN^2 - uu)/2;

(* ------------------------------------------------ Rarita-Schwinger propagator - *)
(* Eq. (43), numerator only; denominators attached later so the complex width      *)
(* survives the spin sums correctly.  vv must be a plain momentum symbol.          *)
Gnum[al_, be_, vv_] :=
  (GS[vv] + MD) . ( -MT[al, be]
                    + (1/3) GA[al] . GA[be]
                    + (2/(3 MD^2)) FV[vv, al] FV[vv, be]
                    - (1/(3 MD)) (FV[vv, al] GA[be] - GA[al] FV[vv, be]) );

(* ****************************************************************************** *)
(*  Vertices, transcribed from ELA_UFO.                                           *)
(*  UFO conventions: every leg momentum is INCOMING; P(mu,i) is leg i's momentum   *)
(*  with index mu; integer index labels refer to leg positions.                    *)
(*                                                                                *)
(*  Momentum assignments (sum of incoming momenta = 0):                            *)
(*    s-channel  V_52 : Delta leg = -(p+q),  p = p,   A = q                        *)
(*    s-channel  V_95 : p~ leg    = -pp,     Delta = +(p+q),  pi0 = -k             *)
(*    u-channel  V_101: Delta leg = -(p-k),  p = p,   pi0 = -k                     *)
(*    u-channel  V_42 : p~ leg    = -pp,     Delta = +(p-k),  A = q                *)
(*                                                                                *)
(*  Levi-Civita and vector slots are expanded by linearity by hand below, so no    *)
(*  compound or negative momentum ever reaches LC[] or FV[].                       *)
(* ****************************************************************************** *)

(* --- V_52: gamma p -> Delta.  nu = Delta index, mu = photon index. ------------ *)
(*   RFV2 = 2 eps^{nu mu}(pDelta, pGamma),  GC_53 = + ee g1D sqrt(3/2)/(2 MN(MD+MN)) *)
(*   RFV3 = [pGamma^nu pDelta^mu - (pDelta.pGamma) g^{nu mu}] gamma5                  *)
(*   GC_54 = - i ee g2D sqrt(3/2)/(MN(MD+MN))                                        *)
(*   pDelta = -(p+q):  eps^{nu mu}(-(p+q), q) = -eps^{nu mu}(p,q)                     *)
(*                     pDelta^mu = -(p^mu + q^mu);  pDelta.pGamma = -(p.q)            *)
cg1 = ee g1D Sqrt[3/2]/(2 MN (MD + MN));
cg2 = ee g2D Sqrt[3/2]/(MN (MD + MN));

VgNDs[nu_, mu_] :=
   cg1 * 2 * (-LC[nu, mu][p, q])
 - I cg2 * ( FV[q, nu] (-FV[p, mu] - FV[q, mu]) + SP[p, q] MT[nu, mu] ) GA[5];

(* --- V_95: Delta -> pi0 p.  nu = Delta index. -------------------------------- *)
(*   FRS2 = - eps^{nu a}(pPi, pDelta) gamma_a gamma5,  GC_29 = + i hD sqrt(2/3)/(fpi MD) *)
(*   pPi = -k, pDelta = +(p+q):  eps^{nu a}(-k, p+q) = -eps^{nu a}(k,p) - eps^{nu a}(k,q) *)
ch = hD Sqrt[2/3]/(fpi MD);

VpiNDs[nu_] :=
  I ch * ( -( -LC[nu, aa][k, p] - LC[nu, aa][k, q] ) GA[aa] . GA[5] );

(* --- V_101: p -> pi0 Delta.  nu = Delta index. ------------------------------- *)
(*   pPi = -k, pDelta = -(p-k):  eps^{nu a}(-k, -(p-k)) = eps^{nu a}(k,p)         *)
VpiNDu[nu_] :=
  I ch * ( -( LC[nu, aa][k, p] ) GA[aa] . GA[5] );

(* --- V_42: Delta gamma -> p.  nu = Delta index, mu = photon index. ----------- *)
(*   GC_52 = -0.5 ee g1D sqrt(3/2)/(MN(MD+MN)),  GC_55 = + i ee g2D sqrt(3/2)/(MN(MD+MN)) *)
(*   pDelta = +(p-k):  eps^{nu mu}(p-k, q) = eps^{nu mu}(p,q) - eps^{nu mu}(k,q)  *)
VgNDu[nu_, mu_] :=
   (-cg1) * 2 * ( LC[nu, mu][p, q] - LC[nu, mu][k, q] )
 + I cg2 * ( FV[q, nu] (FV[p, mu] - FV[k, mu])
             - (SP[p, q] - SP[k, q]) MT[nu, mu] ) GA[5];

(* ****************************************************************************** *)
(*  Gauge invariance.                                                             *)
(*  Both Delta photon vertices are built from field strengths, so each must        *)
(*  vanish identically under eps^mu -> q^mu -- no spinors or on-shell conditions   *)
(*  needed.  This is a sharp test of the UFO transcription.                        *)
(* ****************************************************************************** *)
Print["[fc] gauge-invariance check on the photon vertices ..."];
gS = Contract[ VgNDs[nu, muG] FV[q, muG] ] // DiracSimplify // Simplify;
gU = Contract[ VgNDu[nu, muG] FV[q, muG] ] // DiracSimplify // Simplify;
Print["[fc]   V_52 (s-channel) eps->q : ", gS];
Print["[fc]   V_42 (u-channel) eps->q : ", gU];

(* ****************************************************************************** *)
(*  Amplitude numerators.                                                          *)
(* ****************************************************************************** *)
Print["[fc] building amplitude numerators ..."];
AmpS[mu_] := AmpS[mu] = Contract[ VpiNDs[n1] . Gnum[n1, a1, vs] . VgNDs[a1, mu] ];
AmpU[mu_] := AmpU[mu] = Contract[ VgNDu[n1, mu] . Gnum[n1, a1, vu] . VpiNDu[a1] ];

(* vs = p+q and vu = p-k as plain symbols with fully consistent scalar products;   *)
(* every epsilon/metric contraction depends only on these, so this is exact.       *)
SP[vs, vs] = ss;
SP[vs, p]  = (ss + MN^2)/2;
SP[vs, q]  = (ss - MN^2)/2;
SP[vs, k]  = (MN^2 + mpi^2 - uu)/2 + (mpi^2 - tt)/2;
SP[vs, pp] = MN^2 - tt/2 + (MN^2 - uu)/2;
SP[vu, vu] = uu;
SP[vu, p]  = MN^2 - (MN^2 + mpi^2 - uu)/2;
SP[vu, q]  = (ss - MN^2)/2 - (mpi^2 - tt)/2;
SP[vu, k]  = (MN^2 + mpi^2 - uu)/2 - mpi^2;
SP[vu, pp] = MN^2 - tt/2 - (ss - MN^2)/2;

Print["[fc] numerators built. MaxMemoryUsed: ", N[MaxMemoryUsed[]/2^30], " GiB"];

(* ****************************************************************************** *)
(*  Squared amplitude.                                                            *)
(*                                                                                *)
(*  M^mu = AmpS^mu/Ds + AmpU^mu/Du, with Ds, Du kept symbolic and complex so the   *)
(*  width survives the spin sums.  Photon polarisations are summed with -g_{mu nu} *)
(*  which is legitimate here because gauge invariance was just verified.           *)
(* ****************************************************************************** *)

(* every model parameter is real; only Ds and Du carry an imaginary part *)
realSyms = {MN, MD, mpi, fpi, ee, g1D, g2D, hD, ss, tt, uu};
unconj   = Conjugate[x_] :> x /; MemberQ[realSyms, x];

Print["[fc] spin sums and traces ..."];

ampFull[mu_] := SpinorUBar[pp, MN] . (AmpS[mu]/Ds + AmpU[mu]/Du) . SpinorU[p, MN];

sq = ampFull[m1] ComplexConjugate[ampFull[m2]] /. unconj;
sq = FermionSpinSum[sq];
sq = sq /. DiracTrace -> Tr;
sq = Contract[ sq * (-MT[m1, m2]) ];
Msq = Simplify[ sq /. unconj ];

Print["[fc] |M|^2 built. MaxMemoryUsed: ", N[MaxMemoryUsed[]/2^30], " GiB"];
DumpSave[SCRATCH <> "/msq.mx", {Msq}];

(* ****************************************************************************** *)
(*  Numerics: gamma p -> pi0 p, constant width.                                   *)
(* ****************************************************************************** *)
MNv = 0.9389175; MDv = 1.209; GamV = 0.102;
mpiv = 0.1395673; fpiv = 0.0923;
hv = 0.764; g1vv = 6.061; g2vv = 2.414;
eev = Sqrt[4 Pi/137.035999];

(* CM kinematics at total energy W *)
qstar[W_] := (W^2 - MNv^2)/(2 W);                                        (* photon *)
kstar[W_] := Sqrt[(W^2 - (MNv + mpiv)^2) (W^2 - (MNv - mpiv)^2)]/(2 W);  (* pion   *)
Epi[W_]   := Sqrt[kstar[W]^2 + mpiv^2];
tOf[W_, th_] := mpiv^2 - 2 qstar[W] (Epi[W] - kstar[W] Cos[th]);
uOf[W_, th_] := 2 MNv^2 + mpiv^2 - W^2 - tOf[W, th];

(* s-channel Delta can go on shell -> keep the width.  In the u-channel the        *)
(* resonance is far below threshold, where the Theta functions of Eq. (46) switch  *)
(* Gamma off, so that propagator is taken real.                                    *)
subs[W_, th_] := {
  MN -> MNv, MD -> MDv, mpi -> mpiv, fpi -> fpiv, ee -> eev,
  g1D -> g1vv, g2D -> g2vv, hD -> hv,
  ss -> W^2, tt -> tOf[W, th], uu -> uOf[W, th],
  Ds -> W^2 - MDv^2 + I MDv GamV, Conjugate[Ds] -> W^2 - MDv^2 - I MDv GamV,
  Du -> uOf[W, th] - MDv^2,       Conjugate[Du] -> uOf[W, th] - MDv^2 };

(* spin/polarisation average is 1/4 (2 nucleon spins x 2 photon polarisations) *)
MsqAvg[W_, th_] := Re[ (1/4) (Msq /. subs[W, th]) ];

(* Eq. (5):  dsigma/dOmega = 1/(64 pi^2 s) (k*/E_gamma*) |M|^2,  E_gamma* = q*     *)
(* 0.3894 mb GeV^2 = 389.4 microbarn GeV^2 converts GeV^-2 -> microbarn            *)
dsdo[W_, th_] := 389.4 * MsqAvg[W, th] * kstar[W]/(64 Pi^2 W^2 qstar[W]);
sigTot[W_]    := 2 Pi NIntegrate[ dsdo[W, th] Sin[th], {th, 0, Pi} ];

Print["[fc] ---- gamma p -> pi0 p through Delta(1232), constant width ----"];
Print["[fc]  W(GeV)   Egamma_lab(MeV)   dsig/dOmega(90deg)[ub/sr]   sigma_tot[ub]"];
Do[
  With[{W = Wv},
    Print["[fc]  ", NumberForm[W, {5, 3}], "     ",
      NumberForm[1000 (W^2 - MNv^2)/(2 MNv), {6, 1}], "        ",
      NumberForm[dsdo[W, Pi/2], {6, 3}], "                  ",
      NumberForm[sigTot[W], {6, 2}]]],
  {Wv, {1.100, 1.150, 1.200, 1.232, 1.260, 1.300, 1.350, 1.400}}];

Print["[fc] MaxMemoryUsed: ", N[MaxMemoryUsed[]/2^30], " GiB"];
Print["[fc] done."];
Quit[];
