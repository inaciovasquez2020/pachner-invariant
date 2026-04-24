import PachnerInvariant.RawEdgesCommon
import PachnerInvariant.NormalizeEdgeNoCollision

namespace PachnerInvariant

theorem pairwiseDistinctTet_normalized_edges_pairwise
    (t : Vert × Vert × Vert × Vert)
    (h : pairwiseDistinctTet t) :
    List.Pairwise (· ≠ ·) ((tetToEdges t).map normalizeEdge) := by
  rcases t with ⟨a, b, c, d⟩
  simpa [pairwiseDistinctTet] using
    (tetToEdges_normalized_no_collision
      (a := a) (b := b) (c := c) (d := d)
      (by simpa [pairwiseDistinctTet] using h))

private theorem edge_count_eq_boolToNat_any_of_pairwise_ne
    (xs : List (Vert × Vert))
    (x : Vert × Vert)
    (hxs : List.Pairwise (· ≠ ·) xs) :
    xs.count x = Bool.toNat (xs.any (fun y => y == x)) := by
  induction xs with
  | nil =>
      simp
  | cons a xs ih =>
      cases hxs with
      | cons hhead htail =>
          by_cases hax : a = x
          · have hxnotin : x ∉ xs := by
              intro hxmem
              exact hhead x hxmem hax
            have hcount : xs.count x = 0 := by
              simpa using List.count_eq_zero_of_not_mem hxnotin
            simp [List.any_cons, hax, hcount]
          · have hbeq : (a == x) = false := by
              simpa [beq_iff_eq, hax]
            have ihxs := ih htail
            simp [List.any_cons, hax, hbeq, ihxs]

private theorem edgeEq_normalized_eq_beq
    (e d : Vert × Vert) :
    edgeEq (normalizeEdge e) d =
      (normalizeEdge d == normalizeEdge e) := by
  apply Bool.eq_iff_iff.mpr
  constructor
  · intro h
    rw [beq_iff_eq]
    have hne : normalizeEdge (normalizeEdge e) = normalizeEdge e :=
      normalizeEdge_idem e
    rw [← hne]
    rw [normalizeEdge_eq_iff]
    unfold edgeEq at h
    simp only [Bool.or_eq_true, Bool.and_eq_true, beq_iff_eq] at h
    rcases h with h | h
    · exact Or.inl ⟨h.1.symm, h.2.symm⟩
    · exact Or.inr ⟨h.2.symm, h.1.symm⟩
  · intro h
    rw [beq_iff_eq] at h
    have hne : normalizeEdge (normalizeEdge e) = normalizeEdge e :=
      normalizeEdge_idem e
    rw [← hne] at h
    rw [normalizeEdge_eq_iff] at h
    unfold edgeEq
    simp only [Bool.or_eq_true, Bool.and_eq_true, beq_iff_eq]
    rcases h with h | h
    · exact Or.inl ⟨h.1.symm, h.2.symm⟩
    · exact Or.inr ⟨h.2.symm, h.1.symm⟩

private theorem any_map_normalize_eq_edgeEq
    (xs : List (Vert × Vert))
    (e : Vert × Vert) :
    (xs.map normalizeEdge).any (fun y => y == normalizeEdge e) =
      xs.any (edgeEq (normalizeEdge e)) := by
  induction xs with
  | nil =>
      simp
  | cons d ds ih =>
      simp [List.any_cons, edgeEq_normalized_eq_beq, ih]

theorem tet_normalized_count_eq_boolToNat_any
    (t : Vert × Vert × Vert × Vert)
    (ht : pairwiseDistinctTet t)
    (e : Vert × Vert) :
    ((tetToEdges t).map normalizeEdge).count (normalizeEdge e) =
      Bool.toNat ((tetToEdges t).any (edgeEq (normalizeEdge e))) := by
  have hpair := pairwiseDistinctTet_normalized_edges_pairwise t ht
  have hcount :=
    edge_count_eq_boolToNat_any_of_pairwise_ne
      ((tetToEdges t).map normalizeEdge)
      (normalizeEdge e)
      hpair
  have hany := any_map_normalize_eq_edgeEq (tetToEdges t) e
  exact hcount.trans (congrArg Bool.toNat hany)

end PachnerInvariant
