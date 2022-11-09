import pytest

from flaskr.db import get_db


def test_index(client, auth):
    """
    Test for index page

    :param client: test client
    :param auth: AuthActions instance
    :return:
    """
    resp = client.get("/")
    assert "Log In" in resp.text
    assert "Register" in resp.text

    auth.login()
    resp = client.get("/")
    assert "test title" in resp.text
    assert "test body" in resp.text
    assert "by test on 2022-11-09" in resp.text
    assert 'href="/create"' in resp.text
    assert 'href="/1/update"' in resp.text


@pytest.mark.parametrize(
    argnames="path",
    argvalues=("/create", "/1/update", "/1/delete")
)
def test_login_required(client, path):
    """
    Test login required for change blog

    :param client: test client
    :param path: url path
    :return:
    """
    resp = client.post(path)
    assert resp.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    """
    Test author required for change post

    :param app: app instance
    :param client: test client
    :param auth: AuthActions instance
    :return:
    """
    with app.app_context():
        db = get_db()
        db.execute("UPDATE post SET author_id = 2 WHERE id = 1")
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post("/1/update").status_code == 403
    assert client.post("/1/delete").status_code == 403

    # current user doesn't see edit link
    resp = client.get("/")
    assert 'href="/1/update"' not in resp.text


def test_create(app, client, auth):
    """
    Test for create post

    :param app: app instance
    :param client: test client
    :param auth: AuthActions instance
    :return:
    """
    auth.login()
    client.post("/create", data={"title": "test", "body": "test"})

    with app.app_context():
        db = get_db()
        count = db.execute("SELECT COUNT(id) FROM post").fetchone()[0]
        assert count == 2


def test_update(app, client, auth):
    """
    Test for update post

    :param app: app instance
    :param client: test client
    :param auth: AuthActions instance
    :return:
    """
    auth.login()
    client.post("/1/update", data={"title": "title", "body": "body"})

    with app.app_context():
        db = get_db()
        post = db.execute("SELECT * FROM post WHERE id = 1").fetchone()
        assert post["title"] == "title"
        assert post["body"] == "body"


@pytest.mark.parametrize(
    argnames="path",
    argvalues=("/create", "/1/update")
)
def test_create_update_validate_input(client, auth, path: str):
    """
    Test for validation form on create and update post

    :param client: test client
    :param auth: AuthActions instance
    :param path: url path
    :return:
    """
    auth.login()
    resp = client.post(path, data={"title": "", "body": "body"})
    assert "Title is required." in resp.text


def test_delete(app, client, auth):
    """
    Test for delete post

    :param app: app instance
    :param client: test client
    :param auth: AuthActions instance
    :return:
    """
    auth.login()
    resp = client.post("/1/delete")
    assert resp.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute("SELECT * FROM post WHERE id = 1").fetchone()
        assert post is None
