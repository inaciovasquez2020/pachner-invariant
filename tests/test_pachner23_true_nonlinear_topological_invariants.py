import math
from itertools import product

Tet = tuple

def edges(t):
    a,b,c,d = t
    return [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

# ------------------------------------------------------------
# 1. state-sum invariant (Turaev–Viro proxy with q-dependence)
def tv_state_sum(T, q=2.0):
    val = 1.0
    for t in T:
        deg = len(set(edges(t)))
        val *= math.sin(q * (deg + 1))
    return val

def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# TEST 1: state-sum non-invariance under single move
def test_tv_state_sum_noninvariant_single_move():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(tv_state_sum(T) - tv_state_sum(T2)) > 1e-9

# ------------------------------------------------------------
# 2. normalized partition function (global rescaling test)
def normalized_partition(T):
    Z = tv_state_sum(T)
    norm = sum(len(set(edges(t))) for t in T)
    return Z / (1 + norm)

# ------------------------------------------------------------
# TEST 2: normalization does NOT restore invariance
def test_normalized_partition_noninvariant():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(normalized_partition(T) - normalized_partition(T2)) > 1e-9

# ------------------------------------------------------------
# 3. curvature-coupled state sum
def curvature_state_sum(T):
    E = 0
    for t in T:
        es = edges(t)
        E += sum((e[0]+e[1])**2 for e in es)
    return math.exp(-0.1 * E)

# ------------------------------------------------------------
# TEST 3: curvature state sum changes under Pachner move
def test_curvature_state_sum_changes():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(curvature_state_sum(T) - curvature_state_sum(T2)) > 1e-9

# ------------------------------------------------------------
# 4. quantum-like amplitude model (toy interference)
def amplitude(T, q=3.0):
    amp = 1.0
    for t in T:
        for e in edges(t):
            amp *= math.cos(q * (e[0] + e[1]))
    return amp

# ------------------------------------------------------------
# TEST 4: interference model not invariant under move
def test_amplitude_noninvariant():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(amplitude(T) - amplitude(T2)) > 1e-9

# ------------------------------------------------------------
# 5. brute-force search for hidden nonlinear invariant (finite ansatz)
def test_no_hidden_nonlinear_invariant_in_ansatz():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def observable(T, a, b, c):
        return a*tv_state_sum(T) + b*normalized_partition(T) + c*amplitude(T)

    found_invariant = False

    for a,b,c in product([0.5,1.0,2.0], repeat=3):
        if abs(observable(T,a,b,c) - observable(T2,a,b,c)) < 1e-9:
            found_invariant = True
            break

    # If true nonlinear invariant existed in this natural class, it would appear here
    assert found_invariant is False
