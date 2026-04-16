# Local Edge Classification Plan

Goal:
Replace the constant-zero edge-incidence placeholder by an explicit finite local case split.

Objects:
- `LocalEdgeClass = {removed, preserved, created, nonlocal}`
- `EdgeDelta = {-2,-1,0,1,2}`
- `edgeDeltaValue : EdgeDelta -> Int`

Required closure map:
1. classify each edge by local role
2. prove nonlocal edges have zero delta
3. assign exact delta value on removed/preserved/created classes
4. derive edge-degree delta
5. substitute into ΔΘ

Current state:
classification surface added; explicit combinatorial assignment still open.
