# Valid23 Multiplicity Frontier — 2026-04-26

Status: Open structural assumption.

The vertex-degree update theorem cannot be proved from the current `Valid23`.

Current theorem target:
`vertexDeg (pachner23 T a b c p q) v =
 vertexDeg T v + expectedVertexDeg23Delta a b c p q v`

Counterexample pattern:
If `T.tets` contains duplicate copies of a removed tetrahedron, then `pachner23`
removes all matching copies via `filter`, while the expected delta assumes a
single local 2→3 replacement.

Concrete duplicate example:
`[(0,1,2,3),(0,1,2,3),(0,1,2,4)]`

Observed:
- `vertexDeg p: 2 → 3`, delta `+1`
- `vertexDeg q: 1 → 3`, delta `+2`

Minimal missing structural condition:
`Valid23` must require exact multiplicity of the two removed tetrahedra:
- exactly one tet equivalent to `(a,b,c,p)` occurs in `T.tets`;
- exactly one tet equivalent to `(a,b,c,q)` occurs in `T.tets`.

Boundary:
No vertex-degree update theorem is valid until this multiplicity condition is
added or the move implementation is changed to remove exactly one matching copy.
