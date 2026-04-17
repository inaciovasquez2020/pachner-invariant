from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_verify_local_generators.py"])

def test_schema():
    p = Path("docs/data/g2_local_generator_evidence.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["claim_level"] == "evidence_only"

def test_family():
    p = Path("docs/data/g2_local_generator_evidence.json")
    data = json.loads(p.read_text())
    assert data["generator_family"] == ["square_commutation", "pentagon"]

def test_f6_counts():
    p = Path("docs/data/g2_local_generator_evidence.json")
    data = json.loads(p.read_text())
    assert data["F6"]["cycle_rank"] == 8
