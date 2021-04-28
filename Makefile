BUILDKIT_PREFIX=COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1

all: build

docker-compose.override.yml:
	cp -n docker-compose.override.yml.example docker-compose.override.yml

.PHONY: build
build: docker-compose.override.yml
	$(BUILDKIT_PREFIX) docker-compose build

.PHONY: build-prod
build-prod:
	$(BUILDKIT_PREFIX) docker-compose -f docker-compose.yml -f docker-compose.prod.yml build

.PHONY: web
web: docker-compose.override.yml
	$(BUILDKIT_PREFIX) docker-compose build web

.PHONY: up
up:
	docker-compose up

.PHONY: up-prod
up-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

.PHONY: ssh
ssh:
	docker-compose exec web bash

.PHONY: pre-commit
pre-commit:
	pip3 install pre-commit==2.8.2
	pre-commit install --install-hooks

.PHONY: lint
lint:
	pre-commit --version || make pre-commit
	pre-commit run -a

.PHONY: test
test:
	docker-compose run web make migrate testall

.PHONY: reset_db
reset_db:
	docker-compose run web django reset_db

.PHONY: pdb
pdb:
	docker-compose run --service-ports web
