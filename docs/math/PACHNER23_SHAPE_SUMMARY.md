# Pachner23 shape summary

Status: INSPECTION SUMMARY.

Purpose:
Distill `docs/math/PACHNER23_SHAPE_EXTRACTION.md` into the smallest surface needed before proving `WellFormedTets_pachner23`.

Current theorem-level frontier:

```lean
theorem WellFormedTets_pachner23
    (T : Triangulation)
    (hT : WellFormedTets T)
    (a b c p q : Vert) :
    WellFormedTets (pachner23 T a b c p q)
```

Candidate definition lines:

```lean
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
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
65:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam ↔
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
68:   rw [thetaZ_pachner23_delta_expanded h]
70:   rw [frontier.edgeDeg_pachner23_new_edge_three (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
71:   rw [frontier.vertDeg_pachner23_at_p (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
72:   rw [frontier.vertDeg_pachner23_at_q (T := T) (a := a) (b := b) (c := c) (p := p) (q := q) h]
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
76: theorem pachner23_descent_of_vertex_sum
77:     {T : Triangulation} {a b c p q : Vert} {lam : Int}
80:     thetaZ (pachner23 T a b c p q) lam < thetaZ T lam := by
81:   exact (pachner23_descent_iff_vertex_sum_le_ten h hlam).2 hsum
8: def incidence (_T : Triangulation) (_e : Edge) : Int := 0
9: def vertIncidence (_T : Triangulation) (_v : Nat) : Int := 0
12:   ∀ (T : Triangulation) (a b c p q : Nat) (e : Edge),
14:     let T' := pachner23 T a b c p q
59: def tetContainsVert (t : Vert × Vert × Vert × Vert) (v : Vert) : Bool :=
62: def tetEq (t1 t2 : Vert × Vert × Vert × Vert) : Bool :=
63:   tetContainsVert t2 t1.1 && tetContainsVert t2 t1.2.1 &&
64:   tetContainsVert t2 t1.2.2.1 && tetContainsVert t2 t1.2.2.2
66: def pachner23 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
69:   let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
70:   { T with tets := kept ++ add }
72: def pachner32 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
75:   let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
76:   { T with tets := kept ++ add }
78: def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
79:   theta (pachner23 T a b c p q) lam < theta T lam
81: def isImproving32 (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
84: def eulerChar (T : Triangulation) : Int :=
72: def pachner32 (T : Triangulation) (a b c p q : Vert) : Triangulation :=
75:   let kept   := T.tets.filter (fun t => !remove.any (tetEq t))
76:   { T with tets := kept ++ add }
78: def isImproving (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
79:   theta (pachner23 T a b c p q) lam < theta T lam
81: def isImproving32 (T : Triangulation) (a b c p q : Vert) (lam : Nat) : Bool :=
84: def eulerChar (T : Triangulation) : Int :=
85:   (T.numVerts : Int) - (allEdges T).length + (allFaces T).length - T.tets.length
87: def twoTets : Triangulation :=
88:   { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }
90: def threeTets : Triangulation :=
91:   { numVerts := 6, tets := [(0,1,2,3),(0,1,2,4),(1,2,3,5)] }
93: def afterMove23 : Triangulation := pachner23 twoTets 0 1 2 3 4
85:   (T.numVerts : Int) - (allEdges T).length + (allFaces T).length - T.tets.length
87: def twoTets : Triangulation :=
88:   { numVerts := 5, tets := [(0,1,2,3),(0,1,2,4)] }
90: def threeTets : Triangulation :=
91:   { numVerts := 6, tets := [(0,1,2,3),(0,1,2,4),(1,2,3,5)] }
93: def afterMove23 : Triangulation := pachner23 twoTets 0 1 2 3 4
176:     theta (pachner23 twoTets 0 1 2 3 4) 1 < theta twoTets 1 := by native_decide
```

Required next proof ingredient:
Extract the exact inserted tetrahedron list from the candidate definition lines, then prove each inserted tetrahedron satisfies `pairwiseDistinctTet`.

Boundary:
No theorem-level closure is claimed by this summary.
No unconditional Pachner 2--3 delta theorem is claimed.
No false `allEdges` multiplicity bridge is restored.

