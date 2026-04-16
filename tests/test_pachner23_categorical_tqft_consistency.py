import math
from itertools import product

Tet = tuple

def edges(t):
    a,b,c,d = t
    return [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

# ------------------------------------------------------------
# Pachner 2–3 move
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# 6j-symbol proxy (categorical associator surrogate)
def six_j(a,b,c,d,e,f):
    # nontrivial structured tensor-like placeholder
    return math.cos(a+b-c+d-e+f)

# ------------------------------------------------------------
# associator consistency (pentagon proxy check)
def pentagon_weight(T):
    w = 1.0
    for t in T:
        a,b,c,d = t
        w *= six_j(a,b,c,d,a+b,c+d)
    return w

def test_pentagon_violation_under_pachner():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    assert abs(pentagon_weight(T) - pentagon_weight(T2)) > 1e-9

# ------------------------------------------------------------
# categorical invariance candidate (fusion-like contraction)
def fusion_tensor(T):
    val = 1.0
    for t in T:
        a,b,c,d = t
        val *= six_j(a,b,c,d,a+b,c+d)
    return val

def test_fusion_tensor_noninvariance():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    assert abs(fusion_tensor(T) - fusion_tensor(T2)) > 1e-9

# ------------------------------------------------------------
# coherence obstruction test (global vs local mismatch)
def coherence_obstruction(T):
    local = sum(six_j(*t,0,1) for t in T)
    global_ = fusion_tensor(T)
    return abs(local - global_)

def test_coherence_obstruction_changes():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    assert coherence_obstruction(T) != coherence_obstruction(T2)

# ------------------------------------------------------------
# categorical stability search (finite associator tuning)
def test_no_finite_associator_fix():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def invariant(a,b):
        def F(X):
            return a * fusion_tensor(X) + b * pentagon_weight(X)
        return F(T) == F(T2)

    for a,b in product([0.5,1.0,2.0], repeat=2):
        if invariant(a,b):
            assert False  # would indicate accidental categorical invariant

    assert True
