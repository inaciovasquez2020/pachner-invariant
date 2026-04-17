from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_promote_f5.py"])

def test_n5_promoted_to_exact():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert data["cycles_found"]["5"] == 1
    assert data["generated_by_candidate_G2"]["5"]["full_coverage_verified"] is True
    assert data["generated_by_candidate_G2"]["5"]["generator_family"] == ["pentagon"]
    assert data["certificates"]["5"]["graph_artifact"] == "docs/data/f5_exact_graph.json"
