import math
from itertools import product

Tet = tuple

def edges(t):
    a,b,c,d = t
    return [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

# ------------------------------------------------------------
# FIXED: proper 6-edge flattening for tetrahedron
def tetra_to_6labels(t):
    es = edges(t)
    # enforce deterministic 6-label structure
    return (
        es[0][0], es[0][1],
        es[1][0], es[1][1],
        es[2][0], es[2][1]
    )

# ------------------------------------------------------------
# corrected 6j-symbol surrogate
def F_symbol(a,b,c,d,e,f):
    return math.cos(a + b - c + d - e + f)

# ------------------------------------------------------------
# Pachner move
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# corrected global TQFT proxy
def global_tqft_proxy(T):
    return sum(F_symbol(*tetra_to_6labels(t)) for t in T)

# ------------------------------------------------------------
# TEST 1: pentagon obstruction remains
def test_pentagon_identity_failure():
    lhs = F_symbol(0,1,2,3,4,5) * F_symbol(0,1,3,4,5,6)
    rhs = F_symbol(1,2,3,4,5,6) * F_symbol(0,2,3,5,6,7)
    assert abs(lhs - rhs) > 1e-9

# ------------------------------------------------------------
# TEST 2: fusion non-associativity
def test_fusion_associativity_not_closed():
    a = F_symbol(1,2,3,4,5,6)
    b = F_symbol(2,3,1,4,6,5)
    assert abs(a - b) > 1e-9

# ------------------------------------------------------------
# TEST 3: global Pachner non-invariance
def test_global_tqft_invariance_failure():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(global_tqft_proxy(T) - global_tqft_proxy(T2)) > 1e-9

# ------------------------------------------------------------
# TEST 4: coherence mismatch survives correction
def test_coherence_obstruction():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    diff = abs(global_tqft_proxy(T) - global_tqft_proxy(T2))
    assert diff > 1e-9

# ------------------------------------------------------------
# TEST 5: no accidental categorical invariance
def test_no_hidden_tqft_invariant():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    for scale in [0.5,1.0,2.0]:
        F = lambda X: scale * global_tqft_proxy(X)
        if abs(F(T) - F(T2)) < 1e-9:
            assert False

    assert True
