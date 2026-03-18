set_option linter.unusedVariables false

structure Triangulation where
  vertices : Nat
  edges    : Nat
  faces    : Nat
  is_sphere : Bool

def theta (T : Triangulation) : Nat :=
  -- TODO: implement full Pachner invariant computation here
  0

def pachner_move (T : Triangulation) : Triangulation :=
  -- TODO: implement full Pachner 2-3 / 3-2 move logic here
  T

theorem strict_descent (T : Triangulation) (_ : ¬T.is_sphere) :
    theta (pachner_move T) > theta T :=
  -- TODO: formal Lean proof of strict descent
  sorry
