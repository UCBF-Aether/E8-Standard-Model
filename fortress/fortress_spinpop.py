#!/usr/bin/env python3
"""
FORTRESS STONE 9: Spinor shell populations proved: C(3,n1)*8.
Each spinor 6-signature (+/-1)^6 has n1 same-sign pairs among
(x1,x5),(x2,x6),(x3,x7). Population of B-shell = C(3,n1)*8.
"""
import itertools
from collections import Counter

# All 64 spinor 6-signatures
sigs = list(itertools.product((1,-1), repeat=6))
assert len(sigs) == 64

def n1(sig):
    # # of same-sign pairs among (s0,s3),(s1,s4),(s2,s5)
    return sum(1 for i in range(3) if sig[i] == sig[i+3])

def B_of(n1):
    # B = 3*n1 - n2, n1+n2=3
    return 3*n1 - (3-n1)

pop = Counter()
for s in sigs:
    pop[B_of(n1(s))] += 1

print("Spinor shell populations by B:", flush=True)
for B in sorted(pop):
    n_1 = (B+3)//4  # invert B=4*n1-3
    expected = {0:1, 1:3, 2:3, 3:1}[n_1] * 8  # C(3,n1)*8
    got = pop[B]
    status = "OK" if got == expected else "FAIL"
    print(f"  B={B:2d} (n1={n_1}): {got} = C(3,{n_1})x8 = {expected} [{status}]",
          flush=True)
    assert got == expected

print()
print("="*60)
print("THEOREM (Spinor populations):")
print("  The 64 spinor images split into B-shells with populations")
print("  C(3,n1)*8 for n1=0,1,2,3: 8, 24, 24, 8.")
print("  Proof: choose n1 of 3 pairs to be same-sign: C(3,n1).")
print("  Each pair has 2 sign options: 2^3. Total C(3,n1)*8.")
print("  (Parity of full root is fixed by (x4,x8) completion,")
print("   which doesn't affect the 6-signature count.)")
print("="*60)
