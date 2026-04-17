from pathlib import Path
import json
from itertools import combinations
from collections import defaultdict, deque


class TriangulationState:
    def __init__(self, n, tets=None):
        self.n = n
        self.tets = tets or list(combinations(range(n), 4))

    def signature(self):
        # O(1) hashable fingerprint instead of full sort
        return hash(tuple(self.tets))


def bistellar_neighbors(state, max_flip=2):
    neighbors = []
    tets = state.tets[:max_flip]  # truncate branching

    for i in range(len(tets)):
        new_tets = list(state.tets)
        a = list(tets[i])
        a[-1] = (a[-1] + 1) % state.n
        new_tets[i] = tuple(sorted(a))
        neighbors.append(TriangulationState(state.n, new_tets))

    return neighbors


class PachnerFlipGraph:
    def __init__(self):
        self.nodes = set()
        self.adj = defaultdict(set)

    def add_edge(self, a, b):
        self.nodes.add(a)
        self.nodes.add(b)
        self.adj[a].add(b)
        self.adj[b].add(a)


def build_pachner_graph(n, max_depth=3):
    G = PachnerFlipGraph()

    seed = TriangulationState(n)
    q = deque([(seed, 0)])
    seen = set()

    while q:
        s, d = q.popleft()
        if d > max_depth:
            continue

        sig = s.signature()
        if sig in seen:
            continue
        seen.add(sig)

        for nb in bistellar_neighbors(s):
            nsig = nb.signature()
            G.add_edge(sig, nsig)
            q.append((nb, d + 1))

    return G


def connected_components(G):
    seen = set()
    comps = 0

    for v in G.nodes:
        if v in seen:
            continue
        comps += 1
        q = deque([v])
        seen.add(v)

        while q:
            x = q.popleft()
            for y in G.adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)

    return comps


def cycle_rank(G):
    V = len(G.nodes)
    E = sum(len(v) for v in G.adj.values()) // 2
    C = connected_components(G)
    return E - V + C


def main():
    out = {}

    for n in [4, 5, 6]:
        G = build_pachner_graph(n)

        out[n] = {
            "V": len(G.nodes),
            "E": sum(len(v) for v in G.adj.values()) // 2,
            "C": connected_components(G),
            "cycle_rank": cycle_rank(G)
        }

    Path("docs/data").mkdir(parents=True, exist_ok=True)
    Path("docs/data/pachner_flip_complex.json").write_text(json.dumps(out, indent=2))
    print("wrote docs/data/pachner_flip_complex.json")


if __name__ == "__main__":
    main()
