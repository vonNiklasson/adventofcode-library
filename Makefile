PYTHON ?= python3
SOURCE_FOLDER = adventofcode

# Maintaining targets

.PHONY: clean
clean:
	rm -f .gitinfo
	rm -rf build dist *.egg-info
	find $(SOURCE_FOLDER) -name __pycache__ | xargs rm -rf
	find $(SOURCE_FOLDER) -name '*.pyc' -delete
	rm -rf reports .coverage
	rm -rf docs/build docs/source
	rm -rf .*cache

.PHONY: check
check: check-imports check-code

.PHONY: check-imports
check-imports:
	isort --check-only $(SOURCE_FOLDER)

.PHONY: check-code
check-code:
	black --check $(SOURCE_FOLDER) tests/*

.PHONY: reformat
reformat:
	isort --atomic $(SOURCE_FOLDER) tests/*
	black $(SOURCE_FOLDER)

.PHONY: update
update:
	pip install --upgrade -r requirements-dev.txt

.PHONY: build
build:
	$(PYTHON) setup.py --quiet sdist bdist_wheel

.PHONY: version
version:
	$(PYTHON) -c "import $(SOURCE_FOLDER); print($(SOURCE_FOLDER).__version__)"

.PHONY: tests
tests:
	$(PYTHON) -m pytest tests/

# Versioning targets

.PHONY: bump-version-patch
bump-version-patch:
	bump2version patch --list
	git log --oneline -1


.PHONY: bump-version-minor
bump-version-minor:
	bump2version minor --list
	git log --oneline -1

.PHONY: bump-version-major
bump-version-major:
	bump2version major --list
	git log --oneline -1
