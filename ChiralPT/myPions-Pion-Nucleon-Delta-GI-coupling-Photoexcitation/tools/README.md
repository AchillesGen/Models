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

Two traps these encode, both of which produce plausible-looking wrong answers:

* **Select Lorentz structures by the form factor they carry, never by their
  generated names.**  FeynRules numbers `FRV1..FRVn` in emission order, so the
  names are reshuffled whenever a term is added.  `_vertex.with_ff` does this.

* **Project the Rarita–Schwinger leg on shell** before contracting the Δ index.
  Otherwise the unphysical spin-1/2 components dominate, C6A appears orthogonal
  to everything else, and the calibration returns exactly zero with no change in
  the residual.
