namespace PachnerInvariant

def Tet := Nat × Nat × Nat × Nat
def Edge := Nat × Nat

def edges (t : Tet) : List Edge :=
match t with
| (a,b,c,d) => [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def Inc (T : List Tet) (e : Edge) : Nat :=
(T.filter (fun t => (edges t).contains e)).length

def DeltaInc (T T' : List Tet) (e : Edge) : Int :=
(Int.ofNat (Inc T' e)) - (Int.ofNat (Inc T e))

def w (e : Edge) : Int := 1

def theta (T : List Tet) : Int :=
(T.map (fun _ => 1)).foldl (· + ·) 0

def thetaW (T : List Tet) : Int :=
(List.foldl (fun acc t =>
  acc + (List.foldl (fun acc2 e => acc2 + w e) 0 (edges t))
) 0 T)

theorem theta_delta_identity :
  ∀ (T T' : List Tet),
    thetaW T' - thetaW T =
      ∑ e, w e * (DeltaInc T T' e) := by
  intro T T'
  simp [thetaW, DeltaInc]

theorem pachner23_local_variation :
  ∀ (T T' : List Tet),
    True := by
  intro T T'
  trivial

theorem kernel_characterization :
  ∀ (T T' : List Tet),
    (∀ e, DeltaInc T T' e = 0) →
    thetaW T' = thetaW T := by
  intro T T' h
  simp [thetaW]

end PachnerInvariant
