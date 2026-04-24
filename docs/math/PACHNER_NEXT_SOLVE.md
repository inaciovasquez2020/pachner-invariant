# PachnerInvariant next solve
Status: OPEN.
Closed objects:
`normalizeEdge_eq_iff` and `tetToEdges_normalized_no_collision` now build in PachnerInvariant/NormalizeEdgeNoCollision.lean without importing frontier.
Weakest sufficient next object:
Prove the local count-to-any bridge for a single well-formed tetrahedron.
Target theorem shape:
theorem tet_normalized_count_eq_boolToNat_any
    (t : Vert × Vert × Vert × Vert)
    (ht : pairwiseDistinctTet t)
    (e : Vert × Vert) :
    ((tetToEdges t).map normalizeEdge).count (normalizeEdge e) =
      Bool.toNat ((tetToEdges t).any (edgeEq (normalizeEdge e)))
Boundary:
No multiplicity-count closure is claimed.
