PachnerInvariant next solve
Status: OPEN.
Closed object:
- `rawEdges_count_eq_edgeDeg_countP` now builds.
Inserted tetrahedron pairwise-distinct lemmas now build in PachnerInvariant/Pachner23InsertedPairwise.lean.
Weakest sufficient next object:
Propagate `WellFormedTets` through the Pachner 2--3 move layer.

Constructor connection:
Connect the repository-level `pachner23` constructor to the inserted tetrahedra:
(a,b,p,q), (a,c,p,q), (b,c,p,q)
Target theorem shape:
theorem WellFormedTets_pachner23
    (T : Triangulation)
    (hT : WellFormedTets T)
    (a b c p q : Vert)
    (<needed distinctness hypotheses>) :
    WellFormedTets (pachner23 T a b c p q)
Boundary:
No unconditional Pachner 2--3 delta theorem is claimed.
No false `allEdges` multiplicity bridge is claimed.
