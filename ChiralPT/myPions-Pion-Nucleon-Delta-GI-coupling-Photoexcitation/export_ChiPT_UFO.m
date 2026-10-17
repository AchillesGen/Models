(* ****************************************************************************** *)
(*  export_ChiPT_UFO.m -- generate the UFO for ChiPT.fr                            *)
(*                                                                                 *)
(*  Usage:                                                                         *)
(*                                                                                 *)
(*      math -script export_ChiPT_UFO.m                    (point-like couplings)   *)
(*      CHIPT_FF=Nucleon math -script export_ChiPT_UFO.m   (nucleon F1/F2)          *)
(*      CHIPT_FF=ELA     math -script export_ChiPT_UFO.m   (export LambdaFF)        *)
(*      CHIPT_FF=All     math -script export_ChiPT_UFO.m   (both)                   *)
(*                                                                                 *)
(*  Environment overrides:                                                         *)
(*      FEYNRULES_PATH   where FeynRules lives (default below)                      *)
(*      CHIPT_FF         form-factor flag, see ChiPT.fr header                      *)
(*      CHIPT_OUT        output directory name (default "ChiPT_UFO")                *)
(*                                                                                 *)
(*  The output directory is OVERWRITTEN.                                            *)
(*                                                                                 *)
(* ------------------------------------------------------------------------------ *)
(*  THREE THINGS THIS SCRIPT DOES THAT ARE EASY TO GET WRONG BY HAND                *)
(* ------------------------------------------------------------------------------ *)
(*                                                                                  *)
(*  1. ChiPT$FormFactors is set BEFORE LoadModel.  M$FormFactors is read while the   *)
(*     model file is being loaded, so setting the flag afterwards has no effect.     *)
(*                                                                                   *)
(*  2. ChiPTClearCache[] is called immediately AFTER LoadModel.  FeynRules evaluates  *)
(*     some of the chiral helper functions while the model is still being set up, at  *)
(*     a point where HC[umat] and del[umat,mu] cannot resolve; Series then            *)
(*     differentiates those heads and the memoisation freezes the resulting           *)
(*     Derivative[1][HC][0] / Derivative[1,0][del][0,...] junk permanently.  Without  *)
(*     the purge every pi-N-Delta vertex in the UFO is contaminated.                  *)
(*                                                                                    *)
(*  3. The checks below are not decoration.  The Delta-vertex count in particular     *)
(*     catches a failure mode where LChiPT silently loses the entire Delta sector     *)
(*     (17 vertices, none with a Delta, instead of 58 with 41) -- see the comment at  *)
(*     LChiPT in ChiPT.fr.  If that count comes back 0, do not use the UFO.           *)
(* ****************************************************************************** *)

$HistoryLength = 0;

(* ---------------------------------------------------------------- settings -- *)
frPath = Environment["FEYNRULES_PATH"];
If[frPath === $Failed || frPath === "",
   frPath = FileNameJoin[{$UserBaseDirectory, "Applications", "feynrules"}]];

(* Point FEYNRULES_PATH at a FeynRules installation.  Note that some FeynRules
   versions are incompatible with recent Mathematica releases and emit UFOs whose
   vertices are silently wrong rather than failing outright; the consistency
   checks at the end of this script exist to catch that. *)
If[!DirectoryQ[frPath],
   Print["ERROR: FeynRules not found at ", frPath,
         "\n       set FEYNRULES_PATH to the feynrules-new directory."];
   Quit[1]];

modelDir = Quiet@Check[DirectoryName[$InputFileName], ""];
If[modelDir === "" || !FileExistsQ[FileNameJoin[{modelDir, "ChiPT.fr"}]],
   modelDir = Directory[]];
If[!FileExistsQ[FileNameJoin[{modelDir, "ChiPT.fr"}]],
   Print["ERROR: ChiPT.fr not found in ", modelDir]; Quit[1]];

ffEnv = Environment["CHIPT_FF"];
ChiPT$FormFactors =
  If[ffEnv === $Failed || ffEnv === "" || ffEnv === "None", None, ffEnv];

outName = Environment["CHIPT_OUT"];
If[outName === $Failed || outName === "", outName = "ChiPT_UFO"];

Print["FeynRules      : ", frPath];
Print["model directory: ", modelDir];
Print["ChiPT$FormFactors = ", ChiPT$FormFactors];
Print["output         : ", outName];
Print[];

(* ------------------------------------------------------------------- load -- *)
$FeynRulesPath = SetDirectory[frPath];
Get["FeynRules`"];
SetDirectory[modelDir];

LoadModel["ChiPT.fr"];
Print[];
Print[ChiPTClearCache[]];          (* MUST come straight after LoadModel *)

(* ------------------------------------------------------------------ export -- *)
Print[];
Print["-- WriteUFO --"];
WriteUFO[LTotal, AddDecays -> False, FlavorExpand -> True, Output -> outName, MaxParticles->4];

(* ----------------------------------------------------------------- summary -- *)
Print[];
Module[{vf, ff},
  vf = FileNameJoin[{modelDir, outName, "vertices.py"}];
  ff = FileNameJoin[{modelDir, outName, "form_factors.py"}];
  If[FileExistsQ[vf],
    Module[{txt = Import[vf, "Text"]},
      Print["vertices.py      : ", StringCount[txt, "= Vertex("], " vertices, ",
            StringCount[txt, "Delta"], " Delta mentions"];
      Print["contamination    : ",
            StringCount[txt, "Derivative"] + StringCount[txt, "HC["], " (want 0)"]],
    Print["WARNING: ", vf, " not written"]];
  Print["form_factors.py  : ",
        If[FileExistsQ[ff], "written", "not written (expected unless CHIPT_FF is set)"]]];

(* ------------------------------------------------- form factor leg check -- *)
(*  A form factor Value is a raw Python string, so FeynRules does NOT relabel  *)
(*  the leg index inside it to match the exported vertex ordering (see the     *)
(*  note in ChiPT.fr at the form factor declarations).  A wrong index is       *)
(*  silent: the form factor would simply be evaluated on the wrong leg's       *)
(*  momentum and the vertex would still work.                                  *)
(*                                                                             *)
(*  The rule is uniform and needs no table of names:                            *)
(*      -P(-9,n)**2  is  Q^2      ->  leg n MUST be a gauge boson (spin 3)     *)
(*      +P(-9,n)**2  is  an invariant mass squared                             *)
(*                                ->  leg n must NOT be a gauge boson          *)
(*  V8 checked only the two Delta form factors; every placement is checked now, *)
(*  which is 150-odd of them.  tools/ff_audit.py runs the same test on an       *)
(*  already-built UFO and adds the "which vertices have no form factor at all"  *)
(*  and "which need more than one variable" questions.                          *)
Module[{lf = FileNameJoin[{modelDir, outName, "lorentz.py"}], txt, bad = 0, n = 0},
  If[FileExistsQ[lf],
   txt = Import[lf, "Text"];
   Do[Module[{spins, hits, want, got},
      spins = ToExpression /@ StringSplit[
        First@StringCases[e, "spins = [" ~~ s : Except["]"] .. ~~ "]" :> s], ","];
      hits = StringCases[e,
        nm : ("F" ~~ WordCharacter ..) ~~ "(" ~~ sg : ("-" | "") ~~
          "P(-9," ~~ d : DigitCharacter .. ~~ ")**2)" :> {nm, sg, ToExpression[d]}];
      Do[n++;
         got  = spins[[h[[3]]]];
         want = If[h[[2]] === "-", got === 3, got =!= 3];
         If[!want, bad++;
            Print["   MISMATCH: ",
                  First@StringCases[e, w : WordCharacter .. ~~ " = Lorentz" :> w],
                  " puts ", h[[1]], " on leg ", h[[3]], " (spin ", got, "), but ",
                  If[h[[2]] === "-", "-P**2 means Q^2 and needs a gauge boson",
                     "+P**2 means an invariant mass and needs a hadron"]]],
       {h, hits}]],
    {e, Select[StringSplit[txt, "\n\n"], StringContainsQ[#, "P(-9,"] &]}];
   Print["form factor leg check: ", n, " placements, ", bad, " mismatches",
         If[bad == 0 && n > 0, "  (ok)",
            If[n == 0, "  (no form factors in this build)", "  <-- FIX ChiPT.fr"]]]]];

Print[];
Print["done -> ", FileNameJoin[{modelDir, outName}]];
Quit[];
