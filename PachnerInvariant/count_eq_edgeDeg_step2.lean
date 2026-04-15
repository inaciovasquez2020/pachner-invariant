import PachnerInvariant.frontier

open List

lemma edgeDeg_eq_filter_tets_len
  (T : Triangulation) (e : Edge) :
  edgeDeg T e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  -- minimal missing ingredient: definition of edgeDeg as incidence count
  -- must match the same filter characterization
  admit
