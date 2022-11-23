#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install --no-dev
poetry add gunicorn
