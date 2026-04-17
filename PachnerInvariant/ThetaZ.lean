import Mathlib
import PachnerInvariant

open List

namespace PachnerInvariant

def sqDefectZ (d target : Nat) : Int :=
  let z : Int := (d : Int) - (target : Int)
  z * z

def thetaZ (T : Triangulation) (lam : Int) : Int :=
  ((allEdges T).foldl (fun acc e => acc + sqDefectZ (edgeDeg T e) 3) 0) +
  lam * ((allVertices T).foldl (fun acc v => acc + sqDefectZ (vertexDeg T v) 6) 0)

theorem allEdges_mem_of_pachner23_new_edge
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
  sorry

theorem allEdges_pachner23_eq
    {T : Triangulation} {a b c p q : Vert}
    (h : Valid23 T a b c p q) :
    allEdges (pachner23 T a b c p q) =
      F (allEdges T) a b c p q := by
  sorry

theorem List_foldl_congr_sub_eq_changed_terms
    {α : Type} (l : List α) (f g : α → Int) :
    l.foldl (fun s x => s + f x) 0 - l.foldl (fun s x => s + g x) 0 =
      (l.foldl (fun s x => s + (f x - g x)) 0) := by
  induction l with
  | nil => simp
  | cons x xs ih => simpa [ih, sub_eq_add_neg, add_assoc, add_left_assoc, add_comm]

theorem thetaZ_pachner23_delta_expanded
    {T : Triangulation} {a b c p q : Vert} {lam : Int}
    (h : Valid23 T a b c p q) :
    thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
      DeltaThetaZ T a b c p q lam := by
  sorry

theorem pachner23_descent_iff_vertex_sum_le_ten
    {T : Triangulation} {a b c p q : Vert} {lam : Int}
    (h : Valid23 T a b c p q) (hlam : 0 < lam) :
    thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
      vertexDeg T p + vertexDeg T q ≤ 10 := by
  sorry

theorem pachner23_descent_of_vertex_sum
    {T : Triangulation} {a b c p q : Vert} {lam : Int}
    (h : Valid23 T a b c p q) (hlam : 0 < lam)
    (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
    thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
  exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum

end PachnerInvariant
