# PachnerInvariant

A Lean 4 formalization of a combinatorial invariant for 3-manifold triangulations.

## Invariant

\[
\Theta(T,\lambda)=\sum_e(\deg_e-3)^2+\lambda\sum_v(\deg_v-6)^2.
\]

## Build

`lake build`

## Current frontier

Status: Conditional.

Executable closure is complete.

Canonical remaining wall:
exact \(\mathbb F_2\) generator-matrix certification for the bounded \(G_2\) layer.

Canonical artifacts:
- `docs/data/g2_incidence_matrix_exact.json`
- `docs/data/g2_exact_span_check.json`
- `docs/data/g2_enumeration.json`
- `docs/CURRENT_FRONTIER_2026_04.md`

Exact rank targets:
- `F6`: rank \(=8\)
- `F7`: rank \(=43\)

Promotion rule:
promote `docs/data/g2_enumeration.json` only after the exact rank equalities pass.

## Citation

Canonical citation:

> Vasquez, Inacio. *pachner-invariant*. GitHub repository. Version main. 2026-04-20.

Machine-readable metadata:

- `CITATION.cff`
- `CITATION.json`
- `ATTRIBUTION.md`
