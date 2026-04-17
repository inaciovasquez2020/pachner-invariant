# General Descent Theorem

Status: NOT FORMALIZED

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

Canonical weakest first candidate H:

H1. lam > 0
H2. vertexDeg T p <= 5
H3. vertexDeg T q <= 5
H4. new edge (p,q) contributes zero defect after move
H5. no hidden degree inflation outside p,q

Do not promote beyond NOT FORMALIZED until theorem exists.
