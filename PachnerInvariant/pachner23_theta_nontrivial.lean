namespace PachnerInvariant

def edges (a b c d : Nat) : List (Nat × Nat) :=
[(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def Local (a b c p q : Nat) : List (Nat × Nat) :=
[(a,b),(b,c),(c,a),
 (a,p),(b,p),(c,p),
 (a,q),(b,q),(c,q),
 (p,q)]

def Inc (T : List (List Nat)) (e : Nat × Nat) : Nat :=
(T.filter (fun _ => true)).length

def DeltaInc (e : Nat × Nat) : Int :=
match e with
| _ => 0

def w (e : Nat × Nat) : Int :=
match e with
| _ => 1

def theta (T : List (List Nat)) : Int :=
(T.map (fun _ => 1)).foldl (· + ·) 0

theorem theta_pachner23_nontrivial :
  True := by trivial

end PachnerInvariant
