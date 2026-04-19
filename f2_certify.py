"""
F2 Generator-Matrix Certification for Bounded Pachner G2 Layer
==============================================================
Implements:
  1. F_2 Gaussian elimination with exact rank
  2. Pachner 2-3 move graph G_2^{<=k} construction
  3. Incidence matrix M_G builder (edge/face relations x generators)
  4. Enumeration up to isomorphism via canonical hash
  5. Rank certification: rank(M_G) == r(G)  [targets: F6->8, F7->43]
  6. SHA-256 hash freeze of each (M_G, rank) pair

Usage:
  python3 f2_certify.py
"""

import hashlib
import itertools
from collections import defaultdict
from typing import List, Tuple, Dict, Optional
import numpy as np


# ─────────────────────────────────────────────
#  F_2 Linear Algebra
# ─────────────────────────────────────────────

def f2_row_reduce(M: List[List[int]]) -> Tuple[List[List[int]], int, List[int]]:
    """
    Gaussian elimination over F_2 on a copy of M.
    Returns (row-reduced matrix R, rank, pivot_columns).
    All arithmetic is mod 2.
    """
    if not M or not M[0]:
        return M, 0, []
    rows = [row[:] for row in M]          # deep copy
    m, n = len(rows), len(rows[0])
    pivot_row = 0
    pivot_cols = []

    for col in range(n):
        found = None
        for r in range(pivot_row, m):
            if rows[r][col] == 1:
                found = r
                break
        if found is None:
            continue
        rows[pivot_row], rows[found] = rows[found], rows[pivot_row]
        pivot_cols.append(col)
        for r in range(m):
            if r != pivot_row and rows[r][col] == 1:
                rows[r] = [(rows[r][c] ^ rows[pivot_row][c]) for c in range(n)]
        pivot_row += 1

    rank = pivot_row
    return rows, rank, pivot_cols


def f2_rank(M: List[List[int]]) -> int:
    _, r, _ = f2_row_reduce(M)
    return r


def f2_basis_rows(M: List[List[int]]) -> List[List[int]]:
    R, rank, _ = f2_row_reduce(M)
    return [R[i] for i in range(rank)]


def matrix_hash(M: List[List[int]]) -> str:
    R, rank, _ = f2_row_reduce(M)
    basis = [R[i] for i in range(rank)]
    basis.sort()
    blob = str(rank).encode() + b"|" + str(basis).encode()
    return hashlib.sha256(blob).hexdigest()


# ─────────────────────────────────────────────
#  Triangulation / Pachner Move Structures
# ─────────────────────────────────────────────

Triangle = Tuple[int, int, int]
Triangulation = frozenset


def edges_of(tri: Triangle) -> List[Tuple[int, int]]:
    a, b, c = sorted(tri)
    return [(a, b), (a, c), (b, c)]


def build_edge_map(T: Triangulation) -> Dict[Tuple[int, int], List[Triangle]]:
    em: Dict[Tuple[int, int], List[Triangle]] = defaultdict(list)
    for tri in T:
        for e in edges_of(tri):
            em[e].append(tri)
    return em


def pachner_23_moves(T: Triangulation) -> List[Triangulation]:
    em = build_edge_map(T)
    results = []
    max_v = max(v for tri in T for v in tri) if T else -1

    for (a, b), tris in em.items():
        if len(tris) != 2:
            continue
        t1, t2 = tris
        all_v = set(t1) | set(t2)
        opp = all_v - {a, b}
        if len(opp) != 2:
            continue
        c, d = sorted(opp)
        new_v = max_v + 1
        new_T = (T - {t1, t2}) | {
            tuple(sorted((a, b, new_v))),
            tuple(sorted((a, c, new_v))),
            tuple(sorted((b, d, new_v))),
        }
        results.append(frozenset(new_T))

    return results


# ─────────────────────────────────────────────
#  Canonical Form / Isomorphism
# ─────────────────────────────────────────────

def canonical_form(T: Triangulation) -> Tuple:
    vertices = sorted(set(v for tri in T for v in tri))
    n = len(vertices)
    best = None
    for perm in itertools.permutations(range(n)):
        relabel = {vertices[i]: perm[i] for i in range(n)}
        new_T = tuple(sorted(tuple(sorted(relabel[v] for v in tri)) for tri in T))
        if best is None or new_T < best:
            best = new_T
    return best


def triangulation_hash(T: Triangulation) -> str:
    cf = canonical_form(T)
    return hashlib.sha256(str(cf).encode()).hexdigest()[:16]


# ─────────────────────────────────────────────
#  G_2^{<=k} Graph Enumeration
# ─────────────────────────────────────────────

def enumerate_g2_layer(seeds: List[Triangulation], k: int) -> Dict[str, Triangulation]:
    seen: Dict[str, Triangulation] = {}
    queue = []

    for s in seeds:
        h = triangulation_hash(s)
        if h not in seen and len(s) <= k:
            seen[h] = s
            queue.append(s)

    while queue:
        T = queue.pop(0)
        for T2 in pachner_23_moves(T):
            if len(T2) > k:
                continue
            h = triangulation_hash(T2)
            if h not in seen:
                seen[h] = T2
                queue.append(T2)

    return seen


# ─────────────────────────────────────────────
#  Incidence Matrix M_G Construction
# ─────────────────────────────────────────────

def build_incidence_matrix(G_vertices: List[str],
                           G_edges: List[Tuple[str, str]]) -> List[List[int]]:
    n = len(G_vertices)
    m = len(G_edges)
    if m == 0:
        return [[0] * m for _ in range(n)]
    vidx = {v: i for i, v in enumerate(G_vertices)}
    M = [[0] * m for _ in range(n)]
    for j, (u, v) in enumerate(G_edges):
        M[vidx[u]][j] = 1
        M[vidx[v]][j] = 1
    return M


def build_g2_graph(config_map: Dict[str, Triangulation]
                   ) -> Tuple[List[str], List[Tuple[str, str]]]:
    hashes = list(config_map.keys())
    hash_set = set(hashes)
    edges = []
    seen_edges = set()

    for h, T in config_map.items():
        for T2 in pachner_23_moves(T):
            h2 = triangulation_hash(T2)
            if h2 in hash_set:
                e = tuple(sorted((h, h2)))
                if e not in seen_edges:
                    seen_edges.add(e)
                    edges.append(e)

    return hashes, edges


# ─────────────────────────────────────────────
#  Full Certification Pipeline
# ─────────────────────────────────────────────

TARGET_RANKS = {"F6": 8, "F7": 43}


def certify(label: str, config_map: Dict[str, Triangulation]) -> Dict:
    vertices, edges = build_g2_graph(config_map)
    M = build_incidence_matrix(vertices, edges)

    rank = f2_rank(M)
    target = TARGET_RANKS.get(label)
    h = matrix_hash(M)

    n_cols = len(edges)
    cycle_dim = n_cols - rank

    certified = (rank == target) if target is not None else None

    return {
        "label": label,
        "n_configs": len(vertices),
        "n_moves": len(edges),
        "matrix_shape": (len(M), n_cols),
        "rank_F2": rank,
        "target_rank": target,
        "certified": certified,
        "cycle_space_dim": cycle_dim,
        "matrix_hash_sha256": h,
    }


# ─────────────────────────────────────────────
#  Seed Triangulations
# ─────────────────────────────────────────────

def minimal_torus_triangulation() -> Triangulation:
    tris = [
        (0,1,2),(0,2,3),(0,3,4),(0,4,5),(0,5,6),(0,6,1),
        (1,2,4),(2,3,6),(3,4,1),(4,5,2),(5,6,3),(6,1,5),
        (1,4,6),(2,4,6),
    ]
    return frozenset(tuple(sorted(t)) for t in tris)


def tetrahedron_surface() -> Triangulation:
    return frozenset([
        (0,1,2),(0,1,3),(0,2,3),(1,2,3)
    ])


def octahedron_surface() -> Triangulation:
    return frozenset([
        (0,1,2),(0,2,3),(0,3,4),(0,4,1),
        (5,1,2),(5,2,3),(5,3,4),(5,4,1),
    ])


# ─────────────────────────────────────────────
#  F_2 Rank Certification Demo
# ─────────────────────────────────────────────

def demo_f2_algebra():
    print("=" * 60)
    print("F_2 LINEAR ALGEBRA CERTIFICATION DEMO")
    print("=" * 60)

    M1 = [
        [1,0,1,0],
        [0,1,1,0],
        [1,1,0,0],
        [0,0,0,1],
    ]
    r1 = f2_rank(M1)
    print(f"\nTest matrix (4x4), expected rank 3: got {r1}  {'PASS' if r1==3 else 'FAIL'}")

    M2 = [[0,0,0],[0,0,0]]
    r2 = f2_rank(M2)
    print(f"Zero matrix (2x3), expected rank 0: got {r2}  {'PASS' if r2==0 else 'FAIL'}")

    M3 = [[1,0,0],[0,1,0],[0,0,1]]
    r3 = f2_rank(M3)
    print(f"Identity (3x3), expected rank 3: got {r3}  {'PASS' if r3==3 else 'FAIL'}")

    M4 = [
        [1,0,0],
        [1,1,0],
        [0,1,1],
        [0,0,1],
    ]
    r4 = f2_rank(M4)
    print(f"Path P4 incidence (4x3), expected rank 3: got {r4}  {'PASS' if r4==3 else 'FAIL'}")

    M5 = [
        [1,0,0,1],
        [1,1,0,0],
        [0,1,1,0],
        [0,0,1,1],
    ]
    r5 = f2_rank(M5)
    print(f"Cycle C4 incidence (4x4), expected rank 3: got {r5}  {'PASS' if r5==3 else 'FAIL'}")
    print(f"  cycle_dim = {4 - r5}  (expected 1)")


def demo_small_pachner_graph():
    print("\n" + "=" * 60)
    print("SMALL PACHNER GRAPH CERTIFICATION (octahedron seed, k=10)")
    print("=" * 60)

    seed = octahedron_surface()
    print(f"Seed: octahedron boundary ({len(seed)} triangles)")

    configs = enumerate_g2_layer([seed], k=10)
    print(f"Enumerated {len(configs)} non-isomorphic configurations (k<=10)")

    vertices, edges = build_g2_graph(configs)
    M = build_incidence_matrix(vertices, edges)
    rank = f2_rank(M)
    h = matrix_hash(M)

    print(f"Graph: |V|={len(vertices)}, |E|={len(edges)}")
    print(f"Matrix shape: {len(M)} x {len(edges) if edges else 0}")
    print(f"rank_F2(M) = {rank}")
    print(f"dim Z_1    = {len(edges) - rank}")
    print(f"matrix_hash (sha256[:16]) = {h[:16]}")


def certify_targets():
    print("\n" + "=" * 60)
    print("TARGET CERTIFICATION: F6 (rank=8), F7 (rank=43)")
    print("=" * 60)

    results = []
    for label, k, seed_fn in [
        ("F6", 6, octahedron_surface),
        ("F7", 7, octahedron_surface),
    ]:
        seed = seed_fn()
        configs = enumerate_g2_layer([seed], k=k)
        rec = certify(label, configs)
        results.append(rec)

        status = "✓ CERTIFIED" if rec["certified"] else (
            "✗ MISMATCH" if rec["certified"] is False else "? (no target)"
        )
        print(f"\n{label} ({status})")
        print(f"  configs (non-iso)  : {rec['n_configs']}")
        print(f"  moves (edges)      : {rec['n_moves']}")
        print(f"  matrix shape       : {rec['matrix_shape']}")
        print(f"  rank_F2(M_G)       : {rec['rank_F2']}")
        print(f"  target rank r(G)   : {rec['target_rank']}")
        print(f"  dim Z_1            : {rec['cycle_space_dim']}")
        print(f"  matrix hash        : {rec['matrix_hash_sha256'][:32]}")

    return results


def print_generator_matrix(label: str, k: int, seed_fn):
    seed = seed_fn()
    configs = enumerate_g2_layer([seed], k=k)
    vertices, edges = build_g2_graph(configs)
    M = build_incidence_matrix(vertices, edges)
    B = f2_basis_rows(M)
    rank = len(B)

    print(f"\n{'='*60}")
    print(f"GENERATOR MATRIX B_{label}  (shape: {rank} x {len(edges) if edges else 0})")
    print(f"rowspan(B) = rowspan(M),  rank = {rank}")
    print(f"{'='*60}")
    for i, row in enumerate(B):
        bits = "".join(str(b) for b in row)
        print(f"  row {i:2d}: {bits}")


if __name__ == "__main__":
    demo_f2_algebra()
    demo_small_pachner_graph()
    results = certify_targets()
    print_generator_matrix("F6", 6, octahedron_surface)
    print_generator_matrix("F7", 7, octahedron_surface)

    print("\n" + "=" * 60)
    print("CERTIFICATION SUMMARY")
    print("=" * 60)
    all_pass = all(r["certified"] for r in results if r["certified"] is not None)
    for r in results:
        status = "PASS" if r["certified"] else ("FAIL" if r["certified"] is False else "SKIP")
        print(f"  {r['label']}: rank={r['rank_F2']} target={r['target_rank']}  [{status}]")
        print(f"        hash: {r['matrix_hash_sha256']}")

    print()
    if all_pass:
        print("  ∀ G ∈ G_2^{≤k}: rank_F2(M_G) = r(G)  ← CLOSED")
    else:
        print("  Rank mismatch detected — counterexample found or seed/enumeration")
        print("  requires correction. Check Enum_k and BuildExact conditions.")
