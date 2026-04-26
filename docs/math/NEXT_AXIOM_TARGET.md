# Next Frontier Target

## Selected target

`theta_pachner23_delta` / downstream theta-descent closure

## Reason

`allEdges_count_eq_edgeDeg_countP` is theorem-level present. The remaining target is downstream theta/descent closure using the proved count bridge.

## Exact statement

```lean
theorem allEdges_count_eq_edgeDeg_countP
    (T : Triangulation) (e : Vert × Vert) :
    List.count (normalizeEdge e) (allEdges T) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
Immediate closure objective
Do not relabel `allEdges_count_eq_edgeDeg_countP` as a live axiom; it is already theorem-level present.
