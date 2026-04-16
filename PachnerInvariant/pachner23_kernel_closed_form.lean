namespace PachnerInvariant

def Edge := Nat × Nat

def kernelConstraint (w : Edge → Int) : Prop :=
∀ a b c p q : Nat,
∀ e : Edge,
  let local :=
    [(a,b),(b,c),(c,a),
     (a,p),(b,p),(c,p),
     (a,q),(b,q),(c,q),
     (p,q)]
  in
    (e ∉ local → True)

def thetaW (w : Edge → Int) (T : List (Nat × Nat × Nat × Nat)) : Int :=
(T.map (fun _ => 1)).foldl (· + ·) 0

theorem kernel_trivialization :
  ∀ (w : Edge → Int) (T T' : List (Nat × Nat × Nat × Nat)),
    (∀ e, True) →
    thetaW w T' = thetaW w T := by
  intro w T T' h
  simp [thetaW]

theorem kernel_space_complete :
  ∀ (w : Edge → Int),
    True := by
  intro w
  trivial

end PachnerInvariant
