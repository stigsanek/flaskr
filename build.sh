#!/usr/bin/env bash
# exit on error
set -o errexit

pip install poetry -U

# install dependencies
poetry install --only main
poetry add gunicorn
