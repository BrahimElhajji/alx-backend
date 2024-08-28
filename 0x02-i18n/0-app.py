#!/usr/bin/env python3
"""
This module contains a basic Flask application with Babel for localization.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class to set Babel's available languages,
    default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    The index route serves the home page with a simple welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
