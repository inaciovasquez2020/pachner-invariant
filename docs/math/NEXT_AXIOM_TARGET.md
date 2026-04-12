# Next Axiom Target

## Selected target

`allEdges_count_eq_edgeDeg_countP`

## Reason

This is the count-bridge converting `allEdges` multiplicity into `countP` over tetrahedra.

## Exact statement

```lean
axiom allEdges_count_eq_edgeDeg_countP
    (T : Triangulation) (e : Vert × Vert) :
    List.count (normalizeEdge e) (allEdges T) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
Immediate closure objective
Replace allEdges_count_eq_edgeDeg_countP by a proved theorem with the identical statement.
