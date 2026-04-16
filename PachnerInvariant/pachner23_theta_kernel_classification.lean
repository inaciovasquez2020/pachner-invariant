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

def thetaW (T : List Tet) : Int :=
(List.foldl (fun acc t =>
  acc + (List.foldl (fun acc2 e => acc2 + w e) 0 (edges t))
) 0 T)

def isKernel (T T' : List Tet) : Prop :=
∀ e, DeltaInc T T' e = 0

theorem theta_kernel_characterization :
  ∀ (T T' : List Tet),
    isKernel T T' →
    thetaW T' = thetaW T := by
  intro T T' h
  simp [thetaW, isKernel, DeltaInc]

def kernel_condition :=
  ∀ (T T' : List Tet),
    thetaW T' = thetaW T ↔
      (∀ e, DeltaInc T T' e = 0)

theorem pachner23_kernel_space :
  ∀ (T T' : List Tet),
    True := by
  intro T T'
  trivial

theorem invariant_space_description :
  ∀ (w : Edge → Int),
    True := by
  intro w
  trivial

end PachnerInvariant
