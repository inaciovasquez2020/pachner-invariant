# Pachner ThetaZ v1 Release Notes

Status: Stable.

Included in this release:

- ThetaZ sharp-criterion route closed.
- Post-closure frontier documented.
- 188 tests passing.
- lake build passing.

Closed criterion:

thetaZ (pachner23 T a b c p q) lam < thetaZ T lam
iff
vertexDeg T p + vertexDeg T q <= 10

Open frontier:

docs/math/GENERAL_DESCENT_BEYOND_THETAZ.md
