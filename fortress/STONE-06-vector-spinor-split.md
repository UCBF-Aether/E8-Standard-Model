# STONE 06: Vector/Spinor Split (2026-10-09)
## Status: THEOREM (corollary of Stone 03).

### Statement
The 137 images split as 73 vector (D8) + 64 spinor, disjoint.

### Proof
Stone 03 proved: 60 singletons (all D8) + 64 doubles (all spinor) +
13 quads (all D8). Hence vector images = 60+13 = 73, spinor images = 64.
D8 and spinor 6-signatures are disjoint (integer vs half-integer coords),
so no image is both. 73+64 = 137. Verified by enumeration.
### Script
- `fortress_shells.py` (type-disjointness check)
