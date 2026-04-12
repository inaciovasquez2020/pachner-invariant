# A1* Exact Slot Form

## Exact finite object to prove

Let

```lean
tetToEdges (v1, v2, v3, v4)
be the six-slot edge list of one tetrahedron.
Prove that after applying normalizeEdge to each slot, no two distinct slots are equal.
Weakest sufficient theorem
theorem tetToEdges_normalized_no_collision :
  ∀ (v1 v2 v3 v4 : Vert),
  let es := (tetToEdges (v1, v2, v3, v4)).map normalizeEdge
  Pairwise (· ≠ ·) es
Role
This is the exact finite collision-elimination statement needed for A1*.
