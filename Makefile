run:
	flask --app flaskr:create_app run

run-debug:
	flask --app flaskr:create_app  --debug run

install:
	poetry install

lint:
	poetry run flake8 flaskr tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=flaskr --cov-report xml
