from __future__ import annotations

import json
from pathlib import Path

from pachner_invariant.gk_pachner_boundary import lift_bounded_g2_to_gk


def main() -> None:
    summary = lift_bounded_g2_to_gk(max_k=9)
    Path("artifacts/g2_certification/TRUE_P23_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
