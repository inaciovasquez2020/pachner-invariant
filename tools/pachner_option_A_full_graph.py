# Option A: Unbounded (conceptual full graph — not computable in practice)

from itertools import combinations
from collections import defaultdict, deque

class Triangulation:
    def __init__(self, n):
        self.n = n
        self.tets = tuple(combinations(range(n), 4))

    def sig(self):
        return self.tets


def neighbors_A(state):
    # FULL conceptual Pachner graph (unbounded generation placeholder)
    # WARNING: infinite branching in reality
    n = state.n
    for i in range(len(state.tets)):
        t = list(state.tets)
        new = list(t[i])
        new[-1] = (new[-1] + 1) % n
        t[i] = tuple(sorted(new))
        yield Triangulation(n)


def build_A(n, depth=2):
    G = defaultdict(set)
    seed = Triangulation(n)
    q = deque([(seed, 0)])
    seen = set()

    while q:
        s, d = q.popleft()
        if d > depth:
            continue
        sig = s.sig()
        if sig in seen:
            continue
        seen.add(sig)

        for nb in neighbors_A(s):
            G[sig].add(nb.sig())
            G[nb.sig()].add(sig)
            q.append((nb, d + 1))

    return G
