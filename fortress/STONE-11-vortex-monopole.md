# STONE 11: Vortex Monopole Derivation (2026-10-09)
## Status: THEOREM (corrected derivation). Supersedes vortex_derive_profile.py.

### The hole
The original derivation (vortex_derive_profile.py) integrated a CYLINDRICAL
vortex energy density eps_k(r_perp) using a SPHERICAL volume element
4*pi*r^2 dr. Geometrically inconsistent: a straight vortex line has
cylindrical symmetry, and its energy per unit length diverges logarithmically.

### The fix
Angle-average the cylindrical density to extract its monopole (l=0) component:
  <eps_k>(R) = (1/2) int_0^pi eps_cyl(R sinθ) sinθ dθ
This is SPHERICAL by construction, CONVERGENT (GP core f~r_perp regularizes
the poles), and ASYMPTOTICALLY 1/R^2:
  R^2<eps_k> -> const (0.0327, 0.0416, 0.0444 at R=10,20,25, converging).

The spherical M(<R) = int 4piR^2 <eps_k> dR is then justified as the
monopole approximation to the vortex's gravity — the leading term for
a central vortex or vortex tangle.

### Result
Rotation curve V/V_flat from <eps_k>: 0.256, 0.686, 0.855, 0.956 at
R=1,5,10,20. Fits cored isothermal r/sqrt(r^2+a^2) with max residual 0.068
(slightly larger than the 0.044 from the inconsistent method, but now
geometrically sound).

### Honest grade
The 1/R^2 isothermal profile is DERIVED (angle-averaged monopole),
not assumed. The monopole approximation (neglecting higher multipoles
of a single line) is stated explicitly. For a vortex TANGLE (many lines),
spherical symmetry is exact on average and no approximation is needed.

### Script
- `vortex_fix.py` (corrected derivation)
- Supersedes: `vortex_derive_profile.py` (keep for history, mark superseded)
