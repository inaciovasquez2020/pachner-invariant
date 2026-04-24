PachnerInvariant next solve
Status: OPEN.
Closed object:
`rawEdges_count_eq_edgeDeg_countP` now builds in PachnerInvariant/RawEdgesFlatMapLift.lean.
Weakest sufficient next object:
Propagate `WellFormedTets` through the Pachner 2--3 move layer.
Target theorem shape:
theorem WellFormedTets_pachner23
    (T : Triangulation)
    (hT : WellFormedTets T)
    (a b c p q : Vert) :
    WellFormedTets (pachner23 T a b c p q)
Boundary:
No false `allEdges` multiplicity bridge is claimed.
