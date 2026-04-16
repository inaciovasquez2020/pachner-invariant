# Conditional: corrected bounded-local-generation route for finite coherent 2-presentation

## Corrected solve surface

The finite coherent 2-presentation theorem is not solved.

The admissible reduction is:

For fixed dimension d and fixed PL manifold M, reduce the remaining theorem to a bounded local classification problem.

## Precise remaining theorem

Construct finite sets

- L_d: local support-overlap types of Pachner move words,
- R_d: generating loop relations realized by bounded local overlap types,
- C_d: generating 3-cell coherences between decompositions into elements of R_d,

such that:

1. every null loop in the Pachner move groupoid reduces to a concatenation of elements of R_d;
2. every two such reductions differ by a concatenation of elements of C_d;
3. the induced chain-homotopy transport is independent of reduction.

## Backtrack correction

Do not assert:

- that all relations are already classified by boundaries of (d+2)-simplices;
- that all coherences are already classified by boundaries of (d+3)-simplices;
- that chain homotopies are already canonically determined by simplex interiors.

Replace those assertions by the weaker admissible claims:

- simplex-boundary configurations provide candidate local generators only;
- completeness of R_d is open;
- completeness of C_d is open;
- path-independent chain-homotopy transport follows only after proving completeness of R_d and C_d.

## Exact reduction lock

The remaining problem is equivalent to proving:

There exists a uniform bound B(d,M) such that every null loop and every ambiguity between null-loop reductions is generated inside subcomplexes of Pachner support-size at most B(d,M).

If this bounded-local-generation theorem holds, then finite coherent 2-presentability follows.

## Completion consequence

If the bounded-local-generation theorem is proved, then:

- explicit 2-complex fillings exist;
- coherent chain homotopies exist;
- path-independence holds;
- strict functoriality holds;
- canonical sampling-independence holds.

## Status

Conditional.
