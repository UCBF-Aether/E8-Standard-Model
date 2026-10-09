#!/usr/bin/env python3
"""
FORTRESS BTFR: Derive the vortex pressure deficit from first principles.
Then show the dimensional path to M~V^2 L/G, labeling all inputs.
"""
import numpy as np
from scipy.integrate import solve_bvp, cumulative_trapezoid

# GP vortex
def gp_vortex(r, f):
    y, yp = f
    rs = np.maximum(r, 1e-10)
    return np.array([yp, -yp/rs + y/rs**2 - (1-y**2)*y])
def bc(fa, fb):
    return np.array([fa[0], fb[0]-1.0])

r = np.linspace(0, 30, 3000)
sol = solve_bvp(gp_vortex, bc, r,
                np.array([np.tanh(r/2), np.gradient(np.tanh(r/2), r)]),
                tol=1e-8, max_nodes=5000)
f = np.clip(sol.sol(r)[0], 0, 1)
rs = np.maximum(r, 1e-10)

# Vortex velocity (units kappa=2pi, so v=1/r)
v = 1.0/rs
v[0] = 0

# Pressure deficit from radial equilibrium: dP/dr = rho_s v^2 / r
# (units rho_s=1). Integrate inward from infinity (P->0 at inf).
# dP/dr = f^2 * v^2 / r  (density-weighted)
dPdr = f**2 * v**2 / rs
# P(r) = -int_r^inf dP/dr' dr'
P = -np.array([np.trapz(dPdr[i:], r[i:]) for i in range(len(r))])
# Actually vectorize: cumulative from outside
P2 = np.zeros_like(r)
P2 = - (cumulative_trapezoid(dPdr[::-1], r[::-1], initial=0))[::-1]

print("="*60)
print("Vortex pressure deficit (Bernoulli, from GP vortex)", flush=True)
print("="*60)
print(f"P deficit at core (r->0): {P2[1]:.4f} (units rho_s(kappa/2pi)^2/xi^2)",
      flush=True)
# Analytic: for f=1, dP/dr=1/r^3, P(r)=-1/(2r^2). Check at large r.
r10 = np.argmin(np.abs(r-10))
print(f"P at r=10: {P2[r10]:.6f}, analytic -1/(2*100) = {-0.005:.6f}",
      flush=True)
print(f"Match: {abs(P2[r10]+0.005)/0.005 < 0.05}", flush=True)

# Energy available for trapping: integral of |P| over volume per unit length
# E/L = int_0^inf 2pi r |P(r)| dr  (cylindrical, per unit vortex length)
E_per_L = np.trapz(2*np.pi*r*np.abs(P2), r)
print(f"\nTrapping energy per unit length: {E_per_L:.4f}", flush=True)
print(f"Analytic (f=1): int 2pi r * (1/2r^2) dr = pi*ln(R/xi)", flush=True)
print(f"  pi*ln(30) = {np.pi*np.log(30):.4f} (cutoff at R=30)", flush=True)

# Dimensional path to M_bar ~ V^2 L / G:
print()
print("="*60)
print("Dimensional path to trapping law:", flush=True)
print("="*60)
print("1. Vortex KE/length ~ rho_s kappa^2 ln(R/xi)  [DERIVED above]")
print("2. V_flat^2 = G*M_vortex(<R)/R, M_vortex ~ rho_s kappa^2 R/c^2")
print("   => kappa^2 ~ V_flat^2 c^2/(rho_s G)  [from Stone 11]")
print("3. Trapping: baryons fall into pressure well until")
print("   M_bar c^2 ~ (trapping energy) ~ rho_s kappa^2 L ln")
print("   => M_bar ~ rho_s kappa^2 L/(c^2) ~ V_flat^2 L/G  [DIMENSIONAL]")
print("   *** The O(1) coefficient and 'until' criterion are POSTULATED ***")
print("4. Hydrostatic: L ~ V^2 R^2/(G M_bar)  [STANDARD]")
print("5. Freeman's law: M_bar ~ R^2  [OBSERVATIONAL INPUT]")
print("6. Combine: M_bar ~ V^4  [FOLLOWS from 3+4+5]")
print()
print("INPUTS: trapping coefficient (postulate), Freeman's law (observed).")
print("DERIVED: pressure deficit, V^4 scaling GIVEN the inputs.")
print("="*60)
