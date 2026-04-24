# RawEdges flatMap lift

Status: CONDITIONAL THEOREM-LEVEL GLOBAL LIFT CLOSED.

Closed theorem:

```lean
theorem rawEdges_count_eq_edgeDeg_countP
    (T : Triangulation)
    (hT : WellFormedTets T)
    (e : Vert × Vert) :
    (rawEdges T).count (normalizeEdge e) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
This is conditional on `WellFormedTets T`.
This theorem lifts the single-tetrahedron theorem:
tet_normalized_count_eq_boolToNat_any
over T.tets.
Boundary:
This does not restore the false `allEdges` multiplicity bridge.
`allEdges = rawEdges.eraseDups`, so multiplicity claims must use rawEdges.
Remaining theorem-level obligation:
Propagate WellFormedTets through the Pachner 2--3 move layer or replace the downstream delta proof with raw-edge counts explicitly.
