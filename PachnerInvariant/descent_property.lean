structure Triangulation where
  vertices : Nat
  edges    : Nat
  faces    : Nat
  is_sphere : Bool

def theta (T : Triangulation) : Nat :=
  -- Full Pachner invariant computation here

def pachner_move (T : Triangulation) : Triangulation :=
  -- Full Pachner move logic here

theorem strict_descent (T : Triangulation) (h : ¬T.is_sphere) :
    theta (pachner_move T) > theta T :=
  -- Full formal proof of strict descent goes here
