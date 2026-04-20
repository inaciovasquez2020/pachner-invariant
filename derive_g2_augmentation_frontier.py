import json
from pathlib import Path

TARGETS = {"F6": 8, "F7": 43}

def load_json(path: str):
    return json.loads(Path(path).read_text())

def main() -> None:
    f6 = load_json("artifacts/g2_certification/F6_matrix.json")
    f7 = load_json("artifacts/g2_certification/F7_matrix.json")

    records = {}
    for label, rec in [("F6", f6), ("F7", f7)]:
        observed_rank = int(rec["rank_F2"])
        n_cols = int(rec["matrix_cols"])
        target_rank = int(TARGETS[label])
        required_extra_rows = target_rank - observed_rank
        required_kernel_dim = n_cols - target_rank

        records[label] = {
            "label": label,
            "observed_rank": observed_rank,
            "target_rank": target_rank,
            "matrix_cols": n_cols,
            "required_extra_independent_rows": required_extra_rows,
            "required_kernel_dim": required_kernel_dim,
            "admissible": required_extra_rows >= 0,
            "kernel_dim_nonnegative": required_kernel_dim >= 0,
            "status": "OPEN",
            "missing_object": "Exact repository-native dependent Pachner relation family",
        }

    Path("artifacts/g2_certification/AUGMENTATION_GAP.json").write_text(
        json.dumps(records, indent=2, sort_keys=True) + "\n"
    )

    md = f"""# G2 Missing Constraint Family Frontier

## Status
OPEN

## Current matrix data

For the current bounded \(G_2\) matrices:

- \(\\operatorname{{rank}}_{{\\mathbb F_2}}(M_{{F6}}) = {records["F6"]["observed_rank"]}\), \(\\operatorname{{target}}(F6) = {records["F6"]["target_rank"]}\), \(n_{{F6}} = {records["F6"]["matrix_cols"]}\).
- \(\\operatorname{{rank}}_{{\\mathbb F_2}}(M_{{F7}}) = {records["F7"]["observed_rank"]}\), \(\\operatorname{{target}}(F7) = {records["F7"]["target_rank"]}\), \(n_{{F7}} = {records["F7"]["matrix_cols"]}\).

## Missing family

Define a repository-native family of additional constraint rows
\\[
\\mathcal{{R}}_G = \\{{\\rho_1,\\dots,\\rho_t\\}}
\\]
such that the augmented matrix
\\[
\\widetilde{{M}}_G =
\\begin{{bmatrix}}
M_G \\\\
\\mathcal{{R}}_G
\\end{{bmatrix}}
\\]
satisfies
\\[
\\operatorname{{rank}}_{{\\mathbb F_2}}(\\widetilde{{M}}_{{F6}})=8,
\\qquad
\\operatorname{{rank}}_{{\\mathbb F_2}}(\\widetilde{{M}}_{{F7}})=43.
\\]

## Required augmentation counts from current data

- F6 requires exactly
  \\[
  {records["F6"]["required_extra_independent_rows"]}
  \\]
  additional independent rows beyond the current matrix.

- F7 requires exactly
  \\[
  {records["F7"]["required_extra_independent_rows"]}
  \\]
  additional independent rows beyond the current matrix.

## Kernel compatibility condition

For any admissible augmented matrix:
\\[
\\dim \\ker(\\widetilde{{M}}_G) = n_G - r(G).
\\]

From the current column counts:

- F6 would require
  \\[
  {records["F6"]["required_kernel_dim"]}
  \\]
  kernel dimension.

- F7 would require
  \\[
  {records["F7"]["required_kernel_dim"]}
  \\]
  kernel dimension.

## Obstruction

If \(n_G < r(G)\), then no augmentation using the current generator set can reach target rank.

Therefore the missing object is not merely extra rows; it is the exact repository-native relation-and-generator model whose column set is large enough for the target ranks.

## Finish condition

Replace OPEN only after all of the following are produced:

1. An explicit repository-native definition of the missing relation family \\(\\mathcal{{R}}_G\\).
2. An augmented matrix constructor for each bounded \(G\\).
3. Deterministic \\(\\mathbb F_2\\) elimination on \\(\\widetilde{{M}}_G\\).
4. Verified equalities
   \\[
   \\operatorname{{rank}}_{{\\mathbb F_2}}(\\widetilde{{M}}_{{F6}})=8,
   \\qquad
   \\operatorname{{rank}}_{{\\mathbb F_2}}(\\widetilde{{M}}_{{F7}})=43.
   \\]
"""
    Path("docs/math/G2_MISSING_CONSTRAINT_FAMILY_FRONTIER.md").write_text(md)

    test_text = r'''from pathlib import Path
import json

def test_g2_missing_constraint_family_frontier_lock() -> None:
    s = Path("docs/math/G2_MISSING_CONSTRAINT_FAMILY_FRONTIER.md").read_text()
    assert "## Status" in s
    assert "OPEN" in s
    assert "Exact repository-native dependent Pachner relation family" in Path("artifacts/g2_certification/AUGMENTATION_GAP.json").read_text()
    assert "rank_{\\mathbb F_2}(\\widetilde{M}_{F6})=8" in s
    assert "rank_{\\mathbb F_2}(\\widetilde{M}_{F7})=43" in s

def test_g2_augmentation_gap_json_lock() -> None:
    data = json.loads(Path("artifacts/g2_certification/AUGMENTATION_GAP.json").read_text())
    assert data["F6"]["observed_rank"] == 3
    assert data["F6"]["target_rank"] == 8
    assert data["F6"]["required_extra_independent_rows"] == 5
    assert data["F7"]["observed_rank"] == 7
    assert data["F7"]["target_rank"] == 43
    assert data["F7"]["required_extra_independent_rows"] == 36
'''
    Path("tests/test_g2_missing_constraint_family_frontier_lock.py").write_text(test_text)

    print("Wrote artifacts/g2_certification/AUGMENTATION_GAP.json")
    print("Wrote docs/math/G2_MISSING_CONSTRAINT_FAMILY_FRONTIER.md")
    print("Wrote tests/test_g2_missing_constraint_family_frontier_lock.py")

if __name__ == "__main__":
    main()
