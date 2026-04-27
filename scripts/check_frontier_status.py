from pathlib import Path

status = Path("docs/FRONTIER_BUILD_STATUS_2026_04_26.md").read_text()
root = Path("PachnerInvariant.lean").read_text()

required = [
    "Status: Frontier theorem layer is not build-integrated and remains non-buildable.",
    "`lake build PachnerInvariant.frontier` fails.",
    "No substantive Pachner theorem is verified by the current frontier layer.",
    "vertexDeg (pachner23 T a b c p q) p",
    "edgeDeg_pachner23_delta",
    "non-tautological count-to-degree bridge",
]

for s in required:
    assert s in status, f"missing status marker: {s}"

assert "import PachnerInvariant.frontier" not in root, (
    "Root imports frontier. Update frontier status/checks before merging."
)

print("FRONTIER_STATUS_CHECK: PASS")
