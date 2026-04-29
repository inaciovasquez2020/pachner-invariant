# ThetaZ Remaining Bridges

Status: Conditional.

Previously tracked bridges in `PachnerInvariant/ThetaZ.lean`:

1. `allEdges_mem_of_pachner23_new_edge`
2. `thetaZ_eq_theta_cast`

Consequences:

- `thetaZ_pachner23_delta_expanded` is structurally reduced to the existing theorem
  `theta_pachner23_delta_expanded`.
- `pachner23_descent_iff_vertex_sum_le_ten` is structurally reduced to
  `edgeDeg_pachner23_new_edge_three`,
  `vertDeg_pachner23_at_p`,
  `vertDeg_pachner23_at_q`,
  and the arithmetic identity `sq_step_identity`.

The raw-ready and Valid23WF wrapper theorem surfaces are now present in Lean.
