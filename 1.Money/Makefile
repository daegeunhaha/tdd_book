.PHONY: pylint
pylint:
	pylint src

.PHONY: isort
isort:
	isort src

.PHONY: black
black:
	black src

.PHONY: pyright
pyright:
	pyright src

.PHONY: code
code: isort black

.PHONY: check
check: pylint pyright
