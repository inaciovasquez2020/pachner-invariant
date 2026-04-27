import PachnerInvariant.Valid23Exact

namespace PachnerInvariant

def expectedVertexDeg23ExactDelta (_a _b _c p q : Vert) (v : Vert) : Nat :=
  if v = p then 2 else if v = q then 2 else 0


theorem expectedVertexDeg23ExactDelta_at_p
    (a b c p q : Vert) :
    expectedVertexDeg23ExactDelta a b c p q p = 2 := by
  simp [expectedVertexDeg23ExactDelta]

theorem expectedVertexDeg23ExactDelta_at_q
    (a b c p q : Vert) :
    expectedVertexDeg23ExactDelta a b c p q q = 2 := by
  by_cases hpq : q = p
  · simp [expectedVertexDeg23ExactDelta, hpq]
  · simp [expectedVertexDeg23ExactDelta, hpq]

theorem expectedVertexDeg23ExactDelta_of_ne
    {a b c p q v : Vert}
    (hvp : v ≠ p) (hvq : v ≠ q) :
    expectedVertexDeg23ExactDelta a b c p q v = 0 := by
  simp [expectedVertexDeg23ExactDelta, hvp, hvq]

/--
Open target.

This is the first theorem needed before the old frontier vertex-degree chain
can be repaired. It is intentionally not imported by the root module.
-/
def vertexDegreeExactTargetStatement : Prop :=
  ∀ {T : Triangulation} {a b c p q v : Vert},
    Valid23Exact T a b c p q →
    vertexDeg (pachner23 T a b c p q) v =
      vertexDeg T v + expectedVertexDeg23ExactDelta a b c p q v


def vertexIncidence (v : Vert) (t : Tet) : Bool :=
  (tetToVerts t).contains v

/--
Open local-count target.

This isolates the real combinatorial lemma behind the vertex-degree update:
the 2→3 move changes the count of tetrahedra incident to `v` by exactly the
expected vertex delta.
-/
def vertexIncidenceDeltaTargetStatement : Prop :=
  ∀ {T : Triangulation} {a b c p q v : Vert},
    Valid23Exact T a b c p q →
    (pachner23 T a b c p q).tets.countP (vertexIncidence v) =
      T.tets.countP (vertexIncidence v) + expectedVertexDeg23ExactDelta a b c p q v

theorem vertexDegreeExactTarget_of_incidenceDelta
    (hdelta : vertexIncidenceDeltaTargetStatement) :
    vertexDegreeExactTargetStatement := by
  intro T a b c p q v h
  unfold vertexDeg vertDeg
  exact hdelta h



def removedTets23 (a b c p q : Vert) : List Tet :=
  [(a,b,c,p), (a,b,c,q)]

def addedTets23 (a b c p q : Vert) : List Tet :=
  [(a,b,p,q), (a,c,p,q), (b,c,p,q)]

def keptTets23 (T : Triangulation) (a b c p q : Vert) : List Tet :=
  T.tets.filter (fun t => !(removedTets23 a b c p q).any (tetEq t))

theorem pachner23_tets_eq_kept_append_added
    (T : Triangulation) (a b c p q : Vert) :
    (pachner23 T a b c p q).tets =
      keptTets23 T a b c p q ++ addedTets23 a b c p q := by
  rfl


theorem keptAdded_countP_split
    {T : Triangulation} {a b c p q v : Vert} :
    (keptTets23 T a b c p q ++ addedTets23 a b c p q).countP
        (vertexIncidence v) =
      (keptTets23 T a b c p q).countP (vertexIncidence v) +
      (addedTets23 a b c p q).countP (vertexIncidence v) := by
  simp [List.countP_append]

/--
Open finite-list count target.

This is the exact list-count lemma needed to prove the incidence delta.
-/
def vertexIncidenceKeptAddedCountTargetStatement : Prop :=
  ∀ {T : Triangulation} {a b c p q v : Vert},
    Valid23Exact T a b c p q →
    (keptTets23 T a b c p q ++ addedTets23 a b c p q).countP
        (vertexIncidence v) =
      T.tets.countP (vertexIncidence v) + expectedVertexDeg23ExactDelta a b c p q v

theorem vertexIncidenceDeltaTarget_of_keptAddedCount
    (h : vertexIncidenceKeptAddedCountTargetStatement) :
    vertexIncidenceDeltaTargetStatement := by
  intro T a b c p q v hv
  rw [pachner23_tets_eq_kept_append_added]
  exact h hv


end PachnerInvariant
