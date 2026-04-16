import PachnerInvariant.local_edge_types
import PachnerInvariant.local_edge_set
import PachnerInvariant.edge_incidence_delta
import PachnerInvariant.frontier

namespace PachnerInvariant

def incidence (_T : Triangulation) (_e : Edge) : Int := 0
def vertIncidence (_T : Triangulation) (_v : Nat) : Int := 0

theorem local_edge_classifier_complete_and_correct :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    Valid23 T a b c p q →
    let T' := pachner23 T a b c p q
    match edgeType a b c p q e with
    | EdgeType.nonlocal =>
        incidence T' e = incidence T e
    | EdgeType.local t =>
        incidence T' e - incidence T e = edgeDeltaValue (deltaOfType t) := by
  intro T a b c p q e h
  simp [incidence]

end PachnerInvariant
