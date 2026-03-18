import PachnerInvariant.descent_property
import PachnerInvariant.lambda_optimization
import PachnerInvariant.helpers

open PachnerInvariant

def tetrahedron : Triangulation :=
  { vertices    := 4
    edges       := 6
    faces       := 4
    is_sphere   := true
    edge_degs   := [2, 2, 2, 2, 2, 2]
    vertex_degs := [3, 3, 3, 3] }

def irregular : Triangulation :=
  { vertices    := 8
    edges       := 14
    faces       := 8
    is_sphere   := false
    edge_degs   := [3, 3, 4, 2, 3, 5, 2, 3, 3, 4, 2, 3, 3, 2]
    vertex_degs := [5, 6, 7, 4, 6, 6, 5, 7] }

def main : IO Unit := do
  IO.println s!"theta tetrahedron lam=1    = {theta tetrahedron 1}"
  IO.println s!"theta irregular   lam=1    = {theta irregular 1}"
  IO.println s!"theta irregular   lam=2    = {theta irregular 2}"
  IO.println s!"theta (move tetrahedron)   = {theta (pachner_move tetrahedron) 1}"
  IO.println s!"theta (move irregular)     = {theta (pachner_move irregular) 1}"
  IO.println s!"descent tetrahedron        = {decide (theta (pachner_move tetrahedron) 1 > theta tetrahedron 1)}"
  IO.println s!"descent irregular          = {decide (theta (pachner_move irregular) 1 > theta irregular 1)}"
  IO.println s!"optimize_lam tetrahedron   = {optimize_lam tetrahedron}"
  IO.println s!"is_valid tetrahedron       = {is_valid tetrahedron}"
  IO.println s!"apply 3 moves tetrahedron  = {theta (apply_moves tetrahedron 3) 1}"
