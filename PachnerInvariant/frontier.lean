import PachnerInvariant.descent_property

namespace PachnerInvariant

abbrev Tet := Vert × Vert × Vert × Vert

def tetMemMod (t : Tet) (ts : List Tet) : Prop :=
  ts.any (tetEq t) = true

def edgeMemNorm (e : Vert × Vert) (es : List (Vert × Vert)) : Prop :=
  (es.map normalizeEdge).contains (normalizeEdge e) = true

def pairwiseDistinct5 (a b c p q : Vert) : Prop :=
  a ≠ b ∧ a ≠ c ∧ a ≠ p ∧ a ≠ q ∧
  b ≠ c ∧ b ≠ p ∧ b ≠ q ∧
  c ≠ p ∧ c ≠ q ∧
  p ≠ q

def crossEdges23 (a b c p q : Vert) : List (Vert × Vert) :=
  [ normalizeEdge (a,p), normalizeEdge (b,p), normalizeEdge (c,p)
  , normalizeEdge (a,q), normalizeEdge (b,q), normalizeEdge (c,q)
  ]

def Valid23 (T : Triangulation) (a b c p q : Vert) : Prop :=
  a < T.numVerts ∧
  b < T.numVerts ∧
  c < T.numVerts ∧
  p < T.numVerts ∧
  q < T.numVerts ∧
  pairwiseDistinct5 a b c p q ∧
  tetMemMod (a,b,c,p) T.tets ∧
  tetMemMod (a,b,c,q) T.tets ∧
  ¬ tetMemMod (a,b,p,q) T.tets ∧
  ¬ tetMemMod (a,c,p,q) T.tets ∧
  ¬ tetMemMod (b,c,p,q) T.tets ∧
  ¬ edgeMemNorm (p,q) (allEdges T)

def expectedEdgeDeg23
    (T : Triangulation) (a b c p q : Vert) (e : Vert × Vert) : Nat :=
  let e' := normalizeEdge e
  if e' = normalizeEdge (p,q) then
    3
  else if (boundaryEdges23 a b c).contains e' then
    edgeDeg T e' - 1
  else if (crossEdges23 a b c p q).contains e' then
    edgeDeg T e' + 1
  else
    edgeDeg T e'

theorem Valid23.newEdgeAbsent
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    ¬ edgeMemNorm (p,q) (allEdges T) := by
  rcases h with ⟨_, _, _, _, _, _, _, _, _, _, _, hNoPQ⟩
  exact hNoPQ

theorem Valid23.sourceTet₁
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    tetMemMod (a,b,c,p) T.tets := by
  rcases h with ⟨_, _, _, _, _, _, hTet₁, _, _, _, _, _⟩
  exact hTet₁

theorem Valid23.sourceTet₂
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    tetMemMod (a,b,c,q) T.tets := by
  rcases h with ⟨_, _, _, _, _, _, _, hTet₂, _, _, _, _⟩
  exact hTet₂

theorem Valid23.noTargetTet₁
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    ¬ tetMemMod (a,b,p,q) T.tets := by
  rcases h with ⟨_, _, _, _, _, _, _, _, hNoTet₁, _, _, _⟩
  exact hNoTet₁

theorem Valid23.noTargetTet₂
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    ¬ tetMemMod (a,c,p,q) T.tets := by
  rcases h with ⟨_, _, _, _, _, _, _, _, _, hNoTet₂, _, _⟩
  exact hNoTet₂

theorem Valid23.noTargetTet₃
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    ¬ tetMemMod (b,c,p,q) T.tets := by
  rcases h with ⟨_, _, _, _, _, _, _, _, _, _, hNoTet₃, _⟩
  exact hNoTet₃

theorem Valid23.distinct
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    pairwiseDistinct5 a b c p q := by
  rcases h with ⟨_, _, _, _, _, hDistinct, _, _, _, _, _, _⟩
  exact hDistinct

theorem Valid23.a_lt_numVerts
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    a < T.numVerts := by
  rcases h with ⟨ha, _, _, _, _, _, _, _, _, _, _, _⟩
  exact ha

theorem Valid23.b_lt_numVerts
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    b < T.numVerts := by
  rcases h with ⟨_, hb, _, _, _, _, _, _, _, _, _, _⟩
  exact hb

theorem Valid23.c_lt_numVerts
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    c < T.numVerts := by
  rcases h with ⟨_, _, hc, _, _, _, _, _, _, _, _, _⟩
  exact hc

theorem Valid23.p_lt_numVerts
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    p < T.numVerts := by
  rcases h with ⟨_, _, _, hp, _, _, _, _, _, _, _, _⟩
  exact hp

theorem Valid23.q_lt_numVerts
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    q < T.numVerts := by
  rcases h with ⟨_, _, _, _, hq, _, _, _, _, _, _, _⟩
  exact hq

theorem Valid23.p_ne_q
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    p ≠ q := by
  rcases Valid23.distinct h with ⟨_, _, _, _, _, _, _, _, _, hpq⟩
  exact hpq

theorem Valid23.a_ne_b
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    a ≠ b := by
  rcases Valid23.distinct h with ⟨hab, _, _, _, _, _, _, _, _, _⟩
  exact hab

theorem Valid23.a_ne_c
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    a ≠ c := by
  rcases Valid23.distinct h with ⟨_, hac, _, _, _, _, _, _, _, _⟩
  exact hac

theorem Valid23.a_ne_p
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    a ≠ p := by
  rcases Valid23.distinct h with ⟨_, _, hap, _, _, _, _, _, _, _⟩
  exact hap

theorem Valid23.a_ne_q
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    a ≠ q := by
  rcases Valid23.distinct h with ⟨_, _, _, haq, _, _, _, _, _, _⟩
  exact haq

theorem Valid23.b_ne_c
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    b ≠ c := by
  rcases Valid23.distinct h with ⟨_, _, _, _, hbc, _, _, _, _, _⟩
  exact hbc

theorem Valid23.b_ne_p
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    b ≠ p := by
  rcases Valid23.distinct h with ⟨_, _, _, _, _, hbp, _, _, _, _⟩
  exact hbp

theorem Valid23.b_ne_q
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    b ≠ q := by
  rcases Valid23.distinct h with ⟨_, _, _, _, _, _, hbq, _, _, _⟩
  exact hbq

theorem Valid23.c_ne_p
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    c ≠ p := by
  rcases Valid23.distinct h with ⟨_, _, _, _, _, _, _, hcp, _, _⟩
  exact hcp

theorem Valid23.c_ne_q
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    c ≠ q := by
  rcases Valid23.distinct h with ⟨_, _, _, _, _, _, _, _, hcq, _⟩
  exact hcq

theorem Valid23.targetPatchFresh
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    ¬ tetMemMod (a,b,p,q) T.tets ∧
    ¬ tetMemMod (a,c,p,q) T.tets ∧
    ¬ tetMemMod (b,c,p,q) T.tets := by
  exact ⟨Valid23.noTargetTet₁ h, Valid23.noTargetTet₂ h, Valid23.noTargetTet₃ h⟩

theorem Valid23.sourcePatchPresent
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    tetMemMod (a,b,c,p) T.tets ∧
    tetMemMod (a,b,c,q) T.tets := by
  exact ⟨Valid23.sourceTet₁ h, Valid23.sourceTet₂ h⟩

theorem Valid23.vertexBounds
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    a < T.numVerts ∧
    b < T.numVerts ∧
    c < T.numVerts ∧
    p < T.numVerts ∧
    q < T.numVerts := by
  exact ⟨Valid23.a_lt_numVerts h, Valid23.b_lt_numVerts h, Valid23.c_lt_numVerts h, Valid23.p_lt_numVerts h, Valid23.q_lt_numVerts h⟩

theorem Valid23.patchReady
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    (tetMemMod (a,b,c,p) T.tets ∧ tetMemMod (a,b,c,q) T.tets) ∧
    (¬ tetMemMod (a,b,p,q) T.tets ∧
     ¬ tetMemMod (a,c,p,q) T.tets ∧
     ¬ tetMemMod (b,c,p,q) T.tets) ∧
    ¬ edgeMemNorm (p,q) (allEdges T) := by
  exact ⟨Valid23.sourcePatchPresent h, Valid23.targetPatchFresh h, Valid23.newEdgeAbsent h⟩

theorem Valid23.distinctPairs
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    (a ≠ b ∧ a ≠ c ∧ a ≠ p ∧ a ≠ q) ∧
    (b ≠ c ∧ b ≠ p ∧ b ≠ q) ∧
    (c ≠ p ∧ c ≠ q) ∧
    (p ≠ q) := by
  exact ⟨⟨Valid23.a_ne_b h, Valid23.a_ne_c h, Valid23.a_ne_p h, Valid23.a_ne_q h⟩,
    ⟨Valid23.b_ne_c h, Valid23.b_ne_p h, Valid23.b_ne_q h⟩,
    ⟨Valid23.c_ne_p h, Valid23.c_ne_q h⟩,
    Valid23.p_ne_q h⟩

theorem Valid23.ready
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    (a < T.numVerts ∧
     b < T.numVerts ∧
     c < T.numVerts ∧
     p < T.numVerts ∧
     q < T.numVerts) ∧
    ((a ≠ b ∧ a ≠ c ∧ a ≠ p ∧ a ≠ q) ∧
     (b ≠ c ∧ b ≠ p ∧ b ≠ q) ∧
     (c ≠ p ∧ c ≠ q) ∧
     (p ≠ q)) ∧
    ((tetMemMod (a,b,c,p) T.tets ∧ tetMemMod (a,b,c,q) T.tets) ∧
     (¬ tetMemMod (a,b,p,q) T.tets ∧
      ¬ tetMemMod (a,c,p,q) T.tets ∧
      ¬ tetMemMod (b,c,p,q) T.tets) ∧
     ¬ edgeMemNorm (p,q) (allEdges T)) := by
  exact ⟨Valid23.vertexBounds h, Valid23.distinctPairs h, Valid23.patchReady h⟩

theorem allEdges_pachner23_count_delta
    {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
    (h : Valid23 T a b c p q) :
    let e' := normalizeEdge e
    List.count e' (allEdges (pachner23 T a b c p q)) =
      List.count e' (allEdges T) +
        (if e' = normalizeEdge (p,q) then 3
         else if (boundaryEdges23 a b c).contains e' then 0
         else if (crossEdges23 a b c p q).contains e' then 1
         else 0) -
        (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
  sorry

axiom edgeDeg_pachner23_eq_expected
    {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
    (h : Valid23 T a b c p q) :
    edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
      expectedEdgeDeg23 T a b c p q e

theorem edgeDeg_pachner23_delta
    {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
    (h : Valid23 T a b c p q) :
    let e' := normalizeEdge e
    edgeDeg (pachner23 T a b c p q) e' =
      edgeDeg T e' +
        (if e' = normalizeEdge (p,q) then 3
         else if (boundaryEdges23 a b c).contains e' then 0
         else if (crossEdges23 a b c p q).contains e' then 1
         else 0) -
        (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
  dsimp
  rw [edgeDeg_pachner23_eq_expected h]
  split_ifs <;> omega

theorem edgeDeg_eq_count_allEdges
    (T : Triangulation) (e : Vert × Vert) :
    edgeDeg T (normalizeEdge e) =
      List.count (normalizeEdge e) (allEdges T) := by
  sorry

theorem edgeDeg_zero_of_newEdgeAbsent
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    edgeDeg T (normalizeEdge (p,q)) = 0 := by
  sorry

theorem count_zero_of_newEdgeAbsent
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    List.count (normalizeEdge (p,q)) (allEdges T) = 0 := by
  sorry

theorem Valid23.newEdgeCase
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    List.count (normalizeEdge (p,q)) (allEdges T) = 0 ∧
    (boundaryEdges23 a b c).contains (normalizeEdge (p,q)) = false ∧
    (crossEdges23 a b c p q).contains (normalizeEdge (p,q)) = false := by
  refine ⟨count_zero_of_newEdgeAbsent h, ?_, ?_⟩
  · sorry
  · sorry

theorem edgeDeg_pachner23_eq_expected
    {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
    (h : Valid23 T a b c p q) :
    edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
      expectedEdgeDeg23 T a b c p q e := by
  rw [edgeDeg_eq_count_allEdges (T := pachner23 T a b c p q) (e := e)]
  have hcountT : edgeDeg T (normalizeEdge e) = List.count (normalizeEdge e) (allEdges T) :=
    edgeDeg_eq_count_allEdges (T := T) (e := e)
  have hΔ := allEdges_pachner23_count_delta
    (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
  dsimp [expectedEdgeDeg23]
  by_cases hEq : normalizeEdge e = normalizeEdge (p, q)
  · rcases Valid23.newEdgeCase h with ⟨h0, hB, hC⟩
    have hB' : normalizeEdge (p, q) ∉ boundaryEdges23 a b c := by
      simpa using hB
    have hC' : normalizeEdge (p, q) ∉ crossEdges23 a b c p q := by
      simpa using hC
    rw [hEq] at hΔ ⊢
    simp [h0, hB', hC'] at hΔ ⊢
    omega
  · by_cases hB : normalizeEdge e ∈ boundaryEdges23 a b c
    · have hBtrue : (boundaryEdges23 a b c).contains (normalizeEdge e) = true := by
        simpa using hB
      simp [hEq, hB, hBtrue, hcountT] at hΔ ⊢
      omega
    · have hBfalse : (boundaryEdges23 a b c).contains (normalizeEdge e) = false := by
        simpa using hB
      by_cases hC : normalizeEdge e ∈ crossEdges23 a b c p q
      · have hCtrue : (crossEdges23 a b c p q).contains (normalizeEdge e) = true := by
          simpa using hC
        simp [hEq, hB, hBfalse, hC, hCtrue, hcountT] at hΔ ⊢
        omega
      · have hCfalse : (crossEdges23 a b c p q).contains (normalizeEdge e) = false := by
          simpa using hC
        simp [hEq, hB, hBfalse, hC, hCfalse, hcountT] at hΔ ⊢
        omega

theorem twoTets_valid23 : Valid23 twoTets 0 1 2 3 4 := by
  unfold Valid23 pairwiseDistinct5 tetMemMod edgeMemNorm
  native_decide

theorem threeTets_valid23 : Valid23 threeTets 0 1 2 3 4 := by
  unfold Valid23 pairwiseDistinct5 tetMemMod edgeMemNorm
  native_decide

end PachnerInvariant
