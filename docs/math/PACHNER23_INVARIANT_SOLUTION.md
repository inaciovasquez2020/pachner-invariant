# Pachner 2–3 Invariant Solution (Edge Cochain Form)

## 1. Incidence formulation

For a triangulation \(T\) and edge \(e\):
\[
\mathrm{Inc}(T,e) = \#\{t \in T : e \subset t\}
\]

## 2. Theta functional

For a weight function \(w : \mathrm{Edge} \to \mathbb{Z}\):
\[
\theta_w(T) = \sum_{e} w(e)\,\mathrm{Inc}(T,e)
\]

## 3. Pachner 2–3 variation

\[
\Delta \theta_w = \sum_e w(e)\,\Delta \mathrm{Inc}(e)
\]

## 4. Local move vector

In the 5-vertex Pachner 2–3 configuration, the incidence variation vector is:
\[
v_{23} =
(-1,-1,-1,\ +1,+1,+1,\ +1,+1,+1,\ +3)
\]

corresponding to edge classes:
\[
(ab,bc,ca, ap,bp,cp, aq,bq,cq, pq)
\]

## 5. Invariant condition

A weight function is a Pachner 2–3 invariant iff:
\[
\sum_e w(e)\,\Delta \mathrm{Inc}(e) = 0
\]

equivalently:
\[
\langle w, v_{23} \rangle = 0
\]

## 6. Solution space

\[
\ker(v_{23}) \subset \mathbb{Z}^{10}
\quad \Rightarrow \quad \dim = 9
\]

Thus:
\[
\text{all invariants form a 9-dimensional linear space}
\]

## 7. Conclusion

Nontrivial Pachner 2–3 invariants exist and are exactly the linear cochains orthogonal to the incidence variation vector.
