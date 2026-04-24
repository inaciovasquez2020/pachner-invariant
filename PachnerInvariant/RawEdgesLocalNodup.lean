import PachnerInvariant.RawEdgesCommon
import PachnerInvariant.NormalizeEdgeNoCollision

namespace PachnerInvariant

theorem pairwiseDistinctTet_normalized_edges_pairwise
    (t : Vert × Vert × Vert × Vert)
    (h : pairwiseDistinctTet t) :
    List.Pairwise (· ≠ ·) ((tetToEdges t).map normalizeEdge) := by
  rcases t with ⟨a, b, c, d⟩
  simpa [pairwiseDistinctTet] using
    (tetToEdges_normalized_no_collision
      (a := a) (b := b) (c := c) (d := d)
      (by simpa [pairwiseDistinctTet] using h))

end PachnerInvariant
