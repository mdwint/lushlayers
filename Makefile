install:
	poetry install

lint:
	poetry run flake8
	poetry run black --check --diff .
	poetry run isort --check-only .

format:
	poetry run isort .
	poetry run black .

test:
	poetry run mypy lushlayers/ tests/
	poetry run coverage run -m pytest --failed-first -vv
	poetry run coverage report
	poetry run coverage html

examples/%.json: examples/%.py
	poetry run lushlayers $<

SRCS=$(filter-out examples/shared.py, $(wildcard examples/*.py))
examples: $(SRCS:.py=.json)
