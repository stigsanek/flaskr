# flaskr

[![Github Actions Status](https://github.com/stigsanek/flaskr/workflows/python-ci/badge.svg)](https://github.com/stigsanek/flaskr/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0c82d66f6924f4b8b033/maintainability)](https://codeclimate.com/github/stigsanek/flaskr/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0c82d66f6924f4b8b033/test_coverage)](https://codeclimate.com/github/stigsanek/flaskr/test_coverage)

## Description

A basic blogging application. Users can register, log in, create posts, edit and delete their posts. You will be able to
package and install the application on other computers.

## Install

### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```

If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).

### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you
to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more
about this tool on [the official Poetry website](https://python-poetry.org/)

### Package

To work with the package, you need to clone the repository to your computer. This is done using the `git clone` command.
Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/stigsanek/flaskr.git
# clone via SSH:
>> git@github.com:stigsanek/flaskr.git
```

It remains to move to the directory and install the package:

```bash
>> cd python-project-51
>> poetry build
>> python -m pip install --user dist/*.whl
```

Finally, we can move on to using the project functionality!

## Usage

### Run

```bash
>> flaskr

 * Serving Flask app 'flaskr'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

### Help

```bash
>> flaskr -h

usage: flaskr [-h] [--host HOST] [--port PORT] [--debug] [--no-debug]

A basic blogging application.

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  the hostname to listen on
  --port PORT  the port of the webserver
  --debug      enable debug mode
  --no-debug   disable debug mode
```

## Development

### Useful commands

* `make install` - install all dependencies in the environment.
* `make build` - build the wheel.
* `make lint` - checking code with linter.
* `make test` - run tests.
* `make run` - run app in debug mode.
