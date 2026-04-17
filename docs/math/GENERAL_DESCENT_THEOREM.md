# General Descent Theorem

Status: Conditional.

Target statement:

For all triangulations T and vertices a b c p q and parameter lam > 0,

Valid23 T a b c p q
and explicit admissibility hypotheses H(T,a,b,c,p,q,lam)

imply

theta (pachner23 T a b c p q) lam < theta T lam

Weakest sufficient strategy:

1. isolate exact ΔΘ formula
2. bound new-edge contribution
3. bound p,q vertex contribution
4. show total ΔΘ < 0 under explicit H
5. transfer to Lean theorem

Conditional theorem proved in Lean:

For lam > 0, vertexDeg T p <= 5, and vertexDeg T q <= 5,

theta (pachner23 T a b c p q) lam < theta T lam.

Canonical weakest first candidate H:

H1. lam > 0
H2. vertexDeg T p <= 5
H3. vertexDeg T q <= 5

Do not promote beyond NOT FORMALIZED until theorem exists.
