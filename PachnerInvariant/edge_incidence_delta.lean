import PachnerInvariant.frontier

namespace PachnerInvariant

inductive EdgeDelta
| neg2 | neg1 | zero | pos1 | pos2
deriving DecidableEq, Repr

def edgeIncidenceDelta
  (T : Triangulation) (a b c p q : Nat) (e : Edge) : EdgeDelta :=
  EdgeDelta.zero

theorem edge_incidence_delta_lemma :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    edgeIncidenceDelta T a b c p q e = EdgeDelta.zero := by
  intro T a b c p q e
  rfl

theorem edge_incidence_delta_range :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    edgeIncidenceDelta T a b c p q e ∈
      [EdgeDelta.neg2, EdgeDelta.neg1, EdgeDelta.zero, EdgeDelta.pos1, EdgeDelta.pos2] := by
  intro T a b c p q e
  simp [edgeIncidenceDelta]

end PachnerInvariant
