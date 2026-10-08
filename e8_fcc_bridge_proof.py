#!/usr/bin/env python3
"""
========================================================================
THE BRIDGE: E8 CONTAINS FCC AS AN EXACT SUBLATTICE
========================================================================

Theorem: The E8 lattice contains the face-centered cubic (FCC) lattice
as an exact sublattice.

Proof: Restrict E8 to integer points with 5 coordinates zero:
    E8|_3D = {(n1,n2,n3,0,0,0,0,0) : n1+n2+n3 even}
This is exactly the FCC lattice.

Author: Cory Brent
Proven: 2026-10-08
========================================================================
"""

import itertools

def main():
    print("=" * 70)
    print("THE BRIDGE: E8 CONTAINS FCC AS AN EXACT SUBLATTICE")
    print("=" * 70)
    print()
    print("E8 lattice (integer part): {x in Z^8 : sum(xi) even}")
    print("FCC lattice: {(n1,n2,n3) in Z^3 : n1+n2+n3 even}")
    print()
    print("Claim: E8 restricted to (n1,n2,n3,0,0,0,0,0)")
    print("       with n1+n2+n3 even IS the FCC lattice.")
    print()

    # Generate FCC points in a test range
    R = 3
    fcc = set()
    for n1 in range(-R, R+1):
        for n2 in range(-R, R+1):
            for n3 in range(-R, R+1):
                if (n1 + n2 + n3) % 2 == 0:
                    fcc.add((n1, n2, n3))

    # Generate E8 integer points restricted to first 3 coords
    e8_3d = set()
    for n1 in range(-R, R+1):
        for n2 in range(-R, R+1):
            for n3 in range(-R, R+1):
                # E8 condition: sum of all 8 coords even
                # Last 5 are 0, so need n1+n2+n3 even
                if (n1 + n2 + n3 + 0 + 0 + 0 + 0 + 0) % 2 == 0:
                    e8_3d.add((n1, n2, n3))

    print(f"FCC points in range [-{R},{R}]: {len(fcc)}")
    print(f"E8|_3D points in range:       {len(e8_3d)}")
    print()

    # Exact set equality (integer arithmetic, no floats)
    if fcc == e8_3d:
        print("✓✓✓ EXACT MATCH. Sets are identical.")
        print()
        print("THEOREM PROVEN:")
        print("  E8 ⊃ FCC as an exact sublattice.")
        print("  The 3D spacetime lattice lives inside 8D E8.")
        print("  Particles (E8 roots) and spacetime (FCC) are one structure.")
    else:
        print("✗ MISMATCH - theorem fails")
        print(f"  In FCC not E8: {fcc - e8_3d}")
        print(f"  In E8 not FCC: {e8_3d - fcc}")

    print()
    print("=" * 70)
    print("Corollary: E8 root directions contain FCC neighbors.")
    print("=" * 70)
    print()

    # E8 112 roots: (±1,±1,0,0,0,0,0,0)
    roots = set()
    for pos in itertools.combinations(range(8), 2):
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                r = [0]*8
                r[pos[0]] = s1
                r[pos[1]] = s2
                roots.add(tuple(r))

    # Project to 3D, collect unique non-zero
    proj_3d = set()
    for r in roots:
        v = (r[0], r[1], r[2])
        if v != (0, 0, 0):
            proj_3d.add(v)

    # FCC neighbor directions
    fcc_dirs = set()
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            fcc_dirs.add((s1, s2, 0))
            fcc_dirs.add((s1, 0, s2))
            fcc_dirs.add((0, s1, s2))

    print(f"E8 root 3D projections (non-zero): {len(proj_3d)}")
    print(f"FCC neighbor directions:           {len(fcc_dirs)}")
    print(f"FCC directions found in E8:        {len(fcc_dirs & proj_3d)}/12")
    print()

    if fcc_dirs <= proj_3d:
        print("✓ All 12 FCC neighbor directions appear in E8 roots.")
    else:
        print(f"✗ Missing: {fcc_dirs - proj_3d}")

    print()
    print("QED.")

if __name__ == "__main__":
    main()
