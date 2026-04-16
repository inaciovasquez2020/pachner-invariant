import PachnerInvariant.frontier
import PachnerInvariant.edge_incidence_delta
import PachnerInvariant/local_edge_set

namespace PachnerInvariant

def isNonLocalEdge
  (a b c p q : Nat) (e : Edge) : Prop :=
  ¬ isLocalMoveEdge a b c p q e

theorem nonlocal_edge_incidence_zero :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    isNonLocalEdge a b c p q e →
    edgeIncidenceDelta T a b c p q e = EdgeDelta.zero := by
  intro T a b c p q e h
  rfl

end PachnerInvariant
