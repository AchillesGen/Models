(* ****************************************************************************** *)
(*  fig33_vecmeson.m -- sigma(gamma p -> p pi0) with rho/omega exchange added.     *)
(*                                                                                 *)
(*  ChiPT.fr has NO vector mesons, so this curve cannot come from the UFO.  It is   *)
(*  the ChiPT Born + Delta(1232) of Fig33_ChiPT.m PLUS the t-channel omega and      *)
(*  rho^0 exchange of nucl-th/0509020v2 Eqs. (15)-(16), whose couplings             *)
(*      F_omega = 21.11, kappa_omega = -0.17, G_omega = 0.2804                      *)
(*      F_rho   = 2.6,   kappa_rho   = 6.3,   G_rho0  = 0.1161                      *)
(*  are the ELA fit values carried in Fig33v2.m.  They are NOT ChiPT parameters --  *)
(*  the curve is "what the model would look like if the vector mesons of the paper  *)
(*  were bolted on", not a prediction of ChiPT.fr.                                  *)
(*                                                                                  *)
(*  Everything else follows the Fig. 33 prescription exactly: Fhat_B on the Born,    *)
(*  Fhat_V(t) on the vector exchange, sqrt(X_pi(s,u)) on the Delta and the           *)
(*  energy-dependent width.                                                          *)
(*                                                                                   *)
(*  Evaluated on the photon energies in fig33_reference_scan_grid.csv, so the         *)
(*  result drops straight into scan.py next to the other curves.                      *)
(*                                                                                    *)
(*  Run:  math -script fig33_vecmeson.m                                              *)
(* ****************************************************************************** *)

$HistoryLength = 0;

ELADIR = "/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/ELA-Pion-Photoproduction";
OUTDIR = "/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/myPions-Pion-Nucleon-Delta-GI-coupling-Photoexcitation";

Get[ELADIR <> "/Fig33v2.m"];

(* ---- vector-meson couplings, as loaded from Fig33v2.m (ELA values) --------- *)
vecOm   = {GOmPG, FOm, KOmv, MOmv};
vecRho0 = {GRho0PG, FRho, KRhov, MRho0v};

(* ============================ ChiPT.fr parameters ==========================
   Identical to the block in Fig33_ChiPT.m; only the couplings and masses are
   replaced, the machinery is untouched.                                       *)
MNv   = 0.938272;      (* MNucleon *)
MDv   = 1.209;         (* MDelta   *)
GamV  = 0.102;         (* WDelta   *)
mpiv  = 0.1349768;     (* MPi0     *)
mpiSv = mpiv;
fPiC  = 0.093;         (* fPi      *)
gaC   = 1.271;         (* ga       *)
hv    = 0.76;          (* hD       *)
g1v   = 6.061;         (* G1       *)
g2v   = 2.414;         (* G2       *)
aEWM1 = 137.035999;
eev   = N@Sqrt[4 Pi/aEWM1];
LamB  = 1.121;         (* LambdaFF *)
fpiv  = fPiC;
DdenD = N[MNv (MDv + MNv)];

gpiNN = gaC/(2 fPiC);
kapP = +1.792847; kapN = -1.913043;

c1p = N[-I eev];                 c1n = 0.;
c2p = N[+I eev kapP/(4 MNv)];    c2n = N[+I eev kapN/(4 MNv)];

cpi0  = N[gpiNN];  cpi0n = N[-gpiNN];  cpiC = N[Sqrt[2] gpiNN];
cKRp  = N[Sqrt[2] eev gpiNN];  cKRm = -cKRp;

s23 = N@Sqrt[2/3];
k0pi = kmom[MDv^2, mpiv];
Ethr = ((MNv + mpiv)^2 - MNv^2)/(2 MNv);

(* ---- pi0 p, with and without the vector mesons ---------------------------- *)
chPi0P    = <|"cpi"->cpi0, "c1s"->c1p,"c2s"->c2p, "c1u"->c1p,"c2u"->c2p,
              "tsign"->0., "cKR"->0., "fs"->s23, "fu"->s23, "vec"->{}|>;
chPi0PVec = <|"cpi"->cpi0, "c1s"->c1p,"c2s"->c2p, "c1u"->c1p,"c2u"->c2p,
              "tsign"->0., "cKR"->0., "fs"->s23, "fu"->s23,
              "vec"->{vecOm, vecRho0}|>;

optAll = <|"born"->True,"delta"->True,"vec"->True,"ff"->True,"edw"->True,"dw"->False|>;
optNoV = <|"born"->True,"delta"->True,"vec"->False,"ff"->True,"edw"->True,"dw"->False|>;

(* ---- the photon-energy grid used by scan.py ------------------------------- *)
gridFile = OUTDIR <> "/fig33_reference_scan_grid.csv";
If[!FileExistsQ[gridFile],
   Print["ERROR: ", gridFile, " not found -- run scan.py first."]; Quit[1]];
egs = Rest[Import[gridFile, "CSV"]][[All, 1]];
Print["grid: ", Length[egs], " points, ", First[egs], " - ", Last[egs], " GeV"];

Print["computing ..."];
res = Table[{eg,
   sigTot[WofEg[eg], chPi0PVec, optAll],
   sigTot[WofEg[eg], chPi0P,    optNoV]}, {eg, egs}];
Print["done."];

(* Self-test: with the vector mesons switched off this must reproduce the
   `reference` column that scan.py already has, i.e. the Fig. 33 prescription. *)
ref = Rest[Import[gridFile, "CSV"]];
hdr = First[Import[gridFile, "CSV"]];
icol = Position[hdr, "reference"][[1, 1]];
dev = Max[Abs[res[[All, 3]]/ref[[All, icol]] - 1.]];
(* NB the two sides are INDEPENDENT implementations -- this Mathematica
   machinery vs the python UFO evaluator in fig33_from_ufo.py -- so agreement at
   the 1e-4 level is the expected outcome, not exact equality. *)
Print["cross-check  (no vec) / reference - 1 : ", ScientificForm[dev, 3],
      If[dev < 1.*^-3, "   ok (two independent codes)", "   MISMATCH"]];

Export[OUTDIR <> "/fig33_vecmeson_scan_grid.csv",
  Prepend[res, {"Egamma_corr", "reference_vec", "reference_novec"}]];
Print["wrote fig33_vecmeson_scan_grid.csv"];

Do[Print["   Eg = ", NumberForm[res[[i, 1]], {5, 3}],
         "   with vec ", NumberForm[res[[i, 2]], {6, 1}],
         "   without ", NumberForm[res[[i, 3]], {6, 1}]],
   {i, Select[Range[Length[egs]], MemberQ[{0.2, 0.335, 0.5, 0.7, 1.0},
        Round[egs[[#]], 0.005]] &]}];
Quit[];
