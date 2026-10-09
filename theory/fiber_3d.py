#!/usr/bin/env python3
# FIBER DIRECTIONALS — direct E8->3D projection, find the 12x20 split.
# Try A3 subsystems: project 240 roots onto A3 span, bin by 12 roots.
import math, random, itertools
print("FIBER DIRECTIONALS — E8 -> 3D (A3 subsystem)")
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
def norm(a): return math.sqrt(dot(a,a))

# FCC <110> directions (12)
fcc=[]
for i in range(3):
    for j in range(i+1,3):
        for a in(-1,1):
            for b in(-1,1):
                v=[0]*3;v[i]=a;v[j]=b;fcc.append(tuple(v))

# Find A3 subsystems in E8: three simple roots with A3 Cartan matrix.
# A3: nodes 1-2-3, angles 120 between adjacent, 90 otherwise.
# Simpler: find 3 mutually orthogonal roots? That gives A1^3, not A3.
# For A3, need roots r1,r2,r3 with (r1.r2)=(r2.r3)=-1, (r1.r3)=0.
def find_A3():
    # Use integer roots (112 of them)
    int_roots=[r for r in roots if all(abs(x)==1 or abs(x)==0 for x in r)]
    for i,r1 in enumerate(int_roots):
        for r2 in int_roots[i+1:]:
            if dot(r1,r2)!=-1: continue
            for r3 in int_roots:
                if r3==r1 or r3==r2: continue
                if dot(r2,r3)==-1 and dot(r1,r3)==0:
                    # Check r3 not in span issues; return basis
                    return [r1,r2,r3]
    return None

A3=find_A3()
print(f"A3 simple roots found: {A3 is not None}")
if A3:
    # Orthonormalize to get 3D projection basis
    # Gram-Schmidt
    def gs(vecs):
        out=[]
        for v in vecs:
            w=list(v)
            for u in out:
                d=dot(w,u)/dot(u,u)
                w=[x-d*y for x,y in zip(w,u)]
            n=norm(w)
            if n>1e-9: out.append([x/n for x in w])
        return out
    basis=gs(A3)
    print(f"Orthonormal basis dim: {len(basis)}")
    # Project all 240 roots onto this 3D subspace
    def proj(r):
        return tuple(dot(r,b) for b in basis)
    # The 12 A3 roots in this 3D projection (for binning reference)
    # A3 roots: all integer combinations. Instead, bin projected E8 roots
    # by nearest FCC <110> after aligning.
    # Actually: the projected E8 roots live in 3D. Find their directional clusters.
    projs=[proj(r) for r in roots]
    # Bin by nearest FCC direction (after optimal rotation? skip, try direct)
    # First: check if projected roots align with <110> at all.
    # Compute angle to nearest <110> for each.
    def angle_to_fcc(p):
        pn=norm(p)
        if pn<1e-9: return None
        best=min(dot(p,f)/(pn*norm(f)) for f in fcc)
        return math.acos(max(-1,min(1,best)))*180/math.pi
    angs=[angle_to_fcc(p) for p in projs]
    angs=[a for a in angs if a is not None]
    print(f"\nProjected roots: {len(projs)}, nonzero: {len(angs)}")
    print(f"Mean angle to nearest <110>: {sum(angs)/len(angs):.1f} deg")
    # Bin
    bins=[0]*12
    for p in projs:
        pn=norm(p)
        if pn<1e-9: continue
        bi=max(range(12), key=lambda i: dot(p,fcc[i])/(pn*norm(fcc[i])))
        bins[bi]+=1
    bins_sorted=sorted(bins)
    print(f"Bin distribution: {bins_sorted}")
    print(f"Mean: {sum(bins)/12:.1f}, target 20.0")
    spread=max(bins)-min(bins)
    print(f"Spread: {spread} (was 36 in H4 slice)")

print("\n"+"="*60)
