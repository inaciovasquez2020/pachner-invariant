import PachnerInvariant.frontier

open List

noncomputable section
open scoped BigOperators

-- Next micro-fix: isolate multiplicity counting lemma only

lemma length_eq_sum_edge_counts
  (T : Triangulation) :
  (allEdges T).length =
  ∑ e in (allEdges T).toFinset, (allEdges T).count e := by
  classical
  -- standard list-to-finset counting identity
  simpa using List.length_eq_sum_count (l := allEdges T)

lemma sum_edgeDeg_eq_sum_counts
  (T : Triangulation) :
  ((allEdges T).map (fun e => edgeDeg T e)).sum =
  ∑ e in (allEdges T).toFinset, edgeDeg T e := by
  classical
  -- reduction to multiplicity-weighted sum
  admit

theorem allEdges_count_eq_edgeDeg_countP
  (T : Triangulation) :
  (allEdges T).length =
  (allEdges T).foldl (fun acc e => acc + edgeDeg T e) 0 := by
  classical
  have h1 :
    (allEdges T).foldl (fun acc e => acc + edgeDeg T e) 0
    = ((allEdges T).map (fun e => edgeDeg T e)).sum := by
    simpa using List.foldl_eq_sum_map (l := allEdges T) (f := fun e => edgeDeg T e)
  have h2 := length_eq_sum_edge_counts (T := T)
  have h3 := sum_edgeDeg_eq_sum_counts (T := T)
  -- final remaining bridge: relate counts to edgeDeg
  admit
