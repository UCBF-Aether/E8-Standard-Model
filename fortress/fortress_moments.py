#!/usr/bin/env python3
"""
FORTRESS STONE 1: Are the 180/180/210 moments forced by the spherical 7-design?
Symbolic proof via sympy: compute S^7 average of ||M_t(x)||^{2k} and check
t-independence for k=1,2,3,4.

E8 roots form a spherical 7-design on S^7 (after normalizing to unit sphere).
For any polynomial p of degree <= 7: (1/240) sum_{roots} p(r) = avg_{S^7}(p).

||M_t(x)||^2 is quadratic in x, so ||M_t||^{2k} has degree 2k.
For k=1,2,3: degree 2,4,6 <= 7, design applies.
For k=4: degree 8 > 7, design does NOT apply -> t-dependence allowed.
"""
import sympy as sp

t = sp.symbols('t', real=True)
# Use Gaussian moment method: avg over S^7 of homogeneous degree-2k polynomial
# equals E[p(Z)] / E[|Z|^{2k}] * (normalization), where Z ~ N(0,I_8).
# Actually simpler: avg_{S^7}[p] for homogeneous p of degree d:
#   = (1/|S^7|) * integral, but we can use:
#   E[p(Z)] = E[|Z|^d] * avg_{S^7}[p]  (by writing Z = R*U, R=|Z|, U uniform on S^7)
# So avg_{S^7}[p] = E[p(Z)] / E[R^d].

# p_k(x) = ||M_t(x)||^{2k}, homogeneous degree 2k.
# M_t(x)_i = (x_i + t*x_{i+4})/sqrt(1+t^2), i=1,2,3.
# ||M_t||^2 = sum_i (x_i + t x_{i+4})^2 / (1+t^2).

# E over Z~N(0,I8): use linearity and known Gaussian moments.
# Let s_i = x_i + t*x_{i+4}. Then s_i ~ N(0, 1+t^2), and s_1,s_2,s_3 independent.
# ||M_t||^2 = (s_1^2+s_2^2+s_3^2)/(1+t^2).
# Let Y = s_1^2+s_2^2+s_3^2. Each s_i^2/(1+t^2) ~ chi2_1, so Y/(1+t^2) ~ chi2_3.
# ||M_t||^2 = W where W ~ chi2_3 (t-independent distribution!).
# Wait: Y = sum s_i^2, s_i ~ N(0,1+t^2). Y/(1+t^2) ~ chi-square(3).
# ||M_t||^2 = Y/(1+t^2) ~ chi2_3. INDEPENDENT OF t!

# So E[||M_t||^{2k}] = E[W^k] for W ~ chi2_3, for ALL k, t-independent!
# E[W^k] = 2^k * Gamma(3/2 + k)/Gamma(3/2).
# k=1: 2*Gamma(5/2)/Gamma(3/2) = 2*(3/2) = 3.
# k=2: 4*Gamma(7/2)/Gamma(3/2) = 4*(5/2)(3/2) = 15.
# k=3: 8*Gamma(9/2)/Gamma(3/2) = 8*(7/2)(5/2)(3/2) = 105.
# k=4: 16*Gamma(11/2)/Gamma(3/2) = 16*(9/2)(7/2)(5/2)(3/2) = 945.

# But this is E over GAUSSIAN, not sphere average. Need avg_{S^7}.
# avg_{S^7}[||M_t||^{2k}] = E[W^k] / E[R^{2k}] where R^2 ~ chi2_8.
# E[R^{2k}] = 2^k * Gamma(4+k)/Gamma(4) = 2^k * (4)(5)...(3+k).
# k=1: 2*4 = 8. avg = 3/8.
# k=2: 4*4*5 = 80. avg = 15/80 = 3/16.
# k=3: 8*4*5*6 = 960. avg = 105/960 = 7/64.
# k=4: 16*4*5*6*7 = 13440. avg = 945/13440 = 63/896.

# Now the 7-design: (1/240) sum_{unit roots} ||M_t||^{2k} = avg_{S^7} for 2k<=7.
# Unit roots: r/|r|, |r|^2=2. ||M_t(r)||^{2k} = 2^k * ||M_t(r/|r|)||^{2k}.
# Sum over 240 roots: 240 * 2^k * avg_{S^7} (for k=1,2,3).

print("="*60)
print("SYMBOLIC: S^7 averages of ||M_t||^{2k} (t-INDEPENDENT by chi2 argument)")
print("="*60)
from fractions import Fraction
import math
for k in range(1, 5):
    # E[W^k], W~chi2_3
    EW = (2**k) * math.gamma(1.5+k)/math.gamma(1.5)
    # E[R^{2k}], R^2~chi2_8
    ER = (2**k) * math.gamma(4+k)/math.gamma(4)
    avg = EW/ER
    # Sum over 240 roots of norm^2=2: 240 * 2^k * avg
    S = 240 * (2**k) * avg
    design = "7-design APPLIES" if 2*k <= 7 else "7-design DOES NOT apply"
    print(f"k={k}: avg_S7 = {avg:.6f} = {sp.nsimplify(avg)}, "
          f"sum_240 = {S:.4f}  [{design}]")

print()
print("Observed numerically: S_2=180, S_4=180, S_6=210, S_8 varies with t.")
print()
print("CONCLUSION:")
print("  The t-independence of S_2, S_4, S_6 is FORCED by the spherical")
print("  7-design + the chi-squared structure of the projection.")
print("  It is NOT a new invariant of the map family — it is design theory.")
print("  The t-DEPENDENCE of S_8 is also predicted (degree 8 > 7).")
print("  => The 180/180/210 claim must be REGRADED: standard consequence,")
print("     not a discovery. The novelty lives in the FIBER STRUCTURE,")
print("     which is map-specific and not a design consequence.")
