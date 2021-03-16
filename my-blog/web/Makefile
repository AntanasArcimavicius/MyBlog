all:

.PHONY: run
run:
	uwsgi --ini uwsgi.ini

.PHONY: pdb
pdb:
	docker-compose run --service-ports web

.PHONY: migrate
migrate:
	django migrate
	django dbshell < ddl.sql

.PHONY: test
test:
	pytest

.PHONY: testall
testall:
	pytest

.PHONY: reset_db
reset_db:
	docker-compose run web django reset_db
