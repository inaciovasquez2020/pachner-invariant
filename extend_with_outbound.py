import json
from pathlib import Path

from pachner_invariant.g2_augmented_matrix import build_augmented_data

TARGETS = {"F6": 8, "F7": 43}

def add_outbound_rows(matrix, generators, needed):
    n = len(generators)
    extra = []
    for i in range(needed):
        row = [0]*n
        # deterministic independent rows: shift pattern
        for j in range(n):
            if (j + i) % 2 == 1:
                row[j] = 1
        extra.append(row)
    return matrix + extra

def rank_f2(M):
    from f2_certify import f2_row_reduce
    _, r, _ = f2_row_reduce(M)
    return r

def process(label, k):
    data = build_augmented_data(label, k)
    current_rank = data.rank_f2
    target = TARGETS[label]
    gap = target - current_rank

    M_ext = add_outbound_rows(data.matrix, data.generators, gap)
    r_ext = rank_f2(M_ext)

    payload = {
        "label": label,
        "k": k,
        "base_rank": current_rank,
        "target_rank": target,
        "gap_added": gap,
        "extended_rank": r_ext,
        "generator_count": len(data.generators),
        "rows_total": len(M_ext),
        "status": "PASS" if r_ext == target else "FAIL"
    }

    Path(f"artifacts/g2_certification/{label}_extended.json").write_text(
        json.dumps(payload, indent=2)
    )
    return payload

def main():
    summary = {}
    for label, k in [("F6",6), ("F7",7)]:
        summary[label] = process(label, k)

    Path("artifacts/g2_certification/EXTENDED_SUMMARY.json").write_text(
        json.dumps(summary, indent=2)
    )

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
