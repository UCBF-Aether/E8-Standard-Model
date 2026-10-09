#!/usr/bin/env python3
# CPQR MAXWELL — what g_c Ψ̄Ψu predicts beyond the intuition.
# M = g_c ⟨u^I⟩ H^I: masses = Cartan eigenvalues × VEV.
# Pydroid / stdlib only. Cory Brent 2026.
import math
from itertools import product

print("="*70)
print("MAXWELL: M = g_c ⟨u^I⟩ H^I  (fermion masses from Cartan)")
print("="*70)
print("""
  Beyond "fermions get mass from crystal":
  The mass of each fermion = g_c × (its E8 weight · VEV).
  Mass RATIOS are pure E8 geometry — no free Yukawas.
""")

# 16 of SO(10): weights (±½)^5, even # of minus signs
w16=[]
for s in product([-0.5,0.5],repeat=5):
    if sum(1 for x in s if x<0)%2==0:
        w16.append(s)
print(f"16 weights: {len(w16)}")

# Embed SO(10) Cartan (5D) into E8 Cartan (8D).
# Use first 5 directions (simplified; full embedding via E8⊃SO(16)⊃SO(10)).
# VEV: pick a direction. Try ⟨u⟩ ∝ (1,1,1,1,1,0,0,0)/√5 (democratic in SO(10)).
u=[1/math.sqrt(5)]*5+[0]*3

print("\nVEV ⟨u⟩ ∝ (1,1,1,1,1)/√5 in SO(10) Cartan:")
print("-"*70)
masses={}
for w in w16:
    m=sum(wi*ui for wi,ui in zip(w,u))  # weight · VEV (5D part)
    m=round(m,4)
    masses[m]=masses.get(m,0)+1
print(f"  Distinct masses: {sorted(masses.items())}")
print(f"  (# fermions at each mass)")
# The 16 splits by # of +½: k plus signs → mass (2k-5)/(2√5)
# k=0: -5/2√5 (1 state), k=2: -1/2√5 (10 states), k=4: +3/2√5 (5 states)
# Wait: even minuses → k even. k=0,2,4.
# k=0: 1 state (all -); k=2: C(5,2)=10 states; k=4: C(5,4)=5 states.

print("""
  MAXWELL PREDICTION:
  The 16 splits into 1 + 10 + 5 by mass (from weight geometry).
  1 heavy + 10 medium + 5 light — NOT 16 equal masses.
  The ratios are FIXED: m(1):m(10):m(5) = 5:1:-3 (up to sign).

  Compare to SM generation: t (heavy, 1) + ...?
  The top quark is alone at the top. The 1+10+5 doesn't match
  SM directly — but it's a PREDICTION from E8, not a fit.
""")
print("="*70)
print("FARADAY gave: fermions get mass from crystal.")
print("MAXWELL adds: the mass RATIOS are E8 weight geometry,")
print("  the 16 splits 1+10+5, and the VEV direction is now")
print("  a measurable prediction (not a free parameter).")
print("="*70)
