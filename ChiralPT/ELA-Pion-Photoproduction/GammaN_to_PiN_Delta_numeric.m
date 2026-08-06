(* ****************************************************************************** *)
(*  gamma p -> pi0 p through the Delta(1232), s- and u-channel, constant width.   *)
(*                                                                                *)
(*  Explicit numeric evaluation: 4x4 Dirac matrices, explicit spinors and          *)
(*  polarisation vectors, contracted point by point.  No FeynCalc.                 *)
(*                                                                                *)
(*  Vertices are transcribed from the generated UFO (ELA_UFO), identically to      *)
(*  GammaN_to_PiN_Delta.m, so this validates the exported model end-to-end and     *)
(*  doubles as an independent check on the symbolic FeynCalc route.                *)
(*                                                                                *)
(*  Conventions follow Fernandez-Ramirez: g = diag(1,-1,-1,-1), eps^{0123} = +1,   *)
(*  gamma5 = i g0 g1 g2 g3, and -- note -- q is the PHOTON and k is the PION.      *)
(* ****************************************************************************** *)

$HistoryLength = 0;

(* ----------------------------------------------------------------- constants - *)
MNv = 0.9389175; MDv = 1.209; GamV = 0.102;
mpiv = 0.1395673; fpiv = 0.0923;
hv = 0.764; g1v = 6.061; g2v = 2.414;
eev = Sqrt[4 Pi/137.035999];

cg1 = eev g1v Sqrt[3/2]/(2 MNv (MDv + MNv));
cg2 = eev g2v Sqrt[3/2]/(MNv (MDv + MNv));
ch  = hv Sqrt[2/3]/(fpiv MDv);

(* ------------------------------------------------------- Dirac algebra (4x4) - *)
gmet = DiagonalMatrix[{1, -1, -1, -1}];
sx = {{0, 1}, {1, 0}}; sy = {{0, -I}, {I, 0}}; sz = {{1, 0}, {0, -1}};
id2 = IdentityMatrix[2]; z2 = ConstantArray[0, {2, 2}];
ga0 = ArrayFlatten[{{id2, z2}, {z2, -id2}}];
gaS[si_] := ArrayFlatten[{{z2, si}, {-si, z2}}];
gam = {ga0, gaS[sx], gaS[sy], gaS[sz]};                  (* gamma^mu, mu=0..3    *)
ga5 = I gam[[1]] . gam[[2]] . gam[[3]] . gam[[4]];
id4 = IdentityMatrix[4];
gamLow = Table[Sum[gmet[[a, b]] gam[[b]], {b, 4}], {a, 4}];   (* gamma_a         *)

(* Levi-Civita with eps^{0123} = +1 (Mathematica is 1-indexed: eps_{1234}=+1)     *)
epsT = LeviCivitaTensor[4] // Normal;

low[v_] := gmet . v;                                     (* v_mu from v^mu       *)
dot[a_, b_] := a . gmet . b;                             (* a.b                  *)
slash[v_] := Sum[v[[m]] gamLow[[m]], {m, 4}];            (* v^mu gamma_mu        *)

(* eps^{nu mu alpha beta} a_alpha b_beta, free upper nu, mu *)
LCab[a_, b_] := Module[{la = low[a], lb = low[b]},
  Table[Sum[epsT[[nu, mu, al, be]] la[[al]] lb[[be]], {al, 4}, {be, 4}],
        {nu, 4}, {mu, 4}]];

(* eps^{nu a alpha beta} a_alpha b_beta gamma_a : free upper nu, Dirac matrix *)
LCabG[a_, b_] := Module[{t = LCab[a, b]},
  Table[Sum[t[[nu, aa]] gamLow[[aa]], {aa, 4}], {nu, 4}]];

(* ****************************************************************************** *)
(*  Vertices, transcribed from ELA_UFO (see GammaN_to_PiN_Delta.m for the          *)
(*  leg-by-leg reading of each UFO Lorentz structure and coupling).                *)
(*  Each returns an array over free Lorentz indices whose entries are 4x4 Dirac.   *)
(* ****************************************************************************** *)

(* V_52: gamma p -> Delta.  free nu (Delta), mu (photon) *)
VgNDs[p_, q_] := Module[{lc = LCab[p, q], pq = dot[p, q]},
  Table[ 2 cg1 (-lc[[nu, mu]]) id4
       - I cg2 ( q[[nu]] (-(p[[mu]] + q[[mu]])) + pq gmet[[nu, mu]] ) ga5,
    {nu, 4}, {mu, 4}]];

(* V_95: Delta -> pi0 p.  free nu (Delta) *)
VpiNDs[p_, q_, k_] := Module[{A = LCabG[k, p], B = LCabG[k, q]},
  Table[ I ch (A[[nu]] + B[[nu]]) . ga5, {nu, 4}]];

(* V_101: p -> pi0 Delta.  free nu (Delta) *)
VpiNDu[p_, k_] := Module[{A = LCabG[k, p]},
  Table[ -I ch A[[nu]] . ga5, {nu, 4}]];

(* V_42: Delta gamma -> p.  free nu (Delta), mu (photon) *)
VgNDu[p_, q_, k_] := Module[{l1 = LCab[p, q], l2 = LCab[k, q],
                             pq = dot[p, q], kq = dot[k, q]},
  Table[ -2 cg1 (l1[[nu, mu]] - l2[[nu, mu]]) id4
       + I cg2 ( q[[nu]] (p[[mu]] - k[[mu]]) - (pq - kq) gmet[[nu, mu]] ) ga5,
    {nu, 4}, {mu, 4}]];

(* --------------------------------------- Rarita-Schwinger numerator, Eq. (43) - *)
GnumRS[v_] := Module[{sl = slash[v] + MDv id4},
  Table[ sl . ( -gmet[[nu, et]] id4
                + (1/3) gam[[nu]] . gam[[et]]
                + (2/(3 MDv^2)) v[[nu]] v[[et]] id4
                - (1/(3 MDv)) (v[[nu]] gam[[et]] - gam[[nu]] v[[et]]) ),
    {nu, 4}, {et, 4}]];

(* contract  X^{nu ...} g_{nu nu'} Y^{nu' ...}  : metric is diagonal *)
mlow[T_] := Table[gmet[[i, i]] T[[i]], {i, 4}];

(* ------------------------------------------------------------------- spinors - *)
chi = {{1, 0}, {0, 1}};
uSp[pv_, m_, s_] := Module[{E0 = pv[[1]], pvec = pv[[2 ;; 4]], c = chi[[s]]},
  Sqrt[E0 + m] Join[c, (pvec . {sx, sy, sz} . c)/(E0 + m)]];
ubar[u_] := Conjugate[u] . ga0;

(* polarisation vectors, Eq. (4), photon along +z *)
polV = {-(1/Sqrt[2]) {0, 1, I, 0}, (1/Sqrt[2]) {0, 1, -I, 0}};

(* ****************************************************************************** *)
(*  Amplitude at one kinematic point                                              *)
(* ****************************************************************************** *)
amps[W_, th_] := Module[
  {qs, ks, Ep, Epi, EN, p, q, k, pp, vs, vu, Ds, Du,
   Vs1, Vs2, Vu1, Vu2, Gs, Gu, Ms, Mu, Mtot},
  qs = (W^2 - MNv^2)/(2 W);
  ks = Sqrt[(W^2 - (MNv + mpiv)^2) (W^2 - (MNv - mpiv)^2)]/(2 W);
  Ep = W - qs; Epi = Sqrt[ks^2 + mpiv^2]; EN = W - Epi;
  p  = {Ep, 0, 0, -qs};
  q  = {qs, 0, 0, qs};
  k  = {Epi, ks Sin[th], 0, ks Cos[th]};
  pp = {EN, -ks Sin[th], 0, -ks Cos[th]};
  vs = p + q; vu = p - k;

  (* s-channel Delta can go on shell -> keep the width.  In the u-channel the      *)
  (* resonance is far below threshold, where the Theta functions of Eq. (46)       *)
  (* switch Gamma off, so that propagator is real.                                 *)
  Ds = dot[vs, vs] - MDv^2 + I MDv GamV;
  Du = dot[vu, vu] - MDv^2;

  Vs1 = VpiNDs[p, q, k];  Vs2 = VgNDs[p, q];
  Vu1 = VgNDu[p, q, k];   Vu2 = VpiNDu[p, k];
  Gs  = GnumRS[vs];       Gu  = GnumRS[vu];

  (* M^mu = sum_{nu,et} V1_nu G^{nu et} V2_et , indices lowered with the metric *)
  Ms = Table[ Sum[ gmet[[nu, nu]] gmet[[et, et]] *
                   Vs1[[nu]] . Gs[[nu, et]] . Vs2[[et, mu]], {nu, 4}, {et, 4}],
              {mu, 4}];
  Mu = Table[ Sum[ gmet[[nu, nu]] gmet[[et, et]] *
                   Vu1[[nu, mu]] . Gu[[nu, et]] . Vu2[[et]], {nu, 4}, {et, 4}],
              {mu, 4}];
  Mtot = Table[ Ms[[mu]]/Ds + Mu[[mu]]/Du, {mu, 4}];

  {p, pp, Mtot}];

(* spin- and polarisation-averaged |M|^2 *)
Msq[W_, th_] := Module[{p, pp, Mtot, tot = 0., uIn, uOut, amp},
  {p, pp, Mtot} = amps[W, th];
  Do[
    uIn  = uSp[p, MNv, s1]; uOut = uSp[pp, MNv, s2];
    amp  = Sum[ gmet[[mu, mu]] polV[[lam]][[mu]] *
                (ubar[uOut] . Mtot[[mu]] . uIn), {mu, 4}];
    tot += Abs[amp]^2,
    {s1, 2}, {s2, 2}, {lam, 2}];
  tot/4];

(* Eq. (5): dsigma/dOmega = |M|^2 kcm / (64 pi^2 s Egam_cm); 389.4 ub GeV^2 *)
qstar[W_] := (W^2 - MNv^2)/(2 W);
kstar[W_] := Sqrt[(W^2 - (MNv + mpiv)^2) (W^2 - (MNv - mpiv)^2)]/(2 W);
dsdo[W_, th_] := 389.4 Msq[W, th] kstar[W]/(64 Pi^2 W^2 qstar[W]);
sigTot[W_] := 2 Pi NIntegrate[dsdo[W, th] Sin[th], {th, 0, Pi}, AccuracyGoal -> 6];

(* ****************************************************************************** *)
(*  Checks and output                                                             *)
(* ****************************************************************************** *)
Print["[num] gauge invariance: replace polarisation by q^mu, expect ~0"];
Module[{W = 1.232, th = Pi/2, p, pp, Mtot, qs, q, uIn, uOut, g},
  qs = (W^2 - MNv^2)/(2 W); q = {qs, 0, 0, qs};
  {p, pp, Mtot} = amps[W, th];
  uIn = uSp[p, MNv, 1]; uOut = uSp[pp, MNv, 1];
  g = Sum[gmet[[mu, mu]] q[[mu]] (ubar[uOut] . Mtot[[mu]] . uIn), {mu, 4}];
  Print["[num]   W=1.232, theta=90deg :  ", Chop[g, 10^-10]]];

Print["[num] ---- gamma p -> pi0 p through Delta(1232), constant width ----"];
Print["[num]   W[GeV]  Egam_lab[MeV]  dsig/dOm(90)[ub/sr]   sigma_tot[ub]"];
Do[With[{W = Wv},
   Print["[num]   ", NumberForm[N@W, {5, 3}], "      ",
     NumberForm[1000 (W^2 - MNv^2)/(2 MNv), {6, 1}], "        ",
     NumberForm[dsdo[W, Pi/2], {7, 3}], "            ",
     NumberForm[sigTot[W], {7, 2}]]],
  {Wv, {1.10, 1.15, 1.18, 1.21, 1.232, 1.25, 1.28, 1.32, 1.38, 1.44, 1.50}}];

Print["[num] MaxMemoryUsed: ", N[MaxMemoryUsed[]/2^30], " GiB"];
Print["[num] done."];
Quit[];
