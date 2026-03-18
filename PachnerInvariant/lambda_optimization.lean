import PachnerInvariant.descent_property

namespace PachnerInvariant

def theta_with_lam (T : Triangulation) (lam : Nat) : Nat :=
  theta T lam

def optimize_lam (T : Triangulation) : Nat :=
  [1, 2, 3, 4, 5].foldl (fun best lam =>
    if theta_with_lam T lam < theta_with_lam T best then lam else best) 1

def optimize_lam_after_move (T : Triangulation) (a b c p q : Vert) : Nat :=
  optimize_lam (pachner23 T a b c p q)

-- Find shared vertices between two tets
def sharedVerts (t1 t2 : Vert × Vert × Vert × Vert) : List Vert :=
  (tetToVerts t1).filter ((tetToVerts t2).contains ·)

-- Extract 2→3 move parameters from a tet pair sharing a face
def tetPairToMove (t1 t2 : Vert × Vert × Vert × Vert) :
    Option (Vert × Vert × Vert × Vert × Vert) :=
  let sv := sharedVerts t1 t2
  if sv.length = 3 then
    let apexP := (tetToVerts t1).filter (fun v => !sv.contains v)
    let apexQ := (tetToVerts t2).filter (fun v => !sv.contains v)
    match sv, apexP, apexQ with
    | [a, b, c], [p], [q] => if p ≠ q then some (a, b, c, p, q) else none
    | _, _, _              => none
  else none

-- Find the first improving 2→3 move in T
def findImprovingMove (T : Triangulation) (lam : Nat) :
    Option (Vert × Vert × Vert × Vert × Vert) :=
  (T.tets.flatMap (fun t1 => T.tets.map (fun t2 => (t1, t2)))).findSome?
    (fun (t1, t2) =>
      match tetPairToMove t1 t2 with
      | some (a, b, c, p, q) =>
        if isImproving T a b c p q lam then some (a, b, c, p, q) else none
      | none => none)

-- Greedily apply improving 2→3 moves until none remain (fuel bounds steps)
def greedyImprove (T : Triangulation) (lam : Nat) (fuel : Nat) : Triangulation :=
  match fuel with
  | 0      => T
  | n + 1  =>
    match findImprovingMove T lam with
    | none                  => T
    | some (a, b, c, p, q)  => greedyImprove (pachner23 T a b c p q) lam n

-- Count available improving moves
def countImprovingMoves (T : Triangulation) (lam : Nat) : Nat :=
  (T.tets.flatMap (fun t1 => T.tets.map (fun t2 => (t1, t2)))).countP
    (fun (t1, t2) =>
      match tetPairToMove t1 t2 with
      | some (a, b, c, p, q) => isImproving T a b c p q lam
      | none => false)

end PachnerInvariant
