# Pachner Count Bridge Theorem Status — 2026-04-26

Status: Theorem-level bridge synchronized  
Scope: PachnerInvariant 2--3 edge-count / edge-degree bridge

## 1. Current verified state

The count bridge

```text
allEdges_count_eq_edgeDeg_countP
is theorem-level present in
PachnerInvariant/allEdges_count_eq_edgeDeg_countP.lean
and is imported by
PachnerInvariant/frontier.lean
The downstream 2--3 edge-degree chain uses this theorem-level bridge.
2. Verified downstream chain
The following theorem-level objects are present in PachnerInvariant/frontier.lean:
allEdges_pachner23_count_delta
edgeDeg_pachner23_delta
edgeDeg_pachner23_eq_expected
3. Documentation correction
The repository no longer treats
allEdges_count_eq_edgeDeg_countP
as a live axiom target.
The stale status language was corrected in:
docs/status/PACHNER_FRONTIER_REGISTRY.md
docs/math/NEXT_AXIOM_TARGET.md
docs/math/ALL_EDGES_COUNT_EQ_EDGEDEG_COUNTP_TARGET.md
4. Verification state
Lean build: PASS
pytest: 295/295 passed
commit: ff390fc docs(pachner): sync count bridge theorem status
5. Remaining frontier
The remaining frontier is no longer the count bridge.
The next remaining frontier is downstream theta/descent closure, including the theta/descent theorem surface depending on the already-present 2--3 edge-degree chain.
6. Non-overclaim boundary
No global Pachner descent theorem is asserted here.
No new topological invariant theorem is asserted here.
This snapshot only records that the count bridge and 2--3 edge-degree bridge documentation now matches the theorem-level code state.
