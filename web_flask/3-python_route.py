#!/usr/bin/python3
""" This script Start my App."""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ The module that does the work. """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ The module that display HBNB. """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ This used variable to dispay text """

    text = escape(text).replace("_", " ")
    return "c {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ This used variable to dispay text """

    text = escape(text).replace("_", " ")
    return "c {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
