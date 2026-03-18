import PachnerInvariant.descent_property

namespace PachnerInvariant

def total_simplices (T : Triangulation) : Nat :=
  T.numVerts + (allEdges T).length + T.tets.length

def is_valid (T : Triangulation) : Bool :=
  T.numVerts > 0 && !T.tets.isEmpty

/-- Check that two tets actually share the face (a,b,c) — i.e., the move precondition holds. -/
def can_apply_pachner23 (T : Triangulation) (a b c p q : Vert) : Bool :=
  T.tets.any (tetEq (a, b, c, p)) && T.tets.any (tetEq (a, b, c, q))

/-- Apply n sequential 2→3 moves on the same face, adding new apex vertices. -/
def apply_moves (T : Triangulation) (a b c : Vert) (n : Nat) : Triangulation :=
  (List.range n).foldl (fun acc i =>
    let p := acc.tets.length      -- use tet count as a fresh vertex proxy
    let q := acc.tets.length + 1
    pachner23 acc a b c p q) T

end PachnerInvariant
