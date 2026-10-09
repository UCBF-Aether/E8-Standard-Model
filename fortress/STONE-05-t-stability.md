# STONE 05: t-Stability of the Fiber Structure (2026-10-09)
## Status: THEOREM (proved).

### Statement
For every irrational t, the projection M_t: E8 -> R^3 has exactly the fiber
distribution {1:60, 2:64, 4:13} over 137 images. The flower is stable across
the entire irrational t-family. At rational t, further collisions collapse
the image count (e.g. t=1 -> 33 images).

### Proof
M_t(x) = M_t(y) with t irrational and coordinates in (1/2)Z forces
6-signature equality: xi + t*x_{i+4} = yi + t*y_{i+4} implies xi=yi and
x_{i+4}=y_{i+4} by irrationality of t. Hence the fiber partition equals the
6-signature partition for ALL irrational t, and the combinatorics of
Stone 03 apply verbatim: {1:60, 2:64, 4:13}, 137 images.

At rational t = p/q, distinct 6-signatures can satisfy the collision
equations (linear relations over Q), merging fibers. Verified: t=1 gives
33 images with fibers {1:6, 2:8, 8:12, 16:6, 26:1}; t=1/2 and t=2 give
131 images.

### Why it matters
- The 137-flower is not a phi-specific accident. It is stable across
  a continuum of projections. Phi is special for the RADIUS RATIO
  (Stone 02), not for the fiber combinatorics.
- Rational t values are singular: the projection "misfires" and the
  flower collapses. Irrationality is load-bearing.
- This separates what phi contributes (geometry) from what irrationality
  contributes (combinatorics).

### Script
- `fortress_tstable.py` (verification across t = sqrt(2), e, phi, pi, 1, 1/2, 2)
