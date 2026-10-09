#!/usr/bin/env python3
"""
FORTRESS STONE 6 (corollary) + shell inventory investigation.
Stone 6: the 73/64 vector/spinor split is PROVED (corollary of Stone 3).
Then: enumerate the 12 shells, derive radii and populations.
"""
import numpy as np
from collections import defaultdict, Counter
import itertools

# E8 roots, integer scaled; track type
D8 = set()
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0]*8; v[i] = 2*si; v[j] = 2*sj
            D8.add(tuple(v))
SPIN = set()
for bits in itertools.product((1, -1), repeat=8):
    if sum(1 for b in bits if b < 0) % 2 == 0:
        SPIN.add(tuple(bits))

phi = (1+np.sqrt(5))/2
norm = np.sqrt(1+phi*phi)

def img(r):
    return tuple(round((r[i]+phi*r[i+4])/norm/2, 9) for i in range(3))

# Group images by source type
d8_imgs = set(img(r) for r in D8)
spin_imgs = set(img(r) for r in SPIN)
print(f"D8 images: {len(d8_imgs)}, spinor images: {len(spin_imgs)}", flush=True)
print(f"Overlap: {len(d8_imgs & spin_imgs)}", flush=True)
print(f"Total: {len(d8_imgs | spin_imgs)}", flush=True)
assert len(d8_imgs) == 73 and len(spin_imgs) == 64
assert len(d8_imgs & spin_imgs) == 0
print("STONE 6 PROVED: 73 vector + 64 spinor = 137, disjoint.", flush=True)

# --- Shell inventory ---
all_imgs = d8_imgs | spin_imgs
shells = defaultdict(list)
for p in all_imgs:
    r2 = round(sum(x*x for x in p), 9)
    shells[r2].append(p)

print(f"\nShells (by r^2): {len(shells)}", flush=True)
nonzero = {k: v for k, v in shells.items() if k > 1e-12}
print(f"Nonzero shells: {len(nonzero)}", flush=True)
for r2 in sorted(nonzero):
    pts = nonzero[r2]
    # type breakdown
    nd8 = sum(1 for p in pts if p in d8_imgs)
    nsp = sum(1 for p in pts if p in spin_imgs)
    print(f"  r={np.sqrt(r2):.4f} (r^2={r2:.4f}): {len(pts):3d} pts "
          f"[D8:{nd8:3d} spin:{nsp:3d}]", flush=True)

# Check total
tot = sum(len(v) for v in nonzero.values()) + len(shells.get(0.0, []))
print(f"\nTotal points: {tot} (expect 137)", flush=True)
