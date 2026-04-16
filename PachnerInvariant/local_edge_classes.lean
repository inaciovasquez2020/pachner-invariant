import PachnerInvariant.frontier
import PachnerInvariant.edge_incidence_delta

namespace PachnerInvariant

inductive LocalEdgeClass
| removed
| preserved
| created
| nonlocal
deriving DecidableEq, Repr

def localEdgeClass
  (T : Triangulation) (a b c p q : Nat) (e : Edge) : LocalEdgeClass :=
  LocalEdgeClass.nonlocal

def edgeDeltaValue : EdgeDelta → Int
| EdgeDelta.neg2 => -2
| EdgeDelta.neg1 => -1
| EdgeDelta.zero => 0
| EdgeDelta.pos1 => 1
| EdgeDelta.pos2 => 2

theorem edgeDeltaValue_range :
  ∀ d : EdgeDelta, edgeDeltaValue d ∈ [-2, -1, 0, 1, 2] := by
  intro d
  cases d <;> simp [edgeDeltaValue]

theorem localEdgeClass_cases :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    localEdgeClass T a b c p q e ∈
      [LocalEdgeClass.removed,
       LocalEdgeClass.preserved,
       LocalEdgeClass.created,
       LocalEdgeClass.nonlocal] := by
  intro T a b c p q e
  simp [localEdgeClass]

end PachnerInvariant
