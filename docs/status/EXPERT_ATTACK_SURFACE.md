# Expert Attack Surface

Status: OPEN

Primary expert attacks:

1. Placeholder-generalization attack
   Current issue:
   `edge_incidence_delta_lemma` is a surface theorem stub, not the final local combinatorial formula.

2. Delta-closure attack
   Current issue:
   the general ΔΘ expansion is proved, but the general descent theorem is not yet formalized.

3. Toy-to-general attack
   Current issue:
   concrete `native_decide` examples do not imply the arbitrary `Valid23` case.

4. Semantic-validity attack
   Current issue:
   the precise preservation interface from local move syntax to intended triangulation semantics must be exposed theorem-by-theorem.

5. Invariant-meaning attack
   Current issue:
   Θ must be justified as a structural descent quantity, not only a computed score.

Canonical defense order:

1. prove edge-incidence delta
2. prove vertex-incidence delta
3. derive degree-delta formulas
4. derive ΔΘ expansion
5. prove descent under explicit admissibility hypotheses
