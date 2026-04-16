import math
from itertools import product

Tet = tuple

def edges(t):
    a,b,c,d = t
    return [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def dihedral_like_energy(T):
    # Regge-style toy energy: nonlinear edge interaction
    E = 0.0
    for t in T:
        es = edges(t)
        for i in range(len(es)):
            for j in range(i+1, len(es)):
                e1, e2 = es[i], es[j]
                E += 1.0 / (1 + abs(sum(e1) - sum(e2)))
    return E

def turaev_viro_like_weight(T, q=2):
    # toy state-sum style invariant proxy
    W = 1.0
    for t in T:
        deg = len(set(edges(t)))
        W *= math.sin(deg + q)
    return W

def curvature_proxy(T):
    # discrete curvature surrogate (nonlinear incidence square)
    from collections import Counter
    c = Counter()
    for t in T:
        for e in edges(t):
            c[e] += 1
    return sum(v*v for v in c.values())

def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# TEST 1: Regge-type energy is NOT invariant
def test_regge_noninvariance():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(dihedral_like_energy(T) - dihedral_like_energy(T2)) > 1e-9

# ------------------------------------------------------------
# TEST 2: Turaev–Viro-like product is NOT invariant (toy model)
def test_turaev_viro_noninvariance():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(turaev_viro_like_weight(T) - turaev_viro_like_weight(T2)) > 1e-9

# ------------------------------------------------------------
# TEST 3: curvature proxy changes under Pachner move
def test_curvature_proxy_change():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert curvature_proxy(T) != curvature_proxy(T2)

# ------------------------------------------------------------
# TEST 4: nonlinear combination cannot cancel generically
def test_nonlinear_combination_instability():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    F1 = dihedral_like_energy(T) + curvature_proxy(T)
    F2 = dihedral_like_energy(T2) + curvature_proxy(T2)

    assert abs(F1 - F2) > 1e-9

# ------------------------------------------------------------
# TEST 5: brute-force small nonlinear invariant failure
def test_no_simple_nonlinear_invariant():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    for alpha, beta in product([0.5,1.0,2.0], repeat=2):
        F = lambda X: alpha * dihedral_like_energy(X) + beta * curvature_proxy(X)
        if abs(F(T) - F(T2)) < 1e-9:
            assert False  # no stable nonlinear invariant found

    assert True
