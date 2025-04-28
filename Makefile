# makefile
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
STORAGES_FILE = docker_compose/storages.yaml
APP_CONTAINER = main-app


.PHONY: local-app
local-app:
	@uvicorn --factory src.main:create_app --reload --host 0.0.0.0 --port 8000
