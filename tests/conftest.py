import os
import tempfile

import pytest
from werkzeug.security import generate_password_hash

from flaskr import create_app
from flaskr.db import db
from flaskr.models import User, Post


@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test

    :return:
    """
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()

    # create the app with common test config
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}"
    })

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

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


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
