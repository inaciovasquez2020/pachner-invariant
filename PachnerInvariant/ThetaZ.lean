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
  have hdeg :
      edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
    simpa using edgeDeg_pachner23_new_edge_three
      (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
  have hpos :
      0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
    omega
  simpa [edgeMemNorm] using
    (edgeMem_allEdges_iff_edgeDeg_pos
      (T := pachner23 T a b c p q) (e := (p,q))).2 hpos

theorem sq_step_identity (d : Int) :
    ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
  ring

def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
  ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
  lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
         (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))

theorem thetaZ_eq_theta_cast
    (T : Triangulation) (lam : Int) :
    thetaZ T lam = (theta T lam : Int) := by
  rfl

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
  rw [thetaZ_eq_theta_cast, thetaZ_eq_theta_cast]
  rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
  rfl

theorem pachner23_descent_iff_vertex_sum_le_ten
    {T : Triangulation} {a b c p q : Vert} {lam : Int}
    (h : Valid23 T a b c p q) (hlam : 0 < lam) :
    thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
      vertexDeg T p + vertexDeg T q ≤ 10 := by
  rw [← sub_lt_zero]
  rw [thetaZ_pachner23_delta_expanded h]
  rw [DeltaThetaZ]
  rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
  rw [sq_step_identity, sq_step_identity]
  omega

theorem pachner23_descent_of_vertex_sum
    {T : Triangulation} {a b c p q : Vert} {lam : Int}
    (h : Valid23 T a b c p q) (hlam : 0 < lam)
    (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
    thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
  exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum

end PachnerInvariant
