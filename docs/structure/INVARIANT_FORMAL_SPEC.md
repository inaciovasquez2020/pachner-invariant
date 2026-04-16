# Invariant Formal Specification

Let T be a finite triangulation.

Define edge degrees:
deg_e(T) := number of tetrahedra incident to edge e.

Define vertex degrees:
deg_v(T) := number of tetrahedra incident to vertex v.

Define:
Θ(T, λ) :=
  ∑_{e ∈ E(T)} (deg_e(T) - 3)^2
  + λ ∑_{v ∈ V(T)} (deg_v(T) - 6)^2.

Target condition:
Θ(T, λ) strictly decreases under admissible Pachner 2→3 moves.
