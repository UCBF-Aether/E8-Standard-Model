# STONE 12: BTFR Logical Structure (2026-10-09)
## Status: STRUCTURED DERIVATION with labeled inputs.

### What is derived
1. **Vortex pressure deficit** (Bernoulli, from GP vortex):
   dP/dr = rho_s f(r)^2 v(r)^2 / r, v = kappa/2pir.
   Core deficit: 1.81 rho_s(kappa/2pi)^2/xi^2. Asymptotic: P -> -1/(2r^2).
   Trapping energy/length: 9.44 (vs pi*ln(30) = 10.69 analytic, f=1).
   The GP core regularizes; the 1/r^2 tail is exact.

2. **V^4 scaling** follows from three premises (dimensional):
   M_bar ~ V^2 L/G (trapping) + L ~ V^2R^2/GM (hydrostatic) + M ~ R^2
   => M_bar ~ V^4. The algebra is exact; the premises are labeled below.

### What is input (not derived)
- **Trapping law** M_bar ~ V^2 L/G: DIMENSIONAL POSTULATE. The O(1)
  coefficient and the "until when" criterion are not derived from the
  vortex equations. Plausibility: baryons fall into the pressure well
  until their energy ~ well depth; but the saturation mechanism needs
  a dynamical simulation.
- **Freeman's law** M_bar ~ R^2 (constant surface density): OBSERVED.
  Not derived from the superfluid. This is the key empirical input
  that closes the V^4.
- **Normalization** 46.1 vs 50: depends on O(1) choices (ln(R/xi)/2,
  Sigma_0, sigma/V). Tracked explicitly, not hidden.

### Honest grade
The BTFR is a SCALING SYNTHESIS, not a first-principles derivation.
What is proved: IF Bernoulli trapping AND hydrostatic equilibrium AND
constant surface density, THEN M ~ V^4 with computable normalization.
The "if" parts are labeled. A critic cannot claim circularity because
the inputs are stated; they can only dispute the inputs, which is
legitimate physics debate.

### Script
- `fortress_btfr.py` (pressure deficit + logical structure)
