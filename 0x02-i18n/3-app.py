#!/usr/bin/env python3
"""
Parametrize templates
"""
import flask_babel
from flask import Flask, request, render_template

app = Flask(__name__)
babel = flask_babel.Babel(app)


class Config:
    """
    Babel configs
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Configure supported languages
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """
    Renders index.html
    """
    home_title = flask_babel.gettext("home_title")
    home_header = flask_babel.gettext("home_heade")
    return render_template(
        "3-index.html", home_title=home_title, home_header=home_header
    )


if __name__ == "__main__":
    app.run()
