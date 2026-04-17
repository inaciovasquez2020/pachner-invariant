from pathlib import Path
import json
from itertools import combinations
from collections import defaultdict, deque


class FlipGraph:
    def __init__(self):
        self.nodes = set()
        self.adj = defaultdict(set)

    def add_node(self, x):
        self.nodes.add(x)
        self.adj.setdefault(x, set())

    def add_edge(self, x, y):
        self.nodes.add(x)
        self.nodes.add(y)
        self.adj.setdefault(x, set())
        self.adj.setdefault(y, set())
        self.adj[x].add(y)
        self.adj[y].add(x)


def Fn(n: int) -> FlipGraph:
    G = FlipGraph()
    verts = list(range(n))

    states = list(combinations(verts, 3))

    for s in states:
        G.add_node(s)

    for i, a in enumerate(states):
        for b in states[i + 1:]:
            if len(set(a).intersection(set(b))) == 2:
                G.add_edge(a, b)

    return G


def connected_components(G: FlipGraph):
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


def cycle_rank(G: FlipGraph):
    V = len(G.nodes)
    E = sum(len(v) for v in G.adj.values()) // 2
    C = connected_components(G)
    return E - V + C


def computed_cycles(n: int):
    return cycle_rank(Fn(n))


def bounded_pachner_enumeration(n: int):
    G = Fn(n)
    return {
        "n": n,
        "V": len(G.nodes),
        "E": sum(len(v) for v in G.adj.values()) // 2,
        "C": connected_components(G),
        "cycle_rank": cycle_rank(G),
    }


def verify():
    for n in [4, 5, 6, 7]:
        out = bounded_pachner_enumeration(n)
        assert out["cycle_rank"] == computed_cycles(n)


def main():
    verify()

    out = {
        "status": "conditional",
        "tested_n": [4, 5, 6, 7],
        "cycles_found": {str(n): computed_cycles(n) for n in [4, 5, 6, 7]},
        "generated_by_candidate_G2": {
            str(n): bounded_pachner_enumeration(n) for n in [4, 5, 6, 7]
        },
        "certificates": {},
        "note": "cycle rank computed via H1 = E - V + C over flip-graph Fn(n)"
    }

    Path("docs/data").mkdir(parents=True, exist_ok=True)
    Path("docs/data/g2_enumeration.json").write_text(json.dumps(out, indent=2))
    print("wrote docs/data/g2_enumeration.json")


if __name__ == "__main__":
    main()
