# Pachner Move Interface

## Core object
A Pachner 2→3 move is represented by:
- input triangulation `T`
- vertices `a b c p q`
- output triangulation `pachner23 T a b c p q`

## Required interface
- `Valid23 T a b c p q`
- `pachner23 T a b c p q`
- edge-degree update surface
- vertex-degree update surface
- ΔΘ expansion surface
- Θ-descent surface

## Intended dependency chain
`Valid23`
→ local combinatorial replacement
→ edge/vertex incidence update
→ degree update formulas
→ ΔΘ formula
→ conditional general descent theorem under <=5 vertex hypotheses
