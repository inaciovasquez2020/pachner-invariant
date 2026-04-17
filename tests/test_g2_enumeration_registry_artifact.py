from pathlib import Path
import json

p = Path("docs/data/g2_enumeration_stub.json")
data = json.loads(p.read_text())

def test_status_conditional():
    assert data["status"] == "conditional"

def test_tested_n():
    assert data["tested_n"] == [4, 5, 6, 7]

def test_schema_keys_present():
    assert "cycles_found" in data
    assert "generated_by_candidate_G2" in data
    assert "note" in data
