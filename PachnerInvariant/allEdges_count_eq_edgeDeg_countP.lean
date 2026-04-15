import PachnerInvariant.frontier
import PachnerInvariant.count_eq_edgeDeg_step1
import PachnerInvariant.count_eq_edgeDeg_step2

open List

noncomputable section
open scoped BigOperators

-- Final combinatorial bridge (discharge count_eq_edgeDeg)

lemma count_eq_edgeDeg
  (T : Triangulation) (e : Edge) :
  (allEdges T).count e = edgeDeg T e := by
  classical
  -- canonical reduction: count = number of incident tetrahedra
  -- reduce to existence-of-tet characterization already present in frontier
  have h :
    (allEdges T).count e =
    (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
    simpa using count_allEdges_eq_filter_tets_len (T := T) (e := e)
  have h2 :
    edgeDeg T e =
    (List.filter (fun t => e ∈ edgesOfTet t) (allTets T)).length := by
    simpa using edgeDeg_eq_filter_tets_len (T := T) (e := e)
  simpa [h, h2]

lemma sum_edgeDeg_eq_sum_counts
  (T : Triangulation) :
  ((allEdges T).map (fun e => edgeDeg T e)).sum =
  ∑ e in (allEdges T).toFinset, edgeDeg T e := by
  classical
  -- standard list-to-finset multiplicity expansion
  simpa using List.sum_map_count (l := allEdges T) (f := fun e => edgeDeg T e)

lemma length_eq_sum_edge_counts
  (T : Triangulation) :
  (allEdges T).length =
  ∑ e in (allEdges T).toFinset, (allEdges T).count e := by
  classical
  simpa using List.length_eq_sum_count (l := allEdges T)

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
  have h4 :
    ∑ e in (allEdges T).toFinset, (allEdges T).count e =
    ∑ e in (allEdges T).toFinset, edgeDeg T e := by
    apply Finset.sum_congr rfl
    intro e he
    exact count_eq_edgeDeg T e
  simpa [h1] using (by simpa [h2, h3, h4])

