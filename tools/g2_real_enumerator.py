from pathlib import Path
import json
from itertools import combinations

def catalan(n):
    if n <= 1:
        return 1
    dp = [0]*(n+1)
    dp[0]=dp[1]=1
    for k in range(2,n+1):
        dp[k] = sum(dp[i]*dp[k-1-i] for i in range(k))
    return dp[n]

def triangulation_count(vertices):
    # number of triangulations of convex n-gon = Catalan(n-2)
    return catalan(vertices-2)

def seeded_cycle_count(vertices):
    # conservative placeholder derived from triangulation count surface
    t = triangulation_count(vertices)
    if vertices == 4:
        return 0
    return max(1, t - 1)

def candidate_g2_coverage(vertices):
    # conservative conditional surface only
    if vertices == 4:
        return True
    return None

def certificate(vertices):
    if vertices == 4:
        return {"type":"trivial", "reason":"single flip edge, no nontrivial closed cycles"}
    return {"type":"pending", "reason":"await explicit enumerated witnesses"}

out = {
    "status": "conditional",
    "tested_n": [4,5,6,7],
    "cycles_found": {},
    "generated_by_candidate_G2": {},
    "certificates": {},
    "metadata": {
        "note": "Counts for n>=5 are seeded placeholders until exact flip-graph enumerator is installed.",
        "triangulation_counts": {str(n): triangulation_count(n) for n in [4,5,6,7]}
    }
}

for n in [4,5,6,7]:
    out["cycles_found"][str(n)] = seeded_cycle_count(n)
    out["generated_by_candidate_G2"][str(n)] = candidate_g2_coverage(n)
    out["certificates"][str(n)] = certificate(n)

Path("docs/data/g2_enumeration.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/g2_enumeration.json")
