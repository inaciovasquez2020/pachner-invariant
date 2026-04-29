import PachnerInvariant.allEdges_count_eq_edgeDeg_countP
import PachnerInvariant.NormalizeEdgeNoCollision
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

def boundaryEdges23 (a b c : Vert) : List (Vert × Vert) :=
  [normalizeEdge (a, b), normalizeEdge (b, c), normalizeEdge (c, a)]

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

def expectedVertexDeg23Delta (a b c p q : Vert) (v : Vert) : Nat :=
  if v = p then 1 else if v = q then 1 else 0


theorem vertDeg_pachner23_eq_expected
{T : Triangulation} {a b c p q : Vert} {v : Vert}
(h : Valid23 T a b c p q) :
vertexDeg (pachner23 T a b c p q) v =
vertexDeg T v + expectedVertexDeg23Delta a b c p q v := by
  by_cases hvp : v = p
  · simp [hvp]
  · by_cases hvq : v = q
    · simp [hvp, hvq]
    · simp [hvp, hvq]

theorem vertDeg_pachner23_at_p
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q) :
vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
  simpa [expectedVertexDeg23Delta] using
    (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)

theorem vertDeg_pachner23_at_q
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q) :
vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
  simpa [expectedVertexDeg23Delta] using
    (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)

theorem vertDeg_pachner23_at_p_le_six
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q)
(hp : vertexDeg T p ≤ 5) :
vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
  rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  omega

theorem vertDeg_pachner23_at_q_le_six
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q)
(hq : vertexDeg T q ≤ 5) :
vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
  rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  omega

theorem vertSqDefect_p_monotone
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q)
(hp : vertexDeg T p ≤ 5) :
(vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
  rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  omega

theorem vertSqDefect_q_monotone
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q)
(hq : vertexDeg T q ≤ 5) :
(vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
  rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  omega

theorem edgeDeg_pachner23_new_edge_three
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q) :
edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
  have h_edge :=
    edgeDeg_pachner23_delta
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
  have h_zero : edgeDeg T (normalizeEdge (p,q)) = 0 :=
    edgeDeg_zero_of_newEdgeAbsent (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
  have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
  simpa [h_zero, h_nobdry] using h_edge

theorem vertSqDefect_p_strict
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q)
(hp : vertexDeg T p ≤ 5) :
(vertexDeg (pachner23 T a b c p q) p - 6)^2 < (vertexDeg T p - 6)^2 := by
  rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  omega

theorem vertSqDefect_q_strict
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q)
(hq : vertexDeg T q ≤ 5) :
(vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
  rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  omega

theorem theta_pachner23_delta_expanded
    {T : Triangulation} {a b c p q : Vert} (lam : Nat)
    (h : Valid23 T a b c p q) :
    theta (pachner23 T a b c p q) lam - theta T lam =
      ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
      lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
             ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
  have h_edge :=
    edgeDeg_pachner23_delta
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
  have h_vert_p :=
    vertDeg_pachner23_eq_expected
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
  have h_vert_q :=
    vertDeg_pachner23_eq_expected
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
  simp [theta, h_edge, h_vert_p, h_vert_q]

theorem pachner23_descent_under_vertex_le_five
    {T : Triangulation} {a b c p q : Vert} {lam : Nat}
    (h : Valid23 T a b c p q)
    (hlam : 0 < lam)
    (hp : vertexDeg T p ≤ 5)
    (hq : vertexDeg T q ≤ 5) :
    theta (pachner23 T a b c p q) lam < theta T lam := by
  have hdelta :=
    theta_pachner23_delta_expanded
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h
  have hnew :=
    edgeDeg_pachner23_new_edge_three
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
  have hpstrict :=
    vertSqDefect_p_strict
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hp
  have hqstrict :=
    vertSqDefect_q_strict
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
  have hpneg :
      (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
    omega
  have hqneg :
      (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
    omega
  have hverts :
      (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
      (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
    omega
  have hweighted :
      (lam : Int) *
      ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
    omega
  have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
    rw [hdelta]
    rw [hnew]
    omega
  omega

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



def Valid23RawReady (T : Triangulation) (a b c p q : Vert) : Prop :=
  Valid23 T a b c p q ∧
  WellFormedTets T ∧
  WellFormedTets (pachner23 T a b c p q)



theorem rawEdges_count_eq_edgeDeg_countP_of_Valid23RawReady
    {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
    (h : Valid23RawReady T a b c p q) :
    (rawEdges T).count (normalizeEdge e) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
  exact rawEdges_count_eq_edgeDeg_countP T h.2.1 e

theorem rawEdges_count_eq_edgeDeg_countP_pachner23_of_Valid23RawReady
    {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
    (h : Valid23RawReady T a b c p q) :
    (rawEdges (pachner23 T a b c p q)).count (normalizeEdge e) =
      (pachner23 T a b c p q).tets.countP
        (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
  exact rawEdges_count_eq_edgeDeg_countP
    (pachner23 T a b c p q) h.2.2 e


theorem expectedEdgeDeg23_delta_normal_form
{T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
(h : Valid23 T a b c p q) :
expectedEdgeDeg23 T a b c p q e =
edgeDeg T (normalizeEdge e) +
(if normalizeEdge e = normalizeEdge (p,q) then 3
 else if (crossEdges23 a b c p q).contains (normalizeEdge e) then 1
 else 0) -
(if (boundaryEdges23 a b c).contains (normalizeEdge e) then 1 else 0) := by
  simp [expectedEdgeDeg23]

theorem edgeDeg_pachner23_delta
  {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
  (h : Valid23 T a b c p q) :
  let e' := normalizeEdge e
  edgeDeg (pachner23 T a b c p q) e' =
    edgeDeg T e' +
    (if e' = normalizeEdge (p,q) then 3
     else if (crossEdges23 a b c p q).contains e' then 1
     else 0) -
    (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
  dsimp
  rw [← allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
  rw [← allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
  simpa using
    allEdges_pachner23_count_delta
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h


theorem edgeDeg_pachner23_eq_expected
  {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
  (h : Valid23 T a b c p q) :
  edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
    expectedEdgeDeg23 T a b c p q e := by
  rw [edgeDeg_pachner23_delta
      (T := T) (a := a) (b := b) (c := c)
      (p := p) (q := q) (e := e) h]
  exact expectedEdgeDeg23_delta_normal_form
      (T := T) (a := a) (b := b) (c := c)
      (p := p) (q := q) (e := e) h


theorem edgeDeg_eq_count_tets
    (T : Triangulation) (e : Vert × Vert) :
    edgeDeg T (normalizeEdge e) =
      T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
  rfl

theorem count_zero_of_newEdgeAbsent
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    List.count (normalizeEdge (p,q)) (allEdges T) = 0 := by
  have habs :
      ¬ edgeMemNorm (p, q) (allEdges T) := h.right.right.right.right.right.right.right.right.right.right.right
  simp [edgeMemNorm] at habs
  apply List.count_eq_zero.mpr
  intro he
  by_cases hpq0 : p ≤ q
  · have hmem : (p, q) ∈ allEdges T := by
      simpa [normalizeEdge, hpq0] using he
    exact (habs p q hmem) rfl
  · have hqp : q ≤ p := Nat.le_of_lt (Nat.lt_of_not_ge hpq0)
    have hmem : (q, p) ∈ allEdges T := by
      simpa [normalizeEdge, hpq0] using he
    have heq : normalizeEdge (q, p) = normalizeEdge (p, q) := by
      simp [normalizeEdge, hpq0, hqp]
    exact (habs q p hmem) heq


theorem edgeDeg_zero_of_newEdgeAbsent
{T : Triangulation} {a b c p q : Vert}
(h : Valid23 T a b c p q) :
edgeDeg T (normalizeEdge (p,q)) = 0 := by
rw [edgeDeg_eq_count_tets]
rw [← allEdges_count_eq_edgeDeg_countP T (p, q)]
exact count_zero_of_newEdgeAbsent h

theorem Valid23.newEdgeCase
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    let e' := normalizeEdge (p, q)
    ¬ (boundaryEdges23 a b c).contains e' := by
  dsimp
  rcases h.right.right.right.right.right.left with
    ⟨hab, hac, hap, haq, hbc, hbp, hbq, hcp, hcq, hpq⟩
  simp [boundaryEdges23, List.contains_eq_mem]
  constructor
  · intro hEq
    by_cases hpq0 : p ≤ q
    · by_cases hab0 : a ≤ b
      · simp [normalizeEdge, hpq0, hab0] at hEq
        rcases hEq with ⟨hp, hq⟩
        subst hp
        subst hq
        contradiction
      · simp [normalizeEdge, hpq0, hab0] at hEq
        rcases hEq with ⟨hp, hq⟩
        subst hp
        subst hq
        contradiction
    · by_cases hab0 : a ≤ b
      · simp [normalizeEdge, hpq0, hab0] at hEq
        rcases hEq with ⟨hq, hp⟩
        subst hq
        subst hp
        contradiction
      · simp [normalizeEdge, hpq0, hab0] at hEq
        rcases hEq with ⟨hq, hp⟩
        subst hq
        subst hp
        contradiction
  · constructor
    · intro hEq
      by_cases hpq0 : p ≤ q
      · by_cases hbc0 : b ≤ c
        · simp [normalizeEdge, hpq0, hbc0] at hEq
          rcases hEq with ⟨hp, hq⟩
          subst hp
          subst hq
          contradiction
        · simp [normalizeEdge, hpq0, hbc0] at hEq
          rcases hEq with ⟨hp, hq⟩
          subst hp
          subst hq
          contradiction
      · by_cases hbc0 : b ≤ c
        · simp [normalizeEdge, hpq0, hbc0] at hEq
          rcases hEq with ⟨hq, hp⟩
          subst hq
          subst hp
          contradiction
        · simp [normalizeEdge, hpq0, hbc0] at hEq
          rcases hEq with ⟨hq, hp⟩
          subst hq
          subst hp
          contradiction
    · intro hEq
      by_cases hpq0 : p ≤ q
      · by_cases hca0 : c ≤ a
        · simp [normalizeEdge, hpq0, hca0] at hEq
          rcases hEq with ⟨hp, hq⟩
          subst hp
          subst hq
          contradiction
        · simp [normalizeEdge, hpq0, hca0] at hEq
          rcases hEq with ⟨hp, hq⟩
          subst hp
          subst hq
          contradiction
      · by_cases hca0 : c ≤ a
        · simp [normalizeEdge, hpq0, hca0] at hEq
          rcases hEq with ⟨hq, hp⟩
          subst hq
          subst hp
          contradiction
        · simp [normalizeEdge, hpq0, hca0] at hEq
          rcases hEq with ⟨hq, hp⟩
          subst hq
          subst hp
          contradiction




theorem mem_filter_ne [DecidableEq α] (x a : α) (xs : List α) :
    x ∈ xs.filter (fun b => ¬ (b == a)) ↔ x ∈ xs ∧ x ≠ a := by
  rw [List.mem_filter]
  simp [beq_iff_eq]



theorem edgeEq_true_iff
    (e d : Vert × Vert) :
    edgeEq e d = true ↔
      (e.1 = d.1 ∧ e.2 = d.2) ∨ (e.1 = d.2 ∧ e.2 = d.1) := by
  simp [edgeEq]


theorem edgeMem_allEdges_iff_exists_tet
{T : Triangulation} {e : Vert × Vert} :
e ∈ allEdges T ↔ ∃ t ∈ T.tets, e ∈ t.edges := by
  constructor
  · intro h
    rcases h with ⟨t, ht, hmem⟩
    exact ⟨t, ht, hmem⟩
  · intro h
    rcases h with ⟨t, ht, hmem⟩
    exact ⟨t, ht, hmem⟩

theorem edgeDeg_pos_iff_exists_tet
{T : Triangulation} {e : Vert × Vert} :
edgeDeg T e > 0 ↔ ∃ t ∈ T.tets, e ∈ t.edges := by
  constructor
  · intro h
    rcases h with ⟨t, ht, hmem⟩
    exact ⟨t, ht, hmem⟩
  · intro h
    rcases h with ⟨t, ht, hmem⟩
    exact ⟨t, ht, hmem⟩

theorem edgeMem_allEdges_iff_edgeDeg_pos
    (T : Triangulation) (e : Vert × Vert) :
    ((allEdges T).contains (normalizeEdge e) = true) ↔
      0 < edgeDeg T (normalizeEdge e) := by
  rw [edgeMem_allEdges_iff_exists_tet]
  rw [edgeDeg_pos_iff_exists_tet]




lemma tetIncidence_pachner23_delta
  {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
  (h : Valid23 T a b c p q) :
  let e' := normalizeEdge e
  (edgeDeg (pachner23 T a b c p q) e' - edgeDeg T e') =
    (if e' = normalizeEdge (p,q) then 3
     else if (crossEdges23 a b c p q).contains e' then 1
     else 0) -
    (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
  by_cases hpq : normalizeEdge e = normalizeEdge (p,q)
  · simp [hpq]
  · by_cases hcross : (crossEdges23 a b c p q).contains (normalizeEdge e)
    · simp [hpq, hcross]
    · by_cases hbdry : (boundaryEdges23 a b c).contains (normalizeEdge e)
      · simp [hpq, hcross, hbdry]
      · simp [hpq, hcross, hbdry]

lemma List.count_bind
  {α β : Type} [DecidableEq β]
  (f : α → List β) (l : List α) (x : β) :
  (l.bind f).count x = (l.map (fun a => (f a).count x)).sum := by
  induction l with
  | nil =>
      simp
  | cons a t ih =>
      simp [List.bind, List.count_append, ih, Nat.add_comm, Nat.add_left_comm, Nat.add_assoc]

theorem allEdges_pachner23_count_delta
  {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
  (h : Valid23 T a b c p q) :
  let e' := normalizeEdge e
  (allEdges (pachner23 T a b c p q)).count e' =
    (allEdges T).count e' +
    (if e' = normalizeEdge (p,q) then 3
     else if (crossEdges23 a b c p q).contains e' then 1
     else 0) -
    (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
  dsimp
  rw [allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
  rw [allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
  exact tetIncidence_pachner23_delta
    (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
