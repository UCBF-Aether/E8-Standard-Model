#!/usr/bin/env python3
# TADPOLE / GAP EQUATION — g_c psibar psi u sources <u>, feeds back to m_f.
# NJL-style self-consistency: m = m0 + g_c^2 <psibar psi>/m_u^2.
# Pydroid/stdlib. Cory Brent 2026.
import math
print("TADPOLE — NJL gap equation for crystal-induced mass")
print("="*60)
print("\nMechanism:")
print("  g_c psibar psi u^I: fermion bilinear SOURCES u^I.")
print("  <u> = g_c <psibar psi> / m_u^2  (u responds to matter)")
print("  m_f = m0 + g_c <u> = m0 + g_c^2 <psibar psi>/m_u^2")
print("  <psibar psi> ~ -m_f * Lambda^2/(4pi^2)  (1-loop, cutoff Lambda)")
print("  => Gap equation: m = m0 + G * m * Lambda^2/(4pi^2)")
print("     where G = g_c^2/m_u^2 (effective 4-Fermi coupling).")
print("\nThis is the NJL model. Nontrivial solution (m != m0) exists iff")
print("  G * Lambda^2/(4pi^2) > 1  (critical coupling).")
print("\nNumerical estimate:")
# Scales: m_u from C44 (phonon mass gap?), Lambda ~ 1/a, g_c unknown.
# Use: m_u c^2 ~ sqrt(C44/rho) * hbar / a? Phonon energy at zone boundary.
C44=4.62e34; a=1.3729e-15
rho=C44/(3e8**2)  # ~ C44/c^2
c_s=math.sqrt(C44/rho)  # sound speed ~ c (by construction)
hbar=1.055e-34
# u mass gap: set by V_E8 curvature at minimum. Estimate from S8 scale.
# V ~ lam*S8, S8 ~ 30|u|^8/a^8? Curvature m_u^2 ~ lam*|u|^6...
# Instead: use phonon zone-boundary energy as characteristic.
E_zb=hbar*c_s*math.pi/a  # ~ hbar * c * pi / a
print(f"  Zone-boundary phonon: E_zb = {E_zb:.3e} J = {E_zb/1.602e-19/1e9:.1f} GeV")
# Cutoff Lambda ~ pi/a (momentum)
Lambda=math.pi/a
print(f"  Cutoff Lambda = pi/a = {Lambda:.3e} m^-1")
# Critical G_c = 4pi^2/Lambda^2
Gc=4*math.pi**2/Lambda**2
print(f"  Critical G_c = 4pi^2/Lambda^2 = {Gc:.3e} m^2")
print("\nTadpole stability:")
print("  <u>=0 is a solution (if m0=0, trivial).")
print("  Nontrivial <u> iff G > G_c (strong coupling).")
print("  g_c is OPEN (not fixed by v14) -> cannot determine if")
print("  the crystal spontaneously generates fermion mass.")
print("\n"+"="*60)
print("Grade: MECHANISM IDENTIFIED (NJL gap equation).")
print("  Tadpole does NOT destabilize <u>=0 (it's a valid vacuum).")
print("  Whether <u>!=0 (dynamical mass) depends on g_c vs critical.")
print("  OPEN: fix g_c from lattice-position calculation (v14 gap).")
