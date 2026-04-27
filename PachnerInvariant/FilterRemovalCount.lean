import Mathlib

namespace PachnerInvariant

theorem filter_removal_count_delta {α : Type u} [DecidableEq α]
    (xs : List α) (x : α) (h : x ∈ xs) :
    (xs.erase x).length + 1 = xs.length := by
  induction xs with
  | nil =>
      cases h
  | cons y ys ih =>
      by_cases hy : y = x
      · subst y
        simp [List.erase]
      · have hxys : x ∈ ys := by
          cases h with
          | head =>
              contradiction
          | tail _ htail =>
              exact htail
        have hxy : x ≠ y := by
          intro h'
          exact hy h'.symm
        have hih := ih hxys
        simp [List.erase, hxy, hih]

theorem erase_length_strictly_smaller {α : Type u} [DecidableEq α]
    (xs : List α) (x : α) (h : x ∈ xs) :
    (xs.erase x).length < xs.length := by
  have hlen := filter_removal_count_delta xs x h
  omega

end PachnerInvariant
