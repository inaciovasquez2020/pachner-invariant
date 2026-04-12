# Next Proof Target

## Selected theorem

```lean
theorem pairwiseDistinct4_normalizeEdge_injective_on_tetToEdges :
  ∀ (v1 v2 v3 v4 : Vert),
  pairwiseDistinct4 v1 v2 v3 v4 →
  let es := (tetToEdges (v1, v2, v3, v4)).map normalizeEdge
  es.Nodup
Backtrack role
This upgrades the membership characterization to the exact no-collision statement needed for the single-tetrahedron count bound.
Immediate closure objective
Prove the normalized tetrahedron edge list is duplicate-free under pairwiseDistinct4.
