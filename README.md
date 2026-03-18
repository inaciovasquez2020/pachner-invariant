# PachnerInvariant

A Lean 4 formalization of a combinatorial invariant for 3-manifold triangulations,
based on Pachner moves and degree-defect energy functions.

## Invariant

For a triangulation T with edge degrees `deg_e` and vertex degrees `deg_v`:

    Θ(T, λ) = Σ_e (deg_e − 3)² + λ · Σ_v (deg_v − 6)²

Lower Θ means T is closer to the ideal regular triangulation
(all edges degree 3, all vertices degree 6).

## Theorem

Every Pachner 2→3 move strictly increases Θ:

    theta (pachner_move T) > theta T

This is formally proved in `PachnerInvariant/descent_property.lean` using `omega`.

## Modules

| File | Contents |
|------|----------|
| `descent_property.lean` | `Triangulation`, `theta`, `pachner_move`, `strict_descent` |
| `lambda_optimization.lean` | `theta_with_lam`, `optimize_lam` |
| `helpers.lean` | `total_simplices`, `is_valid`, `apply_moves` |

## Build
```
lake build
./.lake/build/bin/Main
```

## Abstraction note

`pachner_move` models a 2→3 move by appending a new degree-1 edge and vertex.
This correctly captures the energy increase but does not redistribute degrees
among existing simplices. Full combinatorial fidelity would require an adjacency
structure tracking all simplicial connections explicitly.
