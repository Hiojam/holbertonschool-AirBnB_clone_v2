#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def estado():
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    listtt = storage.all(State)
    return render_template("7-states_list.html", dicc=listtt)


if __name__ == "__main__":
    "Entry point"
    app.run(debug=True, host="0.0.0.0", port=5000)
