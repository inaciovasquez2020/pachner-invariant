namespace PachnerInvariant

def edges (a b c d : Nat) : List (Nat × Nat) :=
[(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def Local (a b c p q : Nat) : List (Nat × Nat) :=
[(a,b),(b,c),(c,a),
 (a,p),(b,p),(c,p),
 (a,q),(b,q),(c,q),
 (p,q)]

def isNonLocal (a b c p q : Nat) (e : Nat × Nat) : Prop :=
¬ (e ∈ Local a b c p q)

def DeltaInc (e : Nat × Nat) : Int :=
match e with
| _ => 0

end PachnerInvariant
