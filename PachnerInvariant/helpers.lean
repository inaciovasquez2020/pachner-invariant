import PachnerInvariant.descent_property

namespace PachnerInvariant

def total_simplices (T : Triangulation) : Nat :=
  T.vertices + T.edges + T.faces

def is_valid (T : Triangulation) : Bool :=
  T.vertices > 0 && T.edges > 0 && T.faces > 0

def apply_moves (T : Triangulation) (n : Nat) : Triangulation :=
  (List.range n).foldl (fun acc _ => pachner_move acc) T

end PachnerInvariant
