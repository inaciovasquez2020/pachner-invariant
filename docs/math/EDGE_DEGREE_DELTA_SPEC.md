# Edge Degree Delta Specification

Goal:
Compute the change in edge degree under a Pachner 2→3 move.

Given:
Δ_inc(e) from the edge-incidence delta.

Define:
deg_e(T) := incidence count of e in T.

Then:
Δ_deg(e) := deg_e(pachner23(T)) − deg_e(T)

Required theorem (O3):
Δ_deg(e) is computable directly from Δ_inc(e) and is supported on the local move region.
