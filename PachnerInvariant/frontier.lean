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
  [normalizeEdge (a,b), normalizeEdge (a,c), normalizeEdge (b,c)]

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

theorem twoTets_valid23 : Valid23 twoTets 0 1 2 3 4 := by
  unfold Valid23 pairwiseDistinct5 tetMemMod edgeMemNorm
  native_decide

theorem threeTets_valid23 : Valid23 threeTets 0 1 2 3 4 := by
  unfold Valid23 pairwiseDistinct5 tetMemMod edgeMemNorm
  native_decide

end PachnerInvariant
