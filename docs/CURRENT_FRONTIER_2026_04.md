# CURRENT_FRONTIER_2026_04.md

Active Frontier 2026-04

Status: Conditional.

Canonical remaining wall:
construct the exact \(\mathbb F_2\) generator matrix for the bounded \(G_2\) layer and certify rank equality with the cycle-space targets.

Canonical exact targets:
- `F6`: 21 edge coordinates, cycle-rank target \(8\)
- `F7`: 84 edge coordinates, cycle-rank target \(43\)

Canonical artifacts:
- `docs/data/g2_incidence_matrix_exact.json`
- `docs/data/g2_exact_span_check.json`
- `docs/data/g2_enumeration.json`

Upgrade gate:
do not claim stronger closure until the exact rank equalities
\[
\operatorname{rank}_{\mathbb F_2}(M_{F6})=8,\qquad
\operatorname{rank}_{\mathbb F_2}(M_{F7})=43
\]
are recorded and `docs/data/g2_enumeration.json` is promoted from those passing certificates.
