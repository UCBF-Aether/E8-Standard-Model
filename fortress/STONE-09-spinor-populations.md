# STONE 09: Spinor Shell Populations (2026-10-09)
## Status: THEOREM (proved).

### Statement
The 64 spinor images split into B-shells with populations C(3,n1)*8:
8, 24, 24, 8 for n1 = 0, 1, 2, 3.

### Proof
Spinor 6-signature: (+/-1)^6. Pairs (x1,x5),(x2,x6),(x3,x7).
n1 = # of same-sign pairs. B = 3*n1 - n2 = 4*n1 - 3.
Count signatures with given n1: choose n1 pairs from 3: C(3,n1).
Each pair: 2 sign options. Total per pair-choice: 2^3 = 8.
Population = C(3,n1) * 8.
n1=0: 8, n1=1: 24, n1=2: 24, n1=3: 8. Sum 64. ✓
(Parity completion via (x4,x8) doesn't affect 6-signature count.)

### Script
- `fortress_spinpop.py`
