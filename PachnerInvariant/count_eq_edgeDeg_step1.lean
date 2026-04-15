import PachnerInvariant.frontier

open List

lemma count_allEdges_eq_filter_tets_len
  (T : Triangulation) (e : Edge) :
  (allEdges T).count e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  -- reduce count to membership expansion over concatenation
  -- assumes allEdges is generated from edgesOfTet over allTets
  admit
