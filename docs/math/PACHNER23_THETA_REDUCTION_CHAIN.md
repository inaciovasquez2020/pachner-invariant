# Pachner 2-3 Theta Reduction Chain

Status: Conditional.

## Closed structural chain

The 2-3 Pachner move admits the following structural decomposition:

```lean
@[simp]
lemma pachner23_tets_eq_unchanged_union_added
  (T : Triangulation)
  (a b c d e : Vert) :
  (pachner23 T a b c d e).tets =
    (T.tets.filter (fun t =>
      t ≠ makeTet a b c d ∧
      t ≠ makeTet a b c e)) ∪
    ({makeTet a b d e, makeTet b c d e, makeTet a c d e} : Finset Tetrahedron)
The added tetrahedra are disjoint from the unchanged old tetrahedra under Valid23:
lemma valid23_added_tet_not_in_old
  (T : Triangulation)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  makeTet a b d e ∉ T.tets ∧
  makeTet b c d e ∉ T.tets ∧
  makeTet a c d e ∉ T.tets
Hence edge and vertex degrees after the move are exactly their expected values:
lemma edgeDeg_pachner23_eq_expected
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e)
  (x y : Vert) :
  edgeDeg (pachner23 T a b c d e) (normalizeEdge (x, y)) =
    expectedEdgeDeg23 T a b c d e (normalizeEdge (x, y))
lemma vertexDeg_pachner23_eq_expected
  (T : Triangulation)
  (hT : WellFormedTets T)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e)
  (v : Vert) :
  vertexDeg (pachner23 T a b c d e) v =
    expectedVertexDeg23 T a b c d e v
Therefore the theta value after the move equals the expected theta value:
theorem theta_pachner23_eq_expected
  (T : Triangulation)
  (hT : WellFormedTets T)
  (λ : ℕ)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e) :
  theta (pachner23 T a b c d e) λ =
    expectedTheta23 T λ a b c d e
Remaining obstruction
The full nonincrease theorem reduces to exactly two local penalty inequalities:
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
Given those two inequalities, the theta nonincrease theorem is immediate:
theorem theta_pachner23_nonincreasing
  (T : Triangulation)
  (hT : WellFormedTets T)
  (λ : ℕ)
  (a b c d e : Vert)
  (hvalid : Valid23 T a b c d e)
  (hedge :
    edgePenaltyExpected23 T a b c d e ≤ edgePenalty T)
  (hvertex :
    vertexPenaltyExpected23 T a b c d e ≤ vertexPenalty T) :
  theta (pachner23 T a b c d e) λ ≤ theta T λ
Frontier lock
No unconditional theta decrease or nonincrease is claimed until the two local penalty inequalities are proved.
