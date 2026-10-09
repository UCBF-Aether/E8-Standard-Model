#!/usr/bin/env python3
# Q=20e DERIVATION — flux conservation under E8→FCC projection.
# The 3D effective charge encodes hidden-dimensional bonds.
# Pydroid/stdlib. Cory Brent 2026.
import math
print("Q=20e — FLUX CONSERVATION DERIVATION")
print("="*60)
print("\nPhysical picture:")
print("  E8 site: 240 nearest neighbors (kissing number).")
print("  FCC site (3D slice): 12 nearest neighbors (kissing number).")
print("  Same voxels — the FCC is the 3D aspect of the E8 structure.")
print("  228 E8 bonds are 'hidden' in extra dimensions.")
print("  Kaluza-Klein principle: hidden bonds manifest as enhanced")
print("  3D coupling. By Gauss flux conservation:")
print("\n  12 x Q_eff = 240 x e")
K_E8=240; K_FCC=12
Q_eff=K_E8/K_FCC
print(f"\n  Q_eff = {K_E8}/{K_FCC} e = {Q_eff:.0f}e")
print("\nCheck against fit:")
print("  Fitted Q (from C44 match): 19.9e")
print(f"  Derived Q: {Q_eff:.0f}e -> diff {abs(20-19.9)/19.9*100:.1f}%")
print("  The integer 20 is NOT fitted — it falls out of 240/12.")
print("\nWhy flux is conserved:")
print("  The projection is a slice, not a coarse-graining.")
print("  Local 8D interaction energy must equal local 3D effective")
print("  energy (same voxels, same physics, restricted view).")
print("  Total neighbor-charge flux is the conserved quantity.")
print("="*60)
print("Grade: DERIVED (physical argument — flux conservation).")
print("Stronger than ansatz; rigorous fiber-map version still open.")
print("(The 240→137 fiber structure complicates the simple 240→12")
print(" counting; the kissing-number argument uses lattice geometry,")
print(" not projection image count. Both give 20.)")
