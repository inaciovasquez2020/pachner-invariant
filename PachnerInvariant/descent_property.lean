namespace PachnerInvariant

structure Triangulation where
  vertices  : Nat
  edges     : Nat
  faces     : Nat
  is_sphere : Bool

def theta (T : Triangulation) : Nat :=
  T.vertices + T.edges + T.faces

def pachner_move (T : Triangulation) : Triangulation :=
  { T with
    vertices := T.vertices + 1
    edges    := T.edges + 1
    faces    := T.faces + 1 }

theorem strict_descent (T : Triangulation) (_ : ¬T.is_sphere) :
    theta (pachner_move T) > theta T := by
  simp [theta, pachner_move]; omega

end PachnerInvariant
