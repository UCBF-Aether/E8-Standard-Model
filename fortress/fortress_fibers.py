#!/usr/bin/env python3
"""
FORTRESS STONE 3: Complete fiber distribution {1:60, 2:64, 4:13} by pure
combinatorics. Proves the vector/spinor split: singletons all D8, doubles
all spinor, quads all D8.
"""
import itertools
from collections import defaultdict, Counter

# E8 roots, scaled to integers
D8 = []   # (±2,±2,0^6)
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0]*8; v[i] = 2*si; v[j] = 2*sj
            D8.append(tuple(v))
SPIN = [] # (±1^8), even # of -1
for bits in itertools.product((1, -1), repeat=8):
    if sum(1 for b in bits if b < 0) % 2 == 0:
        SPIN.append(tuple(bits))
assert len(D8) == 112 and len(SPIN) == 128

def sig6(r):
    return (r[0], r[1], r[2], r[4], r[5], r[6])

# --- D8 case analysis ---
# k = # of nonzero coords in 6-signature
d8_by_k = defaultdict(list)
for r in D8:
    s = sig6(r)
    k = sum(1 for x in s if x != 0)
    d8_by_k[k].append((s, (r[3], r[7])))

print("D8 case analysis:", flush=True)
for k in sorted(d8_by_k):
    sigs = set(s for s, c in d8_by_k[k])
    # completions per signature
    comp = defaultdict(set)
    for s, c in d8_by_k[k]:
        comp[s].add(c)
    sizes = set(len(v) for v in comp.values())
    nroots = len(d8_by_k[k])
    print(f"  k={k}: {len(sigs)} signatures, fiber sizes {sizes}, "
          f"{nroots} roots", flush=True)
    # Verify counts: k=2 -> C(6,2)*4=60 sigs; k=1 -> 6*2=12; k=0 -> 1
    expected = {2: 60, 1: 12, 0: 1}[k]
    assert len(sigs) == expected, f"k={k}: {len(sigs)} != {expected}"
    assert sizes == {1} if k == 2 else sizes == {4}, f"k={k} sizes {sizes}"

# --- Spinor case analysis ---
# Every spinor 6-signature (±1^6) has exactly 2 completions (parity).
spin_comp = defaultdict(set)
for r in SPIN:
    s = sig6(r)
    spin_comp[s].add((r[3], r[7]))
sizes = set(len(v) for v in spin_comp.values())
print(f"\nSpinor: {len(spin_comp)} signatures, fiber sizes {sizes}", flush=True)
assert len(spin_comp) == 64, f"{len(spin_comp)} != 64"
assert sizes == {2}, f"spinor sizes {sizes}"
# Verify parity mechanism: completions determined by # of minuses
for s, comps in list(spin_comp.items())[:3]:
    m = sum(1 for x in s if x < 0)
    print(f"  sig minuses={m}: completions {sorted(comps)}", flush=True)

# --- Overlap check: do D8 and spinor share any 6-signature? ---
d8_sigs = set(sig6(r) for r in D8)
spin_sigs = set(sig6(r) for r in SPIN)
overlap = d8_sigs & spin_sigs
print(f"\nD8/spinor signature overlap: {len(overlap)} (expect 0)", flush=True)
assert len(overlap) == 0

# --- Total ---
total_sigs = len(d8_sigs) + len(spin_sigs)
total_roots = 112 + 128
print(f"\nTotal signatures: {total_sigs} (expect 137)", flush=True)
print(f"Total roots: {total_roots} (expect 240)", flush=True)
assert total_sigs == 137 and total_roots == 240

print("\n" + "="*55)
print("THEOREM PROVED:")
print("  60 singletons: all D8 (k=2, both +-2 in signature)")
print("  64 doubles:    all spinor (parity forces exactly 2)")
print("  13 quads:      all D8 (k=1: twelve, k=0: origin)")
print("  60 + 64 + 13 = 137. 60 + 128 + 52 = 240.")
print("="*55)
