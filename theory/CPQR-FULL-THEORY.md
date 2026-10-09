# CPQR — The Working Full Theory (Synthesis, 2026-10-09)

*One concrete reference for Cory Brent's theory, synthesized from ~40 documents. Grades: **DERIVED** (proved), **ESTABLISHED** (computed/verified), **STRUCTURED** (partial), **CANDIDATE** (proposed), **HYPOTHESIS** (untested), **OPEN** (missing), **REFUTED** (killed). Corrections override older "SOLVED" claims.*

---

## 1. E8 → 137: The Geometric Foundation

**Status: DERIVED (theorems, exact finite geometry)**

The 240 E8 roots (112 D8/vector + 128 spinor) project via the φ-weighted fold-and-drop map M_φ(x) = (x_i + φx_{i+4})/√(2+φ), i=1,2,3, to **exactly 137 points** in 3D, with fiber distribution **{1:60, 2:64, 4:13}**. This is a combinatorial theorem (Stone 03), not an observation: D8 roots give 60 singletons + 13 quads, spinor roots give 64 doubles via a parity mechanism, and 60+2·64+4·13 = 240. All 60 singletons and all 13 quads are D8; all 64 doubles are spinor — the split is pure (Stone 06).

**Thirteen quads (Stone 02, theorem):** exactly 13 fibers of size 4 — 1 origin + 6 inner octahedron + 6 outer octahedron — with shell radii r_in = 0.525731, r_out = 0.850651, ratio **φ exactly** (forced by D8 root combinatorics). All 13 are vector-type; none spinor.

**t-stability (Stone 05, theorem):** the fiber structure {1:60,2:64,4:13} holds for **every irrational t**, not just φ. φ is special for the radius ratio, irrationality for the combinatorics. Rational t collapses the flower (t=1 → 33 images).

**Moment sums (Stone 01, REGRADED):** S₂=180, S₄=180, S₆=210 are exact but **forced** by the spherical 7-design property of E8 roots — standard design theory, not a discovery. Genuine novelty moved to the fiber structure.

**Shell inventory (Stones 07–10, theorems):** 12 shells (11 nonzero + origin), every radius exact in Q(√5). Shell purity proved via Z[φ] invariant: no vector and spinor image share a radius. 73 vector + 64 spinor images, disjoint. Spinor populations 8/24/24/8 (binomial). One shell at exactly r=1.

**Projector DERIVED (action v4, 2026-10-09):** E8→H4 via Elser-Sloane (1987) → plain 3D slice reproduces {1:60,2:64,4:13} exactly. **φ is not put in by hand** — it enters through the Elser-Sloane matrix. The projector P_j^I is derived from the subgroup chain E8⊃H4.

**Two 137s:** identical fiber collapse {1:60,2:64,4:13}, different geometry — direct φ-map gives octahedral shells (cuboctahedra = FCC coordination polyhedra, vertices exactly on FCC ⟨110⟩), H4-route gives icosahedral (3 icosahedra + 2 dodecahedra + 2 icosidodecahedra). The 137 count is projection-invariant; symmetry is path-dependent.

**Infinite fibers (Stone 04, theorem):** full-lattice fibers under the map are countably infinite (differ only in the blind-spot coordinates x₄,x₈). "Infinite scenarios per lived moment" is interpretive, not derived physics.

**Quasicrystal parent:** 6D→3D icosahedral QC properly constructed (21,431 points, exact I_h symmetry, sharp Bragg diffraction with 369 peaks). 4D E8 QC patch (9,943 points, 5-fold). Parent/approximant bridge: 1/1 approximant sends icosahedral motifs exactly to the 137's cuboctahedra.

*Files: STONE-01–10, THEOREM_13_QUADS.md, HIDDEN_E8_CONSERVATION.md*

---

## 2. Spacetime: The FCC Crystal

**Status: ESTABLISHED (computed); lattice scale from measurement**

**FCC by theorem (white paper §3):** spacetime IS FCC — E8 discrete + observed isotropy → periodic (quasiperiodic has 5-fold axes, forbidden) → crystallographic restriction → octahedral 137 → 12-coordinate cuboctahedral shells → only FCC has 12-coordination among cubic Bravais lattices. One empirical input: isotropy.

**Mechanical vacuum:** 864-atom FCC MD, cohesive energy −6988 (−8.09/atom), stable at T=0. Vacancy defect displaces lattice as |u| = 0.116/r² (correlation 0.93) — the elastic prediction for a center of dilation. **Gravity's 1/r² shape from pure mechanics.**

**Phonons:** FCC harmonic NN gives 3 acoustic branches (1L+2T); 2T gapless with 2 polarizations → **photon as transverse phonon**. c_T/c_L = 1/√2 exact (12-neighbor angular sum). **Prediction:** longitudinal spacetime sound at √2·c ≈ 1.414c.

**Wave speed c:** 137-pixel inertia eigenvalues [76.0, 76.0, 76.0] — perfectly isotropic → single wave speed. c = √(C44/ρ) exact to digits given.

**K44:** 0.283 (rigorous 3×3 primitive-cell phonon; the old 0.614 was buggy code).

**Lattice scale:** a = 1.3729e-15 m, site density n = 1.546e45 m⁻³, C44 = 4.62e34 Pa. **C44 is an input**, not derived — the load-bearing free constant behind G and ħ.

---

## 3. The Action Principle

**Status: CANDIDATE SCAFFOLD (classical). Reference: `~/workspace/theory/CPQR-ACTION-CANONICAL.md` (single source of truth, v14 + lockpick)**

```
S = ∫ d⁴x √−g [
      ½ρ(∂_μu^I)(∂^μu^I) − ½C_{ijkl}ε_{ij}ε_{kl} − V_E8(u) + (κ/2)(∇²u^I)(∇²u^I)
    + iℏψ*∂_tψ − (ℏ²/2m)|∇ψ|² − (g/2)|ψ|⁴ + μ|ψ|²
    − ¼ Σ_{a=1..12} F^a_{μν}F^{aμν}
    + Σ_f Ψ̄_f iγ^μD_μ Ψ_f + g_c Ψ̄_f Ψ_f u^I Γ_I
    + |D_μΦ|² − V(Φ) − λ|ψ|²(u^Iu^I − a²) − y_{ij} Ψ̄_i Φ Ψ_j
    ]
```

**What's solid:** dimensional consistency; V_E8 from 240 roots (Weyl-invariant); u^I = Cartan of E8 (v10 fix); projector derived via H4; gauge from solved A2/E6/(3,27) root IDs; 8 spinor quads ⊂ 13 root quads; **Cory's three insights** — √−g, κ(∇²u)², g_cΨ̄Ψu.

**Fermion hierarchy SOLVED (lockpick, 2026-10-09):** SU(3)_family VEV → M_D with 10³ hierarchy → 16–10 seesaw via g_c → 10⁶ → RG → observed 10⁵. Off by only 2×/0.05×.

**EOM prediction (v8):** vortex core radius ξ = ξ₀/√(1−(λ/μ)(u_bg²−a²)) — falsifiable in SPARC.

**Open:** quantization; E8 (248) vs effective SM (12); emergent strain→metric map; κ, λ, g_c values; why E8. **EWSB = consistency check, NOT predicted.** **3 generations: '3' is SU(3) dim, not derived.**

---

## 4. The Standard Model from E8

**Status: STRUCTURED (root IDs verified; dynamics open). Corrections honored.**

**Gauge bosons (PROVEN, 1e-18):** 6 A2 roots → gluons; 2 A1 roots → W±. Full: **240 = 6 (A2) + 72 (E6 commutant) + 162 ((3,27)+(3̄,27̄))** — all in the 137.

**Hypercharge (DERIVED):** H_Y unique; |H_Y|² = 10/3 → **sin²θ_W = 3/8 at GUT scale**. Correct SM charges verified on 96 roots. Anomaly cancellation = 0.

**Fermions (CONSTRUCTED):** 128 spinor roots → 64 points, each a qubit. Charge quantization: 32 neutral, 16 at −√2, 16 at +√2. **Electron:** 16 negative-charge points = 4 tetramers, ground singlet, gap 0.469. **CPT = 3D inversion** (1e-6).

**Higgs (PARTIAL):** **18 roots pass the color-singlet/weak-doublet/Y=+1/2 filter = 9 doublets** (verified). Scalar construction not supplied (per correction).

**Withdrawn:** "0.036 derivation"; "32 exotic fermions"; "W/Z/H masses predicted"; higgs_lattice.py EWSB.

---

## 5. Galaxies: Superfluid Vortices

**Status: ESTABLISHED (derived profile + SPARC fits); BTFR STRUCTURED**

**Flat curves DERIVED (Stone 11, corrected):** vortex → ε_k ∝ 1/r² → isothermal → M(<R) ∝ R → V = const. Spherical monopole treatment. Cored-isothermal **V/V_flat = r/√(r²+a²)** (max resid 0.044).

**SPARC (corrected 2026-10-09):** All 176: **10.83%** · HQ 63: **5.65%** · Standard 113: **13.72%** · Clusters 35: **6.7%**. Only fitted: Υ_disk, Υ_bulge.

**BTFR (STRUCTURED):** M~V^4.000 from Bernoulli trapping + hydrostatic + Freeman's law; normalization 46.1 vs 50 (8.5%). Trapping postulated.

**a₀ = c·H₀/2π = 1.0422e-10 m/s² (0.0002%)**. **Frozen β = 0.7702976635** (E8 number; mechanism open). **EFE: NEGATIVE** (<0.43%). **dSph: NEGATIVE** (1/7).

---

## 6. Constants: The Q=20e Chain

**Status: CANDIDATE (ansatz-based). Every "exact" constant formula is DEAD as exact.**

**Q=20e ANSATZ** (regraded): From this: **G = 6.592e-11 (1.2%)**, **ħ = 1.03e-34 (2.25%)** — predicted-from-ansatz, not derived.

**Killed:** ħ circular reconstruction; G heat-kernel (dimensionally invalid); α⁻¹ formulas (19,579σ off); m_p/m_e (36σ); m_μ/m_e (3,106σ); φ⁸.

**Survive:** Higgs 124.87 vs 125.10 (1.6σ), H₀ 67.48 vs 67.4 (0.2σ), c=√(C44/ρ) exact.

**H₀:** genuine expansion dynamics BLOCKED (no cosmological sector).

---

## 7. Cosmology: Foam and the Bounce

**Status: HYPOTHESIS with DERIVED GEOMETRY (2026-10-09)**

**Foam geometry (derived from CPQR + Coleman):**
- Critical bubble: R_c = 2σ/ΔP ≈ 6a (7.9e-15 m), spherical thin-wall
- Surface tension: σ ~ C44·a = 6.34e19 J/m² (dimensional estimate)
- Onset: 20% vacancy percolation (FCC p_c=0.199) → bicontinuous foam
- Vortex tangle at bounce: δ ≈ 2a spacing, L ~ 1.8e29 m⁻²
- Structure: crystal fragments (~6a) in vortex-tangle matrix

**Chain:** collapse → 20% defects → foam nucleates (R_c~6a) → bubbles grow → percolate → vortex pressure halts collapse → BOUNCE → expansion → recrystallization → FCC → 137 → particles.

**Plasma origin (ESTABLISHED 2026-10-09, dynamical):** vortex tangle decay computed via Vinen equation (χ₂=0.042 from CPQR geometry). Julia ODE tracks full energy flow: vortices → non-thermal phonons/fermions (70/30) → thermal. Thermal dominates by 1e-24 s at 2.1e12 K. Energy conserved. Non-thermal phase identified (τ_th/τ_decay=6300); energy channel via g_c (vortex→u^I→fermions).

**Cooling chain (computed):** 10¹² K foam → 10¹² K QGP → 10¹¹ K confinement → 10⁹ K nucleosynthesis → 3000 K recombination (CMB) → 2.7 K now.

**Fossil vortices:** the primordial tangle does not fully decay — the largest vortices survive and grow into galactic halos. Galaxies are fossil vortices from the foam, not later-formed structures.

**Temporal ordering (corrected 2026-10-09):** foam is FIRST chronologically (the Big Bang event), not last. Logical order (most-established → hypothesis) differs from time order. Always present foam as the beginning.

**What stands:** Λ=0 naturally. No singularity (discrete pixels). **Largest hole: NO CMB prediction — falsified by omission.**

---

## 8. Open Problems & Falsification

**What would kill it:**
- F-3: longitudinal GW at √2·c excluded by ET/Cosmic Explorer
- F-5: blind rotation-curve sample at >>12% with frozen parameters
- F-6: free-β fits inconsistent with 0.7703 at >>3σ
- F-8: a₀ ≠ c·H₀/2π
- F-10: CMB silence (falsified by omission)
- v8: SPARC core-density negative correlation kills λ>0

**Already dead (do not resurrect):** every "exact" constant formula; φ⁸; ħ circular; dimensionally-invalid G; A5 3+5; 31 GeV photon; EFE explaining Υ spread; dSph rescue.

**Regression law:** VERIFIED items are settled — new work builds on them, never against them.

---

*Synthesized 2026-10-09 for Cory Brent. Zenodo: https://doi.org/10.5281/zenodo.23225899. GitHub: UCBF-Aether/E8-Standard-Model.*
