command-list:
	@echo "command-list:"
	@echo " make build             - docker-compose build"
	@echo " make build-up          - docker-compose up -d --build"
	@echo " make nbuild            - docker-compose build --no-cache"
	@echo " make python            - docker-compose exec python bash"
	@echo " make python-www-data   - docker-compose exec --user=www-data python bash"
	@echo " make up                - docker-compose up -d"
	@echo " make down              - docker-compose down"
	@echo " make vdown             - docker-compose down -v"


# Docker commands
build:
	docker-compose build

build-up:
	docker-compose up -d --build

nbuild:
	docker-compose build --no-cache

python:
	docker-compose exec python bash

python-www-data:
	docker-compose exec --user=www-data python  bash

up:
	docker-compose up -d

down:
	docker-compose down

vdown:
	docker-compose down -v