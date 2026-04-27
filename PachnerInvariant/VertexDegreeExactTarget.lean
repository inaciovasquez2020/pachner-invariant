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


end PachnerInvariant
