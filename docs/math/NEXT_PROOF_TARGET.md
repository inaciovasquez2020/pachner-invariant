# Next Proof Target

## Selected theorem

```lean
theorem tetToEdges_normalized_mem_characterization :
  ∀ (v1 v2 v3 v4 : Vert) (e : Vert × Vert),
  e ∈ (tetToEdges (v1, v2, v3, v4)).map normalizeEdge ↔
    e = normalizeEdge (v1, v2) ∨
    e = normalizeEdge (v1, v3) ∨
    e = normalizeEdge (v1, v4) ∨
    e = normalizeEdge (v2, v3) ∨
    e = normalizeEdge (v2, v4) ∨
    e = normalizeEdge (v3, v4)
Backtrack role
This fixes the exact normalized membership description before proving distinctness.
Immediate closure objective
Prove the normalized tetrahedron edge-list membership characterization.
