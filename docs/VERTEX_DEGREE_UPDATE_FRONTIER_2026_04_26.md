# Vertex-Degree Update Frontier — 2026-04-26

Status: Open theorem obligation.

Minimal missing theorem:
`vertexDeg (pachner23 T a b c p q) v =
 vertexDeg T v + expectedVertexDeg23Delta a b c p q v`

Current first failing cases:
- `v = p`
- `v = q`
- `v ≠ p ∧ v ≠ q`

Reason this is the first frontier obstruction:
`PachnerInvariant.frontier` reaches this theorem before the later edge-degree and count-to-degree obligations.

Required proof ingredients:
1. unfold `vertexDeg`, `vertDeg`, `pachner23`, and `tetContainsVert`;
2. characterize which tetrahedra are removed by the 2→3 move;
3. characterize which tetrahedra are inserted by the 2→3 move;
4. count vertex incidence before and after replacement;
5. prove the three cases `p`, `q`, and all other vertices.

Boundary:
This file does not prove the theorem.
It isolates the first missing theorem required before the frontier layer can build.
