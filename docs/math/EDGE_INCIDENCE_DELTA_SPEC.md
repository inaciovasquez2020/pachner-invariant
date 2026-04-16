# Edge Incidence Delta Specification

Goal:
Compute the exact change in edge incidence under a Pachner 2→3 move.

Given:
- triangulation T
- valid move parameters (a,b,c,p,q)

Define:
Δ_inc(e) := incidence(pachner23(T), e) − incidence(T, e)

Required theorem (O1):
For all edges e,
Δ_inc(e) is supported only on the local move region and admits a finite explicit case split.

Output requirement:
A closed-form formula for Δ_inc(e) depending only on local combinatorics.
