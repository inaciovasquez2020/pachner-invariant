import Mathlib
import PachnerInvariant.descent_property

namespace PachnerInvariant

theorem normalizeEdge_idem (e : Vert × Vert) :
    normalizeEdge (normalizeEdge e) = normalizeEdge e := by
  rcases e with ⟨a, b⟩
  unfold normalizeEdge
  by_cases h : a ≤ b
  · simp [h]
  · have hbale : b ≤ a := Nat.le_of_not_ge h
    simp [h, hbale]

theorem normalizeEdge_eq_iff
    (a b c d : Vert) :
    normalizeEdge (a,b) = normalizeEdge (c,d) ↔
      (a = c ∧ b = d) ∨ (a = d ∧ b = c) := by
  unfold normalizeEdge
  by_cases hab : a ≤ b
  · by_cases hcd : c ≤ d
    · constructor
      · intro h
        left
        simp [hab, hcd, Prod.ext_iff] at h
        exact h
      · intro h
        rcases h with h | h
        · rcases h with ⟨hac, hbd⟩
          subst c
          subst d
          simp [hab, hcd]
        · rcases h with ⟨had, hbc⟩
          subst d
          subst c
          have hba : b ≤ a := hcd
          have hab_eq : a = b := Nat.le_antisymm hab hba
          subst b
          simp
    · constructor
      · intro h
        right
        simp [hab, hcd, Prod.ext_iff] at h
        exact h
      · intro h
        rcases h with h | h
        · rcases h with ⟨hac, hbd⟩
          subst c
          subst d
          exact False.elim (hcd hab)
        · rcases h with ⟨had, hbc⟩
          subst d
          subst c
          simp [hab, hcd]
  · by_cases hcd : c ≤ d
    · constructor
      · intro h
        right
        simp [hab, hcd, Prod.ext_iff] at h
        exact ⟨h.2, h.1⟩
      · intro h
        rcases h with h | h
        · rcases h with ⟨hac, hbd⟩
          subst c
          subst d
          exact False.elim (hab hcd)
        · rcases h with ⟨had, hbc⟩
          subst d
          subst c
          simp [hab, hcd]
    · constructor
      · intro h
        left
        simp [hab, hcd, Prod.ext_iff] at h
        exact ⟨h.2, h.1⟩
      · intro h
        rcases h with h | h
        · rcases h with ⟨hac, hbd⟩
          subst c
          subst d
          simp [hab, hcd]
        · rcases h with ⟨had, hbc⟩
          subst d
          subst c
          have hba : b ≤ a := Nat.le_of_not_ge hab
          exact False.elim (hcd hba)

end PachnerInvariant
