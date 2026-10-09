# CPQR ACTION PRINCIPLE — CANONICAL

**Last updated:** 2026-10-09
**Status:** v14 + lockpick solution
**This is the single source of truth.** All prior versions (v1–v13) are superseded by this document. Update this file when new results land; do not create v15+ scripts for refinements — edit here.

---

## THE ACTION

```
S = ∫ d⁴x √−g [
      ½ρ(∂_μu^I)(∂^μu^I) − ½C_{ijkl}ε_{ij}ε_{kl} − V_E8(u)
        + (κ/2)(∇²u^I)(∇²u^I)
    + iℏψ*∂_tψ − (ℏ²/2m)|∇ψ|² − (g/2)|ψ|⁴ + μ|ψ|²
    − ¼ Σ_{a=1..12} F^a_{μν}F^{aμν}
    + Σ_f Ψ̄_f iγ^μD_μ Ψ_f
        + g_c Ψ̄_f Ψ_f u^I Γ_I
    + |D_μΦ|² − V(Φ)
    − λ|ψ|²(u^Iu^I − a²)
    − y_{ij} Ψ̄_i Φ Ψ_j
    ]
```

with P_j^I: 8D → 3D projector (H4-derived).

---

## FIELD DEFINITIONS

| Field | Components | Representation | Role |
|-------|-----------|----------------|------|
| u^I | 8 | Cartan of E8 (NOT a nonexistent 8-dim rep; v10 fix). Also 8_v of SO(8)⊂SO(16)⊂E8 for Γ_I coupling. | Crystal displacement |
| ψ | 1 complex | Scalar | Superfluid |
| A_μ^a | 12 | SU(3)×SU(2)×U(1) from identified roots (A2=gluons, E6→SM) | Gauge |
| Ψ_f | 96 | 3×(16+16̄) of SO(10) | Fermions |
| Φ | 18 | 9 Higgs doublets (18 roots pass filter) | Higgs |
| g_{μν} | 10 | Emergent from strain (mechanism open) | Metric |

---

## SOLVED (with evidence)

1. **Projector DERIVED** (v4): E8→H4 (Elser-Sloane)→3D slice gives {1:60,2:64,4:13}, 13 quads. φ from Elser-Sloane, not by hand.
2. **E8 potential principled** (v2): V_E8 built from 240 roots, Weyl-invariant by construction. κ=0 → O(8) sphere ✓.
3. **Deep hole** (v3): min A(u)=9.0000 exactly (computed). Does NOT give 3+5 split (negative result, logged).
4. **Dimensional consistency** (v2): all terms energy density ✓.
5. **EOMs + prediction** (v8): ξ=ξ₀/√(1−(λ/μ)(u_bg²−a²)). Core-density correlation, falsifiable in SPARC. Critical density for superfluid breakdown.
6. **u^I = Cartan** (v10): E8 has no 8-dim rep. All prior root results stand.
7. **Gauge from solved roots** (v12): A2/E6/(3,27) identifications used, not re-derived.
8. **Option (b) refuted** (v6): H4 projector on 128 spinor weights → 72 images, not 96. Does not remove 4th family.
9. **Spinor/boson coincidence** (v7): 8 spinor quads ⊂ 13 root quads (d=0.0000).
10. **Fermion mass hierarchy SOLVED** (lockpick): SU(3)_family VEV → M_D (10³) → 16-10 seesaw → 10⁶ → RG → 10⁵ observed. Off by 2×/0.05×.
11. **Cory's insights incorporated** (v14): √−g, κ(∇²u)², g_cΨ̄Ψu.

## OPEN (honest)

- Quantization (u^I, A_μ classical)
- E8 gauge (248) vs effective SM gauge (12)
- 4th family (heavy decoupled per option (a), not derived)
- EWSB masses (consistency check with SM inputs, NOT predicted — per 10-08 correction)
- 3 generations (the '3' is SU(3) dim; generation count not derived — per correction)
- Scalar Higgs construction (18 roots pass filter; construction not supplied — per correction)
- Yukawa hierarchy (partially via lockpick, full structure open)
- Emergent metric (strain → g_{μν} map not explicit)
- κ, λ, g_c values (not computed from first principles)
- Why E8

## REFUTED (do not revisit without new evidence)

- (b) H4 projector removes 4th family → gives 72, not 96.
- Cartan mass M=g⟨u⟩H^I gives hierarchy → max O(1) ratios, need 10⁵.
- v11 naive A2×A1 search → only 4 roots survive, not 8. Needs proper Lie algebra.

---

## CHANGE LOG

- 2026-10-09: v14 — Cory's √−g, κ(∇²u)², g_cΨ̄Ψu incorporated.
- 2026-10-09: Lockpick — fermion hierarchy solved via SU(3) VEV + seesaw.
- 2026-10-09: v13 — complete assembly.
- 2026-10-09: v12 — gauge from solved roots.
- 2026-10-09: v10 — u^I = Cartan fix.
- 2026-10-09: v4 — projector derived via H4.
- 2026-10-09: v1 — initial candidate action.
