import sqlite3

import click
from flask import Flask, current_app, g


def get_db():
    """
    Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called again.

    :return: g.db
    """
    if "db" not in g:
        g.db = sqlite3.connect(
            database=current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(err=None):
    """
    If this request connected to the database, close the connection

    :param err: error object
    :return:
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """
    Clear existing data and create new tables

    :return:
    """
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))


@click.command("init-db")
def init_db_command():
    """
    CLI command for init db

    :return:
    """
    init_db()
    click.echo("Initialized the database.")


def init_app(app: Flask):
    """
    Register database functions with the Flask app.
    This is called by the application factory.

    :param app: app instance
    :return:
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
