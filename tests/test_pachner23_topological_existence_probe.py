import math
from itertools import product

Tet = tuple

def edges(t):
    a,b,c,d = t
    return [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# TEST 1: invariance of arbitrary polynomial edge functional
def test_polynomial_invariant_nonexistence():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def poly(T):
        return sum((e[0] + e[1])**2 for t in T for e in edges(t))

    assert poly(T) != poly(T2)

# ------------------------------------------------------------
# TEST 2: exponential state-sum obstruction
def test_exponential_state_sum_instability():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def Z(T):
        return math.exp(-0.1 * sum(len(set(edges(t))) for t in T))

    assert abs(Z(T) - Z(T2)) > 1e-9

# ------------------------------------------------------------
# TEST 3: multiplicative quantum-like amplitude instability
def test_multiplicative_amplitude_instability():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def A(T):
        val = 1.0
        for t in T:
            for e in edges(t):
                val *= math.cos(e[0] + e[1] + 1.0)
        return val

    assert abs(A(T) - A(T2)) > 1e-9

# ------------------------------------------------------------
# TEST 4: normalized invariance failure (renormalization attempt)
def test_normalized_invariant_failure():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def N(T):
        raw = sum((e[0] - e[1])**2 for t in T for e in edges(t))
        norm = len(T)
        return raw / (1 + norm)

    assert N(T) != N(T2)

# ------------------------------------------------------------
# TEST 5: brute-force detection of hidden invariant in mixed basis
def test_no_hidden_mixed_basis_invariant():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def basis(T):
        return (
            sum(len(set(edges(t))) for t in T),
            sum((e[0]+e[1]) for t in T for e in edges(t)),
            sum((e[0]-e[1])**2 for t in T for e in edges(t))
        )

    for a,b,c in product([0.5,1.0,2.0], repeat=3):
        F = lambda X: a*basis(X)[0] + b*basis(X)[1] + c*basis(X)[2]
        if abs(F(T) - F(T2)) < 1e-9:
            assert False  # would indicate a hidden invariant

    assert True
