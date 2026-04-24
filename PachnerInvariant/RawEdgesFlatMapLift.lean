import PachnerInvariant.RawEdgesLocalNodup

namespace PachnerInvariant

private theorem rawEdges_count_eq_edgeDeg_countP_aux
    (xs : List (Vert × Vert × Vert × Vert))
    (hxs : ∀ t ∈ xs, pairwiseDistinctTet t)
    (e : Vert × Vert) :
    ((xs.flatMap tetToEdges).map normalizeEdge).count (normalizeEdge e) =
      xs.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
  induction xs with
  | nil =>
      simp
  | cons t ts ih =>
      have ht : pairwiseDistinctTet t := by
        exact hxs t (by simp)
      have hts : ∀ u ∈ ts, pairwiseDistinctTet u := by
        intro u hu
        exact hxs u (by simp [hu])
      have hlocal := tet_normalized_count_eq_boolToNat_any t ht e
      have hih := ih hts
      simp only [List.flatMap_cons, List.map_append, List.count_append]
      rw [hlocal, hih]
      by_cases hb : (tetToEdges t).any (edgeEq (normalizeEdge e)) = true
      · simp [List.countP_cons, hb, Nat.add_comm]
      · have hfalse : (tetToEdges t).any (edgeEq (normalizeEdge e)) = false := by
          exact Bool.eq_false_iff.mpr hb
        simp [List.countP_cons, hfalse]

theorem rawEdges_count_eq_edgeDeg_countP
    (T : Triangulation)
    (hT : WellFormedTets T)
    (e : Vert × Vert) :
    (rawEdges T).count (normalizeEdge e) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
  unfold rawEdges
  exact rawEdges_count_eq_edgeDeg_countP_aux T.tets hT e

end PachnerInvariant
