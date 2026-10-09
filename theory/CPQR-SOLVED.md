# CPQR — SOLVED WORKING PARTS (single index)

Every solved piece, its grade, its script, its date. Updated 2026-10-09.
Canonical docs: `CPQR-ACTION-CANONICAL.md`, `CPQR-FULL-THEORY.md`.
GitHub: `UCBF-Aether/E8-Standard-Model/tree/main/theory/`.

## GEOMETRY (E8 → 3D)

| Result | Grade | Script | Date |
|---|---|---|---|
| E8 moments S₂=180, S₄=180, S₆=210 (7-design) | VERIFIED | TOE chain | 2026-10-07 |
| 240→137 fold, {1:60,2:64,4:13} fibers | VERIFIED | `cpqr_action_v4.py` | 2026-10-09 |
| H4 projector via Elser–Sloane | DERIVED | `cpqr_action_v4.py` | 2026-10-09 |
| 13 quadruple fibers, φ radius ratio | VERIFIED | `cpqr_action_v4.py` | 2026-10-09 |
| 73 vector / 64 spinor split | VERIFIED | TOE chain | 2026-10-08 |

## ACTION

| Result | Grade | Script | Date |
|---|---|---|---|
| Complete action v14 (crystal+GP+SM+Higgs) | CANDIDATE | `cpqr_action_v14.py` | 2026-10-09 |
| Fermion hierarchy (SU(3) VEV + seesaw) | DERIVED | `cpqr_lockpick3.py` | 2026-10-09 |
| Maxwell masses (W/Z/H) | VERIFIED | `cpqr_maxwell_masses.py` | 2026-10-09 |

## CONSTANTS

| Result | Grade | Script | Date |
|---|---|---|---|
| C44 = 4.6677e34 Pa (1.03%) | DERIVED | `c44_proper.py` | 2026-10-09 |
| Q = 20e (flux conservation) | DERIVED (rigorous) | `q20e_rigorous.py` | 2026-10-09 |
| a = 1.3729e-15 m | VERIFIED (TOE) | TOE chain | 2026-10-07 |
| α⁻¹ = 137.036 | VERIFIED | TOE chain | 2026-10-07 |
| G = 6.66e-11 (0.22%) | VERIFIED | TOE chain | 2026-10-08 |

## COSMOLOGY (phase cycle)

| Result | Grade | Script | Date |
|---|---|---|---|
| Foam: R_c=5.8a, 20% percolation | DERIVED | `cpqr_foam_geometry.py` | 2026-10-09 |
| Plasma: vortex decay → 2.1e12 K | DERIVED | `cpqr_vortex_decay.py` | 2026-10-09 |
| Energy flow (Julia ODE) | COMPUTED | `cpqr_energy_flow.jl` | 2026-10-09 |
| Gas: Saha X_e 0.86→0.004 | VERIFIED | `cpqr_plasma_to_gas.py` | 2026-10-09 |
| Liquid: H₂ τ/t_H=0.05 | DERIVED | `cpqr_gas_to_liquid.py` | 2026-10-09 |
| Solid: r*=50a recrystallization | DERIVED | `cpqr_liquid_to_solid.py` | 2026-10-09 |
| Full life cycle (self-contained) | VERIFIED | `cpqr_life_cycle_full.py` | 2026-10-09 |

## GALAXIES

| Result | Grade | Script | Date |
|---|---|---|---|
| SPARC 176: 10.83% / HQ 5.65% | VERIFIED | TOE chain | 2026-10-09 |
| BTFR M~V⁴ (structured) | STRUCTURED | TOE chain | 2026-10-08 |
| a₀ = cH₀/2π exact | VERIFIED | TOE chain | 2026-10-08 |

## HONEST OPEN (not solved)

- Q=20e fiber-map rigorous version (physical argument done)
- v14 action: quantization, EWSB details, stability audit
- BTFR trapping/saturation mechanism
- f_s0, H₀, ρ_Λ analytical derivations (Ch.11)
