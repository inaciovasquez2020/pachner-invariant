import PachnerInvariant.frontier

open List

noncomputable section

-- Identity 1
lemma allEdges_eq_bind_edgesOfTet
  (T : Triangulation) :
  allEdges T = (allTets T).bind edgesOfTet := by
  classical
  rfl

-- Local multiplicity lemma (final remaining local fact)
lemma count_edgesOfTet_eq_indicator
  (t : Tet) (e : Edge) :
  (edgesOfTet t).count e =
    (if e ∈ edgesOfTet t then 1 else 0) := by
  classical
  by_cases h : e ∈ edgesOfTet t
  · -- e appears exactly once in the edge list of a tetrahedron
    have : (edgesOfTet t).count e = 1 := by
      admit
    simp [h, this]
  · -- e does not appear
    have : (edgesOfTet t).count e = 0 := by
      admit
    simp [h, this]

-- Identity 2
lemma edgeDeg_eq_incidence_count
  (T : Triangulation) (e : Edge) :
  edgeDeg T e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  rfl

-- Bind-count reduction
lemma count_allEdges_eq_filter_tets_len
  (T : Triangulation) (e : Edge) :
  (allEdges T).count e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  have h := allEdges_eq_bind_edgesOfTet (T := T)
  -- count over bind = sum of counts
  have :
    (allEdges T).count e =
    ((allTets T).bind edgesOfTet).count e := by simpa [h]
  -- reduce to sum over tets using indicator lemma
  admit

-- Final bridge
lemma count_eq_edgeDeg
  (T : Triangulation) (e : Edge) :
  (allEdges T).count e = edgeDeg T e := by
  classical
  have h1 := count_allEdges_eq_filter_tets_len (T := T) (e := e)
  have h2 := edgeDeg_eq_incidence_count (T := T) (e := e)
  simpa [h2] using h1

