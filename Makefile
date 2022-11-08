init-db:
	flask --app flaskr init-db

run:
	flask --app flaskr --debug run

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 flaskr tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=flaskr --cov-report xml
