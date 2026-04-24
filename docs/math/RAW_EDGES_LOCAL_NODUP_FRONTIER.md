# RawEdges local no-duplicate theorem

Status: THEOREM-LEVEL LOCAL NODUP CLOSED.

Closed lower-module theorem:

```lean
theorem tetToEdges_normalized_no_collision
    {a b c d : Vert}
    (hpair :
      a ≠ b ∧ a ≠ c ∧ a ≠ d ∧
      b ≠ c ∧ b ≠ d ∧
      c ≠ d) :
    let t : Vert × Vert × Vert × Vert := (a,b,c,d)
    let es := (tetToEdges t).map normalizeEdge
    List.Pairwise (· ≠ ·) es
Closed adapter theorem:
theorem pairwiseDistinctTet_normalized_edges_pairwise
    (t : Vert × Vert × Vert × Vert)
    (h : pairwiseDistinctTet t) :
    List.Pairwise (· ≠ ·) ((tetToEdges t).map normalizeEdge)
Both build without importing frontier.
Remaining theorem-level obligation:
(rawEdges T).count (normalizeEdge e) =
  T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
under WellFormedTets T, or an equivalent local count-to-any bridge.
Both build without importing `frontier`.

No multiplicity-count closure is claimed yet.
