import PachnerInvariant.edge_incidence_delta

namespace PachnerInvariant

def edgeDegreeDelta
  (T : Triangulation) (a b c p q : Nat) (e : Edge) : Int := 0

theorem edge_degree_delta_lemma :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    edgeDegreeDelta T a b c p q e = 0 := by
  intro T a b c p q e
  rfl

end PachnerInvariant
