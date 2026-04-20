namespace PachnerInvariant

abbrev Row := List Bool
abbrev RowSpace := List Row

def disjointSupport : Row → Row → Bool
| [], [] => true
| x :: xs, y :: ys => (!(x && y)) && disjointSupport xs ys
| _, _ => false

def allDisjointFrom (r : Row) : RowSpace → Bool
| [] => true
| s :: ss => disjointSupport r s && allDisjointFrom r ss

def SupportSeparated (newCarrier : Row) (liftedPivots newKernelLeads : RowSpace) : Prop :=
  allDisjointFrom newCarrier liftedPivots = true ∧
  allDisjointFrom newCarrier newKernelLeads = true

def FinalWallCleared (newCarrier : Row) (liftedPivots newKernelLeads : RowSpace) : Prop :=
  SupportSeparated newCarrier liftedPivots newKernelLeads

theorem support_separation_implies_final_wall_clear
  (newCarrier : Row) (liftedPivots newKernelLeads : RowSpace)
  (h : SupportSeparated newCarrier liftedPivots newKernelLeads) :
  FinalWallCleared newCarrier liftedPivots newKernelLeads := by
  exact h

end PachnerInvariant
