import os
import tempfile

import pytest

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

    user = User("test", "pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7"
                        "ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f")
    post = Post(author_id=1, title="test title", body="test body")

    # create the database and load test data
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.add(user)
        db.session.add(post)
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


@pytest.fixture
def runner(app):
    """
    A test runner for the app's Click commands

    :param app: app instance
    :return: test cli runner
    """
    return app.test_cli_runner()


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
