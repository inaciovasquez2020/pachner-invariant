# Conditional: GH02t reduction to finite presentability of the Pachner move 2-complex

## Statement
Let \(\mathcal P\) denote the Pachner move graph and let loops in \(\mathcal P\) represent composable move sequences returning to the same sampling.

GH02t is equivalent to the assertion that every loop in \(\mathcal P\) is null-homologous in a finite 2-complex of move relations.

## Reduction
It suffices to fill the following loop generators by explicit 2-cells:

### 1. Inverse cancellation
\[
\sigma \cdot \sigma^{-1}
\]
admits a degenerate 2-cell fill.

### 2. Disjoint move commutation
\[
\sigma_i \sigma_j = \sigma_j \sigma_i
\]
admits a square 2-cell fill.

### 3. Local bistellar relations
\[
\text{dimension-dependent finite local Pachner identities}
\]
admit bounded 2-cell fills.

## Consequence
If the Pachner move system admits a finite presentation by generators and relations using the classes above, then GH02t holds.

Equivalently:
\[
\boxed{
\text{GH02t reduces to finite presentability of the Pachner move 2-complex.}
}
\]

## Status
Conditional.

Current blocking object:
\[
\boxed{
\text{A finite complete set of Pachner move relations generating all loops.}
}
\]

## Integration consequence
Under this reduction, chain-homotopy coherence follows once the finite presentation theorem is supplied.
