# Next Proof Target

## Selected theorem

```lean
theorem tetToEdges_normalized_no_collision_pairwiseDistinct4 :
  ∀ (v1 v2 v3 v4 : Vert),
  pairwiseDistinct4 v1 v2 v3 v4 →
  let es := (tetToEdges (v1, v2, v3, v4)).map normalizeEdge
  Pairwise (· ≠ ·) es
Status
This is the current terminal obstruction for the active hybrid route.
