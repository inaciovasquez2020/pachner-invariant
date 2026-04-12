# Next Proof Target

## Selected theorem

```lean
theorem tetToEdges_count_normalizeEdge_le_one :
  ∀ (t : Tet) (e : Vert × Vert),
  List.count (normalizeEdge e) ((tetToEdges t).map normalizeEdge) ≤ 1
Backtrack role
This is subproblem (A1) for allEdges_count_eq_edgeDeg_countP.
Immediate closure objective
Replace the current count-bridge blockage by proving the single-tetrahedron uniqueness bound first.
