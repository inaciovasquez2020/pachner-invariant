# Conditional: localization program for the Pachner coherence theorem

## Objective

Define a quantitative support-diameter functional on Pachner loops and reduce finite coherent 2-presentability to a bounded-local-generation theorem.

## Step 1. Quantitative support-diameter functional

For a Pachner loop
\[
\gamma=(m_1,\dots,m_k)
\]
acting on triangulations of a fixed PL manifold \(M\), define:

- \(\operatorname{supp}(m_i)\): the subcomplex on which move \(m_i\) acts;
- \(\operatorname{Supp}(\gamma)=\bigcup_i \operatorname{supp}(m_i)\);
- \(D(\gamma)\): the minimal combinatorial diameter of a connected subcomplex containing \(\operatorname{Supp}(\gamma)\);
- \(L(\gamma)=k\): loop length.

Define the energy functional
\[
E(\gamma)=(D(\gamma),L(\gamma))
\]
ordered lexicographically.

## Step 2. Monotone reduction target

Seek a finite family of local rewrite rules
\[
\gamma \rightsquigarrow \gamma'
\]
such that for every null loop \(\gamma\), either:

- \(E(\gamma') < E(\gamma)\), or
- \(\gamma\) factors into a concatenation of loops of strictly smaller support-diameter.

If such a monotone descent system exists, bounded local generation follows.

## Step 3. Dimension-2 test case

For \(d=2\), specialize to the flip graph of triangulated polygons/surfaces.

Targets:

- compute explicit null loops built from flips;
- measure support-diameter and length;
- identify minimal nontrivial circuits;
- test whether every null loop reduces to bounded-diameter circuits.

Candidate local circuits include:
- inverse cancellation;
- disjoint commutation squares;
- pentagon flip relations;
- surface-local exchange circuits.

## Step 4. bistellar word diagrams

Encode each loop as a word diagram:
- vertices: intermediate triangulations;
- directed edges: Pachner moves;
- 2-cells: candidate local relations.

Search for compression rules:
- cancellation;
- commuting disjoint moves;
- replacement of local subwords by shorter equivalent subwords;
- splitting along disconnected support.

## Step 5. Comparison target

Relate the Pachner complex to known complexes where bounded-radius filling or local generation is available, including candidate analogies with:
- flip/associahedron complexes;
- rewriting complexes of finite presentations;
- CAT(0)-type cubical or simplicial models when available;
- complexes admitting bounded diagrammatic fillings.

## Exact remaining theorem

Prove that there exists \(B(d,M)<\infty\) such that every null Pachner loop and every ambiguity between its reductions is generated inside subcomplexes of support-diameter at most \(B(d,M)\).

## Status

Conditional.
