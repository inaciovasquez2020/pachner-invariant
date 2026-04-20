from __future__ import annotations

import json
from pathlib import Path

from pachner_invariant.g2_outbound import replace_identity_rows


def test_f6_outbound_exact_rows_lock() -> None:
    data = replace_identity_rows("F6", 6)
    assert data["base_rank"] == 5
    assert data["d2out_row_count"] == 3
    assert data["extended_rank"] == 8


def test_f7_outbound_exact_rows_lock() -> None:
    data = replace_identity_rows("F7", 7)
    assert data["base_rank"] == 25
    assert data["d2out_row_count"] == 18
    assert data["extended_rank"] == 43


def test_summary_written() -> None:
    p = Path("artifacts/g2_certification/F6_exact_outbound_extension.json")
    if not p.exists():
        replace_identity_rows("F6", 6)
    s = json.loads(p.read_text())
    assert s["status"] == "PASS"
