from collections import defaultdict

Tet = tuple

def edges(t):
    a,b,c,d = t
    return {(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)}

def inc(T, e):
    return sum(1 for t in T if e in edges(t))

def theta(T):
    return sum(len(edges(t)) for t in T)

# Pachner 2–3 move
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# candidate invariant: alternating edge potential (toy cochain)
def w(e):
    x,y = e
    return (x + y) % 2

def theta_w(T):
    total = 0
    for t in T:
        for e in edges(t):
            total += w(e)
    return total

def test_theta_not_topological_invariant():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    # topological invariant would require equality
    assert theta_w(T) != theta_w(T2)

def test_detect_non_invariance_under_pachner():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    diff = theta_w(T2) - theta_w(T)
    assert diff != 0

def test_flow_is_not_conservative():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    deltas = []
    for e in {(i,j) for t in T+T2 for i in t for j in t if i<j}:
        deltas.append(inc(T2,e) - inc(T,e))

    assert any(d != 0 for d in deltas)
