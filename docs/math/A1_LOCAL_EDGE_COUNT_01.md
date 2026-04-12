# A1 Local Edge Count 0-1

## Target

For every tetrahedron `t` and edge `e`,

```lean
List.count (normalizeEdge e) (tetToEdges t) = 0 ∨
List.count (normalizeEdge e) (tetToEdges t) = 1
Role
This is substep (A1) in the proof of:
allEdges_count_eq_edgeDeg_countP.
Immediate proof obligation
Show that a normalized edge can occur in tetToEdges t at most once.
