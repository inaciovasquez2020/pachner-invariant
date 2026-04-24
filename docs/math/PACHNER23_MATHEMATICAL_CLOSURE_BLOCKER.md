# Pachner 2-3 Mathematical Closure Blocker

Status: Open.

The attempted mathematical closure is blocked by an invalid bridge.

False bridge:

```lean
theorem allEdges_count_eq_edgeDeg_countP
Reason:
def allEdges (T : Triangulation) : List (Vert × Vert) :=
  (T.tets.flatMap tetToEdges |>.map normalizeEdge).eraseDups
Therefore (allEdges T).count e ≤ 1, while:
def edgeDeg (T : Triangulation) (e : Vert × Vert) : Nat :=
  T.tets.countP (fun t => (tetToEdges t).any (edgeEq e))
can be greater than 1.
Valid replacement surface already exists:
theorem rawEdges_count_eq_edgeDeg_countP
Full mathematical closure requires replacing the edge-degree delta proof so that it uses rawEdges, not allEdges.
