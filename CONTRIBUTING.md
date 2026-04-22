# Contributing to PachnerInvariant

## Contribution classes

### 1. Documentation improvements

- clarify repository status
- improve onboarding text
- tighten quickstart commands
- improve navigation across frontier files

### 2. Test and verifier hardening

- add regression tests
- improve artifact-surface checks
- tighten verifier-facing documentation

### 3. Formalization refactors without semantic change

- improve readability
- reduce duplication
- reorganize non-semantic proof structure
- add comments and local clarifications

### 4. Semantic or frontier changes

These require explicit justification.

- changing the invariant definition
- changing exact rank targets
- weakening conditional/final-wall language
- expanding theorem-level claim scope

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run checks before commit:

```bash
lake build
python3 -m pytest -q
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- weakening frontier/status language
- expanding proved-scope language without synchronized status updates
