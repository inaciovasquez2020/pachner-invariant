# G_k True Pachner 2-3 Inductive Closure Boundary

## Status
CONDITIONAL

## Theorem
Let \(M_{G_k}\) denote the repository-native \(\mathbb F_2\)-matrix for the bounded Pachner layer \(G_k\), and let
\[
\mathcal C_k=\{c_{k,1},\dots,c_{k,m_k}\}
\]
be the canonical family of Pachner \(2\to3\) outbound boundary carriers.

Assume:

1. **Carrier Independence.**
   The encoded boundary rows
   \[
   \partial^{\mathrm{out}}_2(c_{k,1}),\dots,\partial^{\mathrm{out}}_2(c_{k,m_k})
   \]
   are linearly independent modulo \(\operatorname{rowspan}(M_{G_k})\).

2. **Explicit Lift Rule.**
   There exists a repository-native construction
   \[
   \Phi_k : (M_{G_k},\mathcal C_k)\mapsto (M_{G_{k+1}},\mathcal C_{k+1})
   \]
   such that every new carrier row in \(G_{k+1}\) is obtained by canonical face-edge incidence transport from a carrier in \(G_k\) or by one new terminal carrier attached at the generator complement of \(\operatorname{rowspan}(M_{G_k})\).

3. **Kernel Disjointness Under Lift.**
   For every lifted carrier row \(r\in \partial^{\mathrm{out}}_2(\mathcal C_{k+1})\),
   \[
   r \notin \operatorname{rowspan}(M_{G_{k+1}}) + K_{k+1},
   \]
   where \(K_{k+1}\) is the canonical kernel family inherited from the generator system.

Then the carrier family remains independent modulo the base rowspace at every stage:
\[
\dim_{\mathbb F_2}
\frac{\operatorname{span}\bigl(M_{G_k}\cup \partial^{\mathrm{out}}_2(\mathcal C_k)\bigr)}
{\operatorname{rowspan}(M_{G_k})}
= |\mathcal C_k|.
\]

## Explicit construction rule
For each \(k\ge 7\), define \(G_{k+1}\) from \(G_k\) by:

1. Preserve the canonical representative order of generator columns.
2. Preserve all existing carrier rows by zero-extension to the new generator width.
3. Append one new carrier row supported on the first generator-complement column not used by prior carrier pivots.
4. If the lift introduces a paired boundary face, append the paired support bit on the next admissible complement column.
5. Canonicalize by pivot-chain hash and discard duplicates.

## Kernel-disjointness invariant
For each lifted carrier row \(r_{k+1}\), require:
\[
\operatorname{supp}(r_{k+1}) \cap \operatorname{Lead}(K_{k+1}) = \varnothing
\]
after canonical reduction modulo previously accepted carrier rows and base rows.

## Closure boundary
This document does not claim unconditional theorem-level closure.
It records the exact remaining theorem package required to upgrade the repository from inductive template status to proved \(G_k\)-layer closure.

## Finish condition
Replace `CONDITIONAL` by `PROVED` only after:
1. the carrier-independence theorem is proved,
2. the explicit lift rule is implemented repository-natively,
3. kernel disjointness under lift is proved,
4. the Lean inductive lemma is checked without placeholders.
