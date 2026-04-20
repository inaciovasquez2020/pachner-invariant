# G_k Support Separation Final Wall

## Status
OPEN

## Minimal missing lemma
For every \(k\ge 7\) and every new carrier
\[
c_{k+1}^{\mathrm{new}}\in \partial^{\mathrm{out}}_2(\mathcal C_{k+1})\setminus \Phi_k(\partial^{\mathrm{out}}_2(\mathcal C_k)),
\]
one has
\[
\operatorname{supp}(c_{k+1}^{\mathrm{new}})
\cap
\Bigl(\Phi_k(P_k)\cup \operatorname{Lead}(K_{k+1}^{\mathrm{new}})\Bigr)
=\varnothing.
\]

## Consequence
Then
\[
c_{k+1}^{\mathrm{new}}
\notin
\Phi_k(R_k)\oplus \Phi_k(C_k)\oplus \Phi_k(K_k)\oplus K_{k+1}^{\mathrm{new}},
\]
and therefore
\[
(\Phi_k(R_k)\oplus \Phi_k(C_k))
\cap
\operatorname{span}\!\bigl(\partial^{\mathrm{out}}_2(\mathcal C_{k+1})\setminus \Phi_k(\partial^{\mathrm{out}}_2(\mathcal C_k))\bigr)
=\{0\}.
\]

## Finish condition
Replace `OPEN` by `PROVED` only after the support-separation lemma is proved repository-natively and discharged in Lean without assumptions.
