from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/body-composition")
def body_composition():
    return render_template("body_composition.html")
