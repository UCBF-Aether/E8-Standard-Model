# THEOREM: The 13 Quad Fibers (Proved 2026-10-09)
## Fortress Stone 2

### Statement
For the CPQR fold-and-drop projection M_phi: E8 -> R^3, exactly 13 fibers
have size 4. They form: 1 origin + 6 inner octahedron + 6 outer octahedron,
with shell radii in exact ratio phi.

### Proof (combinatorial)
1. M_phi sees only (x1,x2,x3,x5,x6,x7). By phi-irrationality, two roots
   collide iff they agree on these 6 coordinates. Fibers = 6-signatures.

2. A fiber of size 4 needs 4 distinct (x4,x8) completions of one 6-signature.

3. All 13 quads are D8/vector type (integer signatures). None are spinor
   (verified by enumeration).

4. Case analysis on D8 roots (scaled: two coordinates = +/-2, rest 0):
   
   a) Signature (0,0,0,0,0,0): both +/-2's must sit in (x4,x8).
      Completions: {(+2,+2),(+2,-2),(-2,+2),(-2,-2)} = 4. 
      Image: origin. COUNT: 1.
   
   b) Signature with single +/-2 in (x1,x2,x3), zeros else: the other +/-2
      must be in (x4,x8): {(+2,0),(-2,0),(0,+2),(0,-2)} = 4.
      Image: (+/-1/sqrt(2+phi), 0, 0) and permutations.
      COUNT: 3 positions x 2 signs = 6. (Inner octahedron.)
   
   c) Signature with single +/-2 in (x5,x6,x7), zeros else: same 4 completions.
      Image: (+/-phi/sqrt(2+phi), 0, 0) and permutations.
      COUNT: 3 positions x 2 signs = 6. (Outer octahedron.)

5. Total: 1 + 6 + 6 = 13. No other 6-signature admits 4 completions
   (exhaustive enumeration confirms).

6. Radii: r_inner = 1/sqrt(2+phi) = 0.5257, r_outer = phi/sqrt(2+phi) = 0.8507.
   Ratio = phi EXACTLY (not numerical coincidence).

### Why it matters
- This is a THEOREM about the map, proved by case analysis, not numerics.
- The phi ratio is exact, forced by the D8 root combinatorics.
- It explains WHY the flower has 13 seeds and WHY they sit in phi-ratio
  octahedra: the blind-spot coordinates (x4,x8) can only complete certain
  signatures 4 ways.
- Map-specific: a different projection would give different fiber combinatorics.
  This is NOT a spherical-design consequence.

### Script
- ~/workspace/theory/fortress_quads.py (enumeration + verification)
