# Pachner23 inserted tetrahedron registry

Status: REGISTRY LOCK.

Purpose:
Create the smallest pre-theorem registry needed before proving `WellFormedTets_pachner23`.

Source:
`docs/math/PACHNER23_SHAPE_SUMMARY.md`.

Candidate inserted/removed-shape lines:

```lean
Distill `docs/math/PACHNER23_SHAPE_EXTRACTION.md` into the smallest surface needed before proving `WellFormedTets_pachner23`.
theorem WellFormedTets_pachner23
(T : Triangulation)
(hT : WellFormedTets T)
(a b c p q : Vert) :
WellFormedTets (pachner23 T a b c p q)
12: def thetaZ (T : Triangulation) (lam : Int) : Int :=
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
12: def thetaZ (T : Triangulation) (lam : Int) : Int :=
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
16: theorem allEdges_mem_of_pachner23_new_edge
17:     {T : Triangulation} {a b c p q : Vert}
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
17:     {T : Triangulation} {a b c p q : Vert}
19:     normalizeEdge (p,q) ∈ allEdges (pachner23 T a b c p q) := by
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
41:     (T : Triangulation) (lam : Int) :
21:       edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) = 3 := by
22:     simpa using edgeDeg_pachner23_new_edge_three
25:       0 < edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) := by
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
41:     (T : Triangulation) (lam : Int) :
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
41:     (T : Triangulation) (lam : Int) :
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
29:       (T := pachner23 T a b c p q) (e := (p,q))).2 hpos
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
41:     (T : Triangulation) (lam : Int) :
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
35: def DeltaThetaZ (T : Triangulation) (a b c p q : Vert) (lam : Int) : Int :=
36:   ((edgeDeg (pachner23 T a b c p q) (normalizeEdge (p,q)) - 3)^2 : Int) +
37:   lam * ((((vertexDeg (pachner23 T a b c p q) p - 6)^2 : Int) - (vertexDeg T p - 6)^2) +
38:          (((vertexDeg (pachner23 T a b c p q) q - 6)^2 : Int) - (vertexDeg T q - 6)^2))
41:     (T : Triangulation) (lam : Int) :
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
53: theorem thetaZ_pachner23_delta_expanded
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
54:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
56:     thetaZ (pachner23 T a b c p q) lam - thetaZ T lam =
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
59:   rw [theta_pachner23_delta_expanded (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) (lam := lam) h]
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
62: theorem pachner23_descent_iff_vertex_sum_le_ten
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
63:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
```

Required next theorem-level object:

```lean
theorem pachner23_inserted_tets_pairwiseDistinct
    (a b c p q : Vert)
    (h : <explicit distinctness assumptions>) :
    <each inserted tetrahedron satisfies pairwiseDistinctTet>
```

Missing object:
The exact inserted tetrahedron list must be selected from the registry before a Lean theorem can be stated without placeholders.

Boundary:
No theorem-level closure is claimed.
No unconditional Pachner 2--3 delta theorem is claimed.
No false `allEdges` multiplicity bridge is restored.

