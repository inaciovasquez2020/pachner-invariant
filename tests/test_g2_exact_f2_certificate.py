from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_exact_f2_certificate.py"])

def test_schema():
    p = Path("docs/data/g2_exact_f2_certificate.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["field"] == "F2"

def test_targets():
    p = Path("docs/data/g2_exact_f2_certificate.json")
    data = json.loads(p.read_text())
    assert data["targets"]["F6"]["cycle_rank"] == 8
    assert data["targets"]["F7"]["cycle_rank"] == 43

def test_wall():
    p = Path("docs/data/g2_exact_f2_certificate.json")
    data = json.loads(p.read_text())
    assert "generator incidence matrices" in data["single_remaining_wall"]
