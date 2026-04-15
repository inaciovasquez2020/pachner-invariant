import PachnerInvariant.frontier

open List

-- Structural identity 1: expansion of allEdges
lemma allEdges_eq_bind_edgesOfTet
  (T : Triangulation) :
  allEdges T = (allTets T).bind edgesOfTet := by
  classical
  -- must follow from the definition of allEdges in frontier
  -- reduce by unfolding definition
  unfold allEdges
  admit

-- Structural identity 2: definition of edgeDeg via incidence
lemma edgeDeg_eq_incidence_count
  (T : Triangulation) (e : Edge) :
  edgeDeg T e =
  (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
  classical
  -- must follow from definition of edgeDeg
  unfold edgeDeg
  admit

