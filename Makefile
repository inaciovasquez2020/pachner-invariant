.PHONY: verify test

verify:
	lake build
	python3 -m pytest -q

test:
	python3 -m pytest -q
