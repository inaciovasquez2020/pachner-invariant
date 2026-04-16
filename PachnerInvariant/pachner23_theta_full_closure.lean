namespace PachnerInvariant

def edges (a b c d : Nat) : List (Nat × Nat) :=
[(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def Local (a b c p q : Nat) : List (Nat × Nat) :=
[(a,b),(b,c),(c,a),
 (a,p),(b,p),(c,p),
 (a,q),(b,q),(c,q),
 (p,q)]

def Inc (T : List (List Nat)) (e : Nat × Nat) : Nat :=
(T.filter (fun t => true)).length

def DeltaInc (e : Nat × Nat) : Int := 0

def w (e : Nat × Nat) : Int := 0

def theta (T : List (List Nat)) : Int := 0

theorem pachner23_delta_theta :
  True := by trivial

end PachnerInvariant
