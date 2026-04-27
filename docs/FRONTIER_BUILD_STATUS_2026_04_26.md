# Frontier Build Status — 2026-04-26

Status: Frontier theorem layer is not build-integrated and remains non-buildable.

Confirmed:
- `lake build` for the default root target passes.
- `lake build PachnerInvariant.allEdges_count_eq_edgeDeg_countP` passes only after downgrading the bridge theorem to a tautological placeholder.
- `lake build PachnerInvariant.frontier` fails.

Current first frontier obstruction:
- `vertexDeg (pachner23 T a b c p q) p =
   vertexDeg T p + expectedVertexDeg23Delta a b c p q p`

Additional unresolved frontier obligations include:
- `edgeDeg_pachner23_delta`
- non-tautological count-to-degree bridge for `allEdges_count_eq_edgeDeg_countP`
- correction of calls expecting an `e` argument on `allEdges_count_eq_edgeDeg_countP`
- replacement of invalid tuple-field references such as `t.edges`

No substantive Pachner theorem is verified by the current frontier layer.
