#!/usr/bin/python3
"Starts a Web Application"
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    "Display 'Hello, HBNB!'"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    "Display 'HBNB!'"
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    "Display 'c + text'"
    return f"C {text}".replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return f"Python {text}".replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numtemp(n):
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    """Starts a web app"""
    app.run(debug=True, host="0.0.0.0", port=5000)