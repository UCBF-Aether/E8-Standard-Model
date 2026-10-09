#!/usr/bin/env python3
"""
FORTRESS STONE 10: D8 shell populations proved combinatorially.
D8 6-signatures have 0,1,2 nonzero (+/-2) coords. Count (A,B) per case.
"""
import itertools
from collections import Counter

def AB_of_pair(a, b):
    # (a+b*phi)^2 = (a^2+b^2) + (2ab+b^2)*phi
    return (a*a+b*b, 2*a*b+b*b)

def add(p, q):
    return (p[0]+q[0], p[1]+q[1])

pop = Counter()
detail = {}

# k=0: origin
pop[(0,0)] += 1
detail[(0,0)] = "origin: 1"

# k=1: single +/-2
# a-type (positions 1,2,3): (4,0). 3 pos x 2 signs = 6
pop[(4,0)] += 6
detail[(4,0)] = "k=1 a-type: 3 pos x 2 signs = 6"
# b-type (positions 5,6,7): (4,4). 3 x 2 = 6
pop[(4,4)] += 6
detail[(4,4)] = "k=1 b-type: 3 pos x 2 signs = 6"

# k=2, same pair: (+/-2,+/-2)
# same sign -> (8,12); diff sign -> (8,-4). 3 pairs x 2 each.
pop[(8,12)] += 6
detail[(8,12)] = "k=2 same pair, same sign: 3 x 2 = 6"
pop[(8,-4)] += 6
detail[(8,-4)] = "k=2 same pair, diff sign: 3 x 2 = 6"

# k=2, different pairs: C(3,2)=3 pair choices, 2x2 signs
# both a-type: (8,0). both b-type: (8,8). mixed: (8,4)
pop[(8,0)] += 12
detail[(8,0)] = "k=2 diff pairs, both a-type: 3 x 2 x 2 = 12"
pop[(8,8)] += 12
detail[(8,8)] = "k=2 diff pairs, both b-type: 3 x 2 x 2 = 12"
pop[(8,4)] += 24
detail[(8,4)] = "k=2 diff pairs, mixed: 3 x 2 x 2 x 2 = 24"

print("D8 shell populations:", flush=True)
for ab in sorted(pop, key=lambda x: (x[0]+x[1]*1.618, x[0])):
    print(f"  (A,B)={ab}: {pop[ab]:3d}  [{detail[ab]}]", flush=True)

total = sum(pop.values())
print(f"\nTotal: {total} (expect 73)", flush=True)
assert total == 73

# Cross-check against enumeration
import numpy as np
D8 = set()
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0]*8; v[i] = 2*si; v[j] = 2*sj
            D8.add(tuple(v))
phi = (1+np.sqrt(5))/2
n = np.sqrt(1+phi*phi)
imgs = {}
for r in D8:
    img = tuple(round((r[i]+phi*r[i+4])/n/2, 9) for i in range(3))
    A = B = 0
    for i in range(3):
        a, b = r[i], r[i+4]
        A += a*a+b*b; B += 2*a*b+b*b
    imgs[img] = (A, B)
enum = Counter(imgs.values())
print("\nEnumeration check:", flush=True)
for ab in sorted(enum):
    match = "OK" if enum[ab] == pop[ab] else "MISMATCH"
    print(f"  {ab}: predicted {pop[ab]}, enumerated {enum[ab]} [{match}]", flush=True)
    assert enum[ab] == pop[ab]

print("\n" + "="*60)
print("THEOREM (D8 populations): all 8 D8 shells proved.")
print("="*60)
