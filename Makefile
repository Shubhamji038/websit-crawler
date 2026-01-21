# Makefile for Python Web Crawler

.PHONY: help install install-dev test run clean lint format build upload

# Default target
help:
	@echo "Python Web Crawler - Available commands:"
	@echo ""
	@echo "  install      Install package"
	@echo "  install-dev  Install package with dev dependencies"
	@echo "  test         Run tests"
	@echo "  run          Run GUI application"
	@echo "  clean        Clean build artifacts"
	@echo "  lint         Run linting"
	@echo "  format       Format code"
	@echo "  build        Build package"
	@echo "  upload       Upload to PyPI"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev,gui]"

# Testing
test:
	python -m pytest tests/ -v

test-coverage:
	python -m pytest tests/ --cov=src --cov-report=html --cov-report=term

# Running
run:
	python src/webcrawler.py

run-cli:
	echo "https://httpbin.org" | python src/python_webcrawler.py -d 2 -s

# Development tools
lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/

format-check:
	black --check src/ tests/

# Building
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

upload: build
	python -m twine upload dist/*

upload-test: build
	python -m twine upload --repository testpypi dist/*

# Examples
run-examples:
	python examples/basic_usage.py
	python examples/gui_usage.py

# Documentation
docs:
	@echo "Documentation available in docs/ directory"

# Development setup
setup-dev: install-dev
	@echo "Development environment setup complete!"
	@echo "Run 'make test' to verify installation"
