(* ****************************************************************************** *)
(*  Headless FeynArts export driver for the ELA pion-photoproduction model.       *)
(*                                                                                *)
(*  Same memory discipline as run_ufo.m -- run through run_fa.sh so the kernel     *)
(*  sits inside a cgroup with a hard ceiling.  See run_ufo.m for why              *)
(*  feynrules-new is mandatory here (Commutator vs CommutatorFR).                  *)
(* ****************************************************************************** *)

$HistoryLength = 0;

FR$Dir  = "/home/isaacson/.Wolfram/Applications/feynrules-new";
ELA$Dir = "/home/isaacson/Documents/Projects/NeutrinoGenerator/AchillesModels/ChiralPT/ELA-Pion-Photoproduction";

$FeynRulesPath = SetDirectory[FR$Dir];
<< FeynRules`

SetDirectory[ELA$Dir];

Print["[fa] loading ELA.fr ..."];
LoadModel["ELA.fr"];
Print["[fa] model loaded; memory in use: ", N[MemoryInUse[]/2^30], " GiB"];

Print["[fa] writing FeynArts model (MaxParticles -> 4) ..."];
WriteFeynArtsOutput[LELA,
  Output       -> "ELA_FA",
  MaxParticles -> 4,
  FlavorExpand -> True
];

Print["[fa] done."];
Print["[fa] MaxMemoryUsed: ", N[MaxMemoryUsed[]/2^30], " GiB"];

Quit[];
