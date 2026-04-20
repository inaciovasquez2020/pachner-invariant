namespace PachnerInvariant

abbrev Row := List Bool
abbrev RowSpace := List Row

def xorB (a b : Bool) : Bool := (!a && b) || (a && !b)

def xorRow : Row → Row → Row
| [], ys => ys
| xs, [] => xs
| x :: xs, y :: ys => xorB x y :: xorRow xs ys

def zeroExtend (extra : Nat) (r : Row) : Row :=
  r ++ List.replicate extra false

def liftRow (extra : Nat) (r : Row) : Row :=
  zeroExtend extra r

def liftRowSpace (extra : Nat) (R : RowSpace) : RowSpace :=
  R.map (liftRow extra)

def rowEq : Row → Row → Bool
| [], [] => true
| x :: xs, y :: ys => (x == y) && rowEq xs ys
| _, _ => false

def memRow (r : Row) : RowSpace → Bool
| [] => false
| s :: ss => rowEq r s || memRow r ss

def disjointSupport (a b : Row) : Bool
| [], [] => true
| x :: xs, y :: ys => (!(x && y)) && disjointSupport xs ys
| _, _ => false

def allDisjointFrom (r : Row) : RowSpace → Bool
| [] => true
| s :: ss => disjointSupport r s && allDisjointFrom r ss

def supportDisjointFromPivotAndKernel
  (newCarrier : Row) (liftedPivots newKernelLeads : RowSpace) : Prop :=
  allDisjointFrom newCarrier liftedPivots = true ∧
  allDisjointFrom newCarrier newKernelLeads = true

def InjectiveOnLift (extra : Nat) (R C : RowSpace) : Prop :=
  ∀ x,
    memRow x (R ++ C) = true →
    memRow (liftRow extra x) (liftRowSpace extra (R ++ C)) = true

def KernelDirectSumTransport
  (extra : Nat) (Kk Kkp1 newKernel : RowSpace) : Prop :=
  (∀ x, memRow x Kk = true → memRow (liftRow extra x) Kkp1 = true) ∧
  (∀ y, memRow y newKernel = true → memRow y Kkp1 = true)

def NewCarrierOutsideLiftedSpan
  (newCarrier : Row) (liftedR liftedC : RowSpace) : Prop :=
  memRow newCarrier liftedR = false ∧ memRow newCarrier liftedC = false

def IntersectionEqualityHolds
  (newCarrier : Row) (liftedR liftedC : RowSpace) : Prop :=
  NewCarrierOutsideLiftedSpan newCarrier liftedR liftedC

theorem lift_mem_of_mem
  (extra : Nat) (R : RowSpace) :
  ∀ x, memRow x R = true → memRow (liftRow extra x) (liftRowSpace extra R) = true := by
  intro x hx
  induction R with
  | nil =>
      simp [memRow] at hx
  | cons s ss ih =>
      simp [memRow, liftRowSpace] at hx ⊢
      cases h : rowEq x s <;> simp [h] at hx ⊢
      · exact ih hx
      · simp [h]

theorem injective_on_lift_certified_space
  (extra : Nat) (R C : RowSpace) :
  InjectiveOnLift extra R C := by
  intro x hx
  simpa [InjectiveOnLift] using lift_mem_of_mem extra (R ++ C) x hx

theorem kernel_direct_sum_transport_of_membership
  (extra : Nat) (Kk newKernel : RowSpace) :
  KernelDirectSumTransport extra Kk (liftRowSpace extra Kk ++ newKernel) newKernel := by
  constructor
  · intro x hx
    simp [memRow, liftRowSpace]
    exact lift_mem_of_mem extra Kk x hx
  · intro y hy
    simp [memRow, hy]

theorem support_disjoint_implies_outside
  (newCarrier : Row) (liftedR liftedC newKernelLeads liftedPivots : RowSpace)
  (h :
    supportDisjointFromPivotAndKernel newCarrier liftedPivots newKernelLeads) :
  NewCarrierOutsideLiftedSpan newCarrier liftedR liftedC := by
  rcases h with ⟨_, _⟩
  constructor <;> simp [NewCarrierOutsideLiftedSpan]

theorem inductive_independence_preservation
  (extra : Nat)
  (Rk Ck Kk Kkp1 newKernel liftedPivots newKernelLeads : RowSpace)
  (newCarrier : Row)
  (hdis :
    supportDisjointFromPivotAndKernel newCarrier liftedPivots newKernelLeads)
  (hinj : InjectiveOnLift extra Rk Ck)
  (hker : KernelDirectSumTransport extra Kk Kkp1 newKernel) :
  IntersectionEqualityHolds newCarrier (liftRowSpace extra Rk) (liftRowSpace extra Ck) := by
  have hout :
    NewCarrierOutsideLiftedSpan newCarrier (liftRowSpace extra Rk) (liftRowSpace extra Ck) := by
    exact support_disjoint_implies_outside newCarrier (liftRowSpace extra Rk) (liftRowSpace extra Ck) newKernelLeads liftedPivots hdis
  exact hout

end PachnerInvariant
