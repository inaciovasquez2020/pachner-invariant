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

theorem erase_length_ne_length {α : Type u} [DecidableEq α]
    (xs : List α) (x : α) (h : x ∈ xs) :
    (xs.erase x).length ≠ xs.length := by
  have hlt := erase_length_strictly_smaller xs x h
  omega

theorem erase_ne_self_of_mem {α : Type u} [DecidableEq α]
    (xs : List α) (x : α) (h : x ∈ xs) :
    xs.erase x ≠ xs := by
  intro hxs
  have hlen : (xs.erase x).length = xs.length := by
    exact congrArg List.length hxs
  exact erase_length_ne_length xs x h hlen

theorem erase_eq_self_iff_not_mem {α : Type u} [DecidableEq α]
    (xs : List α) (x : α) :
    xs.erase x = xs ↔ x ∉ xs := by
  constructor
  · intro h hx
    exact erase_ne_self_of_mem xs x hx h
  · intro hx
    exact List.erase_of_not_mem hx

end PachnerInvariant
