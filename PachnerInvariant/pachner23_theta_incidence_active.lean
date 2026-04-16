namespace PachnerInvariant

def Tet := Nat × Nat × Nat × Nat

def Edge := Nat × Nat

def edges (t : Tet) : List Edge :=
match t with
| (a,b,c,d) =>
  [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def Inc (T : List Tet) (e : Edge) : Nat :=
(T.filter (fun t => (edges t).contains e)).length

def Local (a b c p q : Nat) : List Edge :=
[(a,b),(b,c),(c,a),
 (a,p),(b,p),(c,p),
 (a,q),(b,q),(c,q),
 (p,q)]

def isLocal (a b c p q : Nat) (e : Edge) : Bool :=
(Local a b c p q).contains e

def pachner23 (T : List Tet) (t0 t1 t2 t3 : Tet) : List Tet :=
(T.erase t0) ++ [t1,t2,t3]

def DeltaInc (T T' : List Tet) (e : Edge) : Int :=
(Int.ofNat (Inc T' e)) - (Int.ofNat (Inc T e))

def w (_e : Edge) : Int := 1

def theta (T : List Tet) : Int :=
(T.map (fun _ => 1)).foldl (· + ·) 0

theorem incidence_locality :
  ∀ (T T' : List Tet) (a b c p q : Nat) (e : Edge),
    ¬ isLocal a b c p q e →
    DeltaInc T T' e = 0 := by
  intro T T' a b c p q e h
  simp [DeltaInc, Inc]

end PachnerInvariant
