#!/usr/bin/env python3
# g_c FROM LATTICE — fermion-crystal coupling from unit cell positions.
# Fermions sit at lattice sites; g_c ~ overlap of fermion wavefunction
# with crystal displacement field. Pydroid/stdlib. Cory Brent 2026.
import math
print("g_c FROM FCC LATTICE POSITIONS")
print("="*60)

# FCC conventional cell: 4 atoms at
# (0,0,0), (0,1/2,1/2), (1/2,0,1/2), (1/2,1/2,0) in units of a_conv.
# Fermions (qubits) at each site. The coupling g_c psibar psi u^I:
# g_c ~ (energy cost of displacing a fermion) / (displacement).
# Estimate: fermion localized at site with localization length xi_f.
# Displacing the lattice by u shifts the fermion's potential by
# dV ~ (d^2V/dx^2) * xi_f * u. So g_c ~ m_f * omega^2 * xi_f,
# where omega is the trapping frequency, m_f the fermion mass.

# But we can do better: use the NJL critical condition.
# From tadpole_gap.py: G_c = 7.54e-30 m^2, G = g_c^2/m_u^2.
# For dynamical mass: g_c^2 > G_c * m_u^2.
# m_u from V_E8 curvature. Estimate m_u c^2 ~ E_zb ~ 0.5 GeV (from gap script).
print("\nFrom NJL criticality:")
print("  G_c = 7.54e-30 m^2, m_u c^2 ~ 0.5 GeV")
m_u_eV = 0.5e9
hbar_c = 197.3  # eV*nm
m_u_inv_m = m_u_eV / hbar_c * 1e9  # convert to m^-1
print(f"  m_u = {m_u_inv_m:.3e} m^-1")
# g_c^2 > G_c * m_u^2 (in natural units where g_c has dimension of mass)
# g_c is dimensionless? [psibar psi u]: [psi]=3/2, [u]=1/2 (z=2!) -> [g_c]=?
# At z=2: [psi]=3/2? Actually fermion scaling may differ. Assume [g_c]=1 (mass).
# g_c > sqrt(G_c) * m_u
import math
g_c_min = math.sqrt(7.54e-30) * m_u_inv_m  # in m^-1, convert to eV
g_c_min_eV = g_c_min * hbar_c / 1e9
print(f"  g_c > {g_c_min_eV:.3e} eV for dynamical mass generation")

print("\nLattice estimate:")
print("  Fermion at FCC site, localization xi_f ~ a (lattice spacing).")
print("  Crystal displacement u shifts the local potential.")
print("  g_c ~ (dV/du) ~ (E_site / a), E_site ~ fermion mass scale.")
a = 1.3729e-15  # m
# For electron: E_site ~ m_e c^2 = 511 keV
m_e_eV = 511e3
g_c_e = m_e_eV / (a*1e9) * hbar_c  # rough: E/a in eV/m * ...
# Simpler: g_c ~ m_f c^2 / a (energy per displacement), in natural units
# [g_c] = mass^2? Depends on [u]. If [u]=mass (z=1), [g_c]=mass.
# At z=2, [u]=1/2, [psi]=? Let's just give the scale.
print(f"  a = {a:.3e} m")
print(f"  Electron: g_c ~ m_e c^2/a ~ {m_e_eV:.3e} eV / {a:.2e} m")
print(f"    = {m_e_eV/a:.3e} eV/m (coupling per unit displacement)")

print("\n"+"="*60)
print("Grade: SCALE ESTIMATED, not derived.")
print("  Full calculation needs: fermion wavefunction in FCC cell,")
print("  overlap integral with phonon modes, E8 position assignment.")
print("  This is a BAND STRUCTURE calculation (tight-binding).")
print("  OPEN: tight-binding g_c from FCC + E8 site assignment.")
