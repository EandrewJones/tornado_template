## Setup the venv
.PHONY: venv
venv:
	python3 -m venv venv
## Prepare your dependencies
.PHONY: preinstall
preinstall:
	python3 -m pip install --upgrade pip
	python3 -m pip install pip-tools
	pip-compile --output-file requirements.txt requirements.in
	pip-compile --output-file requirements_dev.txt requirements_dev.in

## Install your produuction dependencies
.PHONY: install-prod
install-prod:
	python3 -m pip install -r requirements.txt

## Instal your development dependencies
.PHONY: install-dev
install-dev:
	python3 -m pip install -r requirements_dev.txt

## Setup precommmit
.PHONY: precommmit-setup
precommit-setup:
	pre-commit install

## Run all pre-commit hooks
.PHONY: precommit
precommit:
	pre-commit run --all-file --show-diff-on-failure

## Run tests using pytest
.PHONY: tests
test:
	python3 -m pytest --version
	python3 -m pytest tests

## Run ci part
.PHONY: ci
ci: precommit tests
## Check docker-compose.yaml
.PHONY: docker-inspect
docker-inspect:
	docker compose config
## Build docker image
.PHONY: docker-setup
docker-setup:
	docker compose build --no-cache
## Launch docker container
.PHONY: docker-launch
docker-launch:
	docker compose up --detach --remove-orphans
## Teardown docker container
.PHONY: docker-teardown
docker-teardown:
	docker compose down --remove-orphans