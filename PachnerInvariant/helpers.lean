import PachnerInvariant.descent_property

namespace PachnerInvariant

def total_simplices (T : Triangulation) : Nat :=
  T.numVerts + (allEdges T).length + (allFaces T).length + T.tets.length

def is_valid (T : Triangulation) : Bool :=
  T.numVerts > 0 && !T.tets.isEmpty

def can_apply_pachner23 (T : Triangulation) (a b c p q : Vert) : Bool :=
  T.tets.any (tetEq (a, b, c, p)) && T.tets.any (tetEq (a, b, c, q))

def can_apply_pachner32 (T : Triangulation) (a b c p q : Vert) : Bool :=
  T.tets.any (tetEq (a, b, p, q)) &&
  T.tets.any (tetEq (a, c, p, q)) &&
  T.tets.any (tetEq (b, c, p, q))

def apply_moves (T : Triangulation) (a b c : Vert) (n : Nat) : Triangulation :=
  (List.range n).foldl (fun acc _ =>
    let p := acc.tets.length
    let q := acc.tets.length + 1
    pachner23 acc a b c p q) T

end PachnerInvariant
