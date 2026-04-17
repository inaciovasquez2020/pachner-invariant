# General Descent Theorem

Status: Conditional.

Exact conditional criterion (integer-expanded form):

For lam > 0,

theta decreases under a Valid23 move iff

vertexDeg T p + vertexDeg T q <= 10.

Equivalent sharp formula:

ΔΘ = 2 * lam * (vertexDeg T p + vertexDeg T q - 11)

Hence:

- if sum <= 10, strict descent
- if sum = 11, neutral
- if sum >= 12, increase

This supersedes separate bounds:
vertexDeg T p <= 5 and vertexDeg T q <= 5.

No unconditional global descent is claimed.
