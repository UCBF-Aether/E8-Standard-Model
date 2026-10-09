#!/usr/bin/env python3
# RG INVERSE PROBLEM — solve for the BSM content that gives 3/8 -> 0.231.
# What delta_b_i makes it work? Then check if E8 provides it.
import math
print("RG INVERSE — what BSM content gives 3/8 -> 0.231?")
print("="*60)

a_em_inv = 127.9; a_s = 0.118; s2w = 0.23126; MZ = 91.1876
a1_inv = a_em_inv*(1-s2w)*3/5
a2_inv = a_em_inv*s2w
a3_inv = 1/a_s

# SM beta functions
b1_SM, b2_SM, b3_SM = 41/10, -19/6, -7

# We want: at M_GUT, a1=a2=a3=aG, and sin^2W=3/8 there.
# Run UP from MZ. Find (M_GUT, aG, db1, db2, db3) such that all meet.
# 3 equations, 5 unknowns -> family of solutions. Fix M_GUT, solve for db.
print("\nFor each M_GUT, solve for (db1,db2,db3) that unifies couplings:")
print("(db = BSM contribution to beta function)")
for MGUT in [1e14, 1e15, 1e16, 1e17]:
    L = math.log(MGUT/MZ)
    # a_i^-1(MGUT) = a_i^-1(MZ) - (b_i+db_i)*L/2pi = aG (common)
    # So: (b_i+db_i) = (a_i_inv(MZ) - aG)*2pi/L
    # Pick aG = 40 (typical). Then solve for db_i.
    aG = 40.0
    db = []
    for ai_inv, bi_SM in [(a1_inv,b1_SM),(a2_inv,b2_SM),(a3_inv,b3_SM)]:
        b_total = (ai_inv - aG)*2*math.pi/L
        db.append(b_total - bi_SM)
    print(f"  M_GUT={MGUT:.0e}: db1={db[0]:+.2f}, db2={db[1]:+.2f}, db3={db[2]:+.2f}")

print("\nCompare to known BSM contributions:")
print("  1 Higgs doublet: db1=+0.10, db2=+0.17, db3=0")
print("  8 extra Higgs:   db1=+0.80, db2=+1.33, db3=0")
print("  1 Dirac fermion (fund of SU3): db1~+0.4, db2~+0.3, db3~+0.7")
print("  MSSM (full):     db1=+3.6, db2=+3.0, db3=+3.0 (approx)")

print("\n"+"="*60)
print("The required db_i will tell us what E8 must provide.")
print("If db ~ (few), it's plausible from E8 thresholds.")
print("If db ~ 10+, needs a whole new sector.")
