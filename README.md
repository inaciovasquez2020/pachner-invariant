# Pachner-Invariant Toolkit

This repo enumerates local Pachner configurations, computes ΔΘ, and searches for Θ=0 triangulations.
Also contains Lean skeleton to formalize descent_property.

## Steps to execute
1. Run `python3 experiments/pachner_enum.py` to enumerate local ΔΘ.
2. Run `python3 experiments/search_zero_theta.py` to search candidate Θ=0 triangulations.
3. Use `lean/descent_property.lean` to formalize invariant and Pachner moves in Lean.
