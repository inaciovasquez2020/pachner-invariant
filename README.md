# PachnerInvariant

A Lean 4 formalization of a combinatorial invariant for 3-manifold triangulations.

## Invariant

\[
\Theta(T,\lambda)=\sum_e(\deg_e-3)^2+\lambda\sum_v(\deg_v-6)^2.
\]

## Build

`lake build`


Next theorem target:
- `docs/status/NEXT_TARGET_THEOREM_2026_04_23.md`
- issue: https://github.com/inaciovasquez2020/pachner-invariant/issues/25

## Current frontier

Status: Exact bounded G_2 rank certification complete.

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

## External status

This repository is governed by [`docs/status/EXTERNAL_STATUS_LOCK.md`](docs/status/EXTERNAL_STATUS_LOCK.md). Build success, CI success, dashboards, ledgers, axioms, admits, `sorry`, or placeholder witnesses do not constitute theorem-level closure.
