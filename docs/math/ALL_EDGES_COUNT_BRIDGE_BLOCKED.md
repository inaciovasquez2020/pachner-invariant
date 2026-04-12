# allEdges_count_eq_edgeDeg_countP blocked

## Reason
Current compiled definition:
```lean
def allEdges (T : Triangulation) : List (Vert × Vert) :=
  (T.tets.flatMap tetToEdges |>.map normalizeEdge).eraseDups
Therefore List.count (normalizeEdge e) (allEdges T) is a 0/1 presence count,
not an incidence count across tetrahedra.
Replacement theorem target
theorem edgeMem_allEdges_iff_edgeDeg_pos
    (T : Triangulation) (e : Vert × Vert) :
    ((allEdges T).contains (normalizeEdge e) = true) ↔
      0 < edgeDeg T (normalizeEdge e)
