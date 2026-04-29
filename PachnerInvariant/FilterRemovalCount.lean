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

theorem erase_ne_self_iff_mem {α : Type u} [DecidableEq α]
    (xs : List α) (x : α) :
    xs.erase x ≠ xs ↔ x ∈ xs := by
  constructor
  · intro h
    by_contra hx
    exact h ((erase_eq_self_iff_not_mem xs x).mpr hx)
  · intro hx
    exact erase_ne_self_of_mem xs x hx

theorem countP_filter_not_add_countP_filter {α : Type u}
    (xs : List α) (p q : α → Bool) :
    (xs.filter (fun x => !q x)).countP p + (xs.filter q).countP p =
      xs.countP p := by
  induction xs with
  | nil =>
      simp
  | cons x xs ih =>
      cases hq : q x <;> cases hp : p x <;>
        simp [List.filter, hq, hp, ih, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm]


theorem countP_filter_not_eq_countP_sub_countP_filter {α : Type u}
    (xs : List α) (p q : α → Bool) :
    (xs.filter (fun x => !q x)).countP p =
      xs.countP p - (xs.filter q).countP p := by
  have h := countP_filter_not_add_countP_filter (xs := xs) (p := p) (q := q)
  rw [← h]
  exact (Nat.add_sub_cancel_right
    ((xs.filter (fun x => !q x)).countP p)
    ((xs.filter q).countP p)).symm


theorem countP_filter_not_add_of_filter_countP_eq {α : Type u}
    (xs : List α) (p q : α → Bool) (removed : Nat)
    (hremoved : (xs.filter q).countP p = removed) :
    (xs.filter (fun x => !q x)).countP p + removed =
      xs.countP p := by
  rw [← hremoved]
  exact countP_filter_not_add_countP_filter (xs := xs) (p := p) (q := q)


variable [DecidableEq Edge]

lemma edgesOfTet_count_eq_boole
    (T : Tetrahedron) (e : Edge)
    (hnd : (edgesOfTet T).Nodup) :
    (edgesOfTet T).count e = if e ∈ edgesOfTet T then 1 else 0 := by
  by_cases h : e ∈ edgesOfTet T
  · rw [if_pos h]
    exact hnd.count_eq_one h
  · rw [if_neg h]
    exact List.count_eq_zero.mpr h

theorem allEdges_count_eq_filter_tets_length
    (hnd : ∀ T : Tetrahedron, (edgesOfTet T).Nodup)
    (tets : List Tetrahedron) (e : Edge) :
    (allEdges tets).count e =
      (tets.filter (fun T => e ∈ edgesOfTet T)).length := by
  induction tets with
  | nil =>
      simp [allEdges]
  | cons T ts ih =>
      simp only [allEdges, List.bind_cons, List.count_append, List.filter_cons, ih]
      rw [edgesOfTet_count_eq_boole T e (hnd T)]
      split_ifs <;> simp


end PachnerInvariant
