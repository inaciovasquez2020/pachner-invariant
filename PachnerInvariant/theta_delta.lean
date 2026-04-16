import PachnerInvariant.frontier
import PachnerInvariant.edge_incidence_delta
import PachnerInvariant.edge_degree_delta

namespace PachnerInvariant

def deltaThetaEdgeTerm (T : Triangulation) (a b c p q : Nat) : Int := 0

def deltaThetaVertexTerm (T : Triangulation) (a b c p q : Nat) : Int := 0

def deltaTheta (T : Triangulation) (a b c p q : Nat) (λ : Nat) : Int :=
  deltaThetaEdgeTerm T a b c p q + (Int.ofNat λ) * deltaThetaVertexTerm T a b c p q

axiom vertex_degree_delta_interface :
  ∀ (T : Triangulation) (a b c p q : Nat),
    True

axiom theta_pachner23_delta :
  ∀ (T : Triangulation) (a b c p q : Nat) (λ : Nat),
    True

end PachnerInvariant
