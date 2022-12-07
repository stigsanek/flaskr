import pytest
from flask import g, session
from flaskr.db import db
from flaskr.models import User


def test_register(app, client):
    """
    Test for register user

    :param app: app instance
    :param client: test client
    :return:
    """
    # test that viewing the page renders without template errors
    assert client.get("/auth/register").status_code == 200

    # test that successful registration redirects to the login page
    resp = client.post(
        "/auth/register",
        data={"username": "a", "password": "a"}
    )
    assert resp.headers["Location"] == "/auth/login"

    # test that the user was inserted into the database
    with app.app_context():
        user = db.session.query(User).filter(User.username == "a").first()
        assert user is not None


@pytest.mark.parametrize(
    argnames="username, password, msg",
    argvalues=(
        ("", "", "Username is required."),
        ("a", "", "Password is required."),
        ("test", "test", " is already registered.")
    )
)
def test_register_validate_input(
    client,
    username: str,
    password: str,
    msg: str
):
    """
    Test for validation form on register user

    :param client: test client
    :param username: username
    :param password: password
    :param msg: err message
    :return:
    """
    resp = client.post(
        "/auth/register",
        data={"username": username, "password": password}
    )
    assert msg in resp.text


def test_login(client, auth):
    """
    Test for login user

    :param client: test client
    :param auth: AuthActions instance
    :return:
    """
    # test that viewing the page renders without template errors
    assert client.get("/auth/login").status_code == 200

    resp = auth.login()
    assert resp.headers["Location"] == "/"

    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user.username == "test"


@pytest.mark.parametrize(
    argnames="username, password, msg",
    argvalues=(
        ("a", "test", "Incorrect username."),
        ("test", "a", "Incorrect password.")
    )
)
def test_login_validate_input(
    auth,
    username: str,
    password: str,
    msg: str
):
    """
    Test for validation form on login user

    :param auth: AuthActions instance
    :param username: username
    :param password: password
    :param msg: err message
    :return:
    """
    resp = auth.login(username, password)
    assert msg in resp.text


def test_logout(client, auth):
    """
    Test for logout user

    :param client: test client
    :param auth: AuthActions instance
    :return:
    """
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session
