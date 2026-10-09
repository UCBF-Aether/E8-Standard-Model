#!/usr/bin/env python3
# CPQR FOAM GEOMETRY — derive bubble nucleation + vortex tangle from CPQR parameters.
# Coleman critical bubble + defect overlap + percolation. Pydroid/stdlib. Cory Brent 2026.
import math

print("="*70)
print("CPQR FOAM GEOMETRY — DERIVED")
print("="*70)

# CPQR inputs (established)
a = 1.3729e-15       # lattice spacing (m)
C44 = 4.62e34        # shear modulus (Pa)
n = 1.546e45         # site density (m^-3)
P_zp = 8.84e34       # zero-point pressure (Pa)
P_Mad = -7.24e34     # Madelung pressure (Pa)

print("INPUTS (established)")
print("-"*70)
print(f"  a = {a:.4e} m, C44 = {C44:.2e} Pa, n = {n:.3e} m^-3")

# ── 1. SURFACE TENSION ──
# σ ~ C44 · a (energy/area = pressure × length). Dimensional estimate.
sigma = C44 * a
print(f"\n1. SURFACE TENSION")
print(f"  σ ~ C44·a = {sigma:.2e} J/m²")

# ── 2. ENERGY DENSITY DIFFERENCE ──
# Δε between superheated crystal and foam. From pressure gap.
dP = P_zp + P_Mad  # net (positive = outward)
print(f"\n2. DRIVING PRESSURE")
print(f"  ΔP = P_zp + P_Mad = {dP:.2e} Pa")
print(f"  (22% gap — the superheated crystal pushes outward)")

# ── 3. COLEMAN CRITICAL BUBBLE ──
# R_c = 2σ/ΔP (thin-wall). Bubble of foam in superheated crystal.
R_c = 2*sigma/abs(dP)
print(f"\n3. CRITICAL BUBBLE RADIUS (Coleman thin-wall)")
print(f"  R_c = 2σ/ΔP = {R_c:.2e} m = {R_c/a:.1f} lattice spacings")
print(f"  → Critical foam bubble is ~{R_c/a:.0f}a across. GEOMETRIC PREDICTION.")

# ── 4. NUCLEATION ACTION ──
# S_3 = 16πσ³/(3ΔP²) (3D Euclidean action, thin-wall)
S3 = 16*math.pi*sigma**3/(3*dP**2)
print(f"\n4. NUCLEATION ACTION")
print(f"  S₃ = 16πσ³/3ΔP² = {S3:.2e} J·m = {S3/1.602e-19:.2e} eV·m")
print(f"  (Rate Γ ~ exp(-S₃/T); T at bounce sets the timescale)")

# ── 5. DEFECT OVERLAP ──
# Vacancy strain: |u| = 0.116/r² (r in lattice units, from MD).
# Defects overlap when mean spacing ~ a. Critical vacancy fraction?
# FCC site percolation threshold: p_c ≈ 0.199 (known).
p_c = 0.199
print(f"\n5. DEFECT PERCOLATION")
print(f"  FCC site percolation p_c = {p_c:.3f}")
print(f"  → At ~20% vacancies, defect network percolates = foam onset.")
print(f"  → Foam is BICONTINUOUS (crystal fragments + void network), not isolated bubbles.")

# ── 6. VORTEX TANGLE ──
# At bounce, superfluid is stirred. Vortex line density L (length/volume).
# Intervortex spacing δ ~ L^{-1/2}. For bounce, need vortex pressure ~ ΔP.
# P_vortex ~ (ρ_s κ² /4π) L ln(δ/ξ). Rough: L ~ ΔP / (energy per length).
# Vortex line energy: E/L ~ (ρ_s κ² /4π) ln(δ/ξ). Take ln ~ 1, ρ_s κ² ~ ħ²n/m...
# Order-of-magnitude: E/L ~ C44·a² (elastic energy per length at lattice scale).
E_per_L = C44 * a**2
L_bounce = abs(dP) / E_per_L  # line density for pressure balance
delta = 1/math.sqrt(L_bounce) if L_bounce>0 else float('inf')
print(f"\n6. VORTEX TANGLE AT BOUNCE")
print(f"  Line energy E/L ~ C44·a² = {E_per_L:.2e} J/m")
print(f"  L_bounce ~ ΔP/(E/L) = {L_bounce:.2e} m⁻²")
print(f"  Intervortex spacing δ ~ 1/√L = {delta:.2e} m = {delta/a:.1f}a")
print(f"  → Vortices spaced ~{delta/a:.0f} lattice spacings at bounce.")

# ── 7. FOAM GEOMETRY SUMMARY ──
print(f"\n{'='*70}")
print("FOAM GEOMETRY (derived from CPQR + Coleman)")
print("-"*70)
print(f"  • Critical bubble: R_c ≈ {R_c/a:.0f}a ({R_c:.1e} m), spherical (thin-wall)")
print(f"  • Onset: 20% vacancy percolation → bicontinuous foam")
print(f"  • Vortex spacing at bounce: δ ≈ {delta/a:.0f}a")
print(f"  • Structure: crystal fragments (~{R_c/a:.0f}a) in vortex-tangle matrix")
print(f"  • Percolation: foam percolates at 29% volume (spheres) / 20% (defects)")
print(f"\n  CHAIN: collapse → 20% defects → foam nucleates (R_c~{R_c/a:.0f}a)")
print(f"         → bubbles grow → percolate → vortex pressure → BOUNCE")
print(f"         → expansion → recrystallization → FCC → 137 → particles")
print("="*70)
