#!/usr/bin/env python3
# FIBER EXACT — assign each E8 root to nearest of 12 A3 roots (8D inner product).
import math, itertools
print("FIBER EXACT — 8D nearest-A3-root assignment")
print("="*60)

def E8_roots():
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
roots=E8_roots()
def dot(a,b): return sum(x*y for x,y in zip(a,b))

# A3 subsystem: find 12 roots forming D3/A3.
# A3 simple roots r1,r2,r3. The 12 roots are +/- combos.
# Find via: take three roots with right inner products, generate the 12.
int_roots=[r for r in roots if all(abs(x)==1 or abs(x)==0 for x in r)]
# Find A3 simple system
found=None
for r1 in int_roots:
    for r2 in int_roots:
        if dot(r1,r2)!=-1: continue
        for r3 in int_roots:
            if dot(r2,r3)==-1 and dot(r1,r3)==0 and dot(r1,r2)==-1:
                # Generate A3 root system from simple roots
                # Positive roots: r1, r2, r3, r1+r2, r2+r3, r1+r2+r3
                def add(a,b): return tuple(x+y for x,y in zip(a,b))
                pos=[r1,r2,r3,add(r1,r2),add(r2,r3),add(r1,add(r2,r3))]
                # Check they're all E8 roots
                if all(p in roots for p in pos):
                    neg=[tuple(-x for x in p) for p in pos]
                    found=pos+neg
                    break
        if found: break
    if found: break

print(f"A3 root system (12 roots): {found is not None}")
if found:
    # Assign each E8 root to nearest A3 root
    bins=[0]*12
    for alpha in roots:
        # inner products with the 12 A3 roots
        ips=[dot(alpha,beta) for beta in found]
        bi=max(range(12), key=lambda i: ips[i])
        bins[bi]+=1
    bins_sorted=sorted(bins)
    print(f"Fiber sizes: {bins_sorted}")
    print(f"Sum: {sum(bins)}, target 240")
    print(f"Mean: {sum(bins)/12:.2f}, target 20.0")
    if bins_sorted==[20]*12:
        print("\nEXACT 12x20! Q=20e DERIVED from E8 root geometry.")
    else:
        # Check the structure: are they paired?
        print(f"\nNot exact. Distribution: {bins_sorted}")
        # Maybe it's 12 pairs? Or a different grouping?
print("="*60)
