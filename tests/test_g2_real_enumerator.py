from pathlib import Path
import json
import subprocess
import sys

def test_run():
    subprocess.check_call([sys.executable, "tools/g2_real_enumerator.py"])

def test_schema():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert data["status"] == "conditional"
    assert data["tested_n"] == [4,5,6,7]

def test_keys():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert set(data["cycles_found"]) == {"4","5","6","7"}
    assert set(data["generated_by_candidate_G2"]) == {"4","5","6","7"}
    assert set(data["certificates"]) == {"4","5","6","7"}

def test_n4_locked():
    p = Path("docs/data/g2_enumeration.json")
    data = json.loads(p.read_text())
    assert data["cycles_found"]["4"] == 0
    assert data["generated_by_candidate_G2"]["4"] is True
