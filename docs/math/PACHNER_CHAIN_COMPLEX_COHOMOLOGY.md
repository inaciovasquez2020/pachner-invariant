# Conditional: Integral Pachner chain complex

Chain groups:
- \(C_0\): sampled triangulations
- \(C_1\): directed Pachner paths
- \(C_2\): closed signed cycles in the move graph

Boundary maps:
\[
\partial_1 : C_1 \to C_0,
\qquad
\partial_2 : C_2 \to C_1
\]

Chain identity:
\[
\partial_1 \partial_2 = 0
\]

All \(C_2\) generators are filtered by the exact condition
\[
\partial_1(f)=0.
\]

Structural objects:
\[
\ker(\partial_1), \qquad \operatorname{im}(\partial_2), \qquad
H_1 = \ker(\partial_1)/\operatorname{im}(\partial_2).
\]

Integral analysis is performed via Smith normal form over \(\mathbb{Z}\), after removing every face that violates the chain identity.
