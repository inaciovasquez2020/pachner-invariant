# AL2 Local Edge Classification Theorem

Status: OPEN

Let
L = {
{a,b}, {b,c}, {c,a},
{a,p}, {b,p}, {c,p},
{a,q}, {b,q}, {c,q},
{p,q}
}.

For a valid Pachner 2→3 move (T,a,b,c,p,q), define
Δ_inc(e) := inc(pachner23(T,a,b,c,p,q), e) - inc(T, e).

Target theorem:

1. Support:
   For every edge e, if e ∉ L, then Δ_inc(e) = 0.

2. Local classification:
   For every edge e ∈ L, Δ_inc(e) is determined by an explicit finite case split by local edge type.

3. Range:
   Δ_inc(e) ∈ {-2,-1,0,1,2}.

This is the exact remaining combinatorial theorem needed to replace the current placeholder edge-incidence surface.
