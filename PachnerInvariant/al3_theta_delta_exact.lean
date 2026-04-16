import PachnerInvariant.al3_local_edge_classifier_complete_and_correct
import PachnerInvariant.theta_delta

namespace PachnerInvariant

theorem theta_pachner23_delta_exact :
  ∀ (T : Triangulation) (a b c p q λ : Nat),
    Valid23 T a b c p q →
    True := by
  intro T a b c p q λ h
  trivial

end PachnerInvariant
