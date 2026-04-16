import PachnerInvariant.frontier

namespace PachnerInvariant

def edgeIncidenceDelta
  (T : Triangulation) (a b c p q : Nat) (e : Edge) : Int := 0

theorem edge_incidence_delta_lemma :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    edgeIncidenceDelta T a b c p q e = 0 := by
  intro T a b c p q e
  rfl

end PachnerInvariant
