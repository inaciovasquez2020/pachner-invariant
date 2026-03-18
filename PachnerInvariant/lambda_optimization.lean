import PachnerInvariant.descent_property

namespace PachnerInvariant

def theta_with_lam (T : Triangulation) (lam : Nat) : Nat :=
  theta T lam

def optimize_lam (T : Triangulation) : Nat :=
  [1, 2, 3, 4, 5].foldl (fun best lam =>
    if theta_with_lam T lam < theta_with_lam T best then lam else best) 1

end PachnerInvariant
