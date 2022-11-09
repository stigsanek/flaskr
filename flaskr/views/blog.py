from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db
from flaskr.views.auth import login_required

bp = Blueprint(name="blog", import_name=__name__)


@bp.route("/")
def index():
    """
    Show all the posts, most recent first

    :return: response
    """
    db = get_db()
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username "
        "FROM post p JOIN user u ON p.author_id = u.id ORDER BY created DESC"
    ).fetchall()

    return render_template("blog/index.html", posts=posts)


def get_post(post_id: int, check_author: bool = True) -> dict:
    """
    Get a post and its author by id.
    Checks that the id exists and
    optionally that the current user is the author.

    :param post_id: post id
    :param check_author: (optional) require the current user to be the author
    :return: dict
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    db = get_db()
    post = db.execute(
        "SELECT p.id, title, body, created, author_id, username "
        "FROM post p JOIN user u ON p.author_id = u.id WHERE p.id = ?",
        (post_id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist.")
    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """
    Create a new post for the current user

    :return: response
    """
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        error = None

        if not title:
            error = "Title is required."

        if error is None:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for("blog.index"))

        flash(error)

    return render_template("blog/create.html")


@bp.route("/<int:post_id>/update", methods=("GET", "POST"))
@login_required
def update(post_id: int):
    """
    Update a post if the current user is the author

    :param post_id: post id
    :return: response
    """
    post = get_post(post_id)

    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        error = None

        if not title:
            error = "Title is required."

        if error is None:
            db = get_db()
            db.execute(
                "UPDATE post SET title = ?, body = ? WHERE id = ?",
                (title, body, post_id)
            )
            db.commit()
            return redirect(url_for("blog.index"))

        flash(error)

    return render_template("blog/update.html", post=post)


@bp.post("/<int:post_id>/delete")
@login_required
def delete(post_id: int):
    """
    Delete a post.
    Ensures that the post exists and that the logged in user is the
    author of the post.

    :param post_id:
    :return: response
    """
    get_post(post_id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (post_id,))
    db.commit()

    return redirect(url_for("blog.index"))
