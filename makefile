## Setup the venv
.PHONY: venv
venv:
	python -m venv venv
## Prepare your dependencies
.PHONY: preinstall
preinstall:
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	pip-compile --output-file requirements.txt requirements.in
	pip-compile --output-file requirements_dev.txt requirements_dev.in
## Install your produuction dependencies
.PHONY: install-prod
install-prod:
	python -m pip install -r requirements.txt
## Instal your development dependencies
.PHONY: install-dev
install-dev:
	python -m pip install -r requirements_dev.txt
## Run all pre-commit hooks
.PHONY: precommit
precommit:
	pre-commit run --all-file --show-diff-on-failure
## Lint your code using pylint
.PHONY: lint
lint:
	python -m pylint --version
	find . -type f -name "*.py" | xargs python -m pylint
## Run tests using pytest
.PHONY: tests
test:
	python -m pytest --version
	python -m pytest tests
## Format your code using black
.PHONY: black
black:
	python -m black --version
	python -m black *.py
## Run ci part
.PHONY: ci
ci: precommit tests
