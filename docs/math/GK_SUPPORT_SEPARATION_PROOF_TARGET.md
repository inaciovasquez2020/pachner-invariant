# G_k Support Separation Proof Target

## Status
OPEN

## Target theorem
For every \(k\ge 7\) and every new carrier
\[
c_{k+1}^{\mathrm{new}}\in
\partial^{\mathrm{out}}_2(\mathcal C_{k+1})
\setminus
\Phi_k(\partial^{\mathrm{out}}_2(\mathcal C_k)),
\]
one has
\[
\operatorname{supp}(c_{k+1}^{\mathrm{new}})
\cap
\Bigl(\Phi_k(P_k)\cup \operatorname{Lead}(K_{k+1}^{\mathrm{new}})\Bigr)
=\varnothing.
\]

## Repository-native proof obligations
1. Define the support of each lifted carrier row.
2. Define the transported pivot set \(\Phi_k(P_k)\).
3. Define the lead-support set \(\operatorname{Lead}(K_{k+1}^{\mathrm{new}})\).
4. Prove support disjointness from transported pivots.
5. Prove support disjointness from new-kernel lead coordinates.

## Finish condition
Replace `OPEN` by `PROVED` only after the disjointness theorem is checked in Lean without assumptions.
