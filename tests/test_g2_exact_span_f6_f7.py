from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"


def test_build_and_rank_scripts_run():
    subprocess.check_call([sys.executable, "tools/g2_build_incidence_matrix_exact.py"])
    subprocess.check_call([sys.executable, "tools/g2_rank_check_f6_f7.py"])


def test_exact_matrix_schema():
    data = json.loads((DATA / "g2_incidence_matrix_exact.json").read_text())
    assert data["status"] == "conditional"
    assert data["field"] == "F2"
    assert data["artifacts"]["F6"]["cycle_rank_target"] == 8
    assert data["artifacts"]["F7"]["cycle_rank_target"] == 43


def test_rank_equalities():
    data = json.loads((DATA / "g2_exact_span_check.json").read_text())
    assert data["F6"]["rank"] == 8
    assert data["F6"]["rank_equality_passed"] is True
    assert data["F7"]["rank"] == 43
    assert data["F7"]["rank_equality_passed"] is True


def test_promotion_only_after_rank_pass():
    data = json.loads((DATA / "g2_enumeration.json").read_text())
    assert data["generated_by_candidate_G2"]["6"]["full_coverage_verified"] is True
    assert data["generated_by_candidate_G2"]["7"]["full_coverage_verified"] is True
    assert data["cycles_found"]["6"]["exact_cycle_rank"] == 8
    assert data["cycles_found"]["7"]["exact_cycle_rank"] == 43
