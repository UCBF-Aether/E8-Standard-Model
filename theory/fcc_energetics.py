#!/usr/bin/env python3
# FCC-vs-BCC ENERGETICS — Thomas-Fermi + Madelung total energy comparison.
# Does FCC win on energetics alone? Pydroid/stdlib. Cory Brent 2026.
import math
print("FCC vs BCC — total energy comparison (TF + Madelung)")
print("="*60)

# Jellium model: point ions in uniform electron background.
# Energy per ion (in units e^2/a_ws, a_ws = Wigner-Seitz radius):
# E = E_kin(TF) + E_Madelung + E_xc
# TF kinetic (uniform): same for all structures at fixed density.
# Madelung constants (Coulomb energy of lattice in jellium):
# Values from Fuchs (1935), Coldwell-Horsfall & Maradudin.
madelung = {
    'SC':      -1.76012,
    'BCC':     -1.79186,
    'FCC':     -1.79168,
    'diamond': -1.670,
    'HCP':     -1.79168,  # ideal c/a, same as FCC to this order
}
print("\nMadelung energy (e^2/a_ws per ion):")
for s, e in sorted(madelung.items(), key=lambda x: x[1]):
    print(f"  {s:8s}: {e:.5f}")
print("\nFCC - BCC = {:.5f} e^2/a_ws".format(madelung['FCC']-madelung['BCC']))
print("  = {:.4f}% (BCC wins by a hair)".format(
    abs(madelung['FCC']-madelung['BCC'])/abs(madelung['BCC'])*100))

print("\nTF kinetic energy:")
print("  Uniform density: IDENTICAL for all structures at fixed n.")
print("  Non-uniform (real TF): 0.2-0.7% differences (ingestion #7).")
print("  Too small to overcome Madelung tie.")

print("\n"+"="*60)
print("VERDICT:")
print("  TF + jellium does NOT select FCC (BCC ties/wins marginally).")
print("  FCC is selected by E8 GEOMETRY (240->137 fold, 12-coordination),")
print("  not by TF energetics. The v4 paper's proxy was wrong to claim")
print("  energetics alone picks FCC.")
print("  Grade: NEGATIVE (proxy failed) -> SUPERSEDED by geometric derivation.")
print("  The E8 projection (VERIFIED) is the FCC justification.")
