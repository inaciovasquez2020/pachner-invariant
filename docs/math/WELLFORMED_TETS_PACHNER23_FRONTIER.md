# WellFormedTets pachner23 frontier

Status: OPEN THEOREM-LEVEL FRONTIER.

Closed dependency:
`rawEdges_count_eq_edgeDeg_countP` is theorem-level proved conditional on `WellFormedTets T`.

Weakest sufficient next theorem:

```lean
theorem WellFormedTets_pachner23
    (T : Triangulation)
    (hT : WellFormedTets T)
    (a b c p q : Vert) :
    WellFormedTets (pachner23 T a b c p q)
Required proof ingredient:
Identify the exact tetrahedra inserted and removed by `pachner23`, then prove each inserted tetrahedron satisfies pairwiseDistinctTet.
Boundary:
Valid23 now carries the source well-formedness condition needed by the raw-edge chain.
No false `allEdges` multiplicity bridge is restored.

No unconditional Pachner 2--3 delta theorem is claimed here.
