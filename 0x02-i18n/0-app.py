#!/usr/bin/env python3
"""
This module contains a basic Flask application with a single route.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    The index route serves the home page with a simple welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
