# Conditional: Extended Pachner chain complex

Chain groups:
- \(C_0\): sampled triangulations
- \(C_1\): directed Pachner moves
- \(C_2\): genuine move-composition relations

Boundary maps:
\[
\partial_1 : C_1 \to C_0,
\qquad
\partial_2 : C_2 \to C_1
\]

Chain-complex identity:
\[
\partial_1 \partial_2 = 0
\]

Degree-one cohomology dimension is formed by
\[
\dim H^1 = \dim \ker(\partial_1) - \operatorname{rank}(\partial_2),
\]
provided
\[
\operatorname{im}(\partial_2)\subseteq \ker(\partial_1).
\]

In this sampled model, the \(C_2\) generator is a genuine move-composition loop:
\[
(T_0 \to T_1) + (T_1 \to T_0).
\]
