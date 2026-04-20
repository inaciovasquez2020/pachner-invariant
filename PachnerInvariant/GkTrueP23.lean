namespace PachnerInvariant

def Xor (a b : Bool) : Bool := (!a && b) || (a && !b)

def VecXor : List Bool → List Bool → List Bool
| [], ys => ys
| xs, [] => xs
| x :: xs, y :: ys => Xor x y :: VecXor xs ys

def IsZeroRow : List Bool → Bool
| [] => true
| x :: xs => (!x) && IsZeroRow xs

def ZeroExtend (n : Nat) (row : List Bool) : List Bool :=
  row ++ List.replicate n false

def UnitRow : Nat → Nat → List Bool
| 0, _ => []
| Nat.succ n, 0 => true :: List.replicate n false
| Nat.succ n, Nat.succ j => false :: UnitRow n j

def FirstAvailableComplement (used complement : List Nat) : Option Nat :=
  complement.find? (fun j => !(used.elem j))

def CarrierLiftRow (width extra : Nat) (used complement : List Nat) : List Bool :=
  match FirstAvailableComplement used complement with
  | none => List.replicate (width + extra) false
  | some j => UnitRow (width + extra) j

def NonzeroAfterLift (width extra : Nat) (used complement : List Nat) : Prop :=
  IsZeroRow (CarrierLiftRow width extra used complement) = false

theorem carrierLift_nonzero
  (width extra : Nat)
  (used complement : List Nat)
  (h : ∃ j, complement.elem j = true ∧ used.elem j = false) :
  NonzeroAfterLift width extra used complement := by
  unfold NonzeroAfterLift CarrierLiftRow
  rcases h with ⟨j, hjc, hju⟩
  have hfind : FirstAvailableComplement used complement = some j := by
    unfold FirstAvailableComplement
    simp [List.find?, hjc, hju]
  simp [hfind, UnitRow, IsZeroRow]

def ClosureBoundarySatisfied
  (carrierIndependent explicitLift kernelDisjoint leanChecked : Bool) : Bool :=
  carrierIndependent && explicitLift && kernelDisjoint && leanChecked

theorem closureBoundary_only_if
  (carrierIndependent explicitLift kernelDisjoint leanChecked : Bool)
  (h : ClosureBoundarySatisfied carrierIndependent explicitLift kernelDisjoint leanChecked = true) :
  carrierIndependent = true ∧ explicitLift = true ∧ kernelDisjoint = true ∧ leanChecked = true := by
  unfold ClosureBoundarySatisfied at h
  cases carrierIndependent <;> cases explicitLift <;> cases kernelDisjoint <;> cases leanChecked <;> simp at h

end PachnerInvariant
