# thetaZ Blockers

Status: Conditional.

Minimal missing lemmas:

1. `allEdges_pachner23_eq`
2. `allEdges_mem_of_pachner23_new_edge`
3. `List.foldl_congr_sub_eq_changed_terms`

Blocked theorem:

`thetaZ_pachner23_delta_expanded`

Reason:

`thetaZ_pachner23_delta_expanded` requires the three lemmas above before
`pachner23_descent_iff_vertex_sum_le_ten` can be added.

No unconditional closure is claimed here.
