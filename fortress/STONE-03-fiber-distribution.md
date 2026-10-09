# STONE 03: Complete Fiber Distribution (2026-10-09)
## Status: THEOREM (proved by combinatorics).

### Statement
For M_phi: E8 -> R^3, the 240 roots project to exactly 137 points with
fiber sizes {1:60, 2:64, 4:13}. Moreover:
- All 60 singletons are D8/vector roots.
- All 64 doubles are spinor roots.
- All 13 quads are D8/vector roots.

### Proof
The map sees only (x1,x2,x3,x5,x6,x7). Fibers = 6-signatures.

**D8 roots** (112 = C(8,2)x4, scaled: two coords +/-2, rest 0).
Let k = # of nonzero coords in the 6-signature:
- k=2: both +/-2's in signature. (x4,x8)=(0,0) forced. 1 completion.
  Count: C(6,2) x 2^2 = 60 signatures -> 60 singletons, 60 roots.
- k=1: one +/-2 in signature, other in (x4,x8): 4 completions.
  Count: 6 x 2 = 12 signatures -> 12 quads, 48 roots.
- k=0: signature (0^6). Both +/-2's in (x4,x8): 4 completions.
  Count: 1 signature -> 1 quad (origin), 4 roots.
Total D8: 60 + 48 + 4 = 112. ✓

**Spinor roots** (128 = (+/-1)^8, even # of -1).
6-signature is (+/-1)^6. Completions (x4,x8) in {(+/-1,+/-1)} subject to
even total parity. For a signature with m minuses:
- m even: completions {(+,+),(-,-)} = 2.
- m odd: completions {(+,-),(-,+)} = 2.
Every spinor signature has EXACTLY 2 completions (parity mechanism).
Count: 2^6 / 1 = 64 signatures -> 64 doubles, 128 roots. ✓

**No overlap**: D8 signatures are integer (coords in {0,+/-2}),
spinor signatures are half-integer (coords +/-1). Disjoint. ✓

**Total**: 60 + 64 + 13 = 137 signatures. 60(1) + 64(2) + 13(4) = 240. ✓

### Why it matters
- The 137 count is PROVED, not observed. Every piece is forced.
- The vector/spinor split (60/0 singletons, 0/64 doubles, 13/0 quads)
  is a theorem, explaining the numerical observation.
- The parity mechanism for spinor doubling is elegant and general:
  it applies to any projection that drops exactly 2 coordinates.
- This is the structural foundation beneath the flower (Stone 02).

### Script
- `fortress_fibers.py` (combinatorial proof by enumeration + case analysis)
