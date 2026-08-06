# ELA model — validation against Fernández-Ramírez et al.

Reference: C. Fernández-Ramírez, E. Moya de Guerra, J.M. Udías,
*Effective Lagrangian Approach to pion photoproduction from the nucleon*,
nucl-th/0509020v2 (Annals Phys. **321** (2006) 1408). Paper PDF in `../Notes/`.

Equation and table numbers below refer to that paper.

## 1. Lagrangians — `ELA.fr` vs the paper

| Sector | Paper | `ELA.fr` | Status |
|---|---|---|---|
| πNN pseudovector | Eq. (12) | `LBornPiNN` | matches |
| Anomalous magnetic moment | Eq. (13) | `LBornANNt` | matches |
| Born, all five terms | Eq. (14) | `LBorn` | matches term by term |
| ω exchange | Eq. (15) | `LOmega` | matches |
| ρ exchange | Eq. (16) | `LRho` | matches |
| Δ(1232) P33 | Eq. (36) | `LP33gen` | matches |

Eq. (36) in detail — both pieces reproduced with the correct prefactors:

- strong: `-(h/(fπ M*)) N̄ ε_{μνλβ} γ^β γ⁵ (∂^μ Δ^ν_j)(∂^λ π_j)`
- e.m. (gauge-invariant Pascalutsa coupling):
  `(3e/(2M(M+M*))) N̄ [i g₁ F̃_{μν} + g₂ γ⁵ F^{μν}] (∂^μ Δ^ν_3)`

## 2. Parameters — `ELA$Sets` vs Tables 2 and 3

All six parameter sets verified entry by entry.

- **Table 2** (masses, widths, Λ, K_ρ, F_ωNN, K_ω): all entries match.
- **Table 3** (h, g₁, g₂ and the spin-1/2 couplings for every resonance): all entries match.

Exported defaults (`ELA_UFO/parameters.py`) correspond to **set #1**
(PDG masses and widths, FSI phases included, χ²/χ²_PDG = 1):

| | exported | paper |
|---|---|---|
| `MDelta` | 1.209 | 1.209 |
| `WDelta` | 0.102 | 0.102 |
| `hDelta` | 0.764 | 0.764 |
| `g1Delta` | 6.061 | 6.061 |
| `g2Delta` | 2.414 | 2.414 |
| `F1V` | 1.0 | F₁ˢ = F₁ⱽ = 1 |
| `F2V` | 3.70 | κ_p − κ_n = 3.70 |
| `F2SV` | −0.03243 | F₂ˢ/F₂ⱽ = −0.12/3.70 |
| `fpiN` | 0.97016 | f²_πN/4π = 0.0749 |

## 3. Independent numerical checks

These use quantities *derived* from the exported parameters, so they test the
conventions and relative signs rather than just re-reading the same numbers.

**Eqs. (34)–(35), Δ(1232) electromagnetic form factors** — with
ξ ≡ (M*−M)/(M*+M), G_E = −½ξg₂ and G_M = g₁ + ½ξg₂:

| | computed | Table 3 |
|---|---|---|
| G_E | −0.1518 | −0.152 |
| G_M | +6.2128 | +6.213 |
| EMR | −2.44 % | −2.45 % |

**Eqs. (D.11)–(D.12), Δ(1232) helicity amplitudes:**

| | computed | Table 4 |
|---|---|---|
| A_{1/2} | −0.1290 GeV^−1/2 | −0.129 |
| A_{3/2} | −0.2470 GeV^−1/2 | −0.247 |

The helicity amplitudes are sensitive to the **relative sign of g₁ and g₂**
(they enter as `g₁ ∓ ξg₂`), so this pins down the sign convention that the
unpolarised cross section would otherwise partly hide.

## 4. UFO vertices — Δ(1232) sector

Vertices read back out of the generated `ELA_UFO` and checked against Eq. (36).

| UFO vertex | legs | structure | coupling |
|---|---|---|---|
| `V_52` | Δ⁺~ p A | `RFV2`, `RFV3` | `GC_53` (g₁), `GC_54` (g₂) |
| `V_95` | p~ Δ⁺ π⁰ | `FRS2` | `GC_29` (h) |
| `V_101` | Δ⁺~ p π⁰ | `RFS2` | `GC_29` |
| `V_42` | p~ Δ⁺ A | `FRV2`, `FRV3` | `GC_52`, `GC_55` |

- `FRS2`/`RFS2` = `−ε^{νa}(p_π, p_Δ) γ_a γ⁵` — the Eq. (36) strong vertex.
- `FRV2`/`RFV2` = `2 ε^{νμ}(p_Δ, p_γ)` — the g₁ dual-field-strength term
  (the factor 2 is cancelled by the ½ in `GC_52`/`GC_53`).
- `FRV3`/`RFV3` = `[p_γ^ν p_Δ^μ − (p_Δ·p_γ) g^{νμ}] γ⁵` — the g₂ term.
- `sqrt(2/3)` and `sqrt(3/2)` are the expected isospin Clebsch–Gordan factors.

**Gauge invariance.** Both photon vertices vanish *identically* under
ε^μ → q^μ — exactly zero, with no spinors and no on-shell conditions imposed,
as required for couplings built from field strengths. This is the sharpest
available check that the UFO export preserved the Δ sector correctly.

## 4b. Fig33v2.m amplitudes vs Appendix A

Every helicity amplitude of `Fig33v2.m` was compared, at E_γ = 0.34 GeV and
θ* = 90°, against a from-scratch transcription of the paper's Appendix A —
same kinematics, same spinors, same isospin assembly (Eq. 8). Ratios over all
eight (λ₁, λ₂, λ_γ) combinations:

| block | vs paper | ratio |
|---|---|---|
| Born, all four diagrams, three channels | Eqs. (A.1)–(A.6) | **+1.0000** exact |
| Δ(1232) u-channel | Eq. (A.20) | **+1.0000** exact |
| Δ(1232) s-channel | Eq. (A.19) | **−1.0000** exact |

The s-channel Δ therefore entered with the wrong sign. Cause: both Δ diagrams
were built from one `VDstrong`/`VDem` pair with the Δ leg momentum negated, but
the two vertex orientations (`Δ~ N X` and `N~ Δ X`) are related by hermitian
conjugation, not by p_Δ → −p_Δ. With the sign uncorrected the Δ interferes
*constructively* with the Born instead of destructively, and every channel
overshoots — the π⁰p total peaked at 520 μb and sat at 307 μb at E_γ = 1 GeV,
against ~300 μb and ~20 μb in Fig. 33. Fixed in `Mamp`.

Two further points settled at the same time:

- **Form factors.** The paper's Eq. (48) is a *single* factor
  F̂_B = 1 − (1−F₁)(1−F₂)(1−F₃) on the whole Born amplitude — the `"ff"` branch.
  `Fig33_plot.m` had been running the `"dw"` branch (per-diagram projection onto
  the gauge-invariant M₁…M₄ basis), which is not in the paper; it is now off.
  Note F̂_B is deliberately mild: ≈0.93 even at E_γ = 1 GeV, 90°, because it is
  ≈1 whenever any one of F₁, F₂, F₃ is ≈1. It was never the source of the
  overshoot.
- **Δ vertex normalisations.** Taken separately the two Δ vertices, transcribed
  faithfully from Eq. (36), disagree with the paper's own appendices by exactly
  a factor of two each, in opposite directions:
  Γ(Δ→Nπ) = 24.6 MeV against 98.4 MeV from Eq. (B.7), and
  Γ(Δ→Nγ) = 2.21 MeV against 0.552 MeV from Table 4 via Eqs. (D.11)–(D.12).
  The Δ *amplitude* is the product of one of each, so the two cancel identically
  and pion photoproduction is unaffected — the resonance peak reproduces the
  Breit-Wigner built from Table 4 and Γ = 102 MeV to 3% (297 vs 307 μb at
  W = M*). It is **not** harmless for the exported UFO, where the couplings are
  used independently: `hDelta` is a factor 2 low and `g1Delta`/`g2Delta` a
  factor 2 high relative to the physical widths.

Latent, currently zero: `c1n` in `Fig33v2.m` is written `-(I/2) e F1V (1-F1SV)`,
i.e. ∝ (F₁ⱽ − F₁ˢ) = −2F₁ⁿ, one sign away from the neutron Dirac coupling that
Eq. (14) implies (`c2n` has the matching form with F₂ⁿ). Harmless while
F₁ˢ = F₁ⱽ = 1 at the photon point, wrong the moment q²-dependent form factors
are switched on.

## 5. Scope of the cross-section calculation

`GammaN_to_PiN_Delta.m` computes γp → π⁰p through the Δ(1232), s- and
u-channel, with vertices transcribed from the UFO rather than from the paper's
appendix, so it validates the exported model end-to-end.

Deliberately **not** included in this baseline:

- the energy-dependent width Γ(s,u) of Eqs. (44)–(47) — a constant Γ₀ = 0.102 GeV
  is used instead, with the width kept only in the s-channel propagator (in the
  u-channel the Θ functions of Eq. (46) switch it off);
- the Davidson–Workman form factors of Eqs. (48)–(51) and the √X_π(s,u) vertex
  form factor;
- every non-Δ contribution (Born, ρ/ω, and the other six resonances).

Absolute normalisation away from the resonance peak therefore should **not** be
expected to track the paper's figures.

### Results

Produced by `GammaN_to_PiN_Delta_numeric.m` (explicit 4x4 Dirac matrices,
explicit spinors and polarisation vectors, contracted point by point — no
FeynCalc). Runs in well under a minute at 0.16 GiB.

| W [GeV] | E_γ lab [MeV] | dσ/dΩ(90°) [μb/sr] | σ_tot [μb] |
|---:|---:|---:|---:|
| 1.100 | 174.9 | 0.14 | 1.35 |
| 1.150 | 234.8 | 2.98 | 29.5 |
| 1.180 | 272.0 | 10.94 | 111.0 |
| 1.210 | 310.2 | 26.37 | 274.0 |
| **1.232** | **338.8** | **32.17** | **339.2** |
| 1.250 | 362.6 | 31.12 | 331.7 |
| 1.280 | 403.0 | 26.50 | 286.8 |
| 1.320 | 458.4 | 22.31 | 245.2 |
| 1.380 | 544.7 | 20.22 | 225.0 |
| 1.440 | 634.8 | 20.69 | 230.9 |
| 1.500 | 728.7 | 22.62 | 251.3 |

Checks passed:

- **Gauge invariance is exact.** Replacing the polarisation vector by q^μ in the
  *complete* amplitude — both channels, both propagators, between explicit
  on-shell spinors — gives identically 0. This is stronger than the vertex-level
  check, since it also tests the Rarita-Schwinger propagator and the relative
  normalisation of the s- and u-channel terms.
- **The resonance sits in the right place.** σ_tot peaks at W ≈ 1.235 GeV
  (E_γ ≈ 340 MeV), i.e. at the physical Δ(1232), even though the *fitted* pole
  mass in set #1 is M* = 1.209 GeV. The ~25 MeV upward shift is the expected
  effect of p-wave phase space and the k/q flux factor.
- **The magnitude is the right size.** A peak σ_tot of ~340 μb sits just above
  the measured γp → π⁰p peak of roughly 300 μb. Overshooting slightly is what
  one expects from a Δ-only calculation with no Davidson-Workman form factors
  (which suppress) and a constant width.

Known artefact: σ_tot turns back upward above W ≈ 1.44 GeV. That is the
constant-width, no-form-factor u-channel misbehaving far off resonance — exactly
what Eqs. (46)–(51) exist to cure. It is not a defect of the exported model.

### A note on the symbolic route

`GammaN_to_PiN_Delta.m` (FeynCalc, fully symbolic in s, t, u) builds the
amplitude numerators and reproduces the vertex-level gauge-invariance check in
seconds, but the spin-sum trace did not converge in ~25 minutes and grew past
5 GiB — the Dirac trace carries up to four Levi-Civita tensors from the
εγ⁵ vertices and the Rarita-Schwinger numerator. Both attempts (with and
without pre-substituted numerical constants) were abandoned. The explicit
numeric evaluation above is the route that works; the FeynCalc script is kept
for the gauge check and as a starting point should a closed-form expression in
the Mandelstams ever be wanted.
