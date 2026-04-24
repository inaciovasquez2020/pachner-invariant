# Pachner 2-3 Penalty-Controlled Theta Theorem

Status: Conditional.

## Penalty-control class

```lean
class Valid23PenaltyControlled
  (T : Triangulation)
  (a b c d e : Vert) : Prop where
  edge_nonincrease :
    edgePenaltyExpected23 T a b c d e ≤ edgePenalty T
  vertex_nonincrease :
    vertexPenaltyExpected23 T a b c d e ≤ vertexPenalty T
Conditional theta nonincrease
theorem theta_pachner23_nonincreasing_of_penalty_controlled
  (T : Triangulation)
  (hT : WellFormedTets T)
  (λ : ℕ)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e)
  [hctrl : Valid23PenaltyControlled T a b c d e] :
  theta (pachner23 T a b c d e) λ ≤ theta T λ := by
  rw [theta_pachner23_eq_expected T hT λ a b c d e hvalid]
  unfold expectedTheta23 theta
  exact
    Nat.add_le_add
      hctrl.edge_nonincrease
      (Nat.mul_le_mul_left λ hctrl.vertex_nonincrease)
Frontier status
This theorem closes the theta nonincrease step conditional on local penalty control.
The remaining unconditional targets are:
lemma edgePenaltyExpected23_le_edgePenalty
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  edgePenaltyExpected23 T a b c d e ≤ edgePenalty T
lemma vertexPenaltyExpected23_le_vertexPenalty
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  vertexPenaltyExpected23 T a b c d e ≤ vertexPenalty T
No unconditional global theta nonincrease is claimed without these two local inequalities or an explicit Valid23PenaltyControlled instance.
