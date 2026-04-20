# G_k Lift Map and Kernel Transport

## Status
CONDITIONAL

## Lift map
For each \(k \ge 7\), define the rowspace lift operator
\[
\Phi_k : \mathbb F_2^{n_k} \to \mathbb F_2^{n_{k+1}}
\]
by zero-extension on old coordinates together with insertion of the new carrier-support coordinates prescribed by the canonical lift rule.

For a row \(r=(r_0,\dots,r_{n_k-1})\), write
\[
\Phi_k(r)=(r_0,\dots,r_{n_k-1},0,\dots,0).
\]

For a rowspace \(R_k \subseteq \mathbb F_2^{n_k}\), define
\[
\Phi_k(R_k)=\{\Phi_k(r): r\in R_k\}.
\]

## Kernel transport invariance
Let \(K_k\) be the canonical kernel family of the \(G_k\) generator system.
The required transport statement is
\[
\Phi_k(K_k) \subseteq K_{k+1}.
\]

The strong form needed for closure is
\[
\dim_{\mathbb F_2} \Phi_k(K_k)=\dim_{\mathbb F_2} K_k
\quad\text{and}\quad
K_{k+1}=\Phi_k(K_k)\oplus K^{\mathrm{new}}_{k+1}
\]
with \(K^{\mathrm{new}}_{k+1}\) supported only on the newly introduced generator-complement coordinates.

## New-carrier escape
Let \(c_{k+1}\) be the newly introduced Pachner \(2\to3\) outbound carrier row.
The missing escape statement is
\[
c_{k+1}\notin \Phi_k(\operatorname{rowspan}(M_{G_k}))+\Phi_k(K_k).
\]

## Pivot collision bound
Let \(P_k\) be the pivot set of accepted carrier rows in \(G_k\).
The canonical lift rule must guarantee
\[
\operatorname{supp}(c_{k+1}) \cap \Phi_k(P_k)=\varnothing
\]
after reduction modulo \(\Phi_k(\operatorname{rowspan}(M_{G_k}))\).

Equivalently, if \(j_{k+1}\) is the least unused complement index, then
\[
j_{k+1}\notin \Phi_k(P_k)
\]
and every paired support coordinate is chosen outside \(\Phi_k(P_k)\).

## Inductive closure lemma
Under the four assumptions above,
\[
\dim_{\mathbb F_2}
\frac{\operatorname{span}\bigl(M_{G_{k+1}}\cup \partial^{\mathrm{out}}_2(\mathcal C_{k+1})\bigr)}
{\operatorname{rowspan}(M_{G_{k+1}})}
=
\dim_{\mathbb F_2}
\frac{\operatorname{span}\bigl(M_{G_k}\cup \partial^{\mathrm{out}}_2(\mathcal C_k)\bigr)}
{\operatorname{rowspan}(M_{G_k})}
+1.
\]

## Finish condition
Replace `CONDITIONAL` by `PROVED` only after the Lean lemma corresponding to the inductive closure statement is checked without placeholders.
