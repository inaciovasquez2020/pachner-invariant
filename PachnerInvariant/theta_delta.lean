import PachnerInvariant.frontier

namespace PachnerInvariant

-- Conditional: ΔΘ expansion placeholder

axiom theta_pachner23_delta :
  ∀ (T : Triangulation) (a b c p q : Nat) (λ : Nat),
    Θ (pachner23 T a b c p q) λ
    =
    Θ T λ
    +
    ΔΘ_local T a b c p q λ

end PachnerInvariant
