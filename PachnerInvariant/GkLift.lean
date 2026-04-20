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

def allRowsLifted (extra : Nat) (R : RowSpace) : Prop :=
  ∀ r, memRow r R = true → memRow (liftRow extra r) (liftRowSpace extra R) = true

theorem allRowsLifted_true (extra : Nat) (R : RowSpace) : allRowsLifted extra R := by
  intro r hr
  induction R with
  | nil =>
      simp [memRow] at hr
  | cons s ss ih =>
      simp [memRow, liftRowSpace] at hr ⊢
      cases h1 : rowEq r s <;> simp [h1] at hr ⊢
      · exact ih hr
      · simp [h1]

def kernelTransportInvariant (extra : Nat) (Kk Kkp1 : RowSpace) : Prop :=
  ∀ r, memRow r Kk = true → memRow (liftRow extra r) Kkp1 = true

def newCarrierOutsideTransportedSpan
  (newCarrier : Row) (transportedBase transportedKernel : RowSpace) : Prop :=
  memRow newCarrier transportedBase = false ∧ memRow newCarrier transportedKernel = false

def pivotCollisionFree (used : List Nat) (j : Nat) : Prop :=
  used.elem j = false

def closureBoundarySatisfied
  (kernelTransport carrierEscape pivotFree : Prop) : Prop :=
  kernelTransport ∧ carrierEscape ∧ pivotFree

theorem closureBoundary_split
  (kernelTransport carrierEscape pivotFree : Prop)
  (h : closureBoundarySatisfied kernelTransport carrierEscape pivotFree) :
  kernelTransport ∧ carrierEscape ∧ pivotFree := by
  exact h

theorem lifted_kernel_membership
  (extra : Nat) (K : RowSpace) :
  kernelTransportInvariant extra K (liftRowSpace extra K) := by
  intro r hr
  induction K with
  | nil =>
      simp [memRow] at hr
  | cons s ss ih =>
      simp [kernelTransportInvariant, memRow, liftRowSpace] at hr ⊢
      cases h1 : rowEq r s <;> simp [h1] at hr ⊢
      · exact ih hr
      · simp [h1]

end PachnerInvariant
