# STONE 04: The Infinite Fiber Theorem (2026-10-09)
## Status: THEOREM (proved).

### Statement
Let L be the E8 lattice and M = M_phi: R^8 -> R^3 the fold-and-drop projection.
For every y in M(L), the fiber M^{-1}(y) ∩ L is countably infinite.
All preimages share 6 coordinates; they differ only in (x4, x8).

### Proof
1. **Kernel characterization.** M_phi(x) depends only on (x1,x2,x3,x5,x6,x7).
   x4 and x8 do not appear. If M_phi(x) = M_phi(y) for x,y in (1/2)Z^8,
   phi-irrationality forces xi = yi for i in {1,2,3,5,6,7}, coordinate-wise.
   Fibers differ only in (x4,x8). (Exact, no numerics.)

2. **Infinitude.** Fix a 6-signature s from a lattice point.
   - s integer: (x4,x8) ranges over Z^2 with fixed parity. Infinite.
   - s half-integer: (x4,x8) ranges over (Z+1/2)^2 with parity constraint.
     Infinite.
   Constructive families exist in both cases (see script).

3. **Growth.** Finite patches confirm: max fiber 4 (roots) -> 12 (|x|^2<=6)
   -> 25 (5^8 box) -> infinite (full lattice). Growth ~ R^2 (disk area
   in the (x4,x8) plane).

### Corollary (Multiplicity)
Every observable 3D point corresponds to infinitely many distinct 8D
configurations, indistinguishable from inside the projection. The
multiplicity is structured (confined to kernel directions), not random.
This is the rigorous form of "infinite scenarios per moment."

### Script
- `fortress_infinite.py` (proof sketch + numerical growth confirmation)
