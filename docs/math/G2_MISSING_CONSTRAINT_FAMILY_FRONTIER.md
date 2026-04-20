# G2 Missing Constraint Family Frontier

## Status
OPEN

## Current matrix data

For the current bounded \(G_2\) matrices:

- \(\operatorname{rank}_{\mathbb F_2}(M_{F6}) = 3\), \(\operatorname{target}(F6) = 8\), \(n_{F6} = 3\).
- \(\operatorname{rank}_{\mathbb F_2}(M_{F7}) = 7\), \(\operatorname{target}(F7) = 43\), \(n_{F7} = 7\).

## Missing family

Define a repository-native family of additional constraint rows
\[
\mathcal{R}_G = \{\rho_1,\dots,\rho_t\}
\]
such that the augmented matrix
\[
\widetilde{M}_G =
\begin{bmatrix}
M_G \\
\mathcal{R}_G
\end{bmatrix}
\]
satisfies
\[
\operatorname{rank}_{\mathbb F_2}(\widetilde{M}_{F6})=8,
\qquad
\operatorname{rank}_{\mathbb F_2}(\widetilde{M}_{F7})=43.
\]

## Required augmentation counts from current data

- F6 requires exactly
  \[
  5
  \]
  additional independent rows beyond the current matrix.

- F7 requires exactly
  \[
  36
  \]
  additional independent rows beyond the current matrix.

## Kernel compatibility condition

For any admissible augmented matrix:
\[
\dim \ker(\widetilde{M}_G) = n_G - r(G).
\]

From the current column counts:

- F6 would require
  \[
  -5
  \]
  kernel dimension.

- F7 would require
  \[
  -36
  \]
  kernel dimension.

## Obstruction

If \(n_G < r(G)\), then no augmentation using the current generator set can reach target rank.

Therefore the missing object is not merely extra rows; it is the exact repository-native relation-and-generator model whose column set is large enough for the target ranks.

## Finish condition

Replace OPEN only after all of the following are produced:

1. An explicit repository-native definition of the missing relation family \(\mathcal{R}_G\).
2. An augmented matrix constructor for each bounded \(G\).
3. Deterministic \(\mathbb F_2\) elimination on \(\widetilde{M}_G\).
4. Verified equalities
   \[
   \operatorname{rank}_{\mathbb F_2}(\widetilde{M}_{F6})=8,
   \qquad
   \operatorname{rank}_{\mathbb F_2}(\widetilde{M}_{F7})=43.
   \]
