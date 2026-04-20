# G_k True Pachner 2-3 Construction Rule

## Status
CONDITIONAL

For \(k\ge 7\), let \(n_k\) be the generator width of \(G_k\). Define the lift width by
\[
n_{k+1}=n_k+\delta_k,
\qquad \delta_k\ge 1.
\]

Let \(P_k\subseteq \{0,\dots,n_k-1\}\) be the ordered pivot set used by accepted outbound carrier rows.
Let
\[
C_k=\{0,\dots,n_k-1\}\setminus P_k
\]
be the generator complement.

The canonical lift step is:

1. zero-extend every accepted carrier row from width \(n_k\) to width \(n_{k+1}\);
2. enumerate \(C_{k+1}\) in increasing order;
3. choose the least unused complement index \(j\in C_{k+1}\);
4. create one new carrier row \(e_j\);
5. if the transported Pachner boundary requires a paired support bit, add the least unused \(j'>j\) in \(C_{k+1}\);
6. reduce modulo the base rowspace and prior carrier rows;
7. retain the row iff the reduction is nonzero.

This rule is the canonical repository-native replacement for the inductive template literal.

## Finish condition
Replace this file only when the repository implements the construction directly from Pachner move semantics rather than generator-complement transport.
