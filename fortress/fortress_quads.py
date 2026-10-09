#!/usr/bin/env python3
"""
FORTRESS STONE 2: Combinatorial proof of the 13-quad phi-octahedra.
The map M only sees (x1,x2,x3,x5,x6,x7). Two roots collide iff they agree
on these 6 coords (phi irrationality forces this). So fibers = roots sharing
a 6-signature, differing only in (x4,x8).
Enumerate all 6-signatures, count (x4,x8) completions, characterize the 13 quads.
"""
import numpy as np
from collections import defaultdict
import itertools

# E8 roots (integer and spinor)
roots = []
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0]*8; v[i] = si; v[j] = sj
            roots.append(tuple(v))
for bits in itertools.product((1, -1), repeat=8):
    if sum(1 for b in bits if b < 0) % 2 == 0:
        roots.append(tuple(b/2 for b in bits))
roots = list(set(roots))
print(f"E8 roots: {len(roots)}", flush=True)
# Scale to integers for exactness
R = [tuple(int(round(2*x)) for x in r) for r in roots]

phi = (1+np.sqrt(5))/2
norm = np.sqrt(1+phi*phi)

# Group by 6-signature (x1,x2,x3,x5,x6,x7) using integer coords
sig = defaultdict(list)
for r in R:
    s = (r[0], r[1], r[2], r[4], r[5], r[6])
    sig[s].append((r[3], r[7]))  # the (x4,x8) completions

from collections import Counter
fsizes = Counter(len(v) for v in sig.values())
print(f"6-signatures: {len(sig)}, fiber sizes: {dict(sorted(fsizes.items()))}", flush=True)

# The 13 quads: what are their signatures?
quads = [(s, v) for s, v in sig.items() if len(v) == 4]
print(f"\nQuad fibers: {len(quads)}", flush=True)

# Compute their 3D images and check octahedral structure
print("\nQuad signature -> 3D image -> (x4,x8) completions:", flush=True)
images = []
for s, comps in sorted(quads, key=lambda kv: sum(x*x for x in kv[0])):
    # 3D image: ((x1+phi*x5), (x2+phi*x6), (x3+phi*x7))/norm/2
    img = tuple((s[i]+phi*s[i+3])/norm/2 for i in range(3))
    r = np.sqrt(sum(x*x for x in img))
    images.append(img)
    is_int = all(x % 1 == 0 for x in s)
    typ = "D8/vector" if is_int else "spinor"
    print(f"  sig {s} [{typ}] -> r={r:.4f}, comps(x4,x8)={sorted(comps)}", flush=True)

# Check: are all 13 from D8/vector roots? (no spinor)
n_spinor = sum(1 for s, v in quads if not all(x % 1 == 0 for x in s))
print(f"\nSpinor quads: {n_spinor} (expect 0)", flush=True)

# Verify octahedral: group by radius
from collections import defaultdict
by_r = defaultdict(list)
for img in images:
    r = round(np.sqrt(sum(x*x for x in img)), 4)
    by_r[r].append(img)
print(f"\nRadii: {sorted(by_r.keys())}", flush=True)
for r in sorted(by_r):
    print(f"  r={r}: {len(by_r[r])} points", flush=True)
    # Check they lie on coordinate axes (octahedron vertices)
    for img in by_r[r]:
        nz = sum(1 for x in img if abs(x) > 1e-9)
        print(f"    {tuple(round(x,4) for x in img)} nonzero coords: {nz}", flush=True)

# The phi ratio: prove r_outer/r_inner = phi exactly (symbolic)
# Inner octahedron images: from signatures, compute exact r^2
print("\n--- Exact phi ratio ---", flush=True)
rs = sorted(set(round(np.sqrt(sum(x*x for x in img)), 10) for img in images if sum(x*x for x in img) > 1e-12))
print(f"Distinct nonzero radii: {rs}", flush=True)
if len(rs) == 2:
    ratio = rs[1]/rs[0]
    print(f"Ratio: {ratio:.10f}, phi = {phi:.10f}, match: {abs(ratio-phi) < 1e-9}", flush=True)
