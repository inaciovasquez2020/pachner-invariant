from __future__ import annotations

import json
from pathlib import Path

from pachner_invariant.g2_outbound import replace_identity_rows


OUTDIR = Path("artifacts/g2_certification")
LEVELS = {"F6": 6, "F7": 7}


def main() -> None:
    summary = {}
    for label, k in LEVELS.items():
        summary[label] = replace_identity_rows(label=label, k=k)
    Path(OUTDIR / "EXACT_OUTBOUND_EXTENSION_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
