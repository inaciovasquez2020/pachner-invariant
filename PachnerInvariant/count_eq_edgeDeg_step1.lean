import PachnerInvariant.frontier

open List

lemma count_allEdges_eq_filter_tets_len
  (T : Triangulation) (e : Edge) :
  (allEdges T).count e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  -- minimal missing ingredient: representation of allEdges as concatenation over tets
  -- this step reduces to:
  -- allEdges T = (allTets T).bind edgesOfTet
  admit
