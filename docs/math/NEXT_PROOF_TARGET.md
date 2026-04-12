# Next Proof Target

## Selected theorem

```lean
theorem tetToEdges_normalized_has_length_six :
  ∀ (t : Tet),
  ((tetToEdges t).map normalizeEdge).length = 6
Backtrack role
This fixes the ambient finite shape before proving the single-tetrahedron uniqueness bound.
Immediate closure objective
Prove the normalized tetrahedron edge list has exactly six entries.
