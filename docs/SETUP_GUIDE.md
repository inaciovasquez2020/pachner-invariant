# Setup Guide

This guide is for contributors who want a reliable local environment for PachnerInvariant.

## Prerequisites

```bash
python3 --version
git --version
lake --version
lean --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- Lean 4 with `lake`
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/pachner-invariant.git
cd pachner-invariant
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Lean build

```bash
lake build
```

## Python tests

```bash
python3 -m pytest -q
```

## Combined first pass

```bash
lake build && python3 -m pytest -q
```

## Recommended edit loop

```bash
git pull --ff-only origin main
lake build
python3 -m pytest -q
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `docs/CURRENT_FRONTIER_2026_04.md`
- `NEXT_SINGLE_STEP.md`
