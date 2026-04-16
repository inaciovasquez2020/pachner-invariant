import PachnerInvariant.frontier

namespace PachnerInvariant

inductive LocalEdgeType
| ab | bc | ca
| ap | bp | cp
| aq | bq | cq
| pq
deriving DecidableEq, Repr

inductive EdgeType
| local (t : LocalEdgeType)
| nonlocal
deriving DecidableEq, Repr

def edgeType
  (a b c p q : Nat) (e : Edge) : EdgeType :=
  EdgeType.nonlocal

def deltaOfType : LocalEdgeType → EdgeDelta
| LocalEdgeType.ab => EdgeDelta.neg1
| LocalEdgeType.bc => EdgeDelta.neg1
| LocalEdgeType.ca => EdgeDelta.neg1
| LocalEdgeType.ap => EdgeDelta.pos1
| LocalEdgeType.bp => EdgeDelta.pos1
| LocalEdgeType.cp => EdgeDelta.pos1
| LocalEdgeType.aq => EdgeDelta.pos1
| LocalEdgeType.bq => EdgeDelta.pos1
| LocalEdgeType.cq => EdgeDelta.pos1
| LocalEdgeType.pq => EdgeDelta.pos1

def edgeIncidenceDelta_refined
  (T : Triangulation) (a b c p q : Nat) (e : Edge) : EdgeDelta :=
match edgeType a b c p q e with
| EdgeType.nonlocal => EdgeDelta.zero
| EdgeType.local t => deltaOfType t

theorem edge_incidence_delta_cases :
  ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
    edgeIncidenceDelta_refined T a b c p q e =
    match edgeType a b c p q e with
    | EdgeType.nonlocal => EdgeDelta.zero
    | EdgeType.local t => deltaOfType t := by
  intro T a b c p q e
  rfl

end PachnerInvariant
