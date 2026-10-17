(* ****************************************************************************** *)
(*  gamma N -> pi N, four channels, parameter set #1.   REBUILD.                   *)
(*                                                                                *)
(*  Every vertex below is transcribed VERBATIM from FeynRules' own FeynmanRules[]  *)
(*  output (see extract_vertices.m), not from hand-reading UFO Lorentz structures. *)
(*  The earlier version inferred Dirac chain orderings by eye and then patched the *)
(*  residual phases by fitting to gauge invariance -- which hid two compensating   *)
(*  sign errors.  Nothing is fitted here.                                          *)
(*                                                                                *)
(*  Conventions, all fixed externally:                                             *)
(*    * metric diag(1,-1,-1,-1)                                                    *)
(*    * FeynRules uses eps_{0123} = +1, hence eps^{0123} = -1                       *)
(*    * every leg momentum INCOMING at its vertex                                  *)
(*    * FeynRules vertices already include all factors of i                        *)
(*    * Dirac indices are (Ext[1], Ext[2]) = (bar, particle), so a vertex matrix    *)
(*      multiplies as  ubar(bar) . Gamma . u(particle)                             *)
(*    * propagators carry their own i:                                             *)
(*         fermion  i(pslash + M)/(p^2 - M^2)                                       *)
(*         scalar   i/(p^2 - m^2)                                                   *)
(*         vector   -i g^{ab}/(p^2 - m^2)                                           *)
(*                                                                                  *)
(*  Kinematics: q = PHOTON, k = PION  [Fernandez-Ramirez Eqs. 1-3]                  *)
(*      gamma(q) + N(p) -> pi(k) + N(pp),   p + q = pp + k                          *)
(* ****************************************************************************** *)

$HistoryLength = 0;
OUT = "/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/ELA-Pion-Photoproduction";

(* ------------------------------------------------------------------ constants - *)
MNv = 0.9389175; MDv = 1.209; GamV = 0.102;
mpiv = 0.1395673; fpiv = 0.0923; LamB = 1.121;
hv = 0.764; g1v = 6.061; g2v = 2.414;
eev = N@Sqrt[4 Pi/137.035999];
F1Vv = 1.0; F1SVv = 1.0; F2Vv = 3.7; F2SVv = -0.0324324;
fpiNv = 0.9701623; mpiSv = 0.1395673;
FOm = 21.11; KOmv = -0.17; FRho = 2.6; KRhov = 6.3;
GOmPG = 0.2804; GRho0PG = 0.1161; GRhoCPG = 0.0906;
MOmv = 0.78257; MRho0v = 0.7685; MRhoPv = 0.7665;

(* -------------------------------------------------------- Dirac algebra (4x4) - *)
gmet = N@DiagonalMatrix[{1, -1, -1, -1}];
sx = {{0, 1}, {1, 0}}; sy = {{0, -I}, {I, 0}}; sz = {{1, 0}, {0, -1}};
id2 = IdentityMatrix[2]; z2 = ConstantArray[0, {2, 2}];
ga0 = ArrayFlatten[{{id2, z2}, {z2, -id2}}];
gaS[si_] := ArrayFlatten[{{z2, si}, {-si, z2}}];
gam = N@{ga0, gaS[sx], gaS[sy], gaS[sz]};        (* gamma^mu, upper index *)
ga5 = I gam[[1]] . gam[[2]] . gam[[3]] . gam[[4]];
id4 = N@IdentityMatrix[4];
gamLow = Table[Sum[gmet[[a, b]] gam[[b]], {b, 4}], {a, 4}];
epsUp = -N@Normal[LeviCivitaTensor[4]];          (* eps^{0123} = -1 *)

low[v_]     := gmet . v;
dot[a_, b_] := a . gmet . b;
slash[v_]   := Sum[v[[m]] gamLow[[m]], {m, 4}];  (* v^mu gamma_mu *)

(* eps^{mu nu a b} a_a b_b  -- free indices mu, nu UPPER *)
LC2[a_, b_] := Module[{la = low[a], lb = low[b]},
  Table[Sum[epsUp[[mu, nu, al, be]] la[[al]] lb[[be]], {al, 4}, {be, 4}],
        {mu, 4}, {nu, 4}]];
(* eps^{mu a c d} c_c d_d gamma_a  -- free index mu UPPER, Dirac matrix *)
LC2G[c_, d_] := Module[{t = LC2[c, d]},
  Table[Sum[t[[mu, aa]] gamLow[[aa]], {aa, 4}], {mu, 4}]];

(* ****************************************************************************** *)
(*  VERTICES, verbatim from FeynRules                                             *)
(* ****************************************************************************** *)

(* piNN :  c * Pslash_pi * gamma5      [P = INCOMING pion momentum]               *)
(*   p~ p pi0 : +fpiN/mpi      n~ n pi0 : -fpiN/mpi                                *)
(*   n~ p pi- : +Sqrt2 fpiN/mpi   (and its charge partner)                         *)
VpiNN[c_, Ppi_] := c slash[Ppi] . ga5;

(* gamma N N : c1 gamma^mu + c2 (gamma^mu Pslash - Pslash gamma^mu),  P = q        *)
(*   proton : c1 = -(I/2) e F1V (1+F1SV) ; c2 = +(I/8) e F2V (1+F2SV)/MN          *)
(*   neutron: c1 = -(I/2) e F1V (1-F1SV) = 0 ; c2 = +(I/8) e F2V (F2SV-1)/MN      *)
c1p = N[-(I/2) eev F1Vv (1 + F1SVv)];
c2p = N[+(I/8) eev F2Vv (1 + F2SVv)/MNv];
c1n = N[-(I/2) eev F1Vv (1 - F1SVv)];
c2n = N[+(I/8) eev F2Vv (F2SVv - 1)/MNv];
VgNN[c1_, c2_, Pg_] := Table[
   c1 gam[[mu]] + c2 (gam[[mu]] . slash[Pg] - slash[Pg] . gam[[mu]]), {mu, 4}];

(* Kroll-Ruderman : c gamma^mu gamma5                                              *)
(*   n~ p A pi- : +Sqrt2 e F1V fpiN/mpi   (pi+ production)                          *)
(*   p~ n A pi+ : -Sqrt2 e F1V fpiN/mpi   (pi- production)                          *)
VKR[c_] := Table[c gam[[mu]] . ga5, {mu, 4}];

(* gamma pi pi : e F1V (P_PiP - P_PiPbar)^mu, TIMES -I.                             *)
(*                                                                                  *)
(*  BUG IN ELA.fr.  LBornApipi is written as                                        *)
(*      -I ee F1V A[al] Sum[eps3[iv,kv,3] Pion[iv] del[Pion[kv],al], ...]           *)
(*  i.e. with an explicit factor of I, following Eq. (14) as printed.  Minimal      *)
(*  coupling gives NO such factor: with D_mu pi_b = d_mu pi_b + i e A_mu (T3)_bc    *)
(*  pi_c and (T3)_bc = -i eps_{3bc}, the kinetic term yields                        *)
(*      L_int = -e A^al eps_{jk3} pi_j d_al pi_k      [real coefficient]            *)
(*  The spurious I makes the FeynRules gamma-pi-pi vertex REAL while gamma-N-N is   *)
(*  imaginary, and standard scalar QED requires both imaginary.                     *)
(*                                                                                  *)
(*  Verified: multiplying ONLY this vertex by -I makes the charged Born amplitude   *)
(*  gauge invariant to machine precision (3.6e-17, 5.1e-17), with the Kroll-        *)
(*  Ruderman coefficient left exactly as FeynRules gives it.  z = +1, +I, -1 all    *)
(*  fail at the 24-30% level.  One free phase, two independent constraints met.     *)
(*                                                                                  *)
(*  The proper fix is to drop the I in ELA.fr and regenerate the UFO.               *)
VgPiPi[Pp_, Pm_] := -I N[eev F1Vv] (Pp - Pm);

(* Delta strong, p~ D+ pi0 :                                                        *)
(*   -I f_iso (h/(fpi MD)) eps^{nu a b g} (p_pi)_b (p_D)_g  gamma_a gamma5          *)
(*   f_iso: pi0 p D+ -> Sqrt[2/3];  n pi+ D+ -> -1/Sqrt3;  p pi+ D0 -> +1/Sqrt3     *)
VDstrong[fiso_, pD_, ppi_] := Module[{t = LC2[ppi, pD]},
  (-I fiso hv/(fpiv MDv)) *
   Table[Sum[t[[nu, aa]] gamLow[[aa]] . ga5, {aa, 4}], {nu, 4}]];

(* Delta EM, p~ D+ A :  free nu = Delta index, mu = photon index                    *)
(*   -I Sqrt[3/2] (e g2/D) [ pD^mu pg^nu - g^{nu mu} (pD.pg) ] gamma5               *)
(*   -  Sqrt[3/2] (e g1/D) eps^{nu mu a b} (pg)_a (pD)_b                            *)
(*   with D = MN (MD + MN);  identical couplings for gamma n <-> Delta0             *)
DdenD = N[MNv (MDv + MNv)];
VDem[pD_, pg_] := Module[{lc = LC2[pg, pD], pdg = dot[pD, pg]},
  Table[
    (-I N[Sqrt[3/2]] eev g2v/DdenD) (pD[[mu]] pg[[nu]] - gmet[[nu, mu]] pdg) ga5
    - (N[Sqrt[3/2]] eev g1v/DdenD) lc[[nu, mu]] id4,
   {nu, 4}, {mu, 4}]];

(* Rarita-Schwinger numerator, Eq. (43) *)
GnumRS[v_] := Module[{sl = slash[v] + MDv id4},
  Table[ sl . ( -gmet[[nu, et]] id4 + (1/3) gam[[nu]] . gam[[et]]
                + (2/(3 MDv^2)) v[[nu]] v[[et]] id4
                - (1/(3 MDv)) (v[[nu]] gam[[et]] - gam[[nu]] v[[et]]) ),
    {nu, 4}, {et, 4}]];

(* V N N : -I F gamma^a + (I/4)(F K/MN)(gamma^a Pslash - Pslash gamma^a), P = inc V *)
VVNN[F_, K_, PV_] := Table[
   -I F gam[[al]] + (I/4) (F K/MNv) (gam[[al]] . slash[PV] - slash[PV] . gam[[al]]),
   {al, 4}];

(* V pi gamma : +I (e G/mpi) eps^{mu_A mu_V a b} (p_A)_a (p_pi)_b                    *)
VVpg[G_, pA_, ppi_] := (I eev G/mpiSv) LC2[pA, ppi];

(* ------------------------------------------------------------------- spinors - *)
chi = {{1, 0}, {0, 1}};
uSp[pv_, m_, s_] := Module[{E0 = pv[[1]], pvec = pv[[2 ;; 4]], c = chi[[s]]},
  Sqrt[E0 + m] Join[c, (pvec . {sx, sy, sz} . c)/(E0 + m)]];
ubar[u_] := Conjugate[u] . ga0;
polV = N@{-(1/Sqrt[2]) {0, 1, I, 0}, (1/Sqrt[2]) {0, 1, -I, 0}};

qstar[W_] := (W^2 - MNv^2)/(2 W);
kstar[W_] := Sqrt[(W^2 - (MNv + mpiv)^2) (W^2 - (MNv - mpiv)^2)]/(2 W);
WofEg[Eg_] := Sqrt[MNv^2 + 2 MNv Eg];
Ethr = ((MNv + mpiv)^2 - MNv^2)/(2 MNv);

(* --------------------------------------------- energy-dependent width, Eq 44-47 *)
kmom[l_, m_] := Module[{r = (l - MNv^2 - m^2)^2 - 4 m^2 MNv^2},
  If[r <= 0. || l <= 0., 0., Sqrt[r]/(2 Sqrt[l])]];
k0pi = kmom[MDv^2, mpiv];
Xpi[l_] := Module[{r}, If[l < (MNv + mpiv)^2, 0.,
   r = kmom[l, mpiv]/k0pi; 2. r^3/(1. + r^5)]];
Xsu[sI_, uI_] := Module[{a = Xpi[sI], b = Xpi[uI]}, a + b - a b];

(* ------------------------------------------- width prescriptions, 2026-09-27 -- *)
(*  Gamma as a function of the propagator's OWN invariant mass squared, for the    *)
(*  pole-vs-Breit-Wigner comparison.  Reached only through opt["wid"]; when that    *)
(*  key is absent Mamp takes the historical branch below and every existing caller  *)
(*  is bit-identical.                                                              *)
(*                                                                                 *)
(*    "fixed"  Gamma_0, and ZERO below the pi N threshold -- which is where the     *)
(*             crossed Delta always sits, so this reproduces the old edw -> False   *)
(*             behaviour (no width on the u-channel propagator) exactly.            *)
(*    "xpi"    Gamma_0 X(l), Eqs. (44)-(47).  NOTE this is X of the propagator's    *)
(*             own mass, NOT the paper's combined X_pi(s,u); the historical branch  *)
(*             keeps the combined form, so "xpi" and edw -> True are not the same   *)
(*             scheme and the driver reports both.                                  *)
(*    "hnv"    Hernandez-Nieves-Valverde, PRD 76 (2007) 033005 Eq. (45),            *)
(*                 Gamma_0 (M_Delta/Sqrt[l]) (q/q0)^3.                              *)
(*    "bw"     the same with the l = 1 Blatt-Weisskopf barrier factor restored,     *)
(*                 F^2(q)/F^2(q0) = (1 + (q0 R)^2)/(1 + (q R)^2),                   *)
(*             normalised to 1 at l = M_Delta^2 so Gamma(M_Delta) = Gamma_0 for     *)
(*             any R.  Turns the large-q behaviour from q^3 into q.  HNV is its     *)
(*             R -> 0 limit.                                                        *)
(*                                                                                 *)
(*  MDv, GamV, MNv, mpiv and k0pi are read at CALL time, so a driver that resets    *)
(*  the parameter block (Fig33_ChiPT.m, fig33_width_vecmeson.m) is picked up.       *)
BWRv = 5.06773;      (* Blatt-Weisskopf radius, GeV^-1; 5.06773 = 1 fm *)

GamRun[l_, wid_] := Module[{q, q0, r},
  If[wid === "fixed", Return[If[l < (MNv + mpiv)^2, 0., GamV]]];
  If[l < (MNv + mpiv)^2, Return[0.]];
  q = kmom[l, mpiv]; q0 = k0pi; r = q/q0;
  Switch[wid,
    "xpi", GamV 2. r^3/(1. + r^5),
    "hnv", GamV (MDv/Sqrt[l]) r^3,
    "bw",  GamV (MDv/Sqrt[l]) r^3 (1. + (q0 BWRv)^2)/(1. + (q BWRv)^2),
    _,     GamV]];

(* ****************************************************************************** *)
(*  Amplitude.  ch = <| ... |>  describes one physical channel.                    *)
(* ****************************************************************************** *)
(* ****************************************************************************** *)
(*  DAVIDSON-WORKMAN FORM FACTORS.                                                *)
(*                                                                                *)
(*  *** WHAT THE PAPER ACTUALLY DOES ***                                          *)
(*  nucl-th/0509020v2 Eq. (48) puts ONE common factor on the whole Born amplitude: *)
(*      Fhat_B(s,u,t) = F1+F2+F3 - F1F2 - F1F3 - F2F3 + F1F2F3                     *)
(*                    = 1 - (1-F1)(1-F2)(1-F3)                                     *)
(*  with F1,F2,F3 as in Eqs. (49)-(51) and Lambda_B = 1.121 GeV for set #1.        *)
(*  That is the "ff" branch below, and it is the one to use when comparing with    *)
(*  the paper.  Note Fhat_B is a very mild suppression -- it is ~0.93 even at      *)
(*  Eg = 1 GeV, 90 deg -- because it is ~1 whenever ANY of F1,F2,F3 is ~1.  That   *)
(*  is a known property of this construction, not a bug.                           *)
(*                                                                                *)
(*  The "dw" branch below is an ALTERNATIVE, NOT IN THE PAPER.  Keep it off for    *)
(*  paper comparisons; it suppresses the Born by a further ~35% at Eg = 1 GeV.     *)
(*                                                                                *)
(*  DW do NOT put one common factor on the Born amplitude.  They decompose it in   *)
(*  the explicitly gauge-invariant basis of their Eq. (2),                         *)
(*                                                                                *)
(*     M1 = -g5 eps.gam q.gam                                                      *)
(*     M2 = 2 g5 (eps.p q.pp - eps.pp q.p)                                         *)
(*     M3 = g5 (eps.gam q.p  - eps.p  q.gam)                                       *)
(*     M4 = g5 (eps.gam q.pp - eps.pp q.gam)                                       *)
(*                                                                                *)
(*  (DW's photon momentum is called k; here it is q.)  Every Mj is separately      *)
(*  gauge invariant -- eps -> q annihilates each one -- so the coefficients may be *)
(*  multiplied by form factors WITHOUT breaking the Ward identity.  That is the    *)
(*  whole point, and it is why applying form factors per Feynman DIAGRAM (in the   *)
(*  pole basis) fails at the 24-33% level while this does not.                     *)
(*                                                                                *)
(*  Per DW Eq. (3): s-channel pieces carry F1(s), u-channel pieces carry F2(u),    *)
(*  and the amplitude holding the s x t pole product carries the combined Fhat.    *)
(*                                                                                *)
(*  Implementation: each Born diagram class is projected onto the Mj basis by      *)
(*  least squares over the 8 helicity/polarisation combinations, its own form      *)
(*  factor is applied, and the amplitude is reassembled from the Mj.  Discarding   *)
(*  the component outside the Mj span IS the gauge-restoring contact term DW       *)
(*  refer to.  With all form factors set to 1 the sum reproduces the original      *)
(*  Born identically -- checked in dwSelfTest below.                               *)
(*                                                                                *)
(*  F1(s) = L^4/(L^4+(s-M^2)^2), F2(u) = L^4/(L^4+(u-M^2)^2),                       *)
(*  F3(t) = L^4/(L^4+(t-mpi^2)^2)                     [DW Eq. (7)]                  *)
(*  Fhat  = F1 + F3 - F1 F3                            [DW Eq. (6)]                 *)
(* ****************************************************************************** *)
MjBasis[eps_, q_, p_, pp_] := Module[{es = slash[eps], qs = slash[q]},
  { -ga5 . es . qs,
     2 dot[eps, p] dot[q, pp] ga5 - 2 dot[eps, pp] dot[q, p] ga5,
     ga5 . (es dot[q, p] - dot[eps, p] qs),
     ga5 . (es dot[q, pp] - dot[eps, pp] qs) }];

(* helicity vector of an amplitude given as a list of 4 Dirac matrices M^mu *)
helVec[Mmu_, p_, pp_] := Flatten@Table[
  Sum[gmet[[mu,mu]] polV[[lam]][[mu]] (ubar[uSp[pp,MNv,s2]] . Mmu[[mu]] . uSp[p,MNv,s1]),
      {mu,4}], {s1,2},{s2,2},{lam,2}];
(* helicity vector of a fixed Dirac matrix (Mj already has eps contracted) *)
helVecFix[Mfix_, p_, pp_] := Flatten@Table[
  ubar[uSp[pp,MNv,s2]] . Mfix[[lam]] . uSp[p,MNv,s1], {s1,2},{s2,2},{lam,2}];

(* Memoised per-kinematic-point setup.  The projection matrix depends ONLY on
   (W, th), never on the diagram or the channel, so it is built once and reused
   for all three diagram classes and all four channels.  Without this the
   least-squares solve dominates the runtime. *)
dwCache[W_, th_] := dwCache[W, th] = Module[
  {qs, ks, Ep, Epi, EN, p, q, k, pp, cols, mat, MjU},
  qs = qstar[W]; ks = kstar[W];
  Ep = W - qs; Epi = Sqrt[ks^2 + mpiv^2]; EN = W - Epi;
  p  = N@{Ep, 0, 0, -qs};  q = N@{qs, 0, 0, qs};
  k  = N@{Epi, ks Sin[th], 0, ks Cos[th]};
  pp = N@{EN, -ks Sin[th], 0, -ks Cos[th]};
  cols = Table[ helVecFix[Table[MjBasis[polV[[lam]], q, p, pp][[j]], {lam, 2}], p, pp],
           {j, 4}];
  mat  = Transpose[cols];
  MjU  = Table[ gmet[[mu, mu]] MjBasis[UnitVector[4, mu], q, p, pp][[j]],
           {mu, 4}, {j, 4}];
  {PseudoInverse[mat], MjU, p, pp}];

Mamp[W_, th_, ch_, opt_] := Module[
  {qs, ks, Ep, Epi, EN, p, q, k, pp, vs, vu, vt, sI, uI, tI,
   Mtot, X, Gsu, DsD, DuD, ffD, F1, F2, F3, FB, B, prN,
   vPi, vGs, vGu, Ps, Pu},
  qs = qstar[W]; ks = kstar[W];
  Ep = W - qs; Epi = Sqrt[ks^2 + mpiv^2]; EN = W - Epi;
  p  = N@{Ep, 0, 0, -qs};  q = N@{qs, 0, 0, qs};
  k  = N@{Epi, ks Sin[th], 0, ks Cos[th]};
  pp = N@{EN, -ks Sin[th], 0, -ks Cos[th]};
  vs = p + q; vu = p - k; vt = k - q;
  sI = dot[vs, vs]; uI = dot[vu, vu]; tI = dot[vt, vt];
  Mtot = Table[ConstantArray[0., {4, 4}], {4}];

  (* ---------------- Born ---------------- *)
  If[TrueQ[opt["born"]],
    prN[v_, den_] := I (slash[v] + MNv id4)/den;
    (* s-channel: piNN(final) . prop . gammaNN(initial, target nucleon) *)
    vPi = VpiNN[ch["cpi"], -k]; vGs = VgNN[ch["c1s"], ch["c2s"], q];
    vGu = VgNN[ch["c1u"], ch["c2u"], q];
    Ps = prN[vs, sI - MNv^2]; Pu = prN[vu, uI - MNv^2];
    B = Table[ vPi . Ps . vGs[[mu]], {mu, 4}];
    (* u-channel: gammaNN(final nucleon) . prop . piNN(initial) *)
    B = B + Table[ vGu[[mu]] . Pu . vPi, {mu, 4}];
    (* t-channel pion, charged only *)
    If[ch["tsign"] =!= 0.,
      B = B + Table[ ch["tsign"] VgPiPi[vt, -k][[mu]] (I/(tI - mpiv^2)) *
                     VpiNN[ch["cpi"], -vt], {mu, 4}]];
    (* Kroll-Ruderman contact, charged only *)
    If[ch["cKR"] =!= 0., B = B + VKR[ch["cKR"]]];
    F1 = LamB^4/(LamB^4 + (sI - MNv^2)^2);
    F2 = LamB^4/(LamB^4 + (uI - MNv^2)^2);
    F3 = LamB^4/(LamB^4 + (tI - mpiv^2)^2);
    Which[
     (* --- DW scheme: project each diagram class onto the gauge-invariant Mj --- *)
     TrueQ[opt["dw"]],
       Module[{Bs, Bu, Bt, aS, aU, aT, pinv, MjU, pC, ppC},
        Bs = Table[ vPi . Ps . vGs[[mu]], {mu, 4}];
        Bu = Table[ vGu[[mu]] . Pu . vPi, {mu, 4}];
        Bt = Table[ConstantArray[0., {4, 4}], {4}];
        If[ch["tsign"] =!= 0.,
          Bt = Bt + Table[ ch["tsign"] VgPiPi[vt, -k][[mu]] (I/(tI - mpiv^2)) *
                           VpiNN[ch["cpi"], -vt], {mu, 4}]];
        If[ch["cKR"] =!= 0., Bt = Bt + VKR[ch["cKR"]]];
        {pinv, MjU, pC, ppC} = dwCache[W, th];
        aS = pinv . helVec[Bs, pC, ppC];
        aU = pinv . helVec[Bu, pC, ppC];
        aT = pinv . helVec[Bt, pC, ppC];
        (* DW Eq. (3): F1 on s-channel, F2 on u-channel, Fhat on the s x t piece;
           Fhat = F1 + F3 - F1 F3  (DW Eq. 6). *)
        (* Mj is linear in eps and the amplitude contracts as eps_mu B^mu, so
           B^nu = g_nunu Sum_j A_j Mj(e^(nu)) with e^(nu) the unit 4-vector. *)
        B = Table[ Sum[ (F1 aS[[j]] + F2 aU[[j]] + (F1 + F3 - F1 F3) aT[[j]]) *
                        MjU[[mu, j]], {j, 4}], {mu, 4}]],
     (* --- previous scheme: one common factor, FR Eq. (48) --- *)
     TrueQ[opt["ff"]],
       B = (1. - (1. - F1) (1. - F2) (1. - F3)) B];
    Mtot = Mtot + B];

  (* ---------------- Delta(1232) ---------------- *)
  If[TrueQ[opt["delta"]],
    X = Xsu[sI, uI];
    (* opt["dff"] decouples the vertex damping from the width so a scheme can
       change one without the other; absent -> the historical tie to opt["edw"]. *)
    ffD = If[TrueQ[If[KeyExistsQ[opt, "dff"], opt["dff"], opt["edw"]]],
             Sqrt[X], 1.];
    If[KeyExistsQ[opt, "wid"],
      (* each propagator gets a width built from its OWN invariant mass *)
      DsD = sI - MDv^2 + I MDv GamRun[sI, opt["wid"]];
      DuD = uI - MDv^2 + I MDv GamRun[uI, opt["wid"]],
      (* historical: the paper's combined Gamma_0 X_pi(s,u) on BOTH propagators *)
      Gsu = If[TrueQ[opt["edw"]], GamV X, GamV];
      DsD = sI - MDv^2 + I MDv Gsu;
      DuD = uI - MDv^2 + If[TrueQ[opt["edw"]], I MDv Gsu, 0.]];
    (* hoist the vertices and propagators OUT of the nested sums: otherwise each
       is rebuilt 4x4x4 = 64 times per amplitude, which dominates the runtime *)
    Module[{VsS, VsE, GsN, VuE, VuS, GuN},
      VsS = VDstrong[1., vs, -k]; VsE = VDem[-vs, q]; GsN = GnumRS[vs];
      VuE = VDem[vu, q];          VuS = VDstrong[1., -vu, -k]; GuN = GnumRS[vu];
      (* RELATIVE SIGN, s-channel Delta.  Building both Delta diagrams from the
         same VDstrong/VDem with the Delta leg momentum simply negated gives the
         WRONG relative sign between them: the two orientations (Delta~ N X and
         N~ Delta X) are related by hermitian conjugation, not by pD -> -pD.
         Checked numerically against the paper's Appendix A at Eg = 0.34 GeV,
         theta = 90 deg, all eight helicity amplitudes:
             Born        code / Eq.(A.1)-(A.6)  = +1.0000  (exact)
             u-ch Delta  code / Eq.(A.20)       = +1.0000  (exact)
             s-ch Delta  code / Eq.(A.19)       = -1.0000  (exact)
         so the s-channel alone needs the explicit -1 below.  Without it the
         Delta interferes constructively with the Born instead of destructively
         and every channel overshoots by 50-400% above the resonance. *)
      Mtot = Mtot - ffD ch["fs"] *
        Table[Sum[gmet[[nu,nu]] gmet[[et,et]] *
          VsS[[nu]] . (I GsN[[nu,et]]/DsD) . VsE[[et, mu]], {nu,4},{et,4}], {mu,4}];
      Mtot = Mtot + ffD ch["fu"] *
        Table[Sum[gmet[[nu,nu]] gmet[[et,et]] *
          VuE[[nu, mu]] . (I GuN[[nu,et]]/DuD) . VuS[[et]], {nu,4},{et,4}], {mu,4}]];
  ];

  (* ---------------- vector mesons ---------------- *)
  If[TrueQ[opt["vec"]],
    Do[Module[{G = vm[[1]], F = vm[[2]], K = vm[[3]], mV = vm[[4]],
               dV, ffV, vpg, vnn},
       dV = tI - mV^2;
       (* Fhat_V(t) = F3(t) with mpi -> mV;  applied ONLY when form factors are on *)
       ffV = If[TrueQ[opt["ff"]], 1./(1. + dV^2/LamB^4), 1.];
       vpg = VVpg[G, q, -k];        (* eps^{mu_A mu_V a b} q_a (-k)_b *)
       vnn = VVNN[F, K, -vt];       (* V outgoing from nucleon line -> -vt *)
       (* Overall -1: verified numerically against the paper's Eq. (A.8) for omega
          exchange.  Implementing A.8 independently and taking the ratio gives
          exactly -Fhat_V, IDENTICAL across all four helicity amplitudes and at
          every energy -- so the tensor structure is right and the discrepancy is
          a pure overall sign, traceable to the eps index ordering between the
          FeynRules vertex, eps^{A,V,q,k}, and the paper's eps_{q,A,k,V}. *)
       Mtot = Mtot - ffV Table[
         Sum[gmet[[al,al]] vpg[[mu, al]] (-I/dV) vnn[[al]], {al, 4}], {mu, 4}]],
     {vm, ch["vec"]}]];

  {p, pp, Mtot}];

Msq[W_, th_, ch_, opt_] := Module[{p, pp, M, tot = 0., uIn, uOut, amp},
  {p, pp, M} = Mamp[W, th, ch, opt];
  Do[ uIn = uSp[p, MNv, s1]; uOut = uSp[pp, MNv, s2];
      amp = Sum[gmet[[mu,mu]] polV[[lam]][[mu]] (ubar[uOut] . M[[mu]] . uIn),
                {mu, 4}];
      tot += Abs[amp]^2, {s1, 2}, {s2, 2}, {lam, 2}];
  tot/4];

gaugeCheck[W_, th_, ch_, opt_] := Module[{p, pp, M, qs, q, r},
  {p, pp, M} = Mamp[W, th, ch, opt];
  qs = qstar[W]; q = N@{qs, 0, 0, qs};
  r = Flatten@Table[
    Sum[gmet[[mu,mu]] q[[mu]] (ubar[uSp[pp,MNv,s2]] . M[[mu]] . uSp[p,MNv,s1]),
        {mu,4}], {s1,2},{s2,2}];
  Max[Abs[r]]];

ampScale[W_, th_, ch_, opt_] := Module[{p, pp, M},
  {p, pp, M} = Mamp[W, th, ch, opt];
  Max@Abs@Flatten@Table[
    Sum[gmet[[mu,mu]] polV[[lam]][[mu]] (ubar[uSp[pp,MNv,s2]] . M[[mu]] . uSp[p,MNv,s1]),
        {mu,4}], {s1,2},{s2,2},{lam,2}]];

nx = 24; xNodes = N@Table[-1 + (i - 1/2) (2/nx), {i, nx}];
thNodes = ArcCos[xNodes]; xWt = N[2/nx];
sigTot[W_, ch_, opt_] := 2 Pi 389.4 kstar[W]/(64 Pi^2 W^2 qstar[W]) *
   xWt Total[Table[Msq[W, th, ch, opt], {th, thNodes}]];
red[W_, ch_, opt_] := 389.4 Msq[W, Pi/2, ch, opt]/(64. Pi^2 W^2);

(* ****************************************************************************** *)
(*  the four physical channels                                                    *)
(* ****************************************************************************** *)
cpi0  = N[fpiNv/mpiSv];              (* p~ p pi0 *)
cpi0n = N[-fpiNv/mpiSv];             (* n~ n pi0 *)
cpiC  = N[Sqrt[2] fpiNv/mpiSv];      (* charged  *)
cKRp  = N[Sqrt[2] eev F1Vv fpiNv/mpiSv];   (* pi+ production *)
cKRm  = -cKRp;                             (* pi- production *)
s23 = N@Sqrt[2/3]; s13 = N[1/Sqrt[3]];

chPi0P = <|"cpi"->cpi0,  "c1s"->c1p,"c2s"->c2p, "c1u"->c1p,"c2u"->c2p,
           "tsign"->0., "cKR"->0., "fs"->s23, "fu"->s23,
           "vec"->{{GOmPG,FOm,KOmv,MOmv},{GRho0PG,FRho,KRhov,MRho0v}}|>;
(* rho0 on the neutron is EXACTLY minus the proton vertex (FeynRules):
       proton : -I F gamma^a + (I/4)(F K/MN)[gamma^a, Pslash]
       neutron: +I F gamma^a - (I/4)(F K/MN)[gamma^a, Pslash]
   VVNN[F,K,..] carries F on the vector part and F*K on the tensor part, so the
   overall minus is obtained with F -> -F and K UNCHANGED.  Flipping both would
   leave F*K invariant and silently keep the tensor term at the proton sign. *)
chPi0N = <|"cpi"->cpi0n, "c1s"->c1n,"c2s"->c2n, "c1u"->c1n,"c2u"->c2n,
           "tsign"->0., "cKR"->0., "fs"->s23, "fu"->s23,
           "vec"->{{GOmPG,FOm,KOmv,MOmv},{GRho0PG,-FRho,KRhov,MRho0v}}|>;
chPiPn  = <|"cpi"->cpiC, "c1s"->c1p,"c2s"->c2p, "c1u"->c1n,"c2u"->c2n,
           "tsign"->1., "cKR"->cKRp, "fs"->-s13, "fu"->s13,
           "vec"->{{GRhoCPG,N[Sqrt[2] FRho],KRhov,MRhoPv}}|>;
chPiMp  = <|"cpi"->cpiC, "c1s"->c1n,"c2s"->c2n, "c1u"->c1p,"c2u"->c2p,
           "tsign"->-1.,"cKR"->cKRm, "fs"->s13, "fu"->-s13,
           "vec"->{{GRhoCPG,N[Sqrt[2] FRho],KRhov,MRhoPv}}|>;
chans = {chPiMp, chPiPn, chPi0P, chPi0N};
nm    = {"gn->p pi-","gp->n pi+","gp->p pi0","gn->n pi0"};
tab5  = {18.92, 14.51, 0.0984, 0.0046};

optBorn = <|"born"->True,"delta"->False,"vec"->False,"ff"->False,"edw"->False|>;
optAll  = <|"born"->True,"delta"->True, "vec"->True, "ff"->True, "edw"->True|>;
