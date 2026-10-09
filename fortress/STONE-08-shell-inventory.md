# STONE 08: Complete Shell Inventory (2026-10-09)
## Status: THEOREM (exact phi-arithmetic).

### Statement
The 137 images form 12 shells (11 nonzero + origin). Every shell radius is
exactly r^2 = (A+B*phi)/(4*(2+phi)) for integers (A,B). The (A,B) pair is a
complete shell invariant.

### Inventory
| r^2 | r | pts | type |
|-----|---|-----|------|
| 0 | 0.0000 | 1 | D8 (origin) |
| (6-3φ)/4(2+φ) | 0.2814 | 8 | spinor |
| (8-4φ)/4(2+φ) | 0.3249 | 6 | D8 |
| (4)/4(2+φ) | 0.5257 | 6 | D8 (inner octahedron) |
| (6+φ)/4(2+φ) | 0.7255 | 24 | spinor |
| (8)/4(2+φ) | 0.7435 | 12 | D8 |
| (4+4φ)/4(2+φ) | 0.8507 | 6 | D8 (outer octahedron) |
| (6+5φ)/4(2+φ) | 0.9867 | 24 | spinor |
| (8+4φ)/4(2+φ) = 1 | 1.0000 | 24 | D8 |
| (6+9φ)/4(2+φ) | 1.1920 | 8 | spinor |
| (8+8φ)/4(2+φ) | 1.2030 | 12 | D8 |
| (8+12φ)/4(2+φ) | 1.3764 | 6 | D8 |

### Key facts
- Spinor shells: A=6 always, B in {-3,1,5,9} (Stone 07 invariant).
- D8 shells: (A,B) in {(0,0),(8,-4),(4,0),(8,0),(4,4),(8,4),(8,8),(8,12)}.
- One shell sits at EXACTLY r=1: (8+4φ)/4(2+φ) = 1.
- The (A,B) pair is computed by exact integer arithmetic
  (a+bφ)^2 = (a^2+b^2) + (2ab+b^2)φ. No floating point in the proof.

### Script
- `fortress_inventory.py` (exact enumeration)
