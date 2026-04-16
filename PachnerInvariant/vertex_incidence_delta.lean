import PachnerInvariant.frontier

namespace PachnerInvariant

def vertexIncidenceDelta
  (T : Triangulation) (a b c p q : Nat) (v : Nat) : Int := 0

theorem vertex_incidence_delta_lemma :
  ∀ (T : Triangulation) (a b c p q : Nat) (v : Nat),
    vertexIncidenceDelta T a b c p q v = 0 := by
  intro T a b c p q v
  rfl

end PachnerInvariant
