# PachnerInvariant Quickstart

This is the shortest path from clone to a first successful local verification pass.

## Requirements

- `git`
- `bash`
- `python3`
- Lean 4 with `lake`

## 1. Clone

```bash
git clone https://github.com/inaciovasquez2020/pachner-invariant.git
cd pachner-invariant
```

## 2. Check tools

```bash
python3 --version
git --version
lake --version
lean --version
```

## 3. Build Lean targets

```bash
lake build
```

## 4. Run tests

```bash
python3 -m pytest -q
```

## 5. Review current frontier

- `docs/CURRENT_FRONTIER_2026_04.md`
- `NEXT_SINGLE_STEP.md`

## 6. Next steps

- detailed setup: `docs/SETUP_GUIDE.md`
- contribution policy: `CONTRIBUTING.md`
