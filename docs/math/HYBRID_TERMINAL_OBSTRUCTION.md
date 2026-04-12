# Hybrid Terminal Obstruction

## Firewall-normalized local target

```lean
theorem tetToEdges_normalized_no_collision_pairwiseDistinct4 :
  ∀ (v1 v2 v3 v4 : Vert),
  pairwiseDistinct4 v1 v2 v3 v4 →
  let es := (tetToEdges (v1, v2, v3, v4)).map normalizeEdge
  Pairwise (· ≠ ·) es
Backtrack certificate
Without tetToEdges_normalized_no_collision_pairwiseDistinct4, the current proof route to
allEdges_count_eq_edgeDeg_countP
is not secured.
Hybrid frontier
The weakest sufficient hybrid frontier is:
tetToEdges_normalized_no_collision_pairwiseDistinct4
allEdges_pachner23_count_delta
vertDeg_pachner23_eq_expected
These imply the remaining downstream bridge/theta layer under the current dependency plan.
