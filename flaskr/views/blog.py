from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import db
from flaskr.models import Post
from flaskr.views.auth import login_required

bp = Blueprint(name="blog", import_name=__name__)


@bp.route("/")
def index():
    """
    Show all the posts, most recent first

    :return: response
    """
    posts = db.session.query(Post).all()
    return render_template("blog/index.html", posts=posts)


def get_post(post_id: int, check_author: bool = True) -> Post:
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
    post = db.session.query(Post).filter(Post.post_id == post_id).first()

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist.")
    if check_author and post.author_id != g.user.user_id:
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
            db.session.add(Post(
                author_id=g.user.user_id, title=title, body=body
            ))
            db.session.commit()
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
            post = get_post(post_id)
            post.title = title
            post.body = body

            db.session.commit()
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
    post = get_post(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("blog.index"))
