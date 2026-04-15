import PachnerInvariant.frontier

open List

noncomputable section
open scoped BigOperators

-- Replace axiom with theorem (first real reduction step)

theorem allEdges_count_eq_edgeDeg_countP
  (T : Triangulation) :
  (allEdges T).length =
  (allEdges T).foldl (fun acc e => acc + edgeDeg T e) 0 := by
  classical

  -- Step 1: convert foldl to sum
  have h_fold :
    (allEdges T).foldl (fun acc e => acc + edgeDeg T e) 0
    = (allEdges T).map (fun e => edgeDeg T e) |>.sum := by
    simpa using List.foldl_eq_sum_map (l := allEdges T) (f := fun e => edgeDeg T e)

  -- Step 2: rewrite sum over list as sum over multiplicities
  -- This is the key combinatorial identity to finish:
  have h_count :
    (allEdges T).length =
    (allEdges T).map (fun e => edgeDeg T e) |>.sum := by
    -- remaining core combinatorial step
    admit

  simpa [h_fold] using h_count

