#!/usr/bin/python3
""" This module import storage. """


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ This Method return all states. """
    state = storage.all("State")

    return render_template("7-states_list.html", state=state)


@app.teardown_appcontext
def teardown_app(exc):
    """ This method teardown the app context. """

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
