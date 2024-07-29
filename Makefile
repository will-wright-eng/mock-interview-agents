include .env

.PHONY: $(shell sed -n -e '/^$$/ { n ; /^[^ .\#][^ ]*:/ { s/:.*$$// ; p ; } ; }' $(MAKEFILE_LIST))

.DEFAULT_GOAL := help

help: ## list make commands
	@echo ${MAKEFILE_LIST}
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

#* Docker
up: ## start prod docker-compose yml files
	sudo docker compose -f docker-compose.prod.yml up --build --remove-orphans

upd: ## start prod docker-compose yml files
	sudo docker compose -f docker-compose.prod.yml up --build --remove-orphans -d

run: ## start site locally, uses override yml
	docker compose -f docker-compose.yml up --build --remove-orphans

local: cleanup run ## run locally

open: ## open http://0.0.0.0
	open ${BASE_URL}
	open ${BASE_URL}:${BACKEND_PORT}/api/docs

docker-kill: ## kill all docker containers
	for id in $$(docker ps --format "{{.ID}}"); do docker kill $$id; done

#* Cleaning
pycache-remove: ## cleanup subcommand - pycache-remove
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

dsstore-remove: ## cleanup subcommand - dsstore-remove
	find . | grep -E ".DS_Store" | xargs rm -rf

mypycache-remove: ## cleanup subcommand - mypycache-remove
	find . | grep -E ".mypy_cache" | xargs rm -rf

ipynbcheckpoints-remove: ## cleanup subcommand - ipynbcheckpoints-remove
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

pytestcache-remove: ## cleanup subcommand - pytestcache-remove
	find . | grep -E ".pytest_cache" | xargs rm -rf

rms: ## remove generated files/dirs
	rm -rf frontend/node_modules/
	rm -rf frontend/.next/
	rm frontend/package-lock.json

# cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove rms
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove