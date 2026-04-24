from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/PACHNER_SURVIVAL_PROTOCOL.md"

REQUIRED = [
    "Status: Repository-governance protocol",
    "executable Lean-facing artifact for local Pachner-move invariant verification",
    "solved theorem",
    "closed executable surface",
    "certified frontier",
    "conditional result",
    "open obstruction",
    "`pachner-invariant` must not imply that an open theorem is solved",
    "The durable contribution of `pachner-invariant` is the conversion of local Pachner-move and invariant claims into auditable, Lean-facing, status-normalized artifacts.",
    "Do not expand Pachner merely by adding new terminology.",
]

def main() -> None:
    if not DOC.exists():
        raise SystemExit("missing docs/status/PACHNER_SURVIVAL_PROTOCOL.md")
    text = DOC.read_text()
    for needle in REQUIRED:
        if needle not in text:
            raise SystemExit(f"missing required text: {needle}")
    print("pachner survival protocol verified")

if __name__ == "__main__":
    main()
