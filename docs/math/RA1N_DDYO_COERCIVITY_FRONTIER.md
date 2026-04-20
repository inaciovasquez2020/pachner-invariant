# RA1n DDYO Coercivity Frontier

## Status
CONDITIONAL

## Structural layer
CLOSED

## Geometric layer
CLOSED

## Numerical layer
BENCHMARKED

## Corrected terminal geometry
\[
\Gamma_{\mathrm{term}}^{\sharp}
=
\left\{
(\xi,\eta):
\begin{array}{l}
2^{k-1}\le |\xi|,|\eta|\le 2^{k+1},\\
\bigl||\xi|-|\eta|\bigr|\le 2^{k-C-3},\\
2^{k-C-2}\le |\xi+\eta|\le 2^{k-C}
\end{array}
\right\}.
\]

## Terminal gap lemma
\[
1-\cos\alpha_{\xi,\eta}
=
1+\cos\theta_{\xi,\eta}
=
\frac{|\xi+\eta|^2-(|\xi|-|\eta|)^2}{2|\xi||\eta|}
\ge 3\cdot 2^{-2C-9}.
\]

## Coercivity template
\[
c_{\mathrm{RA1n}}
\ge
\delta \cdot \underline{\kappa}\cdot
\left(
\inf_{\Gamma_{\mathrm{term}}^{\sharp}}
|\partial_\theta^2 \mathfrak M_k^{\mathrm{DDYO}}|
\cdot
3\cdot 2^{-2C-9}
\right)^2.
\]

## Benchmarked packet data
\[
\min \gamma_a = 0.22426,\qquad
\max_{a}\sum_{b\neq a}|m_{ab}| = 0.00228,
\]
\[
\delta = 0.9898,\qquad
|m_{ab}|\le 26.3 e^{-10|a-b|},
\]
\[
c_{\mathrm{RA1n}}^{\mathrm{bench}} \approx 0.222.
\]

## Exact-symbol nondegeneracy package
\[
\mathcal S_{\mathrm{DDYO}}^{\mathrm{explicit}}
=
\left(
\sigma_{\mathrm{eff}}(\xi,\eta),
\kappa_{\mathrm{rank\_defect}}(\xi,\eta),
D_j(\xi,\eta),
\kappa^{\mathrm{DDYO}}(\xi)
\right)
\]
with bounds
\[
0<\underline{\sigma}\le \sigma_{\mathrm{eff}}(\xi,\eta)\le \overline{\sigma}<\infty,
\]
\[
0<\underline{\kappa}_{\mathrm{rank}}
\le
|\kappa_{\mathrm{rank\_defect}}(\xi,\eta)|,
\]
\[
0<\underline{D}\le D_j(\xi,\eta)\le \overline{D}<\infty,
\qquad j\ge k+1,
\]
\[
0<\underline{\kappa}\le \kappa^{\mathrm{DDYO}}(\xi)\le \overline{\kappa}<\infty,
\]
and
\[
\inf_{(\xi,\eta)\in\Gamma_{\mathrm{term}}^{\sharp}}
|d_\perp^2 r_k(\xi,\eta)|
\ge a_{\mathrm{curv}}>0.
\]

## Finish condition
Replace symbolic package by explicit formulas and prove transverse nondegeneracy.
