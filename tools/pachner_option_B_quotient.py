# Option B: Quotient by isomorphism class (canonical representative idea)

from itertools import combinations

def canonical_triangulation(n):
    # placeholder canonical representative
    return tuple(sorted(combinations(range(n), 4)))

def quotient_state(n):
    return canonical_triangulation(n)
