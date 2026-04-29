# Pachner 2→3 Local thetaZ Descent Closed

Status: THEOREM-SURFACE CLOSED.

Final Lean theorem:

```lean
theorem thetaZ_pachner23_lt_of_valid23_vertex_sum
    {T : Triangulation} {a b c p q : Vert} {lam : Int}
    (h : frontier.Valid23 T a b c p q)
    (hlam : 0 < lam)
    (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
    thetaZ (pachner23 T a b c p q) lam < thetaZ T lam
Closed dependencies:
Valid23 carries WellFormedTets T
Valid23.wellFormedTets
Valid23RawReady
Valid23WF
raw-edge count bridge
edge-degree delta bridge
expected edge-degree bridge
theta delta bridge
thetaZ delta bridge
Boundary:
This closes the local 2→3 thetaZ descent theorem under the sharp vertex-sum hypothesis.
It does not assert unconditional global Pachner-loop monotonicity.
