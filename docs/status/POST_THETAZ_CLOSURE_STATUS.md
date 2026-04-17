# Post ThetaZ Closure Status

Status: Current.

Repository surface after PR #19:

- 186 tests passed.
- lake build passed.
- ThetaZ sharp-criterion route closed.
- No remaining `sorry` placeholders in `PachnerInvariant/`.

Closed theorem surface:

thetaZ (pachner23 T a b c p q) lam < thetaZ T lam
iff
vertexDeg T p + vertexDeg T q <= 10

Interpretation:

- Exact conditional descent criterion established.
- Universal unconditional descent is not implied.
- Remaining frontier is any stronger unconditional structural theorem.

Current single frontier:

GENERAL_DESCENT_BEYOND_THETAZ.md
