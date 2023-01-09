# Flaskr

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/stigsanek/flaskr/pyci.yml?branch=main)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/stigsanek/flaskr)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/stigsanek/flaskr)

## Description

A basic blogging application. Users can register, log in, create posts, edit and delete their posts. You will be able to
package and install the application on other computers.

## Usage

You can deploy the project locally or via Docker.

### 1. Locally

#### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```

If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).

#### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you
to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more
about this tool on [the official Poetry website](https://python-poetry.org/)

#### Dependencies

To work with the package, you need to clone the repository to your computer. This is done using the `git clone` command.
Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/stigsanek/flaskr.git
# clone via SSH:
>> git@github.com:stigsanek/flaskr.git
```

It remains to move to the directory and install the dependencies:

```bash
>> cd flaskr
>> poetry install --no-root
```

#### Environment

For the application to work, you need to create a file `.env` in the root of the project:

```
FLASK_SECRET_KEY=your_key
FLASK_DATABASE_URL=sqlite:///flaskr.sqlite

# If you want to enable debug mode
FLASK_DEBUG=True
```

#### Run

```bash
>> flask --app flaskr:create_app run

 * Serving Flask app 'flaskr:create_app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

### 2. Docker

Docker is a platform designed to help developers build, share, and run modern applications.
You can read more about this tool on [the official Docker website](https://www.docker.com/).
You need to [install Docker Desktop](https://www.docker.com/products/docker-desktop/).
Docker Desktop is an application for the building and sharing of containerized applications and microservices.

#### Environment

Depending on the application mode, different environment files are used.
For development mode, the `.env.dev` file with basic settings has already been created.
For production mode, you need to create an `.env.prod` file:

```
# Database environment
POSTGRES_DB=flaskr
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# App environment
FLASK_DEBUG=False
FLASK_SECRET_KEY=prod
FLASK_DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```

#### Run development mode

```bash
>> docker-compose -f compose.dev.yml up -d --build

...
...
...
Creating flaskr_db_1  ... done
Creating flaskr_web_1 ... done
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

#### Run production mode

```bash
>> docker-compose -f compose.prod.yml up -d --build

...
...
...
Creating flaskr_db_1  ... done
Creating flaskr_web_1 ... done
```

Open [http://localhost:5000](http://localhost:5000) in your browser.
