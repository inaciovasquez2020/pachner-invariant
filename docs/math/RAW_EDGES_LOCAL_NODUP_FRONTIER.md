# RawEdges local no-duplicate frontier

Status: PARTIAL THEOREM-LEVEL PROGRESS.

Closed lower-module theorem:

```lean
theorem normalizeEdge_eq_iff
    (a b c d : Vert) :
    normalizeEdge (a,b) = normalizeEdge (c,d) ↔
      (a = c ∧ b = d) ∨ (a = d ∧ b = c)
This theorem now lives in:
PachnerInvariant/NormalizeEdgeNoCollision.lean
Remaining theorem-level obligation:
theorem tetToEdges_normalized_no_collision
    {a b c d : Vert}
    (hpair :
      a ≠ b ∧ a ≠ c ∧ a ≠ d ∧
      b ≠ c ∧ b ≠ d ∧
      c ≠ d) :
    let t : Vert × Vert × Vert × Vert := (a,b,c,d)
    let es := (tetToEdges t).map normalizeEdge
    List.Pairwise (· ≠ ·) es
After this lower theorem is proved, rebuild RawEdgesLocalNodup.
No multiplicity-count closure is claimed yet.
