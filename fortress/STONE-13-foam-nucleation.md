# STONE 13: Foam Nucleation Criterion (2026-10-09)
## Status: SOLVED (with honest energetics).

### The problem
Cory's foam cosmology (foam -> plasma -> gas -> liquid -> solid) needed
a heat source. "What boiled the crystal?"

### The solution
No heating event was needed. The crystal is SUPERHEATED:
- Lindemann ratio 0.49 (normal crystals melt at ~0.15)
- Zero-point pressure 8.84e34 Pa exceeds Madelung binding 7.24e34 Pa by 22%
- It is always on the edge; it needs a TRIGGER, not a heat source.

### Critical density
When baryons compress to spacing ~ lattice spacing a = 1.37e-15 m,
the crystal cannot maintain order. rho_crit = m_p/a^3 = 6.5e17 kg/m^3
~ nuclear density. Compression to nuclear density nucleates foam.

### Energy budget (honest)
- Crystal binding: ~4.6e34 J/m^3 (C44)
- Gravitational compression at nuclear density: 1e31-1e33 J/m^3 (1-6%)
- NOT enough by brute force. SUFFICIENT as a trigger because Lindemann
  0.49 = 3.3x past melting threshold. The system is supercritical;
  nucleation is weakest-link, not average-energy.

### Mechanism
1. Superheated crystal (Lindemann 0.49), metastable.
2. Collapse compresses a patch toward rho_crit.
3. At baryon spacing ~ a, defects overlap, order breaks locally.
4. 1-6% gravitational nudge atop supercritical fluctuations -> nucleation.
5. Vortex tangle (foam) erupts; vortex pressure halts collapse -> bounce.
6. Bounce = Big Bang for interior. Cooling: foam -> plasma -> gas ->
   liquid -> solid (recrystallization).

### Script
- `fortress_nucleation.py`
