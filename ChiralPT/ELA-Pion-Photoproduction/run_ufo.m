(* ****************************************************************************** *)
(*  Headless UFO export driver for the ELA pion-photoproduction model.            *)
(*                                                                                *)
(*  Run it through run_ufo.sh, which puts the kernel in a cgroup with a hard       *)
(*  memory cap.  A previous interactive export exhausted all 30 GB of RAM and      *)
(*  the kernel OOM-killer took down unrelated desktop processes; the cap keeps     *)
(*  any repeat contained to the kernel itself.                                     *)
(*                                                                                *)
(*  Memory measures taken here:                                                    *)
(*    * $HistoryLength = 0    - do not retain In[]/Out[] (FeynRules expressions    *)
(*                              are large and would otherwise never be collected). *)
(*    * AddDecays -> False    - skip GetUFODecays.  This is what blew up: it       *)
(*                              computes analytic 1->2 widths for every particle,  *)
(*                              including four spin-3/2 Rarita-Schwinger           *)
(*                              multiplets.  The model deliberately carries only   *)
(*                              on-shell constant widths anyway (see the header    *)
(*                              of ELA.fr), and UFO's __init__.py treats decays.py *)
(*                              as optional.                                       *)
(*    * MaxParticles -> 4     - drop every term with more than four fields before  *)
(*                              vertices are computed.                             *)
(* ****************************************************************************** *)

$HistoryLength = 0;

(* Must be feynrules-new, with the Python-3 UFO interface overlaid on
   Interfaces/UFO (originals kept in Interfaces/UFO.orig-backup).

   feynrules-current is unusable on Mathematica 14.3: it defines rules on
   Commutator, which is now a protected built-in, so every definition fails
   with SetDelayed::write.  The Wick-contraction rule

       Commutator[psi1_, crea[psi2_, inds_, i_]] := KronDelta[...] uwave[...]

   is therefore never installed and crea[] survives unevaluated all the way
   into couplings.py, producing a syntactically valid but physically
   meaningless UFO.  feynrules-new renames the symbol to CommutatorFR. *)

FR$Dir  = "/home/isaacson/.Wolfram/Applications/feynrules-new";
ELA$Dir = "/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/ELA-Pion-Photoproduction";

$FeynRulesPath = SetDirectory[FR$Dir];
<< FeynRules`

SetDirectory[ELA$Dir];

Print["[driver] loading ELA.fr ..."];
LoadModel["ELA.fr"];
Print["[driver] model loaded; memory in use: ", N[MemoryInUse[]/2^30], " GiB"];

Print["[driver] writing UFO (AddDecays -> False, MaxParticles -> 4) ..."];
WriteUFO[LELA,
  Output        -> "ELA_UFO",
  AddDecays     -> False,
  MaxParticles  -> 4,
  DialogBox     -> False
];

Print["[driver] done."];
Print["[driver] MaxMemoryUsed: ", N[MaxMemoryUsed[]/2^30], " GiB"];

Quit[];
