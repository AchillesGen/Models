(* ****************************************************************************** *)
(*  Fig33_ChiPT.m -- gamma N -> pi N total cross sections from the ChiPT model.    *)
(*                                                                                 *)
(*  Reproduces the layout of Fig. 33 of Fernandez-Ramirez, Moya de Guerra, Udias,   *)
(*  nucl-th/0509020v2, but using the Feynman rules of ChiPT.fr rather than the      *)
(*  ELA ones.                                                                       *)
(*                                                                                  *)
(*  Run:   math -script Fig33_ChiPT.m                                               *)
(*                                                                                  *)
(* ------------------------------------------------------------------------------ *)
(*  HOW THIS IS BUILT, AND WHY                                                      *)
(* ------------------------------------------------------------------------------ *)
(*  It Get-s ELA-Pion-Photoproduction/Fig33v2.m and reuses its machinery wholesale: *)
(*  Dirac algebra, spinors, the Rarita-Schwinger numerator of Eq. (43), the         *)
(*  energy-dependent width Gamma(s,u) and sqrt(X_pi) of Eqs. (44)-(47), the         *)
(*  Davidson-Workman form factor Fhat_B of Eq. (48), the two-body phase space and   *)
(*  the angular quadrature.  That machinery is validated against the paper's        *)
(*  Appendix A to 1e-16 and reproduces Fig. 33 for the ELA model.                   *)
(*                                                                                  *)
(*  ONLY the couplings and masses are replaced, by the ChiPT.fr values.  Nothing is  *)
(*  re-transcribed: every Lorentz structure in the two models was checked vertex by *)
(*  vertex against the exported UFOs and found identical, so swapping the numerical  *)
(*  coefficients is exact rather than approximate.  Re-deriving the vertex algebra   *)
(*  by hand is precisely what produced the s-channel Delta sign error that the       *)
(*  comment in Fig33v2.m documents, so it is deliberately avoided here.             *)
(*                                                                                  *)
(*  The ratio self-test below re-derives each ChiPT/ELA coupling ratio from the      *)
(*  parameters and compares it against the values measured directly from the two    *)
(*  UFOs.  If a coupling is ever mistyped, that test fails loudly.                  *)
(*                                                                                  *)
(* ------------------------------------------------------------------------------ *)
(*  WHAT THIS MODEL CAN AND CANNOT REPRODUCE                                        *)
(* ------------------------------------------------------------------------------ *)
(*  ChiPT.fr contains Born + Delta(1232) only.  It has NO vector mesons (rho, omega)*)
(*  and NONE of the six higher resonances.  So it can describe the Delta region and *)
(*  nothing above it -- expect the curves to fall away where the data show the       *)
(*  second-resonance bump near Eg ~ 0.75 GeV.  The ELA curves in                     *)
(*  ELA-Pion-Photoproduction/fig33_final.png are the fair comparison for the         *)
(*  vector-meson contribution.                                                       *)
(*                                                                                   *)
(*  The nucleon anomalous magnetic moment is included here at the photon point,      *)
(*  F2p(0) = kappa_p, F2n(0) = kappa_n, which is what ChiPT.fr's "Nucleon" form      *)
(*  factor option reduces to at Q^2 = 0.  Built with ChiPT$FormFactors = None the    *)
(*  UFO has no Pauli term at all and the Born would be wrong; set ChiPTPauli = False *)
(*  below to see that.                                                               *)
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

Get[ELADIR <> "/Fig33v2.m"];      (* machinery + the ELA constants *)
Get[ELADIR <> "/pi0p_data.m"];    (* measured sigma(gamma p -> pi0 p)          *)

ChiPTPauli = True;   (* include the nucleon Pauli term (needs CHIPT_FF=Nucleon) *)

(* ---- remember the ELA couplings so the ratios can be checked --------------- *)
elaCpi0 = cpi0; elaC1p = c1p; elaC2p = c2p; elaCKRp = cKRp; elaEE = eev;
elaHfac = hv/(fpiv MDv);
elaKap  = N@Sqrt[3/2] eev/(MNv (MDv + MNv));

(* ============================ ChiPT.fr parameters =========================== *)
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
aEWM1 = 137.035999;    (* SMINPUTS 1: 1/alpha at Q^2 = 0 *)
eev   = N@Sqrt[4 Pi/aEWM1];
LamB  = 1.121;         (* LambdaFF, CHIPTFF 1 *)
fpiv  = fPiC;          (* enters VDstrong as h/(fpi MDelta) *)
DdenD = N[MNv (MDv + MNv)];

(* pseudovector piNN strength: ChiPT generates it from the axial current as
   ga/(2 fPi) (Goldberger-Treiman), where ELA uses f_piN/m_pi. *)
gpiNN = gaC/(2 fPiC);

(* Pauli couplings.  ChiPT's F2p(0), F2n(0) are the anomalous moments, numerically
   the same as ELA's (F2S +- F2V)/2, so only ee and MN change. *)
kapP = +1.792847; kapN = -1.913043;

(* ---- couplings in the conventions of Fig33v2.m ----------------------------- *)
(* Fig33v2 writes the gamma-N-N vertex as c1 gamma^mu + c2 (gamma^mu qslash -
   qslash gamma^mu) with c1p = -I e F1p and c2p = +I e F2p/(4 M).  ChiPT's photon
   has the opposite overall sign, which is an unobservable global phase for a
   single-photon process, so the ELA sign convention is kept here. *)
c1p = N[-I eev];                 c1n = 0.;
c2p = N[+I eev kapP/(4 MNv)];    c2n = N[+I eev kapN/(4 MNv)];
If[!TrueQ[ChiPTPauli], c2p = 0.; c2n = 0.];

cpi0  = N[gpiNN];  cpi0n = N[-gpiNN];  cpiC = N[Sqrt[2] gpiNN];
cKRp  = N[Sqrt[2] eev gpiNN];  cKRm = -cKRp;

s23 = N@Sqrt[2/3]; s13 = N[1/Sqrt[3]];

(* ---- immediates inside Fig33v2.m that depend on the masses ---------------- *)
k0pi = kmom[MDv^2, mpiv];
Ethr = ((MNv + mpiv)^2 - MNv^2)/(2 MNv);

(* ---- channels; "vec" -> {} because ChiPT has no rho/omega ------------------ *)
chPi0P = <|"cpi"->cpi0,  "c1s"->c1p,"c2s"->c2p, "c1u"->c1p,"c2u"->c2p,
           "tsign"->0., "cKR"->0., "fs"->s23, "fu"->s23, "vec"->{}|>;
chPi0N = <|"cpi"->cpi0n, "c1s"->c1n,"c2s"->c2n, "c1u"->c1n,"c2u"->c2n,
           "tsign"->0., "cKR"->0., "fs"->s23, "fu"->s23, "vec"->{}|>;
chPiPn = <|"cpi"->cpiC, "c1s"->c1p,"c2s"->c2p, "c1u"->c1n,"c2u"->c2n,
           "tsign"->1., "cKR"->cKRp, "fs"->-s13, "fu"->s13, "vec"->{}|>;
chPiMp = <|"cpi"->cpiC, "c1s"->c1n,"c2s"->c2n, "c1u"->c1p,"c2u"->c2p,
           "tsign"->-1.,"cKR"->cKRm, "fs"->s13, "fu"->-s13, "vec"->{}|>;
chans  = {chPiMp, chPiPn, chPi0P, chPi0N};

(* ============================== self-tests ================================== *)
Print["-- coupling ratios ChiPT/ELA: derived here vs measured from the two UFOs --"];
chk[lbl_, got_, want_] := Module[{ok = Abs[got - want] < 2. 10.^-4},
   Print["   ", StringPadRight[lbl, 22], NumberForm[got, {8, 5}],
         "   expected ", NumberForm[want, {8, 5}], "   ", If[ok, "ok", "MISMATCH"]];
   ok];
allok = And @@ {
  chk["piNN",        cpi0/elaCpi0,            0.983042],
  chk["gammaNN Dirac", Abs[c1p/elaC1p],       1.000000],
  chk["gamma pi pi", eev/elaEE,               1.000000],
  chk["Kroll-Ruderman", Abs[cKRp/elaCKRp],    0.983042],
  chk["piNDelta",    (hv/(fpiv MDv))/elaHfac, 0.987277],
  chk["gammaNDelta", (N@Sqrt[3/2] eev/DdenD)/elaKap, 1.000989]};
If[!allok, Print["ERROR: a coupling does not match the UFO comparison."]; Quit[1]];
Print["   all consistent with the exported UFOs."];
Print[];

(* =============================== curves ===================================== *)
optD   = <|"born"->False,"delta"->True, "vec"->False,"ff"->True,"edw"->True,"dw"->False|>;
optDB  = <|"born"->True, "delta"->True, "vec"->False,"ff"->True,"edw"->True,"dw"->False|>;

labs = {"\!\(\*SuperscriptBox[\(\[Pi]\), \(-\)]\)p",
        "\!\(\*SuperscriptBox[\(\[Pi]\), \(+\)]\)n",
        "\!\(\*SuperscriptBox[\(\[Pi]\), \(0\)]\)p",
        "\!\(\*SuperscriptBox[\(\[Pi]\), \(0\)]\)n"};
ymax = {350, 300, 400, 400};
EgGrid = Join[{Ethr + 0.002}, Range[0.16, 1.0, 0.02]];

Print["computing ..."];
data = Table[Table[{Eg, sigTot[WofEg[Eg], chans[[ic]], o]}, {Eg, EgGrid}],
   {o, {optD, optDB}}, {ic, 4}];
Print["done."];
Do[Print["   ", StringPadRight[StringTake[labs[[ic]], -6], 8], " peak ",
   Row[Table[NumberForm[Max[data[[m, ic, All, 2]]], {6, 1}], {m, 2}], " / "],
   "   sigma(1 GeV) ",
   Row[Table[NumberForm[Last[data[[m, ic, All, 2]]], {6, 1}], {m, 2}], " / "]], {ic, 4}];

Export[OUTDIR <> "/fig33_chipt_data.csv",
  Join @@ Table[Prepend[#, {"Delta only", "Delta+Born"}[[m]] <> " " <> labs[[ic]]] & /@
     data[[m, ic]], {m, 2}, {ic, 4}]];

{dLo, dHi} = ChiPTData[MNv];
colLo = GrayLevel[0.15]; colHi = RGBColor[0.80, 0.10, 0.10];
legend = {"\[CapitalDelta] only", "\[CapitalDelta] + Born"};
panel[ic_] := ListLinePlot[{data[[1, ic]], data[[2, ic]]},
   PlotRange -> {{0, 1}, {0, ymax[[ic]]}}, Frame -> True, Axes -> False,
   FrameLabel -> {"\!\(\*SubscriptBox[\(E\), \(\[Gamma]\)]\) (GeV)", "\[Sigma] (\[Mu]b)"},
   PlotLabel -> Style[labs[[ic]], 15, Black],
   PlotStyle -> {Directive[Thick, Dotted, GrayLevel[0.1]],
                 Directive[Thick, RGBColor[0.10, 0.30, 0.70]]},
   PlotLegends -> If[ic == 1, Placed[legend, {0.68, 0.82}], None],
   GridLines -> Automatic, GridLinesStyle -> Directive[GrayLevel[0.9]],
   ImageSize -> 400, LabelStyle -> {FontSize -> 13, Black}];
mark[y_, col_, txt_] := {Directive[col, PointSize[0.013]], Point[{0.60, y}],
   Text[Style[txt, 10, Black], {0.63, y}, {-1, 0}]};
panel3 = Show[panel[3],
   ListPlot[{dLo, dHi}, PlotStyle -> {Directive[PointSize[0.007], colLo],
                                      Directive[PointSize[0.007], colHi]},
      IntervalMarkers -> "Bars", PlotRange -> {{0, 1}, {0, ymax[[3]]}}],
   PlotRange -> {{0, 1}, {0, ymax[[3]]}},
   Epilog -> Join[mark[370, colLo, "data, \[CapitalDelta] region"],
                  mark[340, colHi, "data, higher resonances"]]];

fig = Column[{
   Style["\[Gamma]N \[Rule] \[Pi]N total cross sections -- ChiPT.fr Feynman rules",
         16, Bold, Black],
   Style["Born + \[CapitalDelta](1232) only.  ChiPT.fr has NO vector mesons and none of the six higher resonances.", 11, GrayLevel[0.35]],
   Style["Machinery from Fig33v2.m (validated against nucl-th/0509020v2 Appendix A); only the couplings are ChiPT's.",
         10, GrayLevel[0.45]],
   Grid[{{panel[1], panel[2]}, {panel3, panel[4]}}, Spacings -> {1, 1}]},
  Alignment -> Center, Spacings -> 0.6];
Export[OUTDIR <> "/fig33_chipt.png", fig, ImageResolution -> 130];
Print["wrote fig33_chipt.png and fig33_chipt_data.csv"];
Quit[];
