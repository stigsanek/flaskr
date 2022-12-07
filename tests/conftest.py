import os
import tempfile

import pytest
from werkzeug.security import generate_password_hash

from flaskr import create_app
from flaskr.db import db
from flaskr.config import TestingConfig
from flaskr.models import User, Post


@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test

    :return:
    """
    # create the app with common test config
    app = create_app(TestingConfig())

    # create the database and load test data
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.add(
            User("test", generate_password_hash("test"))
        )
        db.session.add(
            Post(author_id=1, title="test title", body="test body")
        )
        db.session.commit()

    yield app


@pytest.fixture
def client(app):
    """
    A test client for the app

    :param app: app instance
    :return: test client
    """
    return app.test_client()


class AuthActions:
    """
    Actions class for user auth
    """

    def __init__(self, client):
        """
        Initialization

        :param client: test client
        """
        self._client = client

    def login(self, username: str = "test", password: str = "test"):
        """
        Login action

        :param username: username
        :param password: password
        :return: response
        """
        return self._client.post(
            "/auth/login",
            data={"username": username, "password": password}
        )

    def logout(self):
        """
        Logout action

        :return:
        """
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    """
    Actions for user auth

    :param client: test client
    :return: AuthActions instance
    """
    return AuthActions(client)
