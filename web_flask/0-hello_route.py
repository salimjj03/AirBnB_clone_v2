#!/usr/bin/python3
""" This script Start my App."""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ The module that does the work. """

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
