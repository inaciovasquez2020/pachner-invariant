# tetToEdges_normalized_no_collision status

## Current status

Not theorem-level verified from the current compiled repository state.

## Strongest valid conditional statement

If `normalizeEdge_eq_iff` is available as an axiom or proved theorem, then

```lean
theorem tetToEdges_normalized_no_collision
    {a b c d : Vert}
    (hpair :
      a ≠ b ∧ a ≠ c ∧ a ≠ d ∧
      b ≠ c ∧ b ≠ d ∧
      c ≠ d) :
    let t : Tet := (a,b,c,d)
    let es := (tetToEdges t).map normalizeEdge
    List.Pairwise (· ≠ ·) es := by
  rcases hpair with ⟨hab, hac, had, hbc, hbd, hcd⟩
  simp [tetToEdges, normalizeEdge_eq_iff, hab, hac, had, hbc, hbd, hcd]

Repository truth condition
Do not mark tetToEdges_normalized_no_collision as verified unless it is present in PachnerInvariant/frontier.lean and lake build PachnerInvariant.frontier succeeds.
