(* ****************************************************************************** *)
(*  fig33_vecmeson.m -- sigma(gamma N -> pi N) with rho/omega exchange added,      *)
(*  for all four single-pion channels:                                             *)
(*                                                                                 *)
(*      pi0p   gamma p -> p pi0        pi+n   gamma p -> n pi+                     *)
(*      pi0n   gamma n -> n pi0        pi-p   gamma n -> p pi-                     *)
(*                                                                                 *)
(*  ChiPT.fr has NO vector mesons, so these curves cannot come from the UFO.  They  *)
(*  are the ChiPT Born + Delta(1232) of Fig33_ChiPT.m PLUS the t-channel omega and  *)
(*  rho exchange of nucl-th/0509020v2 Eqs. (15)-(16), whose couplings               *)
(*      F_omega = 21.11, kappa_omega = -0.17, G_omega  = 0.2804                     *)
(*      F_rho   = 2.6,   kappa_rho   = 6.3,   G_rho0   = 0.1161, G_rho+ = 0.0906    *)
(*  are the ELA fit values carried in Fig33v2.m.  They are NOT ChiPT parameters --  *)
(*  the curves are "what the model would look like if the vector mesons of the      *)
(*  paper were bolted on", not a prediction of ChiPT.fr.                            *)
(*                                                                                  *)
(*  WHICH MESON GOES WHERE (the vec lists are taken verbatim from Fig33v2.m):        *)
(*    pi0 p   omega + rho0                                                           *)
(*    pi0 n   omega + rho0, the rho0 with F -> -F because the rho0-neutron vertex     *)
(*            is exactly minus the proton one.  F -> -F and K UNCHANGED: VVNN carries *)
(*            F on the vector part and F*K on the tensor part, so flipping both would *)
(*            leave F*K invariant and silently keep the tensor term at proton sign.   *)
(*    pi+ n   charged rho only, with F -> Sqrt[2] F_rho                               *)
(*    pi- p   the same charged rho                                                    *)
(*                                                                                    *)
(*  Everything else follows the Fig. 33 prescription exactly: Fhat_B on the Born,      *)
(*  Fhat_V(t) on the vector exchange, sqrt(X_pi(s,u)) on the Delta and the             *)
(*  energy-dependent width.                                                            *)
(*                                                                                      *)
(*  Evaluated on the photon energies in fig33_reference_scan_grid.csv, so the result    *)
(*  drops straight into scan.py and plot_scan.py next to the other curves.  Written as  *)
(*  <channel>_vec and <channel>_novec columns; the _novec ones are the cross-check      *)
(*  against the `reference` curves scan.py computed independently in python.            *)
(*                                                                                      *)
(*  Run:  math -script fig33_vecmeson.m       (after scan.py has written the grid)      *)
(* ****************************************************************************** *)

$HistoryLength = 0;

(* Paths.  Override with the environment variables CHIPT_ELADIR / CHIPT_OUTDIR;
   the defaults assume the ELA reference implementation sits beside this
   directory, which is the layout of the public repository. *)
ELADIR = Environment["CHIPT_ELADIR"];
If[ELADIR === $Failed || ELADIR === "",
   ELADIR = FileNameJoin[{ParentDirectory[Directory[]], "ELA-Pion-Photoproduction"}]];
OUTDIR = Environment["CHIPT_OUTDIR"];
If[OUTDIR === $Failed || OUTDIR === "", OUTDIR = Directory[]];

Get[ELADIR <> "/Fig33v2.m"];

(* ---- vector-meson couplings, as loaded from Fig33v2.m (ELA values) --------- *)
vecOm    = {GOmPG,   FOm,                 KOmv,  MOmv};
vecRho0  = {GRho0PG, FRho,                KRhov, MRho0v};
vecRho0n = {GRho0PG, -FRho,               KRhov, MRho0v};
vecRhoC  = {GRhoCPG, N[Sqrt[2] FRho],     KRhov, MRhoPv};

(* ============================ ChiPT.fr parameters ==========================
   Identical to the block in Fig33_ChiPT.m; only the couplings and masses are
   replaced, the machinery is untouched.                                       *)
MNv   = 0.938272;      (* MNucleon *)
MDv   = 1.209;         (* MDelta   *)
GamV  = 0.102;         (* WDelta   *)
mpiv  = 0.1349768;     (* MPi0     *)
mpiSv = mpiv;          (* the paper uses the pi0 mass in every channel *)
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

s23 = N@Sqrt[2/3]; s13 = N[1/Sqrt[3]];
k0pi = kmom[MDv^2, mpiv];
Ethr = ((MNv + mpiv)^2 - MNv^2)/(2 MNv);

(* ---- the four channels, each with and without the vector mesons ------------ *)
mkCh[cpi_, c1s_, c2s_, c1u_, c2u_, ts_, cKR_, fs_, fu_, vec_] :=
  <|"cpi"->cpi, "c1s"->c1s, "c2s"->c2s, "c1u"->c1u, "c2u"->c2u,
    "tsign"->ts, "cKR"->cKR, "fs"->fs, "fu"->fu, "vec"->vec|>;

chanNames = {"pi0p", "pi+n", "pi0n", "pi-p"};
chanVec = {
  mkCh[cpi0,  c1p,c2p, c1p,c2p,  0., 0.,   s23,  s23,  {vecOm, vecRho0}],
  mkCh[cpiC,  c1p,c2p, c1n,c2n,  1., cKRp, -s13, s13,  {vecRhoC}],
  mkCh[cpi0n, c1n,c2n, c1n,c2n,  0., 0.,   s23,  s23,  {vecOm, vecRho0n}],
  mkCh[cpiC,  c1n,c2n, c1p,c2p, -1., cKRm, s13,  -s13, {vecRhoC}]};
(* the same channels with the vector mesons removed *)
chanNoVec = Map[Append[#, "vec" -> {}] &, chanVec];

optAll = <|"born"->True,"delta"->True,"vec"->True, "ff"->True,"edw"->True,"dw"->False|>;
optNoV = <|"born"->True,"delta"->True,"vec"->False,"ff"->True,"edw"->True,"dw"->False|>;

(* ---- the photon-energy grid used by scan.py ------------------------------- *)
gridFile = OUTDIR <> "/fig33_reference_scan_grid.csv";
If[!FileExistsQ[gridFile],
   Print["ERROR: ", gridFile, " not found -- run scan.py first."]; Quit[1]];
grid = Import[gridFile, "CSV"];
hdr  = First[grid];
egs  = Rest[grid][[All, 1]];
Print["grid: ", Length[egs], " points, ", First[egs], " - ", Last[egs], " GeV"];

Print["computing ", Length[chanNames], " channels x 2 ..."];
res = Table[
   Print["   ", chanNames[[ic]], " ..."];
   Table[{sigTot[WofEg[eg], chanVec[[ic]],   optAll],
          sigTot[WofEg[eg], chanNoVec[[ic]], optNoV]}, {eg, egs}],
   {ic, Length[chanNames]}];
Print["done."];

(* Self-test: with the vector mesons switched off each channel must reproduce the
   `reference` column that scan.py computed, i.e. the Fig. 33 prescription.
   Columns are <channel>_reference, with the bare "reference" of the older
   single-channel file accepted for pi0p. *)
refCol[ch_] := Module[{p},
   p = Position[hdr, ch <> "_reference"];
   If[p === {} && ch === "pi0p", p = Position[hdr, "reference"]];
   If[p === {}, None, Rest[grid][[All, p[[1, 1]]]]]];
(* NB the two sides are INDEPENDENT implementations -- this Mathematica
   machinery vs the python UFO evaluator in fig33_from_ufo.py -- so agreement at
   the 1e-4 level is the expected outcome, not exact equality. *)
Do[Module[{ref = refCol[chanNames[[ic]]], dev},
   If[ref === None,
     Print["cross-check  ", chanNames[[ic]], " : no reference column in the "
           <> "grid file -- skipped"],
     dev = Max[Abs[res[[ic, All, 2]]/ref - 1.]];
     Print["cross-check  ", StringPadRight[chanNames[[ic]], 5],
           "  (no vec)/reference - 1 : ", ToString[ScientificForm[dev, 3]],
           If[dev < 1.*^-3, "   ok (two independent codes)", "   MISMATCH"]]]],
  {ic, Length[chanNames]}];

Export[OUTDIR <> "/fig33_vecmeson_scan_grid.csv",
  Prepend[
    Table[Prepend[Flatten[res[[All, ie]]], egs[[ie]]], {ie, Length[egs]}],
    Prepend[Flatten[Table[{chanNames[[ic]] <> "_vec",
                           chanNames[[ic]] <> "_novec"},
                          {ic, Length[chanNames]}]], "Egamma_corr"]]];
Print["wrote fig33_vecmeson_scan_grid.csv"];

Do[Print["   ", StringPadRight[chanNames[[ic]], 5],
         "  peak with vec ", NumberForm[Max[res[[ic, All, 1]]], {6, 1}],
         "   without ",      NumberForm[Max[res[[ic, All, 2]]], {6, 1}]],
   {ic, Length[chanNames]}];
Quit[];
