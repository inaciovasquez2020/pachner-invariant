PachnerInvariant next solve
Status: OPEN.
Weakest sufficient next object:
Prove `normalizeEdge_eq_iff` in PachnerInvariant/NormalizeEdgeNoCollision.lean without importing frontier.
Current lower-module closed lemma:
theorem normalizeEdge_idem (e : Vert × Vert) :
    normalizeEdge (normalizeEdge e) = normalizeEdge e
After normalizeEdge_eq_iff builds in the lower module, move tetToEdges_normalized_no_collision below frontier, then rebuild RawEdgesLocalNodup.
Boundary:
No multiplicity-count closure is claimed.
