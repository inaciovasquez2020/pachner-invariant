# PachnerInvariant

A Lean 4 formalization of a combinatorial invariant for 3-manifold triangulations.

## Invariant

\[\Theta(T,\lambda)=\sum_e(\deg_e-3)^2+\lambda\sum_v(\deg_v-6)^2.\]

## Current theorem status

Visible proved theorems in `PachnerInvariant/descent_property.lean` are concrete strict-improvement instances.

## Frontier

Valid23 -> edge-degree update -> vertex-degree update -> exact Delta-Theta identity -> Theta-descent criterion.

## Build

`lake build`

## Current frontier notes

* `docs/VALID23_SPEC_2026_04.md`
* `docs/EDGE_DEGREE_UPDATE_2026_04.md`
* `docs/VERTEX_DEGREE_UPDATE_2026_04.md`
* `docs/THETA_DELTA_IDENTITY_2026_04.md`
* `docs/THETA_DESCENT_CRITERION_2026_04.md`
* `docs/CURRENT_FRONTIER_2026_04.md`

## Conditional notes

* `docs/COMBINATORIAL_FIDELITY_NOTE_2026_04.md`
* `docs/REFINEMENT_LIFT_NOTE_2026_04.md`

## Current frontier

Status: Conditional.

Executable closure is complete (build/tests/status surfaces locked).
The only remaining mathematical layer is actual G_2 cycle enumeration, coverage, and certificates for n=5,6,7 in docs/data/g2_enumeration.json.
