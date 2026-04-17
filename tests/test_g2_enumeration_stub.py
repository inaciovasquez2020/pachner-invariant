from pathlib import Path
import json
import subprocess
import sys

def test_stub_runs():
    subprocess.check_call([sys.executable, "tools/g2_enumeration_stub.py"])
    p = Path("docs/data/g2_enumeration_stub.json")
    assert p.exists()

def test_stub_schema():
    p = Path("docs/data/g2_enumeration_stub.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["tested_n"] == [4,5,6,7]
