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
(List.foldl (fun acc t =>
  acc + (List.foldl (fun acc2 e => acc2 + 1) 0 (edges t))
) 0 T)

theorem theta_incidence_link :
  ∀ (T : List Tet),
    theta T = ∑ t in T, (edges t).length := by
  intro T
  simp [theta, edges]

def thetaWeighted (T : List Tet) : Int :=
(List.foldl (fun acc t =>
  acc + (List.foldl (fun acc2 e => acc2 + w e) 0 (edges t))
) 0 T)

theorem theta_weighted_expansion :
  ∀ (T : List Tet),
    thetaWeighted T = ∑ t in T, ∑ e in edges t, w e := by
  intro T
  simp [thetaWeighted]

theorem pachner23_theta_delta_weighted :
  ∀ (T T' : List Tet),
    thetaWeighted T' - thetaWeighted T =
      ∑ e, w e * (DeltaInc T T' e) := by
  intro T T'
  simp [DeltaInc]

end PachnerInvariant
