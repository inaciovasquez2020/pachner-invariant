# Pachner23 shape extraction

Status: INSPECTION LOCK.

Purpose: identify the exact tetrahedra inserted and removed by `pachner23` before attempting `WellFormedTets_pachner23`.

Search target: `pachner23` across `PachnerInvariant/*.lean`.

## PachnerInvariant/ThetaZ.lean:16

```lean
8: def sqDefectZ (d target : Nat) : Int :=
9:   let z : Int := (d : Int) - (target : Int)
10:   z * z
11: 
12: def thetaZ (T : Triangulation) (lam : Int) : Int :=
13:   ((allEdges T).foldl (fun acc e => acc + sqDefectZ (edgeDeg T e) 3) 0) +
14:   lam * ((allVertices T).foldl (fun acc v => acc + sqDefectZ (vertexDeg T v) 6) 0)
15: 
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
18:     (h : Valid23 T a b c p q) :
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
20:   have hdeg :
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
23:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
24:   have hpos :
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
26:     omega
27:   simpa [edgeMemNorm] using
28:     (edgeMem_allEdges_iff_edgeDeg_pos
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
```

## PachnerInvariant/ThetaZ.lean:19

```lean
11: 
12: def thetaZ (T : Triangulation) (lam : Int) : Int :=
13:   ((allEdges T).foldl (fun acc e => acc + sqDefectZ (edgeDeg T e) 3) 0) +
14:   lam * ((allVertices T).foldl (fun acc v => acc + sqDefectZ (vertexDeg T v) 6) 0)
15: 
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
18:     (h : Valid23 T a b c p q) :
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
20:   have hdeg :
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
23:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
24:   have hpos :
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
26:     omega
27:   simpa [edgeMemNorm] using
28:     (edgeMem_allEdges_iff_edgeDeg_pos
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
```

## PachnerInvariant/ThetaZ.lean:21

```lean
13:   ((allEdges T).foldl (fun acc e => acc + sqDefectZ (edgeDeg T e) 3) 0) +
14:   lam * ((allVertices T).foldl (fun acc v => acc + sqDefectZ (vertexDeg T v) 6) 0)
15: 
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
18:     (h : Valid23 T a b c p q) :
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
20:   have hdeg :
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
23:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
24:   have hpos :
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
26:     omega
27:   simpa [edgeMemNorm] using
28:     (edgeMem_allEdges_iff_edgeDeg_pos
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
39: 
```

## PachnerInvariant/ThetaZ.lean:22

```lean
14:   lam * ((allVertices T).foldl (fun acc v => acc + sqDefectZ (vertexDeg T v) 6) 0)
15: 
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
18:     (h : Valid23 T a b c p q) :
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
20:   have hdeg :
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
23:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
24:   have hpos :
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
26:     omega
27:   simpa [edgeMemNorm] using
28:     (edgeMem_allEdges_iff_edgeDeg_pos
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
39: 
40: theorem thetaZ_eq_theta_cast
```

## PachnerInvariant/ThetaZ.lean:25

```lean
17:     {T : Triangulation} {a b c p q : Vert}
18:     (h : Valid23 T a b c p q) :
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
20:   have hdeg :
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
23:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
24:   have hpos :
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
26:     omega
27:   simpa [edgeMemNorm] using
28:     (edgeMem_allEdges_iff_edgeDeg_pos
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
39: 
40: theorem thetaZ_eq_theta_cast
41:     (T : Triangulation) (lam : Int) :
42:     thetaZ T lam = (theta T lam : Int) := by
43:   rfl
```

## PachnerInvariant/ThetaZ.lean:29

```lean
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
23:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
24:   have hpos :
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
26:     omega
27:   simpa [edgeMemNorm] using
28:     (edgeMem_allEdges_iff_edgeDeg_pos
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
39: 
40: theorem thetaZ_eq_theta_cast
41:     (T : Triangulation) (lam : Int) :
42:     thetaZ T lam = (theta T lam : Int) := by
43:   rfl
44: 
45: theorem List_foldl_congr_sub_eq_changed_terms
46:     {α : Type} (l : List α) (f g : α → Int) :
47:     l.foldl (fun s x => s + f x) 0 - l.foldl (fun s x => s + g x) 0 =
```

## PachnerInvariant/ThetaZ.lean:36

```lean
28:     (edgeMem_allEdges_iff_edgeDeg_pos
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
39: 
40: theorem thetaZ_eq_theta_cast
41:     (T : Triangulation) (lam : Int) :
42:     thetaZ T lam = (theta T lam : Int) := by
43:   rfl
44: 
45: theorem List_foldl_congr_sub_eq_changed_terms
46:     {α : Type} (l : List α) (f g : α → Int) :
47:     l.foldl (fun s x => s + f x) 0 - l.foldl (fun s x => s + g x) 0 =
48:       (l.foldl (fun s x => s + (f x - g x)) 0) := by
49:   induction l with
50:   | nil => simp
51:   | cons x xs ih => simpa [ih, sub_eq_add_neg, add_assoc, add_left_assoc, add_comm]
52: 
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
```

## PachnerInvariant/ThetaZ.lean:37

```lean
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
39: 
40: theorem thetaZ_eq_theta_cast
41:     (T : Triangulation) (lam : Int) :
42:     thetaZ T lam = (theta T lam : Int) := by
43:   rfl
44: 
45: theorem List_foldl_congr_sub_eq_changed_terms
46:     {α : Type} (l : List α) (f g : α → Int) :
47:     l.foldl (fun s x => s + f x) 0 - l.foldl (fun s x => s + g x) 0 =
48:       (l.foldl (fun s x => s + (f x - g x)) 0) := by
49:   induction l with
50:   | nil => simp
51:   | cons x xs ih => simpa [ih, sub_eq_add_neg, add_assoc, add_left_assoc, add_comm]
52: 
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
55:     (h : Valid23 T a b c p q) :
```

## PachnerInvariant/ThetaZ.lean:38

```lean
30: 
31: theorem sq_step_identity (d : Int) :
32:     ((d + 1 - 6)^2 - (d - 6)^2) = 2*d - 11 := by
33:   ring
34: 
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
39: 
40: theorem thetaZ_eq_theta_cast
41:     (T : Triangulation) (lam : Int) :
42:     thetaZ T lam = (theta T lam : Int) := by
43:   rfl
44: 
45: theorem List_foldl_congr_sub_eq_changed_terms
46:     {α : Type} (l : List α) (f g : α → Int) :
47:     l.foldl (fun s x => s + f x) 0 - l.foldl (fun s x => s + g x) 0 =
48:       (l.foldl (fun s x => s + (f x - g x)) 0) := by
49:   induction l with
50:   | nil => simp
51:   | cons x xs ih => simpa [ih, sub_eq_add_neg, add_assoc, add_left_assoc, add_comm]
52: 
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
55:     (h : Valid23 T a b c p q) :
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
```

## PachnerInvariant/ThetaZ.lean:53

```lean
45: theorem List_foldl_congr_sub_eq_changed_terms
46:     {α : Type} (l : List α) (f g : α → Int) :
47:     l.foldl (fun s x => s + f x) 0 - l.foldl (fun s x => s + g x) 0 =
48:       (l.foldl (fun s x => s + (f x - g x)) 0) := by
49:   induction l with
50:   | nil => simp
51:   | cons x xs ih => simpa [ih, sub_eq_add_neg, add_assoc, add_left_assoc, add_comm]
52: 
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
55:     (h : Valid23 T a b c p q) :
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
57:       DeltaThetaZ T a b c p q lam := by
58:   rw [thetaZ_eq_theta_cast, thetaZ_eq_theta_cast]
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
60:   rfl
61: 
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
```

## PachnerInvariant/ThetaZ.lean:56

```lean
48:       (l.foldl (fun s x => s + (f x - g x)) 0) := by
49:   induction l with
50:   | nil => simp
51:   | cons x xs ih => simpa [ih, sub_eq_add_neg, add_assoc, add_left_assoc, add_comm]
52: 
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
55:     (h : Valid23 T a b c p q) :
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
57:       DeltaThetaZ T a b c p q lam := by
58:   rw [thetaZ_eq_theta_cast, thetaZ_eq_theta_cast]
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
60:   rfl
61: 
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
```

## PachnerInvariant/ThetaZ.lean:59

```lean
51:   | cons x xs ih => simpa [ih, sub_eq_add_neg, add_assoc, add_left_assoc, add_comm]
52: 
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
55:     (h : Valid23 T a b c p q) :
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
57:       DeltaThetaZ T a b c p q lam := by
58:   rw [thetaZ_eq_theta_cast, thetaZ_eq_theta_cast]
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
60:   rfl
61: 
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
```

## PachnerInvariant/ThetaZ.lean:62

```lean
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
55:     (h : Valid23 T a b c p q) :
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
57:       DeltaThetaZ T a b c p q lam := by
58:   rw [thetaZ_eq_theta_cast, thetaZ_eq_theta_cast]
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
60:   rfl
61: 
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
```

## PachnerInvariant/ThetaZ.lean:65

```lean
57:       DeltaThetaZ T a b c p q lam := by
58:   rw [thetaZ_eq_theta_cast, thetaZ_eq_theta_cast]
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
60:   rfl
61: 
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/ThetaZ.lean:68

```lean
60:   rfl
61: 
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/ThetaZ.lean:70

```lean
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/ThetaZ.lean:71

```lean
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/ThetaZ.lean:72

```lean
64:     (h : Valid23 T a b c p q) (hlam : 0 < lam) :
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
66:       vertexDeg T p + vertexDeg T q ≤ 10 := by
67:   rw [← sub_lt_zero]
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/ThetaZ.lean:76

```lean
68:   rw [thetaZ_pachner23_delta_expanded h]
69:   rw [DeltaThetaZ]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/ThetaZ.lean:80

```lean
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/ThetaZ.lean:81

```lean
73:   rw [sq_step_identity, sq_step_identity]
74:   omega
75: 
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
78:     (h : Valid23 T a b c p q) (hlam : 0 < lam)
79:     (hsum : vertexDeg T p + vertexDeg T q ≤ 10) :
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
82: 
83: end PachnerInvariant
```

## PachnerInvariant/al3_local_edge_classifier_complete_and_correct.lean:14

```lean
6: namespace PachnerInvariant
7: 
8: def incidence (_T : Triangulation) (_e : Edge) : Int := 0
9: def vertIncidence (_T : Triangulation) (_v : Nat) : Int := 0
10: 
11: theorem local_edge_classifier_complete_and_correct :
12:   ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
13:     Valid23 T a b c p q →
14:     let T' := pachner23 T a b c p q
15:     match edgeType a b c p q e with
16:     | EdgeType.nonlocal =>
17:         incidence T' e = incidence T e
18:     | EdgeType.local t =>
19:         incidence T' e - incidence T e = edgeDeltaValue (deltaOfType t) := by
20:   intro T a b c p q e h
21:   simp [incidence]
22: 
23: end PachnerInvariant
```

## PachnerInvariant/descent_property.lean:66

```lean
58: 
59: def tetContainsVert (t : Vert × Vert × Vert × Vert) (v : Vert) : Bool :=
60:   t.1 == v || t.2.1 == v || t.2.2.1 == v || t.2.2.2 == v
61: 
62: def tetEq (t1 t2 : Vert × Vert × Vert × Vert) : Bool :=
63:   tetContainsVert t2 t1.1 && tetContainsVert t2 t1.2.1 &&
64:   tetContainsVert t2 t1.2.2.1 && tetContainsVert t2 t1.2.2.2
65: 
66: def pachner23 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
67:   let remove := [(a, b, c, p), (a, b, c, q)]
68:   let add    := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
69:   let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
70:   { T with tets := kept ++ add }
71: 
72: def pachner32 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
73:   let remove := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
74:   let add    := [(a, b, c, p), (a, b, c, q)]
75:   let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
76:   { T with tets := kept ++ add }
77: 
78: def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
79:   theta (pachner23 T a b c p q) lam < theta T lam
80: 
81: def isImproving32 (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
82:   theta (pachner32 T a b c p q) lam < theta T lam
83: 
84: def eulerChar (T : Triangulation) : Int :=
```

## PachnerInvariant/descent_property.lean:79

```lean
71: 
72: def pachner32 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
73:   let remove := [(a, b, p, q), (a, c, p, q), (b, c, p, q)]
74:   let add    := [(a, b, c, p), (a, b, c, q)]
75:   let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
76:   { T with tets := kept ++ add }
77: 
78: def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
79:   theta (pachner23 T a b c p q) lam < theta T lam
80: 
81: def isImproving32 (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
82:   theta (pachner32 T a b c p q) lam < theta T lam
83: 
84: def eulerChar (T : Triangulation) : Int :=
85:   (T.numVerts : Int) - (allEdges T).length + (allFaces T).length - T.tets.length
86: 
87: def twoTets : Triangulation :=
88:   { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }
89: 
90: def threeTets : Triangulation :=
91:   { numVerts := 6, tets := [(0,1,2,3),(0,1,2,4),(1,2,3,5)] }
92: 
93: def afterMove23 : Triangulation := pachner23 twoTets 0 1 2 3 4
94: 
95: -- ---------------------------------------------------------------
96: -- Helper lemmas
97: -- ---------------------------------------------------------------
```

## PachnerInvariant/descent_property.lean:93

```lean
85:   (T.numVerts : Int) - (allEdges T).length + (allFaces T).length - T.tets.length
86: 
87: def twoTets : Triangulation :=
88:   { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }
89: 
90: def threeTets : Triangulation :=
91:   { numVerts := 6, tets := [(0,1,2,3),(0,1,2,4),(1,2,3,5)] }
92: 
93: def afterMove23 : Triangulation := pachner23 twoTets 0 1 2 3 4
94: 
95: -- ---------------------------------------------------------------
96: -- Helper lemmas
97: -- ---------------------------------------------------------------
98: 
99: private theorem mul_self_eq_zero (n : Nat) : n * n = 0 ↔ n = 0 := by
100:   simp [Nat.mul_eq_zero]
101: 
102: -- Fix 1: use simp to reduce to n=0 form, then split_ifs + omega
103: private theorem sqDiff_eq_zero_iff (d ideal : Nat) :
104:     (if d ≥ ideal then d - ideal else ideal - d) *
105:     (if d ≥ ideal then d - ideal else ideal - d) = 0 ↔ d = ideal := by
106:   rw [mul_self_eq_zero]
107:   by_cases h : d ≥ ideal
108:   · simp only [h, ite_true]; omega
109:   · simp only [h, ite_false]; omega
110: 
111: -- Fix 2: remove unused Nat.zero_eq from simp call
```

## PachnerInvariant/descent_property.lean:176

```lean
168:         exact hv v hvm
169:       simp [this]
170: 
171: -- ---------------------------------------------------------------
172: -- Concrete theorems
173: -- ---------------------------------------------------------------
174: 
175: theorem twoTets_move_improves :
176:     theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by native_decide
177: 
178: theorem twoTets_move_improves_all_lam :
179:     ∀ lam ∈ [1, 2, 3, 4, 5],
180:       theta (pachner23 twoTets 0 1 2 3 4) lam < theta twoTets lam := by native_decide
181: 
182: theorem threeTets_move_improves :
183:     theta (pachner23 threeTets 0 1 2 3 4) 1 < theta threeTets 1 := by native_decide
184: 
185: theorem isImproving_twoTets : isImproving twoTets 0 1 2 3 4 1 = true := by native_decide
186: theorem isImproving_threeTets : isImproving threeTets 0 1 2 3 4 1 = true := by native_decide
187: 
188: theorem pachner32_recovers :
189:     theta (pachner32 afterMove23 0 1 2 3 4) 1 = theta twoTets 1 := by native_decide
190: 
191: theorem pachner32_roundtrip :
192:     (pachner32 afterMove23 0 1 2 3 4).tets = twoTets.tets := by native_decide
193: 
194: theorem eulerChar_preserved_twoTets :
```

## PachnerInvariant/descent_property.lean:180

```lean
172: -- Concrete theorems
173: -- ---------------------------------------------------------------
174: 
175: theorem twoTets_move_improves :
176:     theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by native_decide
177: 
178: theorem twoTets_move_improves_all_lam :
179:     ∀ lam ∈ [1, 2, 3, 4, 5],
180:       theta (pachner23 twoTets 0 1 2 3 4) lam < theta twoTets lam := by native_decide
181: 
182: theorem threeTets_move_improves :
183:     theta (pachner23 threeTets 0 1 2 3 4) 1 < theta threeTets 1 := by native_decide
184: 
185: theorem isImproving_twoTets : isImproving twoTets 0 1 2 3 4 1 = true := by native_decide
186: theorem isImproving_threeTets : isImproving threeTets 0 1 2 3 4 1 = true := by native_decide
187: 
188: theorem pachner32_recovers :
189:     theta (pachner32 afterMove23 0 1 2 3 4) 1 = theta twoTets 1 := by native_decide
190: 
191: theorem pachner32_roundtrip :
192:     (pachner32 afterMove23 0 1 2 3 4).tets = twoTets.tets := by native_decide
193: 
194: theorem eulerChar_preserved_twoTets :
195:     eulerChar (pachner23 twoTets 0 1 2 3 4) = eulerChar twoTets := by native_decide
196: 
197: theorem eulerChar_preserved_threeTets :
198:     eulerChar (pachner23 threeTets 0 1 2 3 4) = eulerChar threeTets := by native_decide
```

## PachnerInvariant/descent_property.lean:183

```lean
175: theorem twoTets_move_improves :
176:     theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by native_decide
177: 
178: theorem twoTets_move_improves_all_lam :
179:     ∀ lam ∈ [1, 2, 3, 4, 5],
180:       theta (pachner23 twoTets 0 1 2 3 4) lam < theta twoTets lam := by native_decide
181: 
182: theorem threeTets_move_improves :
183:     theta (pachner23 threeTets 0 1 2 3 4) 1 < theta threeTets 1 := by native_decide
184: 
185: theorem isImproving_twoTets : isImproving twoTets 0 1 2 3 4 1 = true := by native_decide
186: theorem isImproving_threeTets : isImproving threeTets 0 1 2 3 4 1 = true := by native_decide
187: 
188: theorem pachner32_recovers :
189:     theta (pachner32 afterMove23 0 1 2 3 4) 1 = theta twoTets 1 := by native_decide
190: 
191: theorem pachner32_roundtrip :
192:     (pachner32 afterMove23 0 1 2 3 4).tets = twoTets.tets := by native_decide
193: 
194: theorem eulerChar_preserved_twoTets :
195:     eulerChar (pachner23 twoTets 0 1 2 3 4) = eulerChar twoTets := by native_decide
196: 
197: theorem eulerChar_preserved_threeTets :
198:     eulerChar (pachner23 threeTets 0 1 2 3 4) = eulerChar threeTets := by native_decide
199: 
200: end PachnerInvariant
```

## PachnerInvariant/descent_property.lean:195

```lean
187: 
188: theorem pachner32_recovers :
189:     theta (pachner32 afterMove23 0 1 2 3 4) 1 = theta twoTets 1 := by native_decide
190: 
191: theorem pachner32_roundtrip :
192:     (pachner32 afterMove23 0 1 2 3 4).tets = twoTets.tets := by native_decide
193: 
194: theorem eulerChar_preserved_twoTets :
195:     eulerChar (pachner23 twoTets 0 1 2 3 4) = eulerChar twoTets := by native_decide
196: 
197: theorem eulerChar_preserved_threeTets :
198:     eulerChar (pachner23 threeTets 0 1 2 3 4) = eulerChar threeTets := by native_decide
199: 
200: end PachnerInvariant
```

## PachnerInvariant/descent_property.lean:198

```lean
190: 
191: theorem pachner32_roundtrip :
192:     (pachner32 afterMove23 0 1 2 3 4).tets = twoTets.tets := by native_decide
193: 
194: theorem eulerChar_preserved_twoTets :
195:     eulerChar (pachner23 twoTets 0 1 2 3 4) = eulerChar twoTets := by native_decide
196: 
197: theorem eulerChar_preserved_threeTets :
198:     eulerChar (pachner23 threeTets 0 1 2 3 4) = eulerChar threeTets := by native_decide
199: 
200: end PachnerInvariant
```

## PachnerInvariant/frontier.lean:59

```lean
51:     edgeDeg T e' + 1
52:   else
53:     edgeDeg T e'
54: 
55: def expectedVertexDeg23Delta (a b c p q : Vert) (v : Vert) : Nat :=
56:   if v = p then 1 else if v = q then 1 else 0
57: 
58: 
59: theorem vertDeg_pachner23_eq_expected
60: {T : Triangulation} {a b c p q : Vert} {v : Vert}
61: (h : Valid23 T a b c p q) :
62: vertexDeg (pachner23 T a b c p q) v =
63: vertexDeg T v + expectedVertexDeg23Delta a b c p q v := by
64:   by_cases hvp : v = p
65:   · simp [hvp]
66:   · by_cases hvq : v = q
67:     · simp [hvp, hvq]
68:     · simp [hvp, hvq]
69: 
70: theorem vertDeg_pachner23_at_p
71: {T : Triangulation} {a b c p q : Vert}
72: (h : Valid23 T a b c p q) :
73: vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
```

## PachnerInvariant/frontier.lean:62

```lean
54: 
55: def expectedVertexDeg23Delta (a b c p q : Vert) (v : Vert) : Nat :=
56:   if v = p then 1 else if v = q then 1 else 0
57: 
58: 
59: theorem vertDeg_pachner23_eq_expected
60: {T : Triangulation} {a b c p q : Vert} {v : Vert}
61: (h : Valid23 T a b c p q) :
62: vertexDeg (pachner23 T a b c p q) v =
63: vertexDeg T v + expectedVertexDeg23Delta a b c p q v := by
64:   by_cases hvp : v = p
65:   · simp [hvp]
66:   · by_cases hvq : v = q
67:     · simp [hvp, hvq]
68:     · simp [hvp, hvq]
69: 
70: theorem vertDeg_pachner23_at_p
71: {T : Triangulation} {a b c p q : Vert}
72: (h : Valid23 T a b c p q) :
73: vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
```

## PachnerInvariant/frontier.lean:70

```lean
62: vertexDeg (pachner23 T a b c p q) v =
63: vertexDeg T v + expectedVertexDeg23Delta a b c p q v := by
64:   by_cases hvp : v = p
65:   · simp [hvp]
66:   · by_cases hvq : v = q
67:     · simp [hvp, hvq]
68:     · simp [hvp, hvq]
69: 
70: theorem vertDeg_pachner23_at_p
71: {T : Triangulation} {a b c p q : Vert}
72: (h : Valid23 T a b c p q) :
73: vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
```

## PachnerInvariant/frontier.lean:73

```lean
65:   · simp [hvp]
66:   · by_cases hvq : v = q
67:     · simp [hvp, hvq]
68:     · simp [hvp, hvq]
69: 
70: theorem vertDeg_pachner23_at_p
71: {T : Triangulation} {a b c p q : Vert}
72: (h : Valid23 T a b c p q) :
73: vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
```

## PachnerInvariant/frontier.lean:75

```lean
67:     · simp [hvp, hvq]
68:     · simp [hvp, hvq]
69: 
70: theorem vertDeg_pachner23_at_p
71: {T : Triangulation} {a b c p q : Vert}
72: (h : Valid23 T a b c p q) :
73: vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
```

## PachnerInvariant/frontier.lean:77

```lean
69: 
70: theorem vertDeg_pachner23_at_p
71: {T : Triangulation} {a b c p q : Vert}
72: (h : Valid23 T a b c p q) :
73: vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
```

## PachnerInvariant/frontier.lean:80

```lean
72: (h : Valid23 T a b c p q) :
73: vertexDeg (pachner23 T a b c p q) p = vertexDeg T p + 1 := by
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
```

## PachnerInvariant/frontier.lean:82

```lean
74:   simpa [expectedVertexDeg23Delta] using
75:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h)
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
```

## PachnerInvariant/frontier.lean:84

```lean
76: 
77: theorem vertDeg_pachner23_at_q
78: {T : Triangulation} {a b c p q : Vert}
79: (h : Valid23 T a b c p q) :
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
```

## PachnerInvariant/frontier.lean:88

```lean
80: vertexDeg (pachner23 T a b c p q) q = vertexDeg T q + 1 := by
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
103: (hp : vertexDeg T p ≤ 5) :
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
```

## PachnerInvariant/frontier.lean:89

```lean
81:   simpa [expectedVertexDeg23Delta] using
82:     (vertDeg_pachner23_eq_expected (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h)
83: 
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
103: (hp : vertexDeg T p ≤ 5) :
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
```

## PachnerInvariant/frontier.lean:92

```lean
84: theorem vertDeg_pachner23_at_p_le_six
85: {T : Triangulation} {a b c p q : Vert}
86: (h : Valid23 T a b c p q)
87: (hp : vertexDeg T p ≤ 5) :
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
103: (hp : vertexDeg T p ≤ 5) :
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
```

## PachnerInvariant/frontier.lean:96

```lean
88: vertexDeg (pachner23 T a b c p q) p ≤ 6 := by
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
103: (hp : vertexDeg T p ≤ 5) :
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
```

## PachnerInvariant/frontier.lean:97

```lean
89:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
90:   omega
91: 
92: theorem vertDeg_pachner23_at_q_le_six
93: {T : Triangulation} {a b c p q : Vert}
94: (h : Valid23 T a b c p q)
95: (hq : vertexDeg T q ≤ 5) :
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
103: (hp : vertexDeg T p ≤ 5) :
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
```

## PachnerInvariant/frontier.lean:104

```lean
96: vertexDeg (pachner23 T a b c p q) q ≤ 6 := by
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
103: (hp : vertexDeg T p ≤ 5) :
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
116: theorem edgeDeg_pachner23_new_edge_three
117: {T : Triangulation} {a b c p q : Vert}
118: (h : Valid23 T a b c p q) :
119: edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
120:   have h_edge :=
121:     edgeDeg_pachner23_delta
122:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
```

## PachnerInvariant/frontier.lean:105

```lean
97:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
98:   omega
99: 
100: theorem vertSqDefect_p_monotone
101: {T : Triangulation} {a b c p q : Vert}
102: (h : Valid23 T a b c p q)
103: (hp : vertexDeg T p ≤ 5) :
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
116: theorem edgeDeg_pachner23_new_edge_three
117: {T : Triangulation} {a b c p q : Vert}
118: (h : Valid23 T a b c p q) :
119: edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
120:   have h_edge :=
121:     edgeDeg_pachner23_delta
122:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
123:   have h_zero : edgeDeg T (normalizeEdge (p,q)) = 0 :=
```

## PachnerInvariant/frontier.lean:112

```lean
104: (vertexDeg (pachner23 T a b c p q) p - 6)^2 ≤ (vertexDeg T p - 6)^2 := by
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
116: theorem edgeDeg_pachner23_new_edge_three
117: {T : Triangulation} {a b c p q : Vert}
118: (h : Valid23 T a b c p q) :
119: edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
120:   have h_edge :=
121:     edgeDeg_pachner23_delta
122:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
123:   have h_zero : edgeDeg T (normalizeEdge (p,q)) = 0 :=
124:     edgeDeg_zero_of_newEdgeAbsent (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
125:   have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
126:   simpa [h_zero, h_nobdry] using h_edge
127: 
128: theorem vertSqDefect_p_strict
129: {T : Triangulation} {a b c p q : Vert}
130: (h : Valid23 T a b c p q)
```

## PachnerInvariant/frontier.lean:113

```lean
105:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
106:   omega
107: 
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
116: theorem edgeDeg_pachner23_new_edge_three
117: {T : Triangulation} {a b c p q : Vert}
118: (h : Valid23 T a b c p q) :
119: edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
120:   have h_edge :=
121:     edgeDeg_pachner23_delta
122:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
123:   have h_zero : edgeDeg T (normalizeEdge (p,q)) = 0 :=
124:     edgeDeg_zero_of_newEdgeAbsent (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
125:   have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
126:   simpa [h_zero, h_nobdry] using h_edge
127: 
128: theorem vertSqDefect_p_strict
129: {T : Triangulation} {a b c p q : Vert}
130: (h : Valid23 T a b c p q)
131: (hp : vertexDeg T p ≤ 5) :
```

## PachnerInvariant/frontier.lean:116

```lean
108: theorem vertSqDefect_q_monotone
109: {T : Triangulation} {a b c p q : Vert}
110: (h : Valid23 T a b c p q)
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
116: theorem edgeDeg_pachner23_new_edge_three
117: {T : Triangulation} {a b c p q : Vert}
118: (h : Valid23 T a b c p q) :
119: edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
120:   have h_edge :=
121:     edgeDeg_pachner23_delta
122:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
123:   have h_zero : edgeDeg T (normalizeEdge (p,q)) = 0 :=
124:     edgeDeg_zero_of_newEdgeAbsent (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
125:   have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
126:   simpa [h_zero, h_nobdry] using h_edge
127: 
128: theorem vertSqDefect_p_strict
129: {T : Triangulation} {a b c p q : Vert}
130: (h : Valid23 T a b c p q)
131: (hp : vertexDeg T p ≤ 5) :
132: (vertexDeg (pachner23 T a b c p q) p - 6)^2 < (vertexDeg T p - 6)^2 := by
133:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
134:   omega
```

## PachnerInvariant/frontier.lean:119

```lean
111: (hq : vertexDeg T q ≤ 5) :
112: (vertexDeg (pachner23 T a b c p q) q - 6)^2 ≤ (vertexDeg T q - 6)^2 := by
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
116: theorem edgeDeg_pachner23_new_edge_three
117: {T : Triangulation} {a b c p q : Vert}
118: (h : Valid23 T a b c p q) :
119: edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
120:   have h_edge :=
121:     edgeDeg_pachner23_delta
122:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
123:   have h_zero : edgeDeg T (normalizeEdge (p,q)) = 0 :=
124:     edgeDeg_zero_of_newEdgeAbsent (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
125:   have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
126:   simpa [h_zero, h_nobdry] using h_edge
127: 
128: theorem vertSqDefect_p_strict
129: {T : Triangulation} {a b c p q : Vert}
130: (h : Valid23 T a b c p q)
131: (hp : vertexDeg T p ≤ 5) :
132: (vertexDeg (pachner23 T a b c p q) p - 6)^2 < (vertexDeg T p - 6)^2 := by
133:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
134:   omega
135: 
136: theorem vertSqDefect_q_strict
137: {T : Triangulation} {a b c p q : Vert}
```

## PachnerInvariant/frontier.lean:121

```lean
113:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
114:   omega
115: 
116: theorem edgeDeg_pachner23_new_edge_three
117: {T : Triangulation} {a b c p q : Vert}
118: (h : Valid23 T a b c p q) :
119: edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
120:   have h_edge :=
121:     edgeDeg_pachner23_delta
122:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
123:   have h_zero : edgeDeg T (normalizeEdge (p,q)) = 0 :=
124:     edgeDeg_zero_of_newEdgeAbsent (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
125:   have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
126:   simpa [h_zero, h_nobdry] using h_edge
127: 
128: theorem vertSqDefect_p_strict
129: {T : Triangulation} {a b c p q : Vert}
130: (h : Valid23 T a b c p q)
131: (hp : vertexDeg T p ≤ 5) :
132: (vertexDeg (pachner23 T a b c p q) p - 6)^2 < (vertexDeg T p - 6)^2 := by
133:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
134:   omega
135: 
136: theorem vertSqDefect_q_strict
137: {T : Triangulation} {a b c p q : Vert}
138: (h : Valid23 T a b c p q)
139: (hq : vertexDeg T q ≤ 5) :
```

## PachnerInvariant/frontier.lean:132

```lean
124:     edgeDeg_zero_of_newEdgeAbsent (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
125:   have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
126:   simpa [h_zero, h_nobdry] using h_edge
127: 
128: theorem vertSqDefect_p_strict
129: {T : Triangulation} {a b c p q : Vert}
130: (h : Valid23 T a b c p q)
131: (hp : vertexDeg T p ≤ 5) :
132: (vertexDeg (pachner23 T a b c p q) p - 6)^2 < (vertexDeg T p - 6)^2 := by
133:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
134:   omega
135: 
136: theorem vertSqDefect_q_strict
137: {T : Triangulation} {a b c p q : Vert}
138: (h : Valid23 T a b c p q)
139: (hq : vertexDeg T q ≤ 5) :
140: (vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
```

## PachnerInvariant/frontier.lean:133

```lean
125:   have h_nobdry := Valid23.newEdgeCase (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
126:   simpa [h_zero, h_nobdry] using h_edge
127: 
128: theorem vertSqDefect_p_strict
129: {T : Triangulation} {a b c p q : Vert}
130: (h : Valid23 T a b c p q)
131: (hp : vertexDeg T p ≤ 5) :
132: (vertexDeg (pachner23 T a b c p q) p - 6)^2 < (vertexDeg T p - 6)^2 := by
133:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
134:   omega
135: 
136: theorem vertSqDefect_q_strict
137: {T : Triangulation} {a b c p q : Vert}
138: (h : Valid23 T a b c p q)
139: (hq : vertexDeg T q ≤ 5) :
140: (vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
```

## PachnerInvariant/frontier.lean:140

```lean
132: (vertexDeg (pachner23 T a b c p q) p - 6)^2 < (vertexDeg T p - 6)^2 := by
133:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
134:   omega
135: 
136: theorem vertSqDefect_q_strict
137: {T : Triangulation} {a b c p q : Vert}
138: (h : Valid23 T a b c p q)
139: (hq : vertexDeg T q ≤ 5) :
140: (vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
```

## PachnerInvariant/frontier.lean:141

```lean
133:   rw [vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
134:   omega
135: 
136: theorem vertSqDefect_q_strict
137: {T : Triangulation} {a b c p q : Vert}
138: (h : Valid23 T a b c p q)
139: (hq : vertexDeg T q ≤ 5) :
140: (vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
```

## PachnerInvariant/frontier.lean:144

```lean
136: theorem vertSqDefect_q_strict
137: {T : Triangulation} {a b c p q : Vert}
138: (h : Valid23 T a b c p q)
139: (hq : vertexDeg T q ≤ 5) :
140: (vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
```

## PachnerInvariant/frontier.lean:147

```lean
139: (hq : vertexDeg T q ≤ 5) :
140: (vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
```

## PachnerInvariant/frontier.lean:148

```lean
140: (vertexDeg (pachner23 T a b c p q) q - 6)^2 < (vertexDeg T q - 6)^2 := by
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
```

## PachnerInvariant/frontier.lean:149

```lean
141:   rw [vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
```

## PachnerInvariant/frontier.lean:150

```lean
142:   omega
143: 
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
```

## PachnerInvariant/frontier.lean:152

```lean
144: theorem theta_pachner23_delta_expanded
145:     {T : Triangulation} {a b c p q : Vert} (lam : Nat)
146:     (h : Valid23 T a b c p q) :
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
169:   have hdelta :=
170:     theta_pachner23_delta_expanded
```

## PachnerInvariant/frontier.lean:155

```lean
147:     theta (pachner23 T a b c p q) lam - theta T lam =
148:       ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 - (0 : Int)) +
149:       lam * (((vertexDeg (pachner23 T a b c p q) p - 6)^2 - (vertexDeg T p - 6)^2) +
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
169:   have hdelta :=
170:     theta_pachner23_delta_expanded
171:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h
172:   have hnew :=
173:     edgeDeg_pachner23_new_edge_three
```

## PachnerInvariant/frontier.lean:158

```lean
150:              ((vertexDeg (pachner23 T a b c p q) q - 6)^2 - (vertexDeg T q - 6)^2)) := by
151:   have h_edge :=
152:     edgeDeg_pachner23_delta
153:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := (p,q)) h
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
169:   have hdelta :=
170:     theta_pachner23_delta_expanded
171:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h
172:   have hnew :=
173:     edgeDeg_pachner23_new_edge_three
174:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
175:   have hpstrict :=
176:     vertSqDefect_p_strict
```

## PachnerInvariant/frontier.lean:162

```lean
154:   have h_vert_p :=
155:     vertDeg_pachner23_eq_expected
156:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := p) h
157:   have h_vert_q :=
158:     vertDeg_pachner23_eq_expected
159:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (v := q) h
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
169:   have hdelta :=
170:     theta_pachner23_delta_expanded
171:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h
172:   have hnew :=
173:     edgeDeg_pachner23_new_edge_three
174:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
175:   have hpstrict :=
176:     vertSqDefect_p_strict
177:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hp
178:   have hqstrict :=
179:     vertSqDefect_q_strict
180:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
```

## PachnerInvariant/frontier.lean:168

```lean
160:   simp [theta, h_edge, h_vert_p, h_vert_q]
161: 
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
169:   have hdelta :=
170:     theta_pachner23_delta_expanded
171:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h
172:   have hnew :=
173:     edgeDeg_pachner23_new_edge_three
174:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
175:   have hpstrict :=
176:     vertSqDefect_p_strict
177:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hp
178:   have hqstrict :=
179:     vertSqDefect_q_strict
180:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
181:   have hpneg :
182:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
183:     omega
184:   have hqneg :
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
```

## PachnerInvariant/frontier.lean:170

```lean
162: theorem pachner23_descent_under_vertex_le_five
163:     {T : Triangulation} {a b c p q : Vert} {lam : Nat}
164:     (h : Valid23 T a b c p q)
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
169:   have hdelta :=
170:     theta_pachner23_delta_expanded
171:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h
172:   have hnew :=
173:     edgeDeg_pachner23_new_edge_three
174:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
175:   have hpstrict :=
176:     vertSqDefect_p_strict
177:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hp
178:   have hqstrict :=
179:     vertSqDefect_q_strict
180:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
181:   have hpneg :
182:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
183:     omega
184:   have hqneg :
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
```

## PachnerInvariant/frontier.lean:173

```lean
165:     (hlam : 0 < lam)
166:     (hp : vertexDeg T p ≤ 5)
167:     (hq : vertexDeg T q ≤ 5) :
168:     theta (pachner23 T a b c p q) lam < theta T lam := by
169:   have hdelta :=
170:     theta_pachner23_delta_expanded
171:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h
172:   have hnew :=
173:     edgeDeg_pachner23_new_edge_three
174:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
175:   have hpstrict :=
176:     vertSqDefect_p_strict
177:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hp
178:   have hqstrict :=
179:     vertSqDefect_q_strict
180:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
181:   have hpneg :
182:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
183:     omega
184:   have hqneg :
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
```

## PachnerInvariant/frontier.lean:182

```lean
174:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h
175:   have hpstrict :=
176:     vertSqDefect_p_strict
177:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hp
178:   have hqstrict :=
179:     vertSqDefect_q_strict
180:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
181:   have hpneg :
182:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
183:     omega
184:   have hqneg :
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
192:       (lam : Int) *
193:       ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
194:        (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
195:     omega
196:   have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
197:     rw [hdelta]
198:     rw [hnew]
199:     omega
200:   omega
```

## PachnerInvariant/frontier.lean:185

```lean
177:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hp
178:   have hqstrict :=
179:     vertSqDefect_q_strict
180:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
181:   have hpneg :
182:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
183:     omega
184:   have hqneg :
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
192:       (lam : Int) *
193:       ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
194:        (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
195:     omega
196:   have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
197:     rw [hdelta]
198:     rw [hnew]
199:     omega
200:   omega
201: 
202: theorem Valid23.newEdgeAbsent
203:     {T : Triangulation} {a b c p q : Vert}
```

## PachnerInvariant/frontier.lean:188

```lean
180:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h hq
181:   have hpneg :
182:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
183:     omega
184:   have hqneg :
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
192:       (lam : Int) *
193:       ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
194:        (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
195:     omega
196:   have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
197:     rw [hdelta]
198:     rw [hnew]
199:     omega
200:   omega
201: 
202: theorem Valid23.newEdgeAbsent
203:     {T : Triangulation} {a b c p q : Vert}
204:     (h : Valid23 T a b c p q) :
205:     ¬ edgeMemNorm (p,q) (allEdges T) := by
206:   rcases h with ⟨_, _, _, _, _, _, _, _, _, _, _, hNoPQ⟩
```

## PachnerInvariant/frontier.lean:189

```lean
181:   have hpneg :
182:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) < 0 := by
183:     omega
184:   have hqneg :
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
192:       (lam : Int) *
193:       ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
194:        (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
195:     omega
196:   have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
197:     rw [hdelta]
198:     rw [hnew]
199:     omega
200:   omega
201: 
202: theorem Valid23.newEdgeAbsent
203:     {T : Triangulation} {a b c p q : Vert}
204:     (h : Valid23 T a b c p q) :
205:     ¬ edgeMemNorm (p,q) (allEdges T) := by
206:   rcases h with ⟨_, _, _, _, _, _, _, _, _, _, _, hNoPQ⟩
207:   exact hNoPQ
```

## PachnerInvariant/frontier.lean:193

```lean
185:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
192:       (lam : Int) *
193:       ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
194:        (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
195:     omega
196:   have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
197:     rw [hdelta]
198:     rw [hnew]
199:     omega
200:   omega
201: 
202: theorem Valid23.newEdgeAbsent
203:     {T : Triangulation} {a b c p q : Vert}
204:     (h : Valid23 T a b c p q) :
205:     ¬ edgeMemNorm (p,q) (allEdges T) := by
206:   rcases h with ⟨_, _, _, _, _, _, _, _, _, _, _, hNoPQ⟩
207:   exact hNoPQ
208: 
209: theorem Valid23.sourceTet₁
210:     {T : Triangulation} {a b c p q : Vert}
211:     (h : Valid23 T a b c p q) :
```

## PachnerInvariant/frontier.lean:194

```lean
186:     omega
187:   have hverts :
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
192:       (lam : Int) *
193:       ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
194:        (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
195:     omega
196:   have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
197:     rw [hdelta]
198:     rw [hnew]
199:     omega
200:   omega
201: 
202: theorem Valid23.newEdgeAbsent
203:     {T : Triangulation} {a b c p q : Vert}
204:     (h : Valid23 T a b c p q) :
205:     ¬ edgeMemNorm (p,q) (allEdges T) := by
206:   rcases h with ⟨_, _, _, _, _, _, _, _, _, _, _, hNoPQ⟩
207:   exact hNoPQ
208: 
209: theorem Valid23.sourceTet₁
210:     {T : Triangulation} {a b c p q : Vert}
211:     (h : Valid23 T a b c p q) :
212:     tetMemMod (a,b,c,p) T.tets := by
```

## PachnerInvariant/frontier.lean:196

```lean
188:       (((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
189:       (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2) < 0 := by
190:     omega
191:   have hweighted :
192:       (lam : Int) *
193:       ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
194:        (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2)) < 0 := by
195:     omega
196:   have hsub : ((theta (pachner23 T a b c p q) lam : Nat) : Int) - theta T lam < 0 := by
197:     rw [hdelta]
198:     rw [hnew]
199:     omega
200:   omega
201: 
202: theorem Valid23.newEdgeAbsent
203:     {T : Triangulation} {a b c p q : Vert}
204:     (h : Valid23 T a b c p q) :
205:     ¬ edgeMemNorm (p,q) (allEdges T) := by
206:   rcases h with ⟨_, _, _, _, _, _, _, _, _, _, _, hNoPQ⟩
207:   exact hNoPQ
208: 
209: theorem Valid23.sourceTet₁
210:     {T : Triangulation} {a b c p q : Vert}
211:     (h : Valid23 T a b c p q) :
212:     tetMemMod (a,b,c,p) T.tets := by
213:   rcases h with ⟨_, _, _, _, _, _, hTet₁, _, _, _, _, _⟩
214:   exact hTet₁
```

## PachnerInvariant/frontier.lean:434

```lean
426: expectedEdgeDeg23 T a b c p q e =
427: edgeDeg T (normalizeEdge e) +
428: (if normalizeEdge e = normalizeEdge (p,q) then 3
429:  else if (crossEdges23 a b c p q).contains (normalizeEdge e) then 1
430:  else 0) -
431: (if (boundaryEdges23 a b c).contains (normalizeEdge e) then 1 else 0) := by
432:   simp [expectedEdgeDeg23]
433: 
434: theorem edgeDeg_pachner23_delta
435:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
436:   (h : Valid23 T a b c p q) :
437:   let e' := normalizeEdge e
438:   edgeDeg (pachner23 T a b c p q) e' =
439:     edgeDeg T e' +
440:     (if e' = normalizeEdge (p,q) then 3
441:      else if (crossEdges23 a b c p q).contains e' then 1
442:      else 0) -
443:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
444:   dsimp
445:   rw [← allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
446:   rw [← allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
447:   simpa using
448:     allEdges_pachner23_count_delta
449:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
450: 
451: 
452: theorem edgeDeg_pachner23_eq_expected
```

## PachnerInvariant/frontier.lean:438

```lean
430:  else 0) -
431: (if (boundaryEdges23 a b c).contains (normalizeEdge e) then 1 else 0) := by
432:   simp [expectedEdgeDeg23]
433: 
434: theorem edgeDeg_pachner23_delta
435:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
436:   (h : Valid23 T a b c p q) :
437:   let e' := normalizeEdge e
438:   edgeDeg (pachner23 T a b c p q) e' =
439:     edgeDeg T e' +
440:     (if e' = normalizeEdge (p,q) then 3
441:      else if (crossEdges23 a b c p q).contains e' then 1
442:      else 0) -
443:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
444:   dsimp
445:   rw [← allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
446:   rw [← allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
447:   simpa using
448:     allEdges_pachner23_count_delta
449:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
450: 
451: 
452: theorem edgeDeg_pachner23_eq_expected
453:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
454:   (h : Valid23 T a b c p q) :
455:   edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
456:     expectedEdgeDeg23 T a b c p q e := by
```

## PachnerInvariant/frontier.lean:445

```lean
437:   let e' := normalizeEdge e
438:   edgeDeg (pachner23 T a b c p q) e' =
439:     edgeDeg T e' +
440:     (if e' = normalizeEdge (p,q) then 3
441:      else if (crossEdges23 a b c p q).contains e' then 1
442:      else 0) -
443:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
444:   dsimp
445:   rw [← allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
446:   rw [← allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
447:   simpa using
448:     allEdges_pachner23_count_delta
449:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
450: 
451: 
452: theorem edgeDeg_pachner23_eq_expected
453:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
454:   (h : Valid23 T a b c p q) :
455:   edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
456:     expectedEdgeDeg23 T a b c p q e := by
457:   rw [edgeDeg_pachner23_delta
458:       (T := T) (a := a) (b := b) (c := c)
459:       (p := p) (q := q) (e := e) h]
460:   exact expectedEdgeDeg23_delta_normal_form
461:       (T := T) (a := a) (b := b) (c := c)
462:       (p := p) (q := q) (e := e) h
463: 
```

## PachnerInvariant/frontier.lean:448

```lean
440:     (if e' = normalizeEdge (p,q) then 3
441:      else if (crossEdges23 a b c p q).contains e' then 1
442:      else 0) -
443:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
444:   dsimp
445:   rw [← allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
446:   rw [← allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
447:   simpa using
448:     allEdges_pachner23_count_delta
449:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
450: 
451: 
452: theorem edgeDeg_pachner23_eq_expected
453:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
454:   (h : Valid23 T a b c p q) :
455:   edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
456:     expectedEdgeDeg23 T a b c p q e := by
457:   rw [edgeDeg_pachner23_delta
458:       (T := T) (a := a) (b := b) (c := c)
459:       (p := p) (q := q) (e := e) h]
460:   exact expectedEdgeDeg23_delta_normal_form
461:       (T := T) (a := a) (b := b) (c := c)
462:       (p := p) (q := q) (e := e) h
463: 
464: 
465: theorem edgeDeg_eq_count_tets
466:     (T : Triangulation) (e : Vert × Vert) :
```

## PachnerInvariant/frontier.lean:452

```lean
444:   dsimp
445:   rw [← allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
446:   rw [← allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
447:   simpa using
448:     allEdges_pachner23_count_delta
449:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
450: 
451: 
452: theorem edgeDeg_pachner23_eq_expected
453:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
454:   (h : Valid23 T a b c p q) :
455:   edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
456:     expectedEdgeDeg23 T a b c p q e := by
457:   rw [edgeDeg_pachner23_delta
458:       (T := T) (a := a) (b := b) (c := c)
459:       (p := p) (q := q) (e := e) h]
460:   exact expectedEdgeDeg23_delta_normal_form
461:       (T := T) (a := a) (b := b) (c := c)
462:       (p := p) (q := q) (e := e) h
463: 
464: 
465: theorem edgeDeg_eq_count_tets
466:     (T : Triangulation) (e : Vert × Vert) :
467:     edgeDeg T (normalizeEdge e) =
468:       T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
469:   rfl
470: 
```

## PachnerInvariant/frontier.lean:455

```lean
447:   simpa using
448:     allEdges_pachner23_count_delta
449:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
450: 
451: 
452: theorem edgeDeg_pachner23_eq_expected
453:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
454:   (h : Valid23 T a b c p q) :
455:   edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
456:     expectedEdgeDeg23 T a b c p q e := by
457:   rw [edgeDeg_pachner23_delta
458:       (T := T) (a := a) (b := b) (c := c)
459:       (p := p) (q := q) (e := e) h]
460:   exact expectedEdgeDeg23_delta_normal_form
461:       (T := T) (a := a) (b := b) (c := c)
462:       (p := p) (q := q) (e := e) h
463: 
464: 
465: theorem edgeDeg_eq_count_tets
466:     (T : Triangulation) (e : Vert × Vert) :
467:     edgeDeg T (normalizeEdge e) =
468:       T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
469:   rfl
470: 
471: theorem count_zero_of_newEdgeAbsent
472:     {T : Triangulation} {a b c p q : Vert}
473:     (h : Valid23 T a b c p q) :
```

## PachnerInvariant/frontier.lean:457

```lean
449:       (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
450: 
451: 
452: theorem edgeDeg_pachner23_eq_expected
453:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
454:   (h : Valid23 T a b c p q) :
455:   edgeDeg (pachner23 T a b c p q) (normalizeEdge e) =
456:     expectedEdgeDeg23 T a b c p q e := by
457:   rw [edgeDeg_pachner23_delta
458:       (T := T) (a := a) (b := b) (c := c)
459:       (p := p) (q := q) (e := e) h]
460:   exact expectedEdgeDeg23_delta_normal_form
461:       (T := T) (a := a) (b := b) (c := c)
462:       (p := p) (q := q) (e := e) h
463: 
464: 
465: theorem edgeDeg_eq_count_tets
466:     (T : Triangulation) (e : Vert × Vert) :
467:     edgeDeg T (normalizeEdge e) =
468:       T.tets.countP (fun t => (tetToEdges t).any (edgeEq (normalizeEdge e))) := by
469:   rfl
470: 
471: theorem count_zero_of_newEdgeAbsent
472:     {T : Triangulation} {a b c p q : Vert}
473:     (h : Valid23 T a b c p q) :
474:     List.count (normalizeEdge (p,q)) (allEdges T) = 0 := by
475:   have habs :
```

## PachnerInvariant/frontier.lean:633

```lean
625:     ((allEdges T).contains (normalizeEdge e) = true) ↔
626:       0 < edgeDeg T (normalizeEdge e) := by
627:   rw [edgeMem_allEdges_iff_exists_tet]
628:   rw [edgeDeg_pos_iff_exists_tet]
629: 
630: 
631: 
632: 
633: lemma tetIncidence_pachner23_delta
634:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
635:   (h : Valid23 T a b c p q) :
636:   let e' := normalizeEdge e
637:   (edgeDeg (pachner23 T a b c p q) e' - edgeDeg T e') =
638:     (if e' = normalizeEdge (p,q) then 3
639:      else if (crossEdges23 a b c p q).contains e' then 1
640:      else 0) -
641:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
642:   by_cases hpq : normalizeEdge e = normalizeEdge (p,q)
643:   · simp [hpq]
644:   · by_cases hcross : (crossEdges23 a b c p q).contains (normalizeEdge e)
645:     · simp [hpq, hcross]
646:     · by_cases hbdry : (boundaryEdges23 a b c).contains (normalizeEdge e)
647:       · simp [hpq, hcross, hbdry]
648:       · simp [hpq, hcross, hbdry]
649: 
650: lemma List.count_bind
651:   {α β : Type} [DecidableEq β]
```

## PachnerInvariant/frontier.lean:637

```lean
629: 
630: 
631: 
632: 
633: lemma tetIncidence_pachner23_delta
634:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
635:   (h : Valid23 T a b c p q) :
636:   let e' := normalizeEdge e
637:   (edgeDeg (pachner23 T a b c p q) e' - edgeDeg T e') =
638:     (if e' = normalizeEdge (p,q) then 3
639:      else if (crossEdges23 a b c p q).contains e' then 1
640:      else 0) -
641:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
642:   by_cases hpq : normalizeEdge e = normalizeEdge (p,q)
643:   · simp [hpq]
644:   · by_cases hcross : (crossEdges23 a b c p q).contains (normalizeEdge e)
645:     · simp [hpq, hcross]
646:     · by_cases hbdry : (boundaryEdges23 a b c).contains (normalizeEdge e)
647:       · simp [hpq, hcross, hbdry]
648:       · simp [hpq, hcross, hbdry]
649: 
650: lemma List.count_bind
651:   {α β : Type} [DecidableEq β]
652:   (f : α → List β) (l : List α) (x : β) :
653:   (l.bind f).count x = (l.map (fun a => (f a).count x)).sum := by
654:   induction l with
655:   | nil =>
```

## PachnerInvariant/frontier.lean:660

```lean
652:   (f : α → List β) (l : List α) (x : β) :
653:   (l.bind f).count x = (l.map (fun a => (f a).count x)).sum := by
654:   induction l with
655:   | nil =>
656:       simp
657:   | cons a t ih =>
658:       simp [List.bind, List.count_append, ih, Nat.add_comm, Nat.add_left_comm, Nat.add_assoc]
659: 
660: theorem allEdges_pachner23_count_delta
661:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
662:   (h : Valid23 T a b c p q) :
663:   let e' := normalizeEdge e
664:   (allEdges (pachner23 T a b c p q)).count e' =
665:     (allEdges T).count e' +
666:     (if e' = normalizeEdge (p,q) then 3
667:      else if (crossEdges23 a b c p q).contains e' then 1
668:      else 0) -
669:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
670:   dsimp
671:   rw [allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
672:   rw [allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
673:   exact tetIncidence_pachner23_delta
674:     (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
```

## PachnerInvariant/frontier.lean:664

```lean
656:       simp
657:   | cons a t ih =>
658:       simp [List.bind, List.count_append, ih, Nat.add_comm, Nat.add_left_comm, Nat.add_assoc]
659: 
660: theorem allEdges_pachner23_count_delta
661:   {T : Triangulation} {a b c p q : Vert} {e : Vert × Vert}
662:   (h : Valid23 T a b c p q) :
663:   let e' := normalizeEdge e
664:   (allEdges (pachner23 T a b c p q)).count e' =
665:     (allEdges T).count e' +
666:     (if e' = normalizeEdge (p,q) then 3
667:      else if (crossEdges23 a b c p q).contains e' then 1
668:      else 0) -
669:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
670:   dsimp
671:   rw [allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
672:   rw [allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
673:   exact tetIncidence_pachner23_delta
674:     (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
```

## PachnerInvariant/frontier.lean:671

```lean
663:   let e' := normalizeEdge e
664:   (allEdges (pachner23 T a b c p q)).count e' =
665:     (allEdges T).count e' +
666:     (if e' = normalizeEdge (p,q) then 3
667:      else if (crossEdges23 a b c p q).contains e' then 1
668:      else 0) -
669:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
670:   dsimp
671:   rw [allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
672:   rw [allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
673:   exact tetIncidence_pachner23_delta
674:     (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
```

## PachnerInvariant/frontier.lean:673

```lean
665:     (allEdges T).count e' +
666:     (if e' = normalizeEdge (p,q) then 3
667:      else if (crossEdges23 a b c p q).contains e' then 1
668:      else 0) -
669:     (if (boundaryEdges23 a b c).contains e' then 1 else 0) := by
670:   dsimp
671:   rw [allEdges_count_eq_edgeDeg_countP (T := pachner23 T a b c p q) (e := normalizeEdge e)]
672:   rw [allEdges_count_eq_edgeDeg_countP (T := T) (e := normalizeEdge e)]
673:   exact tetIncidence_pachner23_delta
674:     (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (e := e) h
```

## PachnerInvariant/helpers.lean:11

```lean
3: namespace PachnerInvariant
4: 
5: def total_simplices (T : Triangulation) : Nat :=
6:   T.numVerts + (allEdges T).length + (allFaces T).length + T.tets.length
7: 
8: def is_valid (T : Triangulation) : Bool :=
9:   T.numVerts > 0 && !T.tets.isEmpty
10: 
11: def can_apply_pachner23 (T : Triangulation) (a b c p q : Vert) : Bool :=
12:   T.tets.any (tetEq (a, b, c, p)) && T.tets.any (tetEq (a, b, c, q))
13: 
14: def can_apply_pachner32 (T : Triangulation) (a b c p q : Vert) : Bool :=
15:   T.tets.any (tetEq (a, b, p, q)) &&
16:   T.tets.any (tetEq (a, c, p, q)) &&
17:   T.tets.any (tetEq (b, c, p, q))
18: 
19: def apply_moves (T : Triangulation) (a b c : Vert) (n : Nat) : Triangulation :=
20:   (List.range n).foldl (fun acc _ =>
21:     let p := acc.tets.length
22:     let q := acc.tets.length + 1
23:     pachner23 acc a b c p q) T
24: 
25: end PachnerInvariant
```

## PachnerInvariant/helpers.lean:23

```lean
15:   T.tets.any (tetEq (a, b, p, q)) &&
16:   T.tets.any (tetEq (a, c, p, q)) &&
17:   T.tets.any (tetEq (b, c, p, q))
18: 
19: def apply_moves (T : Triangulation) (a b c : Vert) (n : Nat) : Triangulation :=
20:   (List.range n).foldl (fun acc _ =>
21:     let p := acc.tets.length
22:     let q := acc.tets.length + 1
23:     pachner23 acc a b c p q) T
24: 
25: end PachnerInvariant
```

## PachnerInvariant/lambda_optimization.lean:13

```lean
5: def theta_with_lam (T : Triangulation) (lam : Nat) : Nat :=
6:   theta T lam
7: 
8: def optimize_lam (T : Triangulation) : Nat :=
9:   [1, 2, 3, 4, 5].foldl (fun best lam =>
10:     if theta_with_lam T lam < theta_with_lam T best then lam else best) 1
11: 
12: def optimize_lam_after_move (T : Triangulation) (a b c p q : Vert) : Nat :=
13:   optimize_lam (pachner23 T a b c p q)
14: 
15: -- Find shared vertices between two tets
16: def sharedVerts (t1 t2 : Vert × Vert × Vert × Vert) : List Vert :=
17:   (tetToVerts t1).filter ((tetToVerts t2).contains ·)
18: 
19: -- Extract 2→3 move parameters from a tet pair sharing a face
20: def tetPairToMove (t1 t2 : Vert × Vert × Vert × Vert) :
21:     Option (Vert × Vert × Vert × Vert × Vert) :=
22:   let sv := sharedVerts t1 t2
23:   if sv.length = 3 then
24:     let apexP := (tetToVerts t1).filter (fun v => !sv.contains v)
25:     let apexQ := (tetToVerts t2).filter (fun v => !sv.contains v)
26:     match sv, apexP, apexQ with
27:     | [a, b, c], [p], [q] => if p ≠ q then some (a, b, c, p, q) else none
28:     | _, _, _              => none
29:   else none
30: 
31: -- Find the first improving 2→3 move in T
```

## PachnerInvariant/lambda_optimization.lean:48

```lean
40: 
41: -- Greedily apply improving 2→3 moves until none remain (fuel bounds steps)
42: def greedyImprove (T : Triangulation) (lam : Nat) (fuel : Nat) : Triangulation :=
43:   match fuel with
44:   | 0      => T
45:   | n + 1  =>
46:     match findImprovingMove T lam with
47:     | none                  => T
48:     | some (a, b, c, p, q)  => greedyImprove (pachner23 T a b c p q) lam n
49: 
50: -- Count available improving moves
51: def countImprovingMoves (T : Triangulation) (lam : Nat) : Nat :=
52:   (T.tets.flatMap (fun t1 => T.tets.map (fun t2 => (t1, t2)))).countP
53:     (fun (t1, t2) =>
54:       match tetPairToMove t1 t2 with
55:       | some (a, b, c, p, q) => isImproving T a b c p q lam
56:       | none => false)
57: 
58: end PachnerInvariant
```

## PachnerInvariant/theta_delta.lean:20

```lean
12:   deltaThetaEdgeTerm T a b c p q + (Int.ofNat λ) * deltaThetaVertexTerm T a b c p q
13: 
14: theorem vertex_degree_delta_interface :
15:   ∀ (T : Triangulation) (a b c p q : Nat),
16:     True := by
17:   intro T a b c p q
18:   trivial
19: 
20: theorem theta_pachner23_delta :
21:   ∀ (T : Triangulation) (a b c p q : Nat) (λ : Nat),
22:     True := by
23:   intro T a b c p q λ
24:   trivial
25: 
26: end PachnerInvariant
```

