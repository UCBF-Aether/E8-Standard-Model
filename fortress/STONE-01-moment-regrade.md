# STONE 01: Moment Regrade (2026-10-09)
## Status: REGRADED — standard design-theory consequence, not a discovery.

### The claim (as originally stated)
For the projection family M_t, the power sums
  S_2 = sum ||M_t(a)||^2 = 180
  S_4 = sum ||M_t(a)||^4 = 180
  S_6 = sum ||M_t(a)||^6 = 210
are independent of t (tested at t = 0.5, 1, 1/phi, phi, 2, 3).
This was presented as a candidate new conservation law.

### The regrade
The t-independence is FORCED by the spherical 7-design property of E8 roots.
It is not a new invariant of the map family.

### Proof (symbolic)
1. For Z ~ N(0, I_8), ||M_t(Z)||^2 has chi-squared(3) distribution,
   INDEPENDENT of t. (Each projected coordinate is N(0,1+t^2)/sqrt(1+t^2).)
2. The S^7 average of ||M_t||^{2k} = E[chi2_3^k] / E[chi2_8^k], t-independent:
   k=1: 3/8, k=2: 3/16, k=3: 7/64.
3. E8 roots (normalized) form a spherical 7-design: (1/240) sum = S^7 average
   for polynomial degree <= 7.
4. Sums over 240 roots of norm^2=2: 240 * 2^k * avg:
   k=1: 180, k=2: 180, k=3: 210. EXACT.
5. k=4 (degree 8 > 7): design does not apply -> t-dependence, as observed
   numerically (S_8 varied 272-279 across t values).

### What survives
- The VALUES 180/180/210 remain true and remain in the theory.
- Their explanation is upgraded: proved consequence, not mysterious invariant.
- The proof ADDS structure: chi-squared(3) universality characterizes the
  map's radial profile completely across all t.
- Genuine novelty moves to the FIBER STRUCTURE (Stone 02), which is
  map-specific and not a design consequence.

### Script
- `fortress_moments.py` (symbolic verification)
