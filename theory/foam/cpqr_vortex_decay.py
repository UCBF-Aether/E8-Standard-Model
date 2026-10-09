#!/usr/bin/env python3
# CPQR VORTEX DECAY — Vinen equation for tangle decay at bounce.
# L(t) = L0/(1+χ₂L0·t). Energy → temperature. Pydroid/stdlib. Cory Brent 2026.
import math

print("="*70)
print("CPQR VORTEX DECAY — toward establishing foam→plasma")
print("="*70)

# Bounce conditions (from foam geometry)
L0 = 1.84e29       # initial line density (m^-2)
E_per_L = 8.71e4   # vortex line energy (J/m)
a_rad = 7.5657e-16 # radiation constant
chi2 = 0.1         # Vinen decay coefficient (from He-II experiments)

# Vinen decay: dL/dt = -χ₂L² → L(t) = L0/(1+χ₂L0·t)
tau = 1/(chi2*L0)
print(f"\nVINEN DECAY")
print(f"  L0 = {L0:.2e} m^-2, χ₂ = {chi2}")
print(f"  Decay timescale τ = 1/(χ₂L0) = {tau:.2e} s")

# Energy and temperature evolution
print(f"\nENERGY → TEMPERATURE")
print(f"  {'t/τ':>8s} {'L (m⁻²)':>12s} {'E (J/m³)':>12s} {'T (K)':>12s}")
for n in [0, 1, 2, 5, 10, 20, 50, 100]:
    t = n*tau
    L = L0/(1+chi2*L0*t)
    E = E_per_L * L
    T = (E/a_rad)**0.25 if E>0 else 0
    print(f"  {n:>8d} {L:>12.2e} {E:>12.2e} {T:>12.2e}")

# When does T hit key thresholds?
print(f"\nTHRESHOLD CROSSINGS (if thermalized)")
for T_target, name in [(1e12,"QGP"),(1.5e11,"confinement"),(1e9,"nucleosynthesis")]:
    E_target = a_rad * T_target**4
    L_target = E_target / E_per_L
    # Solve L0/(1+χ₂L0·t) = L_target → t = (L0/L_target - 1)/(χ₂L0)
    if L_target < L0:
        t_cross = (L0/L_target - 1)/(chi2*L0)
        print(f"  {name:16s} T={T_target:.0e} K at t = {t_cross:.2e} s = {t_cross/tau:.1f}τ")
    else:
        print(f"  {name:16s} already below at bounce")

print(f"\n{'='*70}")
print("STATUS")
print("-"*70)
print("  ✓ Vinen decay law applied (standard superfluid physics).")
print("  ✓ Timescale and temperature evolution computed.")
print("  ✗ Thermalization ASSUMED (not derived).")
print("  ✗ Vortex→quark/gluon channel NOT computed (needs QFT).")
print("  ✗ χ₂ from He-II; CPQR value unknown (order-of-magnitude).")
print("  GRADE: CANDIDATE dynamics, not proof. Next: GP simulation")
print("  of tangle decay + energy channel calculation.")
print("="*70)
