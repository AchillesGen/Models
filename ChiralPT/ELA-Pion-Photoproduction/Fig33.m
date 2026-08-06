(* ****************************************************************************** *)
(*  Figure 33 of Fernandez-Ramirez et al. (nucl-th/0509020v2):                    *)
(*  total cross section vs lab photon energy, four channels, parameter set #1.    *)
(*                                                                                *)
(*  STAGES 1-2: Delta(1232) only.  Stage 1 = constant width, no form factors;    *)
(*  stage 2 adds the energy-dependent width Gamma(s,u) of Eqs. (44)-(47) and the  *)
(*  sqrt(X_pi(s,u)) resonance-pion-nucleon vertex form factor.                    *)
(*  This is the current numeric setup extended from gamma p -> pi0 p to all four  *)
(*  physical channels.  Later stages add the energy-dependent width Gamma(s,u),    *)
(*  the Davidson-Workman form factors, and the remaining contributions            *)
(*  (Born, rho/omega, and the other six resonances).                               *)
(*                                                                                *)
(*  All vertices and isospin factors are taken from the generated UFO (ELA_UFO).  *)
(*  Strong-vertex isospin factors, read off the UFO couplings:                    *)
(*                                                                                *)
(*     channel        s-channel      u-channel     UFO couplings                  *)
(*     gp -> pi0 p     sqrt(2/3)      sqrt(2/3)    GC_29                          *)
(*     gn -> pi0 n     sqrt(2/3)      sqrt(2/3)    GC_29                          *)
(*     gp -> pi+ n    -1/sqrt(3)     +1/sqrt(3)    GC_30, GC_31                   *)
(*     gn -> pi- p    +1/sqrt(3)     -1/sqrt(3)    GC_31, GC_30                   *)
(*                                                                                *)
(*  The electromagnetic couplings for gamma p <-> Delta+ and gamma n <-> Delta0    *)
(*  are identical in the UFO (GC_53/GC_54), as required for a pure isovector       *)
(*  I=3/2 transition.  The s/u sign flip in the charged channels reproduces the    *)
(*  paper's A+_s = -2 A-_s vs A+_u = +2 A-_u.                                      *)
(* ****************************************************************************** *)

$HistoryLength = 0;

OUT = "/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/ELA-Pion-Photoproduction";

(* ----------------------------------------------------------------- constants - *)
MNv = 0.9389175; MDv = 1.209; GamV = 0.102;
mpiv = 0.1395673; fpiv = 0.0923;
hv = 0.764; g1v = 6.061; g2v = 2.414;
eev = N@Sqrt[4 Pi/137.035999];

cg1 = N[eev g1v Sqrt[3/2]/(2 MNv (MDv + MNv))];
cg2 = N[eev g2v Sqrt[3/2]/(MNv (MDv + MNv))];

(* ------------------------------------------------------- Dirac algebra (4x4) - *)
gmet = N@DiagonalMatrix[{1, -1, -1, -1}];
sx = {{0, 1}, {1, 0}}; sy = {{0, -I}, {I, 0}}; sz = {{1, 0}, {0, -1}};
id2 = IdentityMatrix[2]; z2 = ConstantArray[0, {2, 2}];
ga0 = ArrayFlatten[{{id2, z2}, {z2, -id2}}];
gaS[si_] := ArrayFlatten[{{z2, si}, {-si, z2}}];
gam = N@{ga0, gaS[sx], gaS[sy], gaS[sz]};
ga5 = I gam[[1]] . gam[[2]] . gam[[3]] . gam[[4]];
id4 = N@IdentityMatrix[4];
gamLow = Table[Sum[gmet[[a, b]] gam[[b]], {b, 4}], {a, 4}];
(* FeynRules convention is eps_{0123} = +1, so eps^{0123} = -1 (det g = -1).
   LCab contracts epsT with LOWERED momenta, i.e. epsT carries the UPPER-index
   components, so it must be MINUS the Mathematica tensor.                     *)
epsT = -N@Normal[LeviCivitaTensor[4]];       (* eps^{0123} = -1 *)

low[v_] := gmet . v;
dot[a_, b_] := a . gmet . b;
slash[v_] := Sum[v[[m]] gamLow[[m]], {m, 4}];

LCab[a_, b_] := Module[{la = low[a], lb = low[b]},
  Table[Sum[epsT[[nu, mu, al, be]] la[[al]] lb[[be]], {al, 4}, {be, 4}],
        {nu, 4}, {mu, 4}]];
LCabG[a_, b_] := Module[{t = LCab[a, b]},
  Table[Sum[t[[nu, aa]] gamLow[[aa]], {aa, 4}], {nu, 4}]];

(* ------------------------------------------------------------------ vertices - *)
(* photon vertices: identical for Delta+ and Delta0 *)
VgNDs[p_, q_] := Module[{lc = LCab[p, q], pq = dot[p, q]},
  Table[ 2 cg1 (-lc[[nu, mu]]) id4
       - I cg2 ( q[[nu]] (-(p[[mu]] + q[[mu]])) + pq gmet[[nu, mu]] ) ga5,
    {nu, 4}, {mu, 4}]];
VgNDu[p_, q_, k_] := Module[{l1 = LCab[p, q], l2 = LCab[k, q],
                             pq = dot[p, q], kq = dot[k, q]},
  Table[ -2 cg1 (l1[[nu, mu]] - l2[[nu, mu]]) id4
       + I cg2 ( q[[nu]] (p[[mu]] - k[[mu]]) - (pq - kq) gmet[[nu, mu]] ) ga5,
    {nu, 4}, {mu, 4}]];

(* strong vertices: isospin factor fs (s-channel) / fu (u-channel) *)
VpiNDs[p_, q_, k_, fs_] := Module[{A = LCabG[k, p], B = LCabG[k, q],
                                   c = hv fs/(fpiv MDv)},
  Table[ I c (A[[nu]] + B[[nu]]) . ga5, {nu, 4}]];
VpiNDu[p_, k_, fu_] := Module[{A = LCabG[k, p], c = hv fu/(fpiv MDv)},
  Table[ -I c A[[nu]] . ga5, {nu, 4}]];

GnumRS[v_] := Module[{sl = slash[v] + MDv id4},
  Table[ sl . ( -gmet[[nu, et]] id4
                + (1/3) gam[[nu]] . gam[[et]]
                + (2/(3 MDv^2)) v[[nu]] v[[et]] id4
                - (1/(3 MDv)) (v[[nu]] gam[[et]] - gam[[nu]] v[[et]]) ),
    {nu, 4}, {et, 4}]];

(* ------------------------------------------------------------------- spinors - *)
chi = {{1, 0}, {0, 1}};
uSp[pv_, m_, s_] := Module[{E0 = pv[[1]], pvec = pv[[2 ;; 4]], c = chi[[s]]},
  Sqrt[E0 + m] Join[c, (pvec . {sx, sy, sz} . c)/(E0 + m)]];
ubar[u_] := Conjugate[u] . ga0;
polV = N@{-(1/Sqrt[2]) {0, 1, I, 0}, (1/Sqrt[2]) {0, 1, -I, 0}};

(* ****************************************************************************** *)
(*  amplitude / cross section, parametrised by the isospin factors                *)
(* ****************************************************************************** *)
qstar[W_] := (W^2 - MNv^2)/(2 W);
kstar[W_] := Sqrt[(W^2 - (MNv + mpiv)^2) (W^2 - (MNv - mpiv)^2)]/(2 W);

(* The amplitude is LINEAR in the isospin factors: Ms carries fs, Mu carries fu.  *)
(* So build both with unit coupling once per kinematic point, then every channel  *)
(* is a cheap linear combination -- four channels for the price of one.           *)
(* kern returns bare NUMERATORS plus the invariants; the stage-dependent          *)
(* denominators and vertex form factor are applied afterwards in Msq.             *)
kern[W_, th_] := kern[W, th] = Module[
  {qs, ks, Ep, Epi, EN, p, q, k, pp, vs, vu, Gs, Gu,
   V1s, V2s, V1u, V2u, Ms, Mu},
  qs = qstar[W]; ks = kstar[W];
  Ep = W - qs; Epi = Sqrt[ks^2 + mpiv^2]; EN = W - Epi;
  p  = N@{Ep, 0, 0, -qs};
  q  = N@{qs, 0, 0, qs};
  k  = N@{Epi, ks Sin[th], 0, ks Cos[th]};
  pp = N@{EN, -ks Sin[th], 0, -ks Cos[th]};
  vs = p + q; vu = p - k;
  Gs = GnumRS[vs]; Gu = GnumRS[vu];
  (* vertices built ONCE per point, with unit isospin factor *)
  V1s = VpiNDs[p, q, k, 1.]; V2s = VgNDs[p, q];
  V1u = VgNDu[p, q, k];      V2u = VpiNDu[p, k, 1.];
  Ms = Table[Sum[gmet[[nu, nu]] gmet[[et, et]] *
      V1s[[nu]] . Gs[[nu, et]] . V2s[[et, mu]], {nu, 4}, {et, 4}], {mu, 4}];
  Mu = Table[Sum[gmet[[nu, nu]] gmet[[et, et]] *
      V1u[[nu, mu]] . Gu[[nu, et]] . V2u[[et]], {nu, 4}, {et, 4}], {mu, 4}];
  {p, pp, Ms, Mu, dot[vs, vs], dot[vu, vu]}];

(* ****************************************************************************** *)
(*  BORN TERMS, Eq. (14) / amplitudes A.1-A.6, vertices taken from ELA_UFO.       *)
(*                                                                                *)
(*  UFO Lorentz structures:                                                       *)
(*    FFS2  (piNN)   = pslash_pi gamma5          coupling GC_63/64/65             *)
(*    FFV1  (gNN)    = gamma^mu                  coupling GC_2 (p), GC_3 (n)      *)
(*    FFV2  (gNN)    = [gamma^mu, qslash]        coupling GC_32 (p), GC_33 (n)    *)
(*    VSS1  (g pi pi)= (p_{pi-} - p_{pi+})^mu    coupling GC_1                    *)
(*    FFVS1 (KR)     = gamma^mu gamma5           coupling GC_66/67                *)
(*                                                                                *)
(*  Every UFO leg momentum is INCOMING, so an outgoing pion of momentum k enters  *)
(*  its vertex as -k.                                                             *)
(*                                                                                *)
(*  There is no gamma-pi0-pi0 vertex and no neutral Kroll-Ruderman vertex, so      *)
(*  pi0 production gets Born from the nucleon poles alone, while charged pion      *)
(*  production also picks up the t-channel pion and the KR contact term.  That is  *)
(*  precisely why the charged channels were undershooting.                         *)
(* ****************************************************************************** *)
F1Vv = 1.0; F1SVv = 1.0; F2Vv = 3.7; F2SVv = -0.0324324;
fpiNv = 0.9701623; mpiSv = 0.1395673;
LamB = 1.121;    (* Lambda, set #1, Table 2; Lambda_B = Lambda_V = Lambda *)

(* --- vector mesons, Eqs. (15)-(16); all values match Table 2 / sec 4.1.1 ------ *)
FOm = 21.11; KOmv = -0.17; FRho = 2.6; KRhov = 6.3;
GOmPG = 0.2804; GRho0PG = 0.1161; GRhoCPG = 0.0906;
MOmv = 0.78257; MRho0v = 0.7685; MRhoPv = 0.7665;
GC4  = N[-(FOm I)];                         GC46 = N[-0.25 (FOm I KOmv)/MNv];
GC5  = N[-(FRho I)];                        GC47 = N[-0.25 (FRho I KRhov)/MNv];
GC6  = N[FRho I];                           GC48 = N[(FRho I KRhov)/(4 MNv)];
GC7  = N[-(FRho I Sqrt[2])];                GC49 = N[-0.5 (FRho I KRhov)/(MNv Sqrt[2])];
GC68 = N[(eev I GOmPG)/mpiSv];
GC69 = N[(eev I GRho0PG)/mpiSv];
GC70 = N[(eev I GRhoCPG)/mpiSv];
phV  = -I;   (* see PHASE CAVEAT above; the flipped choice is computed too *)

GC1  = N[-(eev F1Vv)];                                        (* g pi+ pi-       *)
GC2  = N[-0.5 (eev F1Vv I) - (eev F1SVv F1Vv I)/2];            (* g p p, Dirac    *)
GC32 = -N[-0.125 (eev F2Vv I)/MNv - (eev F2SVv F2Vv I)/(8 MNv)];(* g p p, Pauli; sign from FFV2 = -[ga^mu,qslash] *)
GC3  = N[(eev F1Vv I)/2 - (eev F1SVv F1Vv I)/2];               (* g n n, Dirac =0 *)
GC33 = -N[(eev F2Vv I)/(8 MNv) - (eev F2SVv F2Vv I)/(8 MNv)];  (* g n n, Pauli; same sign fix *)
GC63 = N[-(fpiNv/mpiSv)];                                      (* p p pi0         *)
GC64 = N[fpiNv/mpiSv];                                         (* n n pi0         *)
GC65 = N[-(fpiNv Sqrt[2]/mpiSv)];                              (* p n pi+/n p pi- *)
GC66 = N[-(eev F1Vv fpiNv Sqrt[2]/mpiSv)];                     (* KR, pi+ prod    *)
GC67 = N[eev F1Vv fpiNv Sqrt[2]/mpiSv];                        (* KR, pi- prod    *)

(* six Born structure blocks, built once per kinematic point *)
bornKern[W_, th_] := bornKern[W, th] = Module[
  {qs, ks, Ep, Epi, EN, p, q, k, pp, vs, vu, vt, dS, dU, dT,
   kg5, Ps, Pu, S1, S2, U1, U2, T, KR},
  qs = qstar[W]; ks = kstar[W];
  Ep = W - qs; Epi = Sqrt[ks^2 + mpiv^2]; EN = W - Epi;
  p  = N@{Ep, 0, 0, -qs};       q  = N@{qs, 0, 0, qs};
  k  = N@{Epi, ks Sin[th], 0, ks Cos[th]};
  pp = N@{EN, -ks Sin[th], 0, -ks Cos[th]};
  vs = p + q; vu = p - k; vt = k - q;
  dS = dot[vs, vs] - MNv^2;  dU = dot[vu, vu] - MNv^2;
  dT = dot[vt, vt] - mpiv^2;
  kg5 = (-slash[k]) . ga5;                    (* piNN vertex: outgoing pion -> -k *)
  Ps = slash[vs] + MNv id4;  Pu = slash[vu] + MNv id4;
  S1 = Table[kg5 . Ps . gam[[mu]]/dS, {mu, 4}];
  S2 = Table[kg5 . Ps . (gam[[mu]] . slash[q] - slash[q] . gam[[mu]])/dS, {mu, 4}];
  U1 = Table[gam[[mu]] . Pu . kg5/dU, {mu, 4}];
  U2 = Table[(gam[[mu]] . slash[q] - slash[q] . gam[[mu]]) . Pu . kg5/dU, {mu, 4}];
  (* The relative phase of the t-channel and contact terms w.r.t. the nucleon     *)
  (* poles depends on how many momenta sit inside each UFO Lorentz structure       *)
  (* (each carries an implicit factor of i) and on the propagator convention.      *)
  (* Rather than guess, both factors were FIXED by demanding gauge invariance:     *)
  (* the violation is linear in them, and a least-squares solve over 4 kinematic   *)
  (* points x 4 spin combinations returns exactly -I for both, with residual       *)
  (* 1.8e-15 against a violation of scale 2.45.  Heavily overdetermined, so the    *)
  (* result is a genuine convention fix, not a fitted fudge factor.                *)
  T  = Table[-I (2 k[[mu]] - q[[mu]]) ((-slash[vt]) . ga5)/dT, {mu, 4}];
  KR = Table[-I gam[[mu]] . ga5, {mu, 4}];
  (* Davidson-Workman form factor, Eqs. (48)-(51).  Eq. (48) is equivalent to     *)
  (*     Fhat_B = 1 - (1-F1(s))(1-F2(u))(1-F3(t))                                 *)
  (* so Fhat_B -> 1 whenever any single F -> 1, i.e. residues at each pole are     *)
  (* untouched.  It is ONE common factor on all four Born diagrams, which is why   *)
  (* it preserves gauge invariance -- gauge invariance is a property of the sum.   *)
  (* Note dS, dU, dT are already exactly (s-M^2), (u-M^2), (t-mpi^2).             *)
  (* also return F1(s), F2(u), F3(t) separately, for the per-diagram variant *)
  {S1, S2, U1, U2, T, KR,
   1. - (1. - 1./(1. + dS^2/LamB^4)) (1. - 1./(1. + dU^2/LamB^4)) *
        (1. - 1./(1. + dT^2/LamB^4)),
   1./(1. + dS^2/LamB^4), 1./(1. + dU^2/LamB^4), 1./(1. + dT^2/LamB^4)}];

(* ****************************************************************************** *)
(*  VECTOR MESON EXCHANGE, Eqs. (15)-(16) / amplitudes A.7-A.8.                   *)
(*                                                                                *)
(*  UFO structures:  VNN = FFV1 (gamma^alpha) + FFV2 ([gamma^alpha, Pslash_V])     *)
(*                   V pi gamma = VVS1 = Epsilon(1,2,-1,-2) P(-1,1) P(-2,3)       *)
(*                                     = eps^{mu nu a b} q_a (-k)_b               *)
(*                                                                                *)
(*  The exchanged V carries vt = k - q, so at the VNN vertex its incoming          *)
(*  momentum is -vt.                                                               *)
(*                                                                                *)
(*  Because the V-pi-gamma vertex comes from Ftilde_{mu nu}, contracting the V      *)
(*  index with vt^nu gives zero, so the vt^a vt^b / m_V^2 piece of the massive      *)
(*  vector propagator drops identically and g^{ab} is exact -- consistent with     *)
(*  the paper writing g^{alpha mu} in Eq. (A.7).                                    *)
(*                                                                                *)
(*  Form factor Fhat_V(t) = F3(t) with m_pi -> m_V and Lambda_V = Lambda (sec 3.6).*)
(*                                                                                *)
(*  PHASE CAVEAT: each V diagram is separately gauge invariant (eps -> q kills the *)
(*  Ftilde vertex identically), so the gauge condition that fixed the Born t and   *)
(*  KR phases says nothing here.  phV below is therefore NOT independently         *)
(*  verified; both choices are computed and compared.                              *)
(* ****************************************************************************** *)
kin[W_, th_] := kin[W, th] = Module[{qs, ks, Ep, Epi, EN, p, q, k, pp},
  qs = qstar[W]; ks = kstar[W];
  Ep = W - qs; Epi = Sqrt[ks^2 + mpiv^2]; EN = W - Epi;
  p  = N@{Ep, 0, 0, -qs};  q = N@{qs, 0, 0, qs};
  k  = N@{Epi, ks Sin[th], 0, ks Cos[th]};
  pp = N@{EN, -ks Sin[th], 0, -ks Cos[th]};
  {p, q, k, pp, k - q}];

(* vm = {cgpv, c1, c2, mV} *)
vecAmp[W_, th_, vm_, ph_] := Module[
  {p, q, k, pp, vt, tI, lc, Vn, dV, ffV},
  {p, q, k, pp, vt} = kin[W, th];
  tI = dot[vt, vt];
  dV = tI - vm[[4]]^2;
  ffV = 1./(1. + dV^2/LamB^4);
  lc = LCab[q, k];                       (* eps^{mu nu a b} q_a k_b *)
  Vn = Table[ vm[[2]] gam[[al]]
            - vm[[3]] (gam[[al]] . slash[vt] - slash[vt] . gam[[al]]), {al, 4}];
  ph ffV vm[[1]]/dV *
    Table[Sum[gmet[[nu, nu]] (-lc[[mu, nu]]) Vn[[nu]], {nu, 4}], {mu, 4}]];

(* ------------------------------------------- energy-dependent width, Eqs 44-47 *)
(* Delta(1232): Table 1 gives Gamma_pi/Gamma = 1.00, Gamma_pipi/Gamma = 0.00, so  *)
(* only the pi channel contributes.  P33 is a P wave -> L = 1 -> exponents 3, 5.  *)
kmom[l_, m_] := Module[{r = (l - MNv^2 - m^2)^2 - 4 m^2 MNv^2},
  If[r <= 0. || l <= 0., 0., Sqrt[r]/(2 Sqrt[l])]];
k0pi = kmom[MDv^2, mpiv];
Xpi[l_] := Module[{r},
  If[l < (MNv + mpiv)^2, 0.,                       (* Theta function, Eq. (46) *)
     r = kmom[l, mpiv]/k0pi;
     2. r^3/(1. + r^5)]];
(* crossing-symmetric combination, Eq. (45) *)
Xsu[sI_, uI_] := Module[{a = Xpi[sI], b = Xpi[uI]}, a + b - a b];

(* Full amplitude M^mu for one channel.                                           *)
(*   stage 1 : Delta only, constant width                                          *)
(*   stage 2 : Delta with Gamma(s,u) + sqrt(X_pi)                                  *)
(*   stage 3 : stage 2 + Born terms                                                *)
(* ch = {label, fs, fu, ymax, cgS1, cgS2, cgU1, cgU2, cpi, tsign, cKR}             *)
Mamp[W_, th_, ch_, stage_] := Module[
  {p, pp, Ms, Mu, sI, uI, X, Gsu, Ds, Du, ff, M, B, blk},
  {p, pp, Ms, Mu, sI, uI} = kern[W, th];
  If[stage === 1,
    Ds = sI - MDv^2 + I MDv GamV;  Du = uI - MDv^2;  ff = 1.,
    X = Xsu[sI, uI]; Gsu = GamV X;
    Ds = sI - MDv^2 + I MDv Gsu;   Du = uI - MDv^2 + I MDv Gsu;  ff = Sqrt[X]];
  M = ff (ch[[2]] Ms/Ds + ch[[3]] Mu/Du);
  If[stage >= 3,
    blk = bornKern[W, th];
    B = ch[[9]] ch[[5]] blk[[1]] + ch[[9]] ch[[6]] blk[[2]]
      + ch[[9]] ch[[7]] blk[[3]] + ch[[9]] ch[[8]] blk[[4]]
      + ch[[10]] GC1 ch[[9]] blk[[5]] + ch[[11]] blk[[6]];
    (* stage 4: one common Davidson-Workman factor on the whole Born amplitude *)
    If[stage >= 4 && stage =!= 7, B = blk[[7]] B];
    (* stage 7: PER-DIAGRAM form factors -- s-channel x F1(s), u-channel x F2(u), *)
    (* t-channel x F3(t), contact x Fhat_B(s,u,t).  This is the alternative       *)
    (* reading of the Davidson-Workman prescription.                              *)
    If[stage === 7,
      B = blk[[8]] (ch[[9]] ch[[5]] blk[[1]] + ch[[9]] ch[[6]] blk[[2]])
        + blk[[9]] (ch[[9]] ch[[7]] blk[[3]] + ch[[9]] ch[[8]] blk[[4]])
        + blk[[10]] (ch[[10]] GC1 ch[[9]] blk[[5]])
        + blk[[7]]  (ch[[11]] blk[[6]])];
    M = M + B];
  If[stage >= 5,
    M = M + Total[vecAmp[W, th, #, If[stage === 6, -phV, phV]] & /@ ch[[12]]]];
  {p, pp, M}];

Msq[W_, th_, ch_, stage_] := Module[{p, pp, M, tot = 0., uIn, uOut, amp},
  {p, pp, M} = Mamp[W, th, ch, stage];
  Do[ uIn = uSp[p, MNv, s1]; uOut = uSp[pp, MNv, s2];
      amp = Sum[gmet[[mu, mu]] polV[[lam]][[mu]] (ubar[uOut] . M[[mu]] . uIn),
                {mu, 4}];
      tot += Abs[amp]^2, {s1, 2}, {s2, 2}, {lam, 2}];
  tot/4];

(* gauge invariance: eps^mu -> q^mu must annihilate the FULL amplitude.  The Born *)
(* diagrams are NOT individually gauge invariant -- only s+u+t+KR together are -- *)
(* so this is a genuine test of all the relative signs and momentum routings.     *)
gaugeCheck[W_, th_, ch_, stage_] := Module[{p, pp, M, qs, q, uIn, uOut, r},
  {p, pp, M} = Mamp[W, th, ch, stage];
  qs = qstar[W]; q = N@{qs, 0, 0, qs};
  r = Table[uIn = uSp[p, MNv, s1]; uOut = uSp[pp, MNv, s2];
      Sum[gmet[[mu, mu]] q[[mu]] (ubar[uOut] . M[[mu]] . uIn), {mu, 4}],
      {s1, 2}, {s2, 2}];
  Max[Abs[Flatten[r]]]];

dsdo[W_, th_, ch_, stage_] :=
  389.4 Msq[W, th, ch, stage] kstar[W]/(64 Pi^2 W^2 qstar[W]);

(* Uniform midpoint rule in x = cos(theta).  The integrand is smooth, and a fixed *)
(* node set lets all four channels reuse the cached kernel at identical angles.   *)
(*   sigma_tot = 2 pi Int_{-1}^{1} (dsigma/dOmega) dx                             *)
nx = 40;
xNodes = N@Table[-1 + (i - 1/2) (2/nx), {i, nx}];
xWt = N[2/nx];
thNodes = ArcCos[xNodes];
sigTot[W_, ch_, stage_] :=
  2 Pi * 389.4 * kstar[W]/(64 Pi^2 W^2 qstar[W]) *
    xWt * Total[Table[Msq[W, th, ch, stage], {th, thNodes}]];

(* lab photon energy <-> cm energy *)
WofEg[Eg_] := Sqrt[MNv^2 + 2 MNv Eg];
Ethr = ((MNv + mpiv)^2 - MNv^2)/(2 MNv);     (* pion production threshold *)

(* ****************************************************************************** *)
(*  four channels                                                                 *)
(* ****************************************************************************** *)
s23 = N@Sqrt[2/3]; s13 = N[1/Sqrt[3]];
(* {label, fs, fu, ymax, cgS1, cgS2, cgU1, cgU2, cpi, tsign, cKR}                 *)
(* s-channel photon vertex uses the TARGET nucleon couplings, u-channel uses the  *)
(* FINAL nucleon couplings.                                                        *)
channels = {
  (* gamma n -> pi- p : target n, final p, t-channel pi-, KR = GC_67 *)
  {"\!\(\*SuperscriptBox[\(\[Pi]\), \(-\)]\)p",  s13, -s13, 350,
     GC3, GC33, GC2, GC32, GC65, +1., GC67,
     {{GC70, GC7, GC49, MRhoPv}}},
  (* gamma p -> pi+ n : target p, final n, t-channel pi+, KR = GC_66 *)
  {"\!\(\*SuperscriptBox[\(\[Pi]\), \(+\)]\)n", -s13,  s13, 300,
     GC2, GC32, GC3, GC33, GC65, -1., GC66,
     {{GC70, GC7, GC49, MRhoPv}}},
  (* gamma p -> pi0 p : no t-channel, no KR *)
  {"\!\(\*SuperscriptBox[\(\[Pi]\), \(0\)]\)p",  s23,  s23, 400,
     GC2, GC32, GC2, GC32, GC63, 0., 0.,
     {{GC68, GC4, GC46, MOmv}, {GC69, GC5, GC47, MRho0v}}},
  (* gamma n -> pi0 n : no t-channel, no KR *)
  {"\!\(\*SuperscriptBox[\(\[Pi]\), \(0\)]\)n",  s23,  s23, 400,
     GC3, GC33, GC3, GC33, GC64, 0., 0.,
     {{GC68, GC4, GC46, MOmv}, {GC69, GC6, GC48, MRho0v}}}};

EgGrid = Join[{Ethr + 0.002}, Range[0.16, 1.0, 0.02]];

(* --- gauge invariance of the full stage-3 amplitude, per channel -------------- *)
Print["[fig33] gauge check (eps -> q), stage 3, at Eg = 0.34 GeV, 90 deg:"];
Do[ Print["[fig33]   ", channels[[ic, 1]], " : ",
      ScientificForm[gaugeCheck[WofEg[0.34], Pi/2, channels[[ic]], 3], 3],
      "   stage 4: ",
      ScientificForm[gaugeCheck[WofEg[0.34], Pi/2, channels[[ic]], 4], 3]],
  {ic, 4}];

Print["[fig33] computing four channels, stages 1-6 ..."];
data = Table[
   Table[{Eg, sigTot[WofEg[Eg], channels[[ic]], st]}, {Eg, EgGrid}],
   {st, 6}, {ic, 4}];
Print["[fig33] done computing."];

stageName = {"\[CapitalDelta] only, const. \[CapitalGamma]",
             "\[CapitalDelta], \[CapitalGamma](s,u)+\[Sqrt]X\[Pi]",
             "+ Born",
             "+ form factors",
             "+ \[Rho]/\[Omega]",
             "+ \[Rho]/\[Omega] (opp. phase)"};
Do[ Print["[fig33] stage ", st, " ", channels[[ic, 1]],
     "  peak = ", NumberForm[Max[data[[st, ic, All, 2]]], {6, 1}],
     " ub at Eg = ",
     NumberForm[data[[st, ic, First@Ordering[-data[[st, ic, All, 2]]], 1]],
                {4, 3}], " GeV   |  sigma(1 GeV) = ",
     NumberForm[Last[data[[st, ic, All, 2]]], {6, 1}], " ub"],
  {st, 6}, {ic, 4}];

Export[OUT <> "/fig33_data.csv",
  Join @@ Table[
    Prepend[#, stageName[[st]] <> " " <> channels[[ic, 1]]] & /@ data[[st, ic]],
    {st, 6}, {ic, 4}]];

panel[ic_] := ListLinePlot[{data[[4, ic]], data[[5, ic]], data[[6, ic]]},
   PlotRange -> {{0, 1}, {0, channels[[ic, 4]]}},
   Frame -> True, Axes -> False,
   FrameLabel -> {"\!\(\*SubscriptBox[\(E\), \(\[Gamma]\)]\) (GeV)",
                  "\[Sigma] (\[Mu]b)"},
   PlotLabel -> channels[[ic, 1]],
   PlotStyle -> {Directive[Thin, Dotted, RGBColor[0.55, 0.55, 0.60]],
                 Directive[Thick, RGBColor[0.10, 0.30, 0.70]],
                 Directive[Thin, Dashed, RGBColor[0.85, 0.30, 0.20]]},
   PlotLegends -> If[ic == 1,
       Placed[{stageName[[4]], stageName[[5]], stageName[[6]]}, {0.62, 0.80}],
       None],
   GridLines -> Automatic,
   GridLinesStyle -> Directive[GrayLevel[0.9]],
   ImageSize -> 380, LabelStyle -> {FontSize -> 13, Black}];

fig = Grid[{{panel[1], panel[2]}, {panel[3], panel[4]}}, Spacings -> {1, 1}];
Export[OUT <> "/fig33_stage5.png", fig, ImageResolution -> 130];
Print["[fig33] wrote fig33_stage5.png and fig33_data.csv"];
Print["[fig33] MaxMemoryUsed: ", N[MaxMemoryUsed[]/2^30], " GiB"];
Quit[];
