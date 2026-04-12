# A1* Exact Slot Form

## Target

```lean
theorem tetToEdges_normalized_no_collision
    (t : Tet) :
    let es := (tetToEdges t).map normalizeEdge
    List.Pairwise (· ≠ ·) es
Role
This is the exact finite collision-elimination statement needed for A1*.
