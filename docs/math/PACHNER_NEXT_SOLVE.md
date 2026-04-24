# PachnerInvariant next solve

Status: OPEN.

Closed object:
`tet_normalized_count_eq_boolToNat_any` builds in `PachnerInvariant/RawEdgesLocalNodup.lean`.

Weakest sufficient next object:
Lift the single-tetrahedron count-to-any theorem over `T.tets`.

Target theorem shape:

```lean
theorem rawEdges_count_eq_edgeDeg_countP
    (T : Triangulation)
    (hT : WellFormedTets T)
    (e : Vert × Vert) :
    (rawEdges T).count (normalizeEdge e) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
Boundary:
No global multiplicity-count closure is claimed until the fold/flatMap lift builds.
