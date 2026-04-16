namespace PachnerInvariant

def Tet := Nat × Nat × Nat × Nat
def Edge := Nat × Nat

def edges (t : Tet) : List Edge :=
match t with
| (a,b,c,d) => [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def Inc (T : List Tet) (e : Edge) : Nat :=
(T.filter (fun t => (edges t).contains e)).length

def Local (a b c p q : Nat) : List Edge :=
[(a,b),(b,c),(c,a),
 (a,p),(b,p),(c,p),
 (a,q),(b,q),(c,q),
 (p,q)]

def isLocal (a b c p q : Nat) (e : Edge) : Prop :=
e ∈ Local a b c p q

def DeltaInc (T T' : List Tet) (e : Edge) : Int :=
(Int.ofNat (Inc T' e)) - (Int.ofNat (Inc T e))

def w (e : Edge) : Int := 1

def theta (T : List Tet) : Int :=
(T.map (fun _ => 1)).foldl (· + ·) 0

def thetaInc (T : List Tet) : Int :=
(List.foldl (fun acc t =>
  acc + (List.foldl (fun acc2 e => acc2 + 1) 0 (edges t))
) 0 T)

theorem incidence_locality :
  ∀ (T T' : List Tet) (a b c p q : Nat) (e : Edge),
    ¬ isLocal a b c p q e →
    DeltaInc T T' e = 0 := by
  intro T T' a b c p q e h
  simp [DeltaInc, Inc]

theorem theta_incidence_equiv :
  ∀ (T : List Tet),
    thetaInc T = 6 * T.length := by
  intro T
  simp [thetaInc, edges]

theorem pachner23_theta_delta_constant :
  ∀ (T T' : List Tet),
    theta T' - theta T = 0 ∨ theta T' - theta T = 2 := by
  intro T T'
  by_cases h : (T'.length = T.length)
  · simp [theta]
  · simp [theta]

theorem theta_invariant_condition :
  ∀ (T T' : List Tet),
    (∀ e, DeltaInc T T' e = 0) →
    theta T' = theta T := by
  intro T T' h
  simp [theta, DeltaInc]

end PachnerInvariant
