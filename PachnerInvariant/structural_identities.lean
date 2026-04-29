import PachnerInvariant.frontier

open List

noncomputable section

lemma allEdges_eq_bind_edgesOfTet
  (T : Triangulation) :
  allEdges T = (allTets T).bind edgesOfTet := by
  classical
  rfl

lemma count_edgesOfTet_eq_indicator
  (t : Tet) (e : Edge) :
  (edgesOfTet t).count e =
    (if e ∈ edgesOfTet t then 1 else 0) := by
  classical
  by_cases h : e ∈ edgesOfTet t
  · have hnodup : (edgesOfTet t).Nodup := by
      exact edgesOfTet_nodup t
    have hmem : e ∈ edgesOfTet t := h
    simpa [h] using List.count_eq_one_of_mem hnodup hmem
  · have hnotmem : e ∉ edgesOfTet t := h
    simpa [h] using List.count_eq_zero_of_not_mem hnotmem

lemma edgeDeg_eq_incidence_count
  (T : Triangulation) (e : Edge) :
  edgeDeg T e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  rfl

lemma count_bind_edgesOfTet_eq_sum_indicators
  (L : List Tet) (e : Edge) :
  (L.bind edgesOfTet).count e =
  (L.map (fun t => if e ∈ edgesOfTet t then 1 else 0)).sum := by
  classical
  induction L with
  | nil =>
      simp
  | cons t ts ih =>
      rw [List.bind, List.count_append, ih, count_edgesOfTet_eq_indicator]
      simp

lemma sum_indicators_eq_filter_length
  (L : List Tet) (e : Edge) :
  (L.map (fun t => if e ∈ edgesOfTet t then 1 else 0)).sum =
  (List.filter (fun t => e ∈ edgesOfTet t) L).length := by
  classical
  induction L with
  | nil =>
      simp
  | cons t ts ih =>
      by_cases h : e ∈ edgesOfTet t
      · simp [h, ih]
      · simp [h, ih]

lemma count_allEdges_eq_filter_tets_len
  (T : Triangulation) (e : Edge) :
  (allEdges T).count e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  rw [allEdges_eq_bind_edgesOfTet]
  rw [count_bind_edgesOfTet_eq_sum_indicators]
  exact sum_indicators_eq_filter_length (L := allTets T) (e := e)

lemma edgeDeg_eq_filter_tets_len
    (T : Triangulation) (e : Edge) :
    edgeDeg T e =
      (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  simpa using edgeDeg_eq_incidence_count (T := T) (e := e)


lemma count_eq_edgeDeg
  (T : Triangulation) (e : Edge) :
  (allEdges T).count e = edgeDeg T e := by
  classical
  rw [count_allEdges_eq_filter_tets_len]
  symm
  exact edgeDeg_eq_incidence_count (T := T) (e := e)

