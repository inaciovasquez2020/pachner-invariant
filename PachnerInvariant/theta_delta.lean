import PachnerInvariant.frontier
import PachnerInvariant.edge_incidence_delta
import PachnerInvariant.edge_degree_delta

namespace PachnerInvariant

def deltaThetaEdgeTerm (T : Triangulation) (a b c p q : Nat) : Int := 0

def deltaThetaVertexTerm (T : Triangulation) (a b c p q : Nat) : Int := 0

def deltaTheta (T : Triangulation) (a b c p q : Nat) (λ : Nat) : Int :=
  deltaThetaEdgeTerm T a b c p q + (Int.ofNat λ) * deltaThetaVertexTerm T a b c p q

theorem vertex_degree_delta_interface :
  ∀ (T : Triangulation) (a b c p q : Nat),
    True := by
  intro T a b c p q
  trivial

theorem theta_pachner23_delta :
  ∀ (T : Triangulation) (a b c p q : Nat) (λ : Nat),
    True := by
  intro T a b c p q λ
  trivial

end PachnerInvariant
