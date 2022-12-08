# Flaskr

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/stigsanek/flaskr/python-ci)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/stigsanek/flaskr)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/stigsanek/flaskr)

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

### Dependencies

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
>> poetry install
```

Finally, we can move on to using the project functionality!

## Usage

### Run

```bash
>> flask --app flaskr:create_app run

 * Serving Flask app 'flaskr:create_app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## Development

### Useful commands

* `make install` - install all dependencies in the environment.
* `make build` - build the wheel.
* `make lint` - checking code with linter.
* `make test` - run tests.
* `make run` - run app in debug mode.
