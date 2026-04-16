# Conditional: global functoriality integration

## Global object layer
For each underlying triangulated space \(X\), let \(\mathcal I_X\) be the filtered index category of admissible samplings. Define
\[
\mathcal F(X):=\varinjlim_{S\in\mathcal I_X} H_1^S(X).
\]

This requires:
\[
\forall S,T\in \mathcal I_X,\ \exists U\in \mathcal I_X\text{ with }S,T\le U,
\]
\[
\phi^X_{S,S}=\mathrm{id},\qquad
\phi^X_{T,U}\circ \phi^X_{S,T}=\phi^X_{S,U}.
\]

## Morphism layer
For every Pachner-groupoid morphism
\[
f:X\to Y
\]
and admissible samplings \(S\in \mathcal I_X\), \(T\in \mathcal I_Y\), assume compatible homomorphisms
\[
f_{S,T}:H_1^S(X)\to H_1^T(Y)
\]
satisfying
\[
\phi^Y_{T,T'}\circ f_{S,T}=f_{S,T'},
\qquad
f_{S',T}\circ \phi^X_{S,S'}=f_{S,T},
\]
and
\[
(g\circ f)_{S,U}=g_{T,U}\circ f_{S,T},
\qquad
(\mathrm{id}_X)_{S,S}=\mathrm{id}_{H_1^S(X)}.
\]

## Induced global functor
Under these assumptions,
\[
\mathcal F(f):\mathcal F(X)\to \mathcal F(Y),
\qquad
\mathcal F(f)([x]_S):=[f_{S,T}(x)]_T
\]
is well-defined and functorial.

## Boundary statement
Before construction of the compatible family \(f_{S,T}\), the framework yields only sampled/global-object colimit structure, not a full functor
\[
\mathcal G_{\mathrm{Pachner}}\to \mathbf{Ab}.
\]
