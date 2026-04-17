from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_f6f7_span_check.py"])

def test_schema():
    p = Path("docs/data/g2_span_check.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["field"] == "F2"

def test_f6():
    p = Path("docs/data/g2_span_check.json")
    data = json.loads(p.read_text())
    assert data["F6"]["cycle_rank"] == 8

def test_f7():
    p = Path("docs/data/g2_span_check.json")
    data = json.loads(p.read_text())
    assert data["F7"]["cycle_rank"] == 43
