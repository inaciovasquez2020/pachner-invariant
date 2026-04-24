# RawEdges theorem implementation status

Status: CONDITIONAL.

Implemented objects:

```lean
def rawEdges (T : Triangulation) : List (Vert × Vert)
def pairwiseDistinctTet (t : Vert × Vert × Vert × Vert) : Prop
def WellFormedTets (T : Triangulation) : Prop
theorem rawEdges_def
theorem allEdges_eq_rawEdges_eraseDups
The unconditional theorem
(rawEdges T).count (normalizeEdge e) =
  T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
requires `WellFormedTets T` or an equivalent local no-duplicate theorem for normalized tetrahedral edges.
The old allEdges bridge remains invalid because allEdges = rawEdges.eraseDups.
No theorem-level multiplicity-count closure is claimed in this file.
