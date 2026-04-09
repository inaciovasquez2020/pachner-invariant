# Refinement Lift Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
The repository proves
\[
\Theta(\texttt{pachner\_move}(T),\lambda)>\Theta(T,\lambda)
\]
for the current abstract degree-level move model.

It does not yet prove the corresponding statement for a full adjacency-faithful Pachner \(2\to3\) move.

## Weakest sufficient missing theorem
Let
\[
\mathcal T_{\mathrm{full}}
\]
be a future adjacency-faithful triangulation model and
\[
\mathcal T_{\mathrm{abs}}
\]
the current abstract model.

Let
\[
\pi:\mathcal T_{\mathrm{full}}\to\mathcal T_{\mathrm{abs}}
\]
be a refinement map.

The weakest sufficient theorem is:

\[
\forall X\in\mathcal T_{\mathrm{full}},
\quad
\pi(M^{\mathrm{full}}_{2\to3}(X))=M^{\mathrm{abs}}_{2\to3}(\pi(X))
\]
and
\[
\Theta_{\mathrm{full}}(X,\lambda)=\Theta_{\mathrm{abs}}(\pi(X),\lambda)
\]
imply
\[
\Theta_{\mathrm{full}}(M^{\mathrm{full}}_{2\to3}(X),\lambda)>\Theta_{\mathrm{full}}(X,\lambda).
\]

## Minimal next artifact
The weakest next artifact is an executable refinement audit emitting:
1. preserved degree data under \(\pi\);
2. lost adjacency data under \(\pi\);
3. commutation status of \(M^{\mathrm{full}}_{2\to3}\) with \(M^{\mathrm{abs}}_{2\to3}\);
4. factorization status of \(\Theta_{\mathrm{full}}\) through \(\pi\).

## Label
This note is CONDITIONAL.
It isolates the weakest sufficient lifting theorem from the current abstract model to a full adjacency-faithful Pachner \(2\to3\) model.
