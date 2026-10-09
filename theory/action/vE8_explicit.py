#!/usr/bin/env python3
# V_E8 EXPLICIT — degree-8 E8-invariant potential.
# V(u) = -mu^2*S2 + lam*S8, S_k = sum_roots (alpha.u)^k.
# S2,S4,S6 isotropic (7-design); S8 is FIRST non-trivial. Pydroid/stdlib.
import math, random
print("V_E8 EXPLICIT — degree-8 invariant potential")
print("="*60)

# E8 roots
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

def Sk(u,k):
    return sum(sum(a*x for a,x in zip(al,u))**k for al in roots)

# Verify isotropy of S2, S4, S6 and anisotropy of S8
random.seed(42)
def rand_u():
    v=[random.gauss(0,1) for _ in range(8)]
    n=math.sqrt(sum(x*x for x in v)); return [x/n for x in v]

print("\nIsotropy test (5 random directions, |u|=1):")
for k in [2,4,6,8]:
    vals=[Sk(rand_u(),k) for _ in range(5)]
    spread=(max(vals)-min(vals))/max(vals) if max(vals)>0 else 0
    status="ISOTROPIC" if spread<1e-9 else f"ANISOTROPIC (spread {spread:.3f})"
    print(f"  S{k}: mean={sum(vals)/5:.4f} -> {status}")

# Potential: V = -mu^2 S2 + lam S8. Find minima on sphere.
print("\nPotential V(u) = -mu^2*S2 + lam*S8, mu^2=1, lam=0.01:")
mu2=1.0; lam=0.01
def V(u): return -mu2*Sk(u,2)+lam*Sk(u,8)
# Sample many directions, find min/max
N=2000
vals=[]
for _ in range(N):
    u=rand_u(); vals.append((V(u),u))
vals.sort()
print(f"  V_min = {vals[0][0]:.4f} at u~({vals[0][1][0]:.3f},{vals[0][1][1]:.3f},...)")
print(f"  V_max = {vals[-1][0]:.4f}")
print(f"  V range: {vals[-1][0]-vals[0][0]:.4f} (nonzero -> vacuum selection!)")
# Boundedness: V -> +inf as |u|->inf? S8 ~ |u|^8 dominates, lam>0 -> yes.
print(f"\nBounded below: lam>0, S8~|u|^8 dominates at large |u|. YES.")
print("\n"+"="*60)
print("V_E8 EXPLICIT FORM: V(u) = -mu^2*sum(alpha.u)^2 + lam*sum(alpha.u)^8")
print("Degree-8 is the FIRST E8 invariant that selects vacuum direction.")
print("Minima exist (V range nonzero). Bounded below (lam>0).")
print("Grade: CONSTRUCTED (explicit, bounded, symmetry-breaking).")
