# RawEdges local count-to-any theorem
Status: THEOREM-LEVEL LOCAL COUNT-TO-ANY CLOSED.
Closed theorem:
theorem tet_normalized_count_eq_boolToNat_any
    (t : Vert × Vert × Vert × Vert)
    (ht : pairwiseDistinctTet t)
    (e : Vert × Vert) :
    ((tetToEdges t).map normalizeEdge).count (normalizeEdge e) =
      Bool.toNat ((tetToEdges t).any (edgeEq (normalizeEdge e)))
This theorem builds below frontier.
Remaining theorem-level obligation:
theorem rawEdges_count_eq_edgeDeg_countP
    (T : Triangulation)
    (hT : WellFormedTets T)
    (e : Vert × Vert) :
    (rawEdges T).count (normalizeEdge e) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
No global multiplicity-count closure is claimed yet.
