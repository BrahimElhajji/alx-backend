#!/usr/bin/env python3
"""
Flask app with Babel for internationalization and user login emulation.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import re

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class for the Flask app.
    Sets available languages, default locale, and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_user():
    """
    Retrieve a user from the users dictionary based on login_as URL parameter.
    """
    login_as = request.args.get("login_as")
    if not login_as:
        return None
    user = users.get(int(login_as))
    if not user:
        return None
    return user


@app.before_request
def before_request():
    """
    Executed before each request to set the global user.
    """
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    locale_param = request.args.get("locale")
    locale_head = request.headers.get("locale")
    locale_user = None
    if g.get("user"):
        locale_user = g.user.get("locale")
    if locale_param and locale_param in app.config["LANGUAGES"]:
        return locale_param
    elif locale_user and locale_user in app.config["LANGUAGES"]:
        return locale_user
    elif locale_head and locale_head in app.config["LANGUAGES"]:
        return locale_head
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """
    The index route serves the home page.
    Displays a welcome message based on login status.
    """
    user = g.get("user")
    if user:
        return render_template("5-index.html", username=user["name"])
    return render_template("5-index.html", username=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
