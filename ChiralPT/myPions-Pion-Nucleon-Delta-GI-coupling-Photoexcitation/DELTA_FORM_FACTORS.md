# Δ(1232) form factors in the UFO

How much of the Fig. 33 Δ prescription can be carried by the UFO form-factor
mechanism, what it costs, and how to switch it on.

Reference: Fernández-Ramírez, Moya de Guerra, Udías, nucl-th/0509020v2
(paper PDF in `../Notes/`). Machinery: `../ELA-Pion-Photoproduction/Fig33v2.m`,
couplings: `Fig33_ChiPT.m`.

## 1. What Fig. 33 actually puts on the Δ

Three separate things, only one of which is a vertex-level object:

| | what | where |
|---|---|---|
| (a) | `sqrt(X_π(s,u))`, one factor per Δ diagram, Eqs. (44)–(47) | strong π-N-Δ vertex |
| (b) | energy-dependent width `Γ(s,u) = Γ_Δ X_π(s,u)` | both Δ propagators |
| (c) | nothing | γ-N-Δ vertex |

with `X_π(s,u) = X(s) + X(u) − X(s)X(u)`, `X(l) = 2r³/(1+r⁵)`,
`r = k(l)/k(M_Δ²)`, `k` the π-N cm momentum at invariant mass² `l`, and
`X(l) = 0` below the π-N threshold.

(c) is not an omission: Fig. 33 is real-photon photoproduction, so any Q²
dependence of the γ-N-Δ vertex is invisible to it.

## 2. What survives translation to a UFO form factor

A UFO form factor is a function of **one vertex's own momenta**. `X_π(s,u)`
mixes the Mandelstams of two different diagrams, so it is not a vertex-level
object. The vertex-level object is `X_π(p_Δ²)` — the Δ leg's own invariant
mass squared.

The two agree **exactly** on the s-channel diagram: over the whole physical
region of γN → πN, `u ≤ (M_N − m_π)² < (M_N + m_π)²`, so `X(u) = 0` and
`X_π(s,u) = X_π(s)`. (Checked numerically on the Fig. 33 grid: `max X_π(u) = 0`.)

They differ on the **u-channel Δ**, which Fig. 33 damps by `sqrt(X_π(s))` but a
vertex form factor kills outright. Item (b), the running width, cannot be routed
through the form-factor mechanism at all — it belongs to the propagator.

## 3. What that costs — σ_tot(γN → πN), Born + Δ, µb

`fig33` is the paper's prescription; `vertexrun`/`vertexfix` are what a UFO
form factor gives with a running / fixed Δ width; `none` is the model as it
stands today (no Δ form factor, fixed width).

| channel | scheme | peak | 0.34 GeV | 0.60 GeV | 1.00 GeV |
|---|---|---|---|---|---|
| π⁰p | fig33      | 353.5 | 353.5 |  95.1 |  93.6 |
|     | vertexrun  | 360.3 | 360.3 | 105.4 |  94.6 |
|     | vertexfix  | 371.2 | 371.2 | 103.9 |  94.7 |
|     | fig33fix   | 364.2 | 364.2 |  93.7 |  93.5 |
|     | **none**   | 357.2 | 357.2 | **170.0** | **299.2** |
| π⁺n | fig33      | 244.3 | 220.5 |  34.3 |  19.1 |
|     | vertexrun  | 248.7 | 223.7 |  40.0 |  21.9 |
|     | **none**   | 246.1 | 221.5 |  48.9 |  40.5 |
| π⁻p | fig33      | 304.9 | 268.2 |  76.0 |  52.2 |
|     | vertexrun  | 309.3 | 271.4 |  83.1 |  58.4 |
|     | **none**   | 301.5 | 268.8 |  81.3 |  43.4 |

Read off:

- Missing the Δ form factor entirely is a **factor 3.2** error at Eγ = 1 GeV for
  π⁰p — the whole tail above the resonance.
- A vertex-local form factor recovers essentially all of it: **+2 %** at the peak,
  +9…17 % at 0.6 GeV, +1…15 % at 1 GeV against `fig33`. That residual **is** the
  missing u-channel Δ (it interferes destructively, so dropping it raises σ).
- The running width on its own (`fig33fix` vs `fig33`) is a ~3 % effect at the
  peak and negligible in the tail.

Scan script and CSV: see the session scratchpad (`deltaff_test.m`,
`deltaff_scan.csv`); it re-implements only the Δ block of `Mamp` and self-tests
against the untouched `Fig33v2.m` to machine precision.

## 4. Switching it on

```sh
CHIPT_FF=Delta CHIPT_OUT=ChiPT_UFO_DeltaFF math -script export_ChiPT_UFO.m   # Δ only
CHIPT_FF=All   CHIPT_OUT=ChiPT_UFO_DeltaFF math -script export_ChiPT_UFO.m   # + nucleon F1/F2
```

`ChiPT$FormFactors = "Delta"` swaps `LPiNDeltaGI`/`LGammaNDelta` for
`LPiNDeltaGIFF`/`LGammaNDeltaFF` in `LChiPT`. The export script's
`Delta FF leg check` verifies that every emitted form factor sits on the leg it
claims (`FpiNDelta` on the spin-4 leg, `FgNDelta*` on the photon) — a wrong leg
index is otherwise silent, because FeynRules cannot relabel a form factor whose
value is a raw Python string.

Five functions the generator must supply:

| UFO call | argument | Fig. 33 value |
|---|---|---|
| `FpiNDelta(p_Δ²)` | **p_Δ², not Q²** (GeV², positive) | `sqrt(X_π(p_Δ²))` |
| `FgNDeltaPG1(Q²)`, `FgNDeltaPG2(Q²)` | Q² = −q² | 1 |
| `FgNDeltaNG1(Q²)`, `FgNDeltaNG2(Q²)` | Q² = −q² | 1 |

The γ-N-Δ four **multiply** the fitted couplings G1 = 6.061, G2 = 2.414, so
normalising them to 1 at Q² = 0 leaves the Fig. 33 comparison untouched. Achilles
(`sherpa3-0`, `src/plugins/Sherpa/FormFactors.cc`) already registers
`FDeltaPG1 = Gep + Gmp`, `FDeltaPG2 = 2 Gep (M+M*)/(M−M*)` and the neutron pair,
but those are *replacements* for the coupling, not multipliers —
`FDeltaPG1(0) = 1 + µ_p = 3.79` — so they are deliberately **not** wired to these
names. Use them only with G1, G2 rescaled to compensate.

## 5. Generator side (Sherpa/Achilles)

Sherpa emits one `Lorentz_Calculator` per structure that pulls a `Form_Factor` by
ID and multiplies the whole current by `p_ff->FF(arg)`, with `arg` evaluated from
the UFO string (see `ChiPT_UFO/.sherpa/FFV8.C` for the nucleon case).

Full chain, as run for `ChiPT_UFO_DeltaFF`:

```sh
Sherpa-generate-model ChiPT_UFO_DeltaFF/     # writes .sherpa/, builds, installs
# ^ writes 18 form-factor calculators: FpiNDelta x6, FgNDelta*G* x2 each,
#   F1p/F1n/F2p/F2n x1 each
cp FormFactors.C ChiPT_UFO_DeltaFF/.sherpa/  # NOT generated -- add by hand
#   and register it in .sherpa/CMakeLists.txt, in BOTH the add_library list and
#   the set_source_files_properties list
cd ChiPT_UFO_DeltaFF/.sherpa/build && cmake .. && make -j8 && make install
#   `make install` matters: Sherpa loads the copy in
#   <sherpa>/build/lib/SHERPA-MC/, not the one in .sherpa/build.  Skipping it
#   gives "Fatal error: Form factor not implemented 'F1p'" at process setup.
```

Verified: `Sherpa -f run.yaml` with `2212 22 -> 2212 111` builds the process and
passes Comix's tests.

### Sherpa UFO reader: one form factor occurrence per structure

`ufo_interface/lorentz_algebra.py` accumulates form factors multiplicatively,

```python
self.form_factor *= sympy.Function(func_name)(*args)      # visit_Call
```

so a structure that mentions the *same* form factor twice yields `FF**2`, a
sympy `Pow`, and `lorentz_printer.set_form_factor` then dies with

```
AttributeError: 'Pow' object has no attribute 'name'
```

That is what the four G2 γ-N-Δ structures do naturally, being a two-term
difference. Worked around on the model side: `Interfaces/UFO/PYFormFactors.m`
now `Collect`s the form factors before splicing the value string, emitting
`FF*(a - b)` instead of `FF*a - FF*b`. The parser line should really be
idempotent rather than multiplicative — `FF*a + FF*b` is legal UFO — so this is
worth reporting upstream.

The additions to `.sherpa/FormFactors.C` are:

```cpp
// X_pi of nucl-th/0509020v2 Eqs. (44)-(47).  NB s here is p_Delta^2, not Q^2.
static double XPi(double s) {
    constexpr double MN = 0.938272, MPi = 0.1349768, MD = 1.209;
    if(s < (MN + MPi) * (MN + MPi)) return 0.;
    auto k = [](double l) {
        const double a = l - MN * MN - MPi * MPi;
        const double r = a * a - 4 * MPi * MPi * MN * MN;
        return r <= 0. ? 0. : std::sqrt(r) / (2 * std::sqrt(l));
    };
    const double r = k(s) / k(MD * MD);
    return 2. * r * r * r / (1. + std::pow(r, 5));
}

// inside FormFactorInterface::FF(double arg):
if(m_id == "FpiNDelta") return std::sqrt(XPi(arg));
if(m_id == "FgNDeltaPG1" || m_id == "FgNDeltaPG2" ||
   m_id == "FgNDeltaNG1" || m_id == "FgNDeltaNG2") return 1.;

FORM_FACTOR_IMPLEMENTATION(FpiNDelta)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaPG1)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaPG2)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaNG1)
FORM_FACTOR_IMPLEMENTATION(FgNDeltaNG2)
```

Two interface caveats:

- This needs the `FF(double)` interface (Achilles `sherpa3-0`, `an-attempt-at-DIS`).
  The older `double FF()` on most Achilles branches ignores the UFO argument and
  recomputes Q² from the photon leg — a p_Δ²-dependent form factor cannot work
  there.
- `FpiNDelta` must **not** be routed through `(*p_ff)(Q2)`, the Achilles nucleon
  form-factor object; it is a resonance shape function, not an e.m. form factor.

## 6. Known limitations

- **u-channel Δ is switched off** by the vertex form factor (Sec. 2–3).
- **Running width is not included.** If you also want `Γ_Δ(s)`, it is a
  propagator-level change (UFO `propagators.py` / generator side), not a form
  factor. Note that `sqrt(X_π(s))` on the vertex plus a *fixed* width gives the
  numerator of the Fig. 33 resonance shape but not its denominator; the peak is
  then ~5 % high (`vertexfix` vs `fig33`).
- `FpiNDelta` reaches **every** vertex the gauged strong term produces, not just
  π-N-Δ: the Δ-sector Kroll-Ruderman contact `Δ~ N A π`, the W/Z contacts, and
  the three-point weak N → Δ transition currents. That is deliberate — they share
  the strong vertex and the same Δ leg, and splitting the pion piece off the
  gauge pieces of the vielbein would break gauge invariance — but it does mean
  that switching this on changes the weak Δ production currents too. If those
  should carry their own axial transition form factor instead, they need their
  own Lagrangian term.
- FeynRules prints `Form factor ... appears in more than one vertex` and
  `Fatal Error: Cannot find particle permutation` during the export. Both are
  noise from the momentum-relabelling code path, which cannot act on string
  values; the export completes and the leg check is what proves the result.
