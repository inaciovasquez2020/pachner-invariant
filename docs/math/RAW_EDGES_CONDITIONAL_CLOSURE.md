# Raw-Edges Conditional Closure

Status: Conditional.

The old bridge

```lean
(allEdges T).count e = edgeDeg T e
is false because allEdges erases duplicates while edgeDeg counts tetrahedral incidences.
The correct replacement is:
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

theorem rawEdges_count_eq_edgeDeg_countP
  (T : Triangulation)
  (hT : WellFormedTets T)
  (e : Vert × Vert) :
  (rawEdges T).count (normalizeEdge e) =
    T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e)))
This is the weakest sufficient bridge. The remaining theorem-level obligation is to propagate `WellFormedTets` through the Pachner 2--3 move layer or prove the corresponding local source/target incidence delta directly.
