# Conditional: density-functional route for Pachner coherence

## Corrected status

The density-functional route is a sufficient conditional reduction, not a proved mechanism.

## I. Operational energy functional

For a null Pachner loop \(\gamma\), define
\[
\Phi(\gamma) := \bigl(D(\gamma), \delta_{\mathrm{sep}}(\gamma), \delta_{\mathrm{cr}}(\gamma), L(\gamma)\bigr)
\]
with lexicographic order.

Interpretation:

- \(D(\gamma)\): support-diameter;
- \(\delta_{\mathrm{sep}}(\gamma)\): separator-based non-squeezing obstruction;
- \(\delta_{\mathrm{cr}}(\gamma)\): local congestion;
- \(L(\gamma)\): word length.

## II. Conditional descent theorem (corrected)

Do not assert descent holds.

Replace by:

If there exists a finite local rewrite system \(\mathcal W_d\) such that for every null loop \(\gamma\),
\[
\gamma \rightsquigarrow \gamma'
\quad\Rightarrow\quad
\Phi(\gamma') < \Phi(\gamma)
\ \text{or}\
\gamma \equiv \gamma_1\cdots\gamma_k,\ \max_j D(\gamma_j) < D(\gamma),
\]
then bounded local generation follows.

## III. d=2 specialization (corrected)

Do not assert solved.

Replace by:

In \(d=2\), squares (disjoint commutation) and pentagons (flip cycles) form a candidate generating family, and associahedral coherence provides a candidate model for relations among relations.

The claim that all null loops are \(\Phi_2\)-descending remains a conjectural test case.

## IV. Separation obstruction (corrected)

\[
\delta_{\mathrm{sep}}(\gamma)
\]
measures obstruction to decomposition across separating subcomplexes.

Do not assert a threshold \(B_{crit}\) exists.

Replace by:

Bounded reducibility of \(\delta_{\mathrm{sep}}\) under local rewrites is an open condition equivalent to localization.

## V. Final conditional statement (corrected)

The following is sufficient:

If every null Pachner loop is \(\Phi\)-descending modulo bounded-local splitting, then finite coherent \(2\)-presentability holds.

## Status

Conditional.
