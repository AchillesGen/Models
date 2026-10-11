# ChiPT V0 → V1 vertex diff: change patterns

Oct 11, 2026 · @H

The two vertex files (vrtx\_ChiPT-V0.m and vrtx\_ChiPT-V1.m) contain the same vertex set, so every difference is a sign. Those sign flips fall into four groups.

The pion sector is identical between the two files, including Pi0⁴ = I MPi²/fPi² and the (FV1 + FV2 − 2 FV3)/3 weights for W → 3π. So this V0 already had the UMat fix, and the diff isolates the baryon-convention change.

## 1. Unchanged (bit-identical)

These vertices are the same in both files.

- **Pion and meson–gauge sector:** 4π, γππ, γγππ, Wππ, W/Z → 3π, the AπW and WZπ mixing contacts, Zππ, ZZππ.
- **Nucleon vertices with no pion:** `p~ p A`, `p~ n W`, `n~ p W~`, `p~ p Z`, `n~ n Z`.
- **Nucleon Weinberg–Tomozawa ππ vertices:** `p~ p π⁺π⁻`, `n~ n π⁺π⁻`, `n~ p π⁰π⁻`.
- **γNΔ:** the G1/G2 vertices.
- **Δ vector couplings:** ΔΔγ, ΔΔππ, and the vector parts (`ME·Ga`, AD terms, `Ga·Ga·Ga`) of ΔΔW, ΔΔZ, ΔΔπW and ΔΔπZ.

## 2. Nucleon: flips only where the vertex has an odd number of pions

Only nucleon vertices with an odd pion count change sign.

| Vertex | V0 | V1 |
| --- | --- | --- |
| `n~ n π⁰` | −ga/(2fPi) | +ga/(2fPi) |
| `p~ n π⁺` | +ga/(√2 fPi) | −ga/(√2 fPi) |
| `n~ p A π⁻` (Kroll–Ruderman) | −ee ga/(√2 fPi) | +ee ga/(√2 fPi) |
| `n~ n π⁻ W`, γ^μ / γ^μγ5 | +¼ / −ga/4 | −¼ / +ga/4 |
| `n~ p π⁻ Z` | + … | − … (both halves) |

The W and Z couplings to N̄N are untouched. This is exactly a Φ → −Φ redefinition in the nucleon sector, as the header describes. It moves the nucleon's W/π ratio from −I/2 to +I/2, matching the pion sector and the Δ.

## 3. Δ sector: every axial vertex flips, whatever its pion count

Every vertex proportional to hD, g1D, g2D or g3D flips:

- **N–Δ:** πNΔ, γπNΔ, πNΔW, πNΔZ, and also the pion-free `n~ Δ⁻ W` (+½ → −½) and `n~ Δ⁰ Z` (+ → −).
- **Δ–Δ:** πΔΔ, γπΔΔ, the g-terms of πΔΔW and πΔΔZ, and the g-terms of the pion-free `Δ0~ Δ⁻ W` (+(I/2)g1D/√6 → −(I/2)g1D/√6) and `Δ0~ Δ0 Z`.

This is not Φ → −Φ. It is an overall sign flip of the Δ axial couplings. So the header's statement that "no W/Z coupling without pions moves" holds for the nucleon but not for the Δ.

For the N–Δ part that is fine and actually forced:

- **Fig. 33.** The Born/Δ sign in photoproduction is a field-redefinition invariant ∝ sign(πNN · πNΔ · G). Once πNN flipped, πNΔ had to flip to keep the validated result.
- **Goldberger–Treiman.** The W/π ratio in the N–Δ sector then forces the W–NΔ axial coupling to flip with it.
- **Weak build.** The result is the same as the V2.0 Weak build's patched C5A sign, so the earlier CVC and C5A validations carry over.

## 4. The one that looks wrong: the Δ's own axial charge

V1 flips the Δ's axial-to-vector ratio, which no convention choice can change. Take the pion-free `Δ0~ Δ⁻ W` vertex and compare its ME·γ^μ and ME·γ^μγ5 coefficients:

|  | V0 | V1 | Nucleon (`p~ n W`, both files) |
| --- | --- | --- | --- |
| structure | γ^μ(1 − (g1D/3)γ5) | γ^μ(1 + (g1D/3)γ5) | γ^μ(1 − ga γ5) |

V0 had the Δ "V−A-like", with the same sign as the nucleon. V1 makes it "V+A-like" for g1D > 0. That is the opposite of the quark-model expectation g1 = (9/5)gA > 0.

The cause is the sign in front of `LDeltaPi1–3`. The Hemmert–Holstein–Kambor form puts the coupling inside the kinetic bracket:

```latex
\mathcal{L}_\Delta = -\bar\Psi^\mu\left[(i\not{D} - M)g_{\mu\nu} + \dots + \tfrac{g_1}{2}\,\not{u}\,\gamma_5\, g_{\mu\nu} + \dots\right]\Psi^\nu
```

Your `LDeltaKin1` carries that leading minus, so the axial terms should read **−(g1D/2), −(g2D/2), −(g3D/2)**, not +.

Reverting those three prefactors would:

- **W/Z–ΔΔ:** restore γ^μ(1 − (g1D/3)γ5).
- **Goldberger–Treiman:** keep the ΔΔ W/π ratio at +I/2, because W and π flip together.
- **Strong ratio:** flip πΔΔ relative to πNN. That flip is what V0 actually needed, since its strong and weak ΔΔ-to-N ratios were mutually inconsistent.

This has no effect on Fig. 33 or on any tree-level single-pion process, because ΔΔ vertices don't enter those. It matters for 2π production and anything with Δ rescattering.

**Sanity check after the change:** in `Δ0~ Δ⁻ W`, the ratio of the ME·γ^μγ5 coefficient to the ME·γ^μ coefficient should come out as −g1D/3.
