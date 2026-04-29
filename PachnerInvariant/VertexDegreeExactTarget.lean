import PachnerInvariant.Valid23Exact
import PachnerInvariant.FilterRemovalCount

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

theorem keptRemovesExactIncidenceTarget :
    keptRemovesExactIncidenceTargetStatement := by
  exact keptRemovesExactIncidenceTarget_of_filterRemovesExactTwoTets
    (filterRemovesExactTwoTetsTarget_of_primitive
      filterRemovesExactTwoTetsPrimitiveTarget)


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
Open removed/added contribution target.

This isolates the local arithmetic needed after the append split:
the added tetrahedra contribute exactly the removed tetrahedra contribution
plus the expected vertex-degree delta.
-/
def removedAddedIncidenceContributionTargetStatement : Prop :=
  ∀ {a b c p q v : Vert},
    pairwiseDistinct5 a b c p q →
    (addedTets23 a b c p q).countP (vertexIncidence v) =
      (removedTets23 a b c p q).countP (vertexIncidence v) +
        expectedVertexDeg23ExactDelta a b c p q v


theorem removedAddedIncidenceContribution
    {a b c p q v : Vert}
    (h : pairwiseDistinct5 a b c p q) :
    (addedTets23 a b c p q).countP (vertexIncidence v) =
      (removedTets23 a b c p q).countP (vertexIncidence v) +
        expectedVertexDeg23ExactDelta a b c p q v := by
  rcases h with ⟨hab, hac, hap, haq, hbc, hbp, hbq, hcp, hcq, hpq⟩
  have hba : b ≠ a := Ne.symm hab
  have hca : c ≠ a := Ne.symm hac
  have hpa : p ≠ a := Ne.symm hap
  have hqa : q ≠ a := Ne.symm haq
  have hcb : c ≠ b := Ne.symm hbc
  have hpb : p ≠ b := Ne.symm hbp
  have hqb : q ≠ b := Ne.symm hbq
  have hpc : p ≠ c := Ne.symm hcp
  have hqc : q ≠ c := Ne.symm hcq
  have hqp : q ≠ p := Ne.symm hpq
  by_cases hvp : v = p
  · subst v
    simp [addedTets23, removedTets23, vertexIncidence, tetToVerts,
      expectedVertexDeg23ExactDelta, hpa, hpb, hpc, hpq]
  · by_cases hvq : v = q
    · subst v
      simp [addedTets23, removedTets23, vertexIncidence, tetToVerts,
        expectedVertexDeg23ExactDelta, hvp, hqa, hqb, hqc]
    · by_cases hva : v = a
      · subst v
        simp [addedTets23, removedTets23, vertexIncidence, tetToVerts,
          expectedVertexDeg23ExactDelta, hvp, hvq, hab, hac]
      · by_cases hvb : v = b
        · subst v
          simp [addedTets23, removedTets23, vertexIncidence, tetToVerts,
            expectedVertexDeg23ExactDelta, hvp, hvq, hba, hbc]
        · by_cases hvc : v = c
          · subst v
            simp [addedTets23, removedTets23, vertexIncidence, tetToVerts,
              expectedVertexDeg23ExactDelta, hvp, hvq, hca, hcb]
          · simp [addedTets23, removedTets23, vertexIncidence, tetToVerts,
              expectedVertexDeg23ExactDelta, hvp, hvq, hva, hvb, hvc]

theorem removedAddedIncidenceContributionTarget :
    removedAddedIncidenceContributionTargetStatement := by
  intro a b c p q v h
  exact removedAddedIncidenceContribution (a := a) (b := b) (c := c) (p := p) (q := q) (v := v) h


def removedContribution23 (a b c p q v : Vert) : Nat :=
  (removedTets23 a b c p q).countP (vertexIncidence v)

def addedContribution23 (a b c p q v : Vert) : Nat :=
  (addedTets23 a b c p q).countP (vertexIncidence v)

theorem removedContribution23_eq_countP
    (a b c p q v : Vert) :
    removedContribution23 a b c p q v =
      (removedTets23 a b c p q).countP (vertexIncidence v) := by
  rfl

theorem addedContribution23_eq_countP
    (a b c p q v : Vert) :
    addedContribution23 a b c p q v =
      (addedTets23 a b c p q).countP (vertexIncidence v) := by
  rfl

theorem removedAddedIncidenceContribution_named
    {a b c p q v : Vert}
    (h : pairwiseDistinct5 a b c p q) :
    addedContribution23 a b c p q v =
      removedContribution23 a b c p q v +
        expectedVertexDeg23ExactDelta a b c p q v := by
  unfold addedContribution23 removedContribution23
  exact removedAddedIncidenceContribution (a := a) (b := b) (c := c) (p := p) (q := q) (v := v) h

/--
Open kept/removal target.

This is the remaining global-list fact: filtering out the exact removed
tetrahedra subtracts precisely the removed local incidence contribution.
-/
def keptRemovesExactIncidenceTargetStatement : Prop :=
  ∀ {T : Triangulation} {a b c p q v : Vert},
    Valid23Exact T a b c p q →
    (keptTets23 T a b c p q).countP (vertexIncidence v) +
      (removedTets23 a b c p q).countP (vertexIncidence v) =
        T.tets.countP (vertexIncidence v)


/--
Open filter-removal target.

This is the exact remaining finite-list theorem: if the two removed
tetrahedron classes occur exactly once, then filtering out those classes
subtracts exactly their vertex-incidence contribution.
-/
def filterRemovesExactTwoTetsTargetStatement : Prop :=
  ∀ {T : Triangulation} {a b c p q v : Vert},
    Valid23Exact T a b c p q →
    (keptTets23 T a b c p q).countP (vertexIncidence v) +
      removedContribution23 a b c p q v =
        T.tets.countP (vertexIncidence v)

theorem keptRemovesExactIncidenceTarget_of_filterRemovesExactTwoTets
    (h : filterRemovesExactTwoTetsTargetStatement) :
    keptRemovesExactIncidenceTargetStatement := by
  intro T a b c p q v hv
  exact h hv

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



/--
Open primitive list-filter count lemma.

This is the exact finite-list theorem behind `filterRemovesExactTwoTetsTargetStatement`.
It says that if two removed tet classes occur with exact multiplicity one, then
filtering them out plus their removed contribution recovers the original
vertex-incidence count.
-/
def filterRemovesExactTwoTetsPrimitiveTargetStatement : Prop :=
  ∀ {T : Triangulation} {a b c p q v : Vert},
    countTetMod (a,b,c,p) T.tets = 1 →
    countTetMod (a,b,c,q) T.tets = 1 →
    (keptTets23 T a b c p q).countP (vertexIncidence v) +
      removedContribution23 a b c p q v =
        T.tets.countP (vertexIncidence v)



theorem keptAddedCountTarget :
    keptAddedCountTargetStatement := by
  intro T a b c p q v h
  rw [keptAdded_countP_split]
  rw [removedAddedIncidenceContributionTarget (a := a) (b := b) (c := c) (p := p) (q := q) (v := v) h]
  rw [← Nat.add_assoc]
  rw [keptRemovesExactIncidenceTarget (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := v) h]

theorem vertexIncidenceDeltaTarget :
    vertexIncidenceDeltaTargetStatement := by
  exact vertexIncidenceDeltaTarget_of_keptAddedCount keptAddedCountTarget


theorem filterRemovesExactTwoTetsPrimitiveTarget :
    filterRemovesExactTwoTetsPrimitiveTargetStatement := by
  intro T a b c p q v hp hq
  unfold keptTets23 removedContribution23
  exact countP_filter_not_add_of_filter_countP_eq
    (xs := T.tets)
    (p := vertexIncidence v)
    (q := fun t => (removedTets23 a b c p q).any (tetEq t))
    (removed := (removedTets23 a b c p q).countP (vertexIncidence v))
    (by
      simp [removedTets23, vertexIncidence, tetToVerts, hp, hq,
        Bool.or_eq_true, List.any_eq_true])


theorem filterRemovesExactTwoTetsTarget_of_primitive
    (h : filterRemovesExactTwoTetsPrimitiveTargetStatement) :
    filterRemovesExactTwoTetsTargetStatement := by
  intro T a b c p q v hv
  exact h
    (Valid23Exact_removed_p_count (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) hv)
    (Valid23Exact_removed_q_count (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) hv)


end PachnerInvariant
