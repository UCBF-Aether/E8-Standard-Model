# STONE 10: D8 Shell Populations (2026-10-09)
## Status: THEOREM (proved).

### Statement
The 73 D8 images split into 8 shells with populations:
(A,B)=(0,0):1, (4,0):6, (4,4):6, (8,-4):6, (8,0):12, (8,4):24, (8,8):12, (8,12):6.

### Proof
D8 6-signature: 0, 1, or 2 nonzero (+/-2) coords. (A,B) from (a+bφ)^2.
- k=0: (0,0). 1 signature.
- k=1: single +/-2. a-type (pos 1-3): (4,0), 3x2=6. b-type (pos 5-7): (4,4), 3x2=6.
- k=2, same pair (+/-2,+/-2): same sign (8,12), 3x2=6; diff sign (8,-4), 3x2=6.
- k=2, different pairs: C(3,2)=3 choices.
  Both a-type: (8,0), 3x2x2=12. Both b-type: (8,8), 3x2x2=12.
  Mixed: (8,4), 3x2x2x2=24.
Total: 1+6+6+6+6+12+12+24 = 73. ✓ Cross-checked by enumeration.

### Script
- `fortress_d8pop.py`
