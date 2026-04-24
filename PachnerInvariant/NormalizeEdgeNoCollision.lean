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

end PachnerInvariant
