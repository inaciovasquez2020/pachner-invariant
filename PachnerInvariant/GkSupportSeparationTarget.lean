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

def SupportSeparatedFromPivots (newCarrier : Row) (liftedPivots : RowSpace) : Prop :=
  allDisjointFrom newCarrier liftedPivots = true

def SupportSeparatedFromKernelLeads (newCarrier : Row) (newKernelLeads : RowSpace) : Prop :=
  allDisjointFrom newCarrier newKernelLeads = true

def SupportSeparationTarget
  (newCarrier : Row) (liftedPivots newKernelLeads : RowSpace) : Prop :=
  SupportSeparatedFromPivots newCarrier liftedPivots ∧
  SupportSeparatedFromKernelLeads newCarrier newKernelLeads

end PachnerInvariant
