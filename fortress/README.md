# FORTRESS

Proven stones of the E8 projection theory. Each stone is either a theorem
(proved by case analysis or symbolic computation) or an honest regrade
(a claim surrendered before critics could take it).

A fortress isn't built from claims nobody can knock down. It's built from
surrendering the weak ones yourself and proving the strong ones.

## Stones

| # | Stone | Status | Date |
|---|-------|--------|------|
| 01 | [Moment regrade](STONE-01-moment-regrade.md) | REGRADED (design theory) | 2026-10-09 |
| 02 | [Thirteen quads](STONE-02-thirteen-quads.md) | THEOREM (proved) | 2026-10-09 |

## Scripts

- `fortress_moments.py` — symbolic proof that 180/180/210 are forced by the
  spherical 7-design (chi-squared structure of the projection).
- `fortress_quads.py` — combinatorial enumeration proving exactly 13 fibers
  of size 4, in 1+6+6 octahedral arrangement with exact phi ratio.

## Standard

Every stone must have:
1. A clear statement (theorem or regrade).
2. A proof (case analysis, symbolic computation, or exhaustive enumeration)
   — not just numerics.
3. The script that verifies it, runnable standalone.
4. An honest grade: THEOREM, REGRADED, or CANDIDATE.
