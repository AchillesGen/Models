# Consistency checks

These scripts verify the model against its own symmetries rather than against
data.  Every normalisation in the weak sector is either fixed by a conservation
law or calibrated against one, and these are the calibrations.

Run them from this directory.  `CHIPT_MODEL` selects the UFO (default
`ChiPT_UFO_V8`); `CHIPT_DIR` overrides the repository root.

| script | what it checks | expected |
|---|---|---|
| `cvc_ndelta.py` | weak vector N→Δ against the model's own photon N→Δ | ratio `1.00000000`, residual ~1e-16 |
| `pcac_nucleon.py` | induced pseudoscalar on the W and the Z | contracted current suppressed to `mpi^2/(Q^2+mpi^2)` |
| `pcac_delta.py` | Adler C6A, and the calibration of `C6AN` | multiplier `1.000000`, residue equal to the PCAC value |
| `w_distribution.py` | cumulative σ(W < Wmax) | — |
| `isospin_vector_mesons.py` | isospin weights of ω/ρ exchange in the photo and CC channels | `A(0)` absent from every CC channel |
| `ward_background.py` | `q_mu V^mu = 0` on the assembled background for γN→πN, eN→e'Nπ, νN→νNπ and νN→μ⁻Nπ | every residual ~1e-16 with `--isospin-exact` |
| `ff_audit.py` | every vertex with a hadron on it: does it carry a form factor, is the argument on the right leg, does it really depend on one variable | 0 leg mismatches; a short list of one-variable approximations |
| `ccqe_ls.py` | `nu_mu n -> mu- p` against Llewellyn Smith 1972 — the only check here against an EXTERNAL result | see its header: it currently reports an F_P sign error and a factor 2 against Sherpa |
| `run_ccqe.py` | drives Sherpa over the CCQE energy grid, writes `ccqe_sherpa.csv` | — |
| `imd_check.py` | `nu_mu e- -> mu- nu_e` against the closed tree formula — no hadrons, no form factors, only `G_F` | spin factor `2.00000`, i.e. Sherpa averages over both neutrino helicities |
| `adler_ndelta.py` | fits the weak N→Δ vertex to the eight Adler structures | exact fit; `C4A/C5A = -1/8` where the card claims `-1/4` |
| `pin_scattering.py` | `pi+ p -> pi+ p` against the unitarity limit at the Δ — **no neutrino in it** | peak 216.9 mb = 0.937 of `8π/k²`, vs 0.90 predicted |
| `pcac_1pi.py` | Adler/PCAC: `q·A` on the CC1π current vs the model's own πN amplitude | ~0.32 at Q²→0 — the size of the missing pion pole |

Three traps these encode, all of which produce plausible-looking wrong answers:

* **Select Lorentz structures by the form factor they carry, never by their
  generated names.**  FeynRules numbers `FRV1..FRVn` in emission order, so the
  names are reshuffled whenever a term is added.  `_vertex.with_ff` does this.

* **Project the Rarita–Schwinger leg on shell** before contracting the Δ index.
  Otherwise the unphysical spin-1/2 components dominate, C6A appears orthogonal
  to everything else, and the calibration returns exactly zero with no change in
  the residual.

* **"Vector half" is not "the structure without Gamma5."**  On the four-point
  contact term the correspondence is inverted: the `gamma^mu` (Weinberg–Tomozawa)
  half multiplies the *axial* source and belongs to `<pi N|A^mu|N>`, while the
  `gamma^mu gamma5` (Kroll–Ruderman) half belongs to `<pi N|V^mu|N>` and is the
  one CVC constrains.  The photon proves it: `l = r` there, so the axial source
  vanishes and the `gamma^mu` photon contact does not exist at all.  V8 had the
  two form factors the other way round; `ward_background.py` is what catches it.

## Running order after a model change

```
rm -rf ChiPT_UFO_V9
FEYNRULES_PATH=$HOME/.Wolfram/Applications/feynrules-new \
  CHIPT_FF=All CHIPT_OUT=ChiPT_UFO_V9 math -script export_ChiPT_UFO.m
cd tools
CHIPT_MODEL=ChiPT_UFO_V9 python3 ward_background.py --isospin-exact
CHIPT_MODEL=ChiPT_UFO_V9 python3 ff_audit.py
CHIPT_MODEL=ChiPT_UFO_V9 python3 cvc_ndelta.py
CHIPT_MODEL=ChiPT_UFO_V9 python3 pcac_nucleon.py
CHIPT_MODEL=ChiPT_UFO_V9 python3 pcac_delta.py
```

The Sherpa plugin is a separate step and is **not** produced by the FeynRules
export.  It has already been run for V9; repeat it after any rebuild of the UFO,
because `.sherpa/` is generated from `lorentz.py` and the structure names move:

```sh
export PATH=$HOME/Documents/Projects/sherpa/570-update-achilles-interface/build/bin:$PATH
Sherpa-generate-model ChiPT_UFO_V9/        # writes .sherpa/, builds, installs
cp FormFactors.C ChiPT_UFO_V9/.sherpa/     # NOT generated -- add by hand, and
                                           # register it in .sherpa/CMakeLists.txt:
                                           # the add_library list, plus its OWN
                                           # set_source_files_properties(FormFactors.C
                                           #   PROPERTIES COMPILE_OPTIONS "-g;-O2")
cd ChiPT_UFO_V9/.sherpa/build && cmake .. && make -j8 && make install
```

`FormFactors.C` gets `-O2` but **not** `-ffast-math`, unlike the generated Lorentz
calculators: it has to evaluate the same numbers as `formfactors.py`, and its
per-argument cache uses a NaN sentinel that `-ffinite-math-only` would fold away.
Check `.sherpa/build/CMakeFiles/*.dir/flags.make` after `cmake ..` -- the flags
must actually appear there.  Until the fix in Sherpa's
`MODEL/UFO/src/ufo_interface/Templates/CMakeLists.txt.in`, `PROPERTIES
COMPILE_OPTIONS -g -O2 -ffast-math` was read as the pairs `(COMPILE_OPTIONS, -g)`
and `(-O2, -ffast-math)`, so every UFO model silently built at `-O0`.  Fixing that
and caching the param-card lookups took a 100k-event Sherpa-backend run from
1h02m to 5m40s with the cross sections unchanged to thirteen significant figures.

`FormFactors.C` gained `FZ1pi` in V9; without it Sherpa stops at process setup
with `Fatal error: Form factor not implemented 'FZ1pi'`.  See
`DELTA_FORM_FACTORS.md` §5 for why `make install` matters.

`Sherpa-generate-model` **rewrites the param card**.  Check it afterwards: it
reverts hand-edited entries to the UFO defaults.  For V9 that is harmless --
every calibrated value (hD, G1, G2, C4AN, C6AN) lives in `ChiPT.fr` and the
regenerated card is identical to V8's.

`ward_background.py` without `--isospin-exact` leaves a ~1e-3 residual in the
charged-current channels.  That is not a bug: the pion-in-flight there exchanges
a `pi0` while the produced pion is a `pi+`, and the Ward identity closes only up
to `m_pi+^2 - m_pi0^2`.  The flag sets the two masses equal and the residual
drops to 1e-16, which is how you tell isospin breaking from a real violation.
