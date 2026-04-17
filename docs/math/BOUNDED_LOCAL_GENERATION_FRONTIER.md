# Bounded Local Generation Frontier

Status: Conditional

## Remaining theorem

There exists a universal constant C such that every Pachner loop γ admits a decomposition

γ = Σ_i R_i

where each generator/relation block R_i has support diameter at most C.

## Equivalent boundary form

For every loop γ in the Pachner move complex, there exists a 2-chain Σ with

∂Σ = γ

and every 2-cell used in Σ is supported inside a patch of diameter ≤ C.

## Reduction path

1. Prove d=2 flip-graph circuit classification.
2. Derive bounded local generators in dimension 2.
3. Lift generator schema to dimension 3 bistellar relations.
4. Add coherence moves.
5. Conclude bounded local generation.

## New ingredient

Support-diameter functional:

D(γ) := minimal maximal patch diameter among valid decompositions of γ.

Target:

sup_γ D(γ) < ∞
