# G2 Canonical Generator System

## Status
CONDITIONAL

## Generator expansion rule

For each bounded Pachner move-edge
\[
e=(u,v)\in E_G,
\]
define
\[
\Phi(e)=\Gamma(e):=\{(e,\tau,\epsilon): \tau\in\partial(e),\ \epsilon\in\{0,1\}\}.
\]

The full generator system is
\[
\Gamma_G=\bigsqcup_{e\in E_G}\Phi(e).
\]

## Dependent relation family

The canonical relation family is
\[
\mathcal R_G=\mathcal R_G^{\mathrm{inc}}\cup \mathcal R_G^{\mathrm{cycle}}\cup \mathcal R_G^{\mathrm{overlap}}.
\]

The augmented matrix is
\[
\widetilde M_G=
\begin{bmatrix}
\mathcal R_G^{\mathrm{inc}}\\
\mathcal R_G^{\mathrm{cycle}}\\
\mathcal R_G^{\mathrm{overlap}}
\end{bmatrix}.
\]

## Target equalities

\[
\operatorname{rank}_{\mathbb F_2}(\widetilde M_{F6})=8,
\qquad
\operatorname{rank}_{\mathbb F_2}(\widetilde M_{F7})=43.
\]
