# STONE 07: Shell Purity Theorem (2026-10-09)
## Status: THEOREM (proved by Z[phi] invariant).

### Statement
No D8 image and no spinor image of M_phi share the same radius.
Every shell of the 137-point projection is pure vector or pure spinor.

### Proof
Write r^2 * 4(2+phi) = A + B*phi in Z[phi]. The constant term A is invariant.

Spinor: each coordinate pair (+/-1,+/-1) contributes (1+phi)^2 = 2+3phi
or (1-phi)^2 = 2-phi. Every pair has A=2. Three pairs: A=6 ALWAYS.

D8: 6-signature coords in {0,+/-2}, at most two nonzero.
- (0,0) -> 0 (A=0)
- (+/-2,0) -> 4 (A=4)
- (0,+/-2) -> 4+4phi (A=4)
- (+/-2,+/-2) -> 8+12phi or 8-4phi (A=8)
By case on nonzero count: A in {0, 4, 8}.

{0,4,8} ∩ {6} = ∅. No common radius. PROVED.

### Observed shells (11 nonzero + origin)
Spinor: r-shells with 8, 24, 24, 8 points (= 64).
D8: r-shells with 6, 6, 12, 6, 24, 12, 6 points (= 72, +origin = 73).
No mixed shells.

### Script
- `fortress_purity.py` (invariant proof)
- `fortress_shells.py` (enumeration)
