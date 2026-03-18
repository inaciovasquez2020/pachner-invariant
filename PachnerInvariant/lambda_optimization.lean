import PachnerInvariant.descent_property

namespace PachnerInvariant

def theta_with_lam (T : Triangulation) (lam : Nat) : Nat :=
  theta T lam

/-- Find the λ in [1..5] that minimises Θ(T, λ). -/
def optimize_lam (T : Triangulation) : Nat :=
  [1, 2, 3, 4, 5].foldl (fun best lam =>
    if theta_with_lam T lam < theta_with_lam T best then lam else best) 1

/-- Find the λ that minimises Θ after applying a specific move. -/
def optimize_lam_after_move (T : Triangulation) (a b c p q : Vert) : Nat :=
  optimize_lam (pachner23 T a b c p q)

end PachnerInvariant
