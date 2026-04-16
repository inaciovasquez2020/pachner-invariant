# Conditional: GH02t chain-homotopy coherence

## GH02t input
Every loop in the Pachner move graph bounds a finite 2-chain in the move-composition complex:
\[
\forall p,q:S\rightsquigarrow T,\quad \exists\, \Sigma_{p,q}\in C_2^{\mathrm{moves}}
\text{ with } \partial \Sigma_{p,q}=p^{-1}\cdot q.
\]

## Construction
Define the chain homotopy
\[
H_{p,q}(w):=\sum_{\sigma\in \Sigma_{p,q}} \mathcal A_\sigma(w),
\]
where \(\mathcal A_\sigma\) is the local 2-cell action induced by a Pachner relation.

## Consequence
\[
\Psi_p-\Psi_q=\partial_2^T H_{p,q}\quad \text{on }\ker(\partial_1^S).
\]

Hence
\[
[\Psi_p(w)]=[\Psi_q(w)].
\]

## Coherence
\[
H_{p,r}=H_{p,q}+H_{q,r},\qquad
H_{p\ast p',\,q\ast q'}=H_{p,q}+H_{p',q'}.
\]

## Result
This yields path-independence and functoriality:
\[
\mathcal F:\mathcal G_{\mathrm{Pachner}}\to \mathbf{Ab}.
\]

## Status
Conditional on GH02t.
