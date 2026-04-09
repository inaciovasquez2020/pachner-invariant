# Combinatorial Fidelity Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository proves strict increase of the declared energy functional
\[
\Theta(T,\lambda)=\sum_e(\deg_e-3)^2+\lambda\sum_v(\deg_v-6)^2
\]
for the repository's abstract move model.

It does not by itself prove the corresponding theorem for fully faithful Pachner 2→3 moves on explicit simplicial adjacency data.

## Isolated abstraction gap
The current move model
\[
\texttt{pachner\_move}
\]
is degree-level and abstract.
It appends a new degree-1 edge and a new degree-1 vertex.
It does not redistribute incidences among pre-existing simplices.

Therefore the current formal theorem establishes:
\[
\Theta(\texttt{pachner\_move}(T),\lambda)>\Theta(T,\lambda)
\]
for the repository model,
not yet the full adjacency-faithful statement.

## Weakest admissible extension
Let
\[
\mathcal T_{\mathrm{abs}}
\]
be the current abstract triangulation model and
\[
\mathcal T_{\mathrm{full}}
\]
a future adjacency-faithful triangulation model.

The weakest next structural artifact is a refinement map
\[
\pi:\mathcal T_{\mathrm{full}}\to\mathcal T_{\mathrm{abs}}
\]
such that:
\[
\pi(M_{2\to3}^{\mathrm{full}}(X))=M_{2\to3}^{\mathrm{abs}}(\pi(X))
\]
whenever the abstract move is intended to represent the full move.

## Minimal next artifact
The weakest next artifact is an executable refinement audit emitting:
1. the data lost under \(\pi\);
2. degree statistics preserved under \(\pi\);
3. whether \(\Theta\) factors through \(\pi\);
4. whether strict increase in the abstract model lifts to the full model.

## Label
This note is CONDITIONAL.
It preserves the repository's current abstract formalization claim and isolates the remaining combinatorial-fidelity gap.
