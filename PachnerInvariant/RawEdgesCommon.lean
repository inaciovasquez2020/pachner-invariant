import PachnerInvariant.descent_property

namespace PachnerInvariant

def rawEdges (T : Triangulation) : List (Vert × Vert) :=
  (T.tets.flatMap tetToEdges).map normalizeEdge

def pairwiseDistinctTet (t : Vert × Vert × Vert × Vert) : Prop :=
  t.1 ≠ t.2.1 ∧
  t.1 ≠ t.2.2.1 ∧
  t.1 ≠ t.2.2.2 ∧
  t.2.1 ≠ t.2.2.1 ∧
  t.2.1 ≠ t.2.2.2 ∧
  t.2.2.1 ≠ t.2.2.2

def WellFormedTets (T : Triangulation) : Prop :=
  ∀ t ∈ T.tets, pairwiseDistinctTet t

theorem rawEdges_def (T : Triangulation) :
    rawEdges T = (T.tets.flatMap tetToEdges).map normalizeEdge := by
  rfl

theorem allEdges_eq_rawEdges_eraseDups (T : Triangulation) :
    allEdges T = (rawEdges T).eraseDups := by
  rfl

end PachnerInvariant
