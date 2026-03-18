import PachnerInvariant.descent_property
import PachnerInvariant.lambda_optimization
import PachnerInvariant.helpers

open PachnerInvariant

def T1 : Triangulation := { vertices := 4, edges := 6, faces := 4, is_sphere := true }
def T2 : Triangulation := { vertices := 5, edges := 8, faces := 5, is_sphere := false }

def main : IO Unit := do
  IO.println s!"theta T1            = {theta T1}"
  IO.println s!"theta T2            = {theta T2}"
  IO.println s!"theta (move T1)     = {theta (pachner_move T1)}"
  IO.println s!"descent holds T1    = {decide (theta (pachner_move T1) > theta T1)}"
  IO.println s!"total_simplices T1  = {total_simplices T1}"
  IO.println s!"is_valid T1         = {is_valid T1}"
  IO.println s!"is_valid empty      = {is_valid { vertices := 0, edges := 0, faces := 0, is_sphere := false }}"
  IO.println s!"optimize_lam T1     = {optimize_lam T1}"
  IO.println s!"theta_with_lam T1 3 = {theta_with_lam T1 3}"
  IO.println s!"apply 5 moves T1    = {theta (apply_moves T1 5)}"
