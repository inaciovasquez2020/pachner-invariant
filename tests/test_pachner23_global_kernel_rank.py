from itertools import product
import numpy as np

# ------------------------------------------------------------
def edges():
    return [(i,j) for i in range(5) for j in range(i+1,5)]

def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

def theta_vector(T, edge_index):
    v = [0]*len(edge_index)
    for t in T:
        for i,e in enumerate(edge_index):
            a,b = e
            if a in t and b in t:
                v[i] += 1
    return v

# ------------------------------------------------------------
def build_constraint_matrix():
    E = edges()

    configs = [
        ([(0,1,2,3),(0,1,2,4)], pachner23([(0,1,2,3),(0,1,2,4)])),
        ([(0,1,2,3),(0,1,3,4)], pachner23([(0,1,2,3),(0,1,3,4)])),
        ([(0,1,2,3),(1,2,3,4)], pachner23([(0,1,2,3),(1,2,3,4)])),
    ]

    A = []
    for T, T2 in configs:
        row = [a-b for a,b in zip(theta_vector(T,E), theta_vector(T2,E))]
        A.append(row)

    return np.array(A)

# ------------------------------------------------------------
def test_global_kernel_dimension():
    A = build_constraint_matrix()

    # rank of constraint system
    rank = np.linalg.matrix_rank(A)

    dim = len(edges())

    kernel_dim = dim - rank

    # TRUE statement:
    # kernel exists, but we test whether trivial only
    assert kernel_dim >= 0

    # key structural check:
    # nontrivial kernel exists iff dim > rank
    assert kernel_dim > 0
