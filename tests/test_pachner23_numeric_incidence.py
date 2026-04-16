from collections import Counter

Tet = tuple

def edges(t):
    a,b,c,d = t
    return [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

def inc(T, e):
    return sum(1 for t in T if e in edges(t))

def theta(T):
    return sum(len(edges(t)) for t in T)

# valid Pachner 2–3 local configuration
def pachner23(T):
    T_old = [(0,1,2,3),(0,1,2,4)]  # two tetrahedra sharing face (0,1,2)
    T_new = [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]
    return T_new

def test_incidence_nontrivial():
    T = [(0,1,2,3),(0,1,2,4)]
    e = (0,1)
    assert inc(T,e) > 0

def test_theta_changes_under_move():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert theta(T2) != theta(T)

def test_delta_inc_behavior():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    e1 = (0,1)
    e2 = (0,2)
    e3 = (3,4)  # new interior interaction edge in construction

    assert inc(T,e1) != inc(T2,e1) or inc(T,e2) != inc(T2,e2) or inc(T,e3) != inc(T2,e3)
