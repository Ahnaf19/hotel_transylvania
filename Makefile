ENV_NAME = hotel3.10
.PHONY: help env install run test

ifeq ($(OS), Windows_NT)

help:
	@echo "Available targets:"
	@echo "  help    - Display all targets and their descriptions"
	@echo "  env     - Create a virtual environment if it doesn't exist"
	@echo "  install - Install dependencies from requirements.txt"
	@echo "  run     - Run the FastAPI application"
	@echo "  test    - Run tests using pytest"

env:
	@if not exist "$(ENV_NAME)" ( \
		echo Creating virtual environment... && \
		python -m venv $(ENV_NAME) \
	) else ( \
		echo Virtual environment: $(ENV_NAME) already exists \
	)
	@echo To activate run: .\$(ENV_NAME)\Scripts\activate

install: env requirements.txt
	.\$(ENV_NAME)\Scripts\pip install -r requirements.txt

run: env install
	.\$(ENV_NAME)\Scripts\uvicorn app.main:app --reload

test: env install requirements_test.txt
	.\$(ENV_NAME)\Scripts\pip install -r requirements_test.txt
	.\$(ENV_NAME)\Scripts\pytest tests/

else

help:
	@echo "Available targets:"
	@echo "  help    - Display all targets and their descriptions"
	@echo "  env     - Create a virtual environment if it doesn't exist"
	@echo "  install - Install dependencies from requirements.txt"
	@echo "  run     - Run the FastAPI application"
	@echo "  test    - Run tests using pytest"

env:
	@if [ ! -d "$(ENV_NAME)" ]; then \
		echo "Creating virtual environment..."; \
        sudo apt install -y python3.10-venv; \
		python3.10 -m venv $(ENV_NAME); \
	else \
		echo "Virtual environment: $(ENV_NAME) already exists"; \
	fi
	@echo "To activate run: source $(ENV_NAME)/bin/activate"

install: requirements.txt
	$(ENV_NAME)/bin/pip install -r requirements.txt

run: env install
	$(ENV_NAME)/bin/uvicorn app.main:app --reload

test: env install requirements_test.txt
	$(ENV_NAME)/bin/pip install -r requirements_test.txt
	$(ENV_NAME)/bin/pytest tests/
endif