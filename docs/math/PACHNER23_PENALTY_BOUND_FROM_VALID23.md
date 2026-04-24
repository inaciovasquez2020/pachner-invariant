# Pachner 2-3 Penalty Bound from Valid23

Status: Open.

## Weakest missing theorem

```lean
lemma penalty_bound_from_valid23
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  edgePenaltyExpected23 T a b c d e ≤ edgePenalty T ∧
  vertexPenaltyExpected23 T a b c d e ≤ vertexPenalty T
Immediate consequences
lemma pachner23_local_edge_penalty_nonincrease
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  edgePenaltyExpected23 T a b c d e ≤ edgePenalty T := by
  exact (penalty_bound_from_valid23 T hT a b c d e hvalid).1
lemma pachner23_local_vertex_penalty_nonincrease
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  vertexPenaltyExpected23 T a b c d e ≤ vertexPenalty T := by
  exact (penalty_bound_from_valid23 T hT a b c d e hvalid).2
lemma valid23_implies_penalty_controlled
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  Valid23PenaltyControlled T a b c d e :=
{
  edge_nonincrease :=
    (penalty_bound_from_valid23 T hT a b c d e hvalid).1,
  vertex_nonincrease :=
    (penalty_bound_from_valid23 T hT a b c d e hvalid).2
}
theorem theta_pachner23_nonincreasing
  (T : Triangulation)
  (hT : WellFormedTets T)
  (λ : ℕ)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  theta (pachner23 T a b c d e) λ ≤ theta T λ := by
  have hctrl :=
    valid23_implies_penalty_controlled T hT a b c d e hvalid
  exact
    theta_pachner23_nonincreasing_of_penalty_controlled
      T hT λ a b c d e hvalid
Frontier lock
The full unconditional theta nonincrease theorem is equivalent, within the current proof chain, to proving penalty_bound_from_valid23.
No unconditional proof is claimed here.
