#!/usr/bin/env python3
"""
This module contains a Flask application with Babel for internationalization.
It includes a locale selector to determine the best language match.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index route serves the home page with a simple welcome message.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
