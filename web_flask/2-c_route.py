#!/usr/bin/python3
""" This script Start my App."""

from flask import Flask


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
    txt = ""
    if "_" in text:
        for i in range(len(text)):
            if text[i] == "_":
                txt = txt+" "
            else:
                txt = txt+text[i]
    else:
        txt = text
    return "c {}".format(txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
