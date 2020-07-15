SHELL := /bin/bash

.PHONY := test

format:
	black .

lint:
	black . --check

test:
	@echo "Running all tests..." 
	@echo "If you want to test a specific directory, run: pytest <directory>"
	pytest
