# G_k Inductive Independence Preservation

## Status
CONDITIONAL

## Setup
Let
\[
R_k=\operatorname{rowspan}(M_{G_k}),
\qquad
C_k=\operatorname{span}\!\bigl(\partial^{\mathrm{out}}_2(\mathcal C_k)\bigr),
\qquad
P_k=\text{pivot set of the accepted carrier rows in }G_k.
\]

Let
\[
\Phi_k:\mathbb F_2^{n_k}\to\mathbb F_2^{n_{k+1}}
\]
be the canonical zero-extension lift together with the repository-native carrier-coordinate insertion rule.

Let
\[
K_{k+1}= \Phi_k(K_k)\oplus K_{k+1}^{\mathrm{new}}
\]
be the desired kernel splitting, where \(K_{k+1}^{\mathrm{new}}\) is supported only on newly created generator-complement coordinates.

## Carrier support disjointness
For every new carrier row \(c_{k+1}^{\mathrm{new}}\), require
\[
\operatorname{supp}(c_{k+1}^{\mathrm{new}})
\cap
\Bigl(\Phi_k(P_k)\cup \operatorname{Lead}(K_{k+1}^{\mathrm{new}})\Bigr)
=\varnothing.
\]

## Lift injectivity on the old certified space
Require
\[
\Phi_k|_{R_k\oplus C_k} : R_k\oplus C_k \to \mathbb F_2^{n_{k+1}}
\]
to be injective.

Equivalently,
\[
\Phi_k(x)=0,\ x\in R_k\oplus C_k
\quad\Longrightarrow\quad
x=0.
\]

## Kernel direct-sum transport
Require
\[
K_{k+1}= \Phi_k(K_k)\oplus K_{k+1}^{\mathrm{new}}
\]
with
\[
\Phi_k(K_k)\cap K_{k+1}^{\mathrm{new}}=\{0\}.
\]

## Intersection equality
Under the three hypotheses above, the new carrier rows satisfy
\[
\Phi_k(R_k)\cap
\operatorname{span}\!\bigl(\partial^{\mathrm{out}}_2(\mathcal C_{k+1})\setminus \Phi_k(\partial^{\mathrm{out}}_2(\mathcal C_k))\bigr)
=\{0\}.
\]

More strongly,
\[
\bigl(\Phi_k(R_k)\oplus \Phi_k(C_k)\bigr)
\cap
\operatorname{span}\!\bigl(\partial^{\mathrm{out}}_2(\mathcal C_{k+1})\setminus \Phi_k(\partial^{\mathrm{out}}_2(\mathcal C_k))\bigr)
=\{0\}.
\]

Hence the independence quotient grows by the number of new carriers:
\[
\dim_{\mathbb F_2}
\frac{\operatorname{span}\!\bigl(M_{G_{k+1}}\cup \partial^{\mathrm{out}}_2(\mathcal C_{k+1})\bigr)}
{\operatorname{rowspan}(M_{G_{k+1}})}
=
\dim_{\mathbb F_2}
\frac{\operatorname{span}\!\bigl(M_{G_k}\cup \partial^{\mathrm{out}}_2(\mathcal C_k)\bigr)}
{\operatorname{rowspan}(M_{G_k})}
+
\#\bigl(\mathcal C_{k+1}\setminus \Phi_k(\mathcal C_k)\bigr).
\]

## Finish condition
Replace `CONDITIONAL` by `PROVED` only after the Lean theorem `inductive_independence_preservation`
is checked without placeholders and the repository-native lift realizes each hypothesis.
