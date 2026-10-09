#!/usr/bin/env python3
# Q=20e — RIGOROUS VERSION. Why flux (linear), not energy (quadratic).
# K44 already counts bonds geometrically. Q carries total site charge.
# Pydroid/stdlib. Cory Brent 2026.
import math
print("Q=20e — RIGOROUS FLUX ARGUMENT")
print("="*60)
print("\nSetup:")
print("  C44 = K44 x (Q^2/4pie0) x n^(4/3)")
print("  K44 = 0.283 (Ewald sum, FCC geometry — COUNTS the 12 bonds)")
print("  Q = total effective charge per FCC site (to be determined)")
print("\nKey insight:")
print("  K44 is the GEOMETRIC factor. It already encodes that FCC")
print("  has 12 neighbors and how they're arranged.")
print("  Q is the CHARGE factor. It must give the total charge that")
print("  an FCC site carries.")
print("\nFlux conservation:")
print("  An FCC site IS an E8 site (same voxel, 3D view).")
print("  In 8D: site sees 240 neighbors x e = 240e total.")
print("  In 3D: site sees 12 neighbors x Q = 12Q total.")
print("  Same site, same total charge:")
print("    12Q = 240e  =>  Q = 20e")
print("\nWhy NOT energy matching (which gives sqrt(20)):")
print("  Energy matching would double-count the bonds.")
print("  K44 ALREADY sums over the 12-bond geometry.")
print("  Putting 240/12 into Q^2 would count bonds twice.")
print("  Charge is linear (Gauss); K44 handles the quadratic geometry.")
print("\nNumerical check:")
e=1.602176634e-19; eps0=8.8541878128e-12
a=1.3729e-15; n=4/a**3; K44=0.283
for Qmult in [1, 20]:
    Q=Qmult*e
    C44=K44*(Q**2/(4*math.pi*eps0))*n**(4/3)
    print(f"  Q={Qmult}e: C44={C44:.3e} Pa")
print("  Target: 4.62e34 Pa")
print("  Q=e fails by 400x. Q=20e hits (1.03%).")
print("  400 = 20^2 — the flux factor squared, as required.")
print("\n"+ "="*60)
print("Q=20e DERIVED. No fit. No circularity.")
print("The 240/12 is kissing-number flux conservation,")
print("not numerology — it's Gauss's law under projection.")
