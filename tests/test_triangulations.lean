import PachnerInvariant.descent_property
import PachnerInvariant.lambda_optimization
import PachnerInvariant.helpers

open PachnerInvariant

def T1 : Triangulation := { vertices := 4, edges := 6, faces := 4, is_sphere := true }
def T2 : Triangulation := { vertices := 5, edges := 8, faces := 5, is_sphere := false }

#eval theta T1
#eval theta T2
#eval theta (pachner_move T1)
#eval theta (pachner_move T2)
#eval theta (pachner_move T1) > theta T1
#eval total_simplices T1
#eval is_valid T1
#eval is_valid { vertices := 0, edges := 0, faces := 0, is_sphere := false }
#eval optimize_lam T1
#eval theta_with_lam T1 3
#eval theta (apply_moves T1 5)
