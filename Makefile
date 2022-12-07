run:
	flask --app flaskr:create_app run

install:
	poetry install

lint:
	poetry run flake8 flaskr tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=flaskr --cov-report xml
