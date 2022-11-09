import sqlite3

import pytest

from flaskr.db import get_db


def test_get_close_db(app):
    """
    Test closing database after request

    :param app: app instance
    :return:
    """
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as err:
        db.execute("SELECT 1")

    assert "closed" in str(err.value)


def test_init_db_command(runner, monkeypatch):
    """
    Test initialized the database command

    :param runner: test runner for cli commands
    :param monkeypatch: monkeypatch fixture
    :return:
    """

    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("flaskr.db.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])

    assert "initialized" in result.output.lower()
    assert Recorder.called
