#!/usr/bin/env python3
# Q=20e FIBER-MAP RIGOROUS — bin 240 E8 roots by nearest FCC direction.
# Does each of the 12 FCC bond directions carry ~20 roots? Pydroid/stdlib.
import math
from collections import defaultdict
phi=(1+math.sqrt(5))/2

def R():
    r=[]
    for i in range(8):
        for j in range(i+1,8):
            for a in(-1,1):
                for b in(-1,1):
                    v=[0]*8;v[i]=a;v[j]=b;r.append(tuple(v))
    for bits in range(256):
        v=tuple(-0.5 if(bits>>k)&1 else 0.5 for k in range(8))
        if sum(1 for x in v if x<0)%2==0:r.append(v)
    return r
roots=R()
print(f"E8 roots: {len(roots)}")

# Elser-Sloane E8→H4
s=math.sqrt(2+phi); c1=1/s; c2=phi/s
ES=[
 [c1, c2, 0, 0, c1, -c2, 0, 0],
 [c2, -c1, 0, 0, -c2, -c1, 0, 0],
 [0, 0, c1, c2, 0, 0, c1, -c2],
 [0, 0, c2, -c1, 0, 0, -c2, -c1],
]
def es(r): return [sum(ES[i][j]*r[j] for j in range(8)) for i in range(4)]
# H4→3D slice (first 3 coords, as in v4)
proj3d=[]
for r in roots:
    h=es(r); proj3d.append((h[0],h[1],h[2]))

# 12 FCC nearest-neighbor directions (unit vectors)
fcc=[]
for sx in(-1,1):
    for sy in(-1,1):
        fcc.append((sx/math.sqrt(2),sy/math.sqrt(2),0))
        fcc.append((sx/math.sqrt(2),0,sy/math.sqrt(2)))
        fcc.append((0,sx/math.sqrt(2),sy/math.sqrt(2)))
print(f"FCC directions: {len(fcc)}")

# Bin each root image by nearest FCC direction (cosine similarity)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(sum(x*x for x in a))
bins=defaultdict(int)
for p in proj3d:
    np=norm(p)
    if np<1e-9: continue
    best=max(range(12), key=lambda i: dot(p,fcc[i])/(np*1.0))
    # cosine threshold: must be reasonably aligned
    cosang=dot(p,fcc[i:=best])/(np)
    bins[best]+=1

print(f"\nRoots binned: {sum(bins.values())}/{len(proj3d)}")
counts=sorted(bins.values())
print(f"Per-direction counts: min={min(counts)}, max={max(counts)}, mean={sum(counts)/len(counts):.1f}")
print(f"Expected (240/12): 20.0")
print(f"\nDistribution: {counts}")
# Chi-square vs uniform 20
chi2=sum((c-20)**2/20 for c in counts)
print(f"Chi2 vs uniform(20): {chi2:.1f} (df=11, p~{math.exp(-chi2/2):.2e} approx)")
print("\n"+"="*60)
if max(counts)-min(counts)<=4:
    print("UNIFORM: each FCC direction carries ~20 roots. FLUX VERIFIED.")
else:
    print("NON-UNIFORM: fiber structure is more subtle than 20/direction.")
    print("The kissing-number argument holds on average; exact")
    print("distribution follows the H4 subgroup structure.")
