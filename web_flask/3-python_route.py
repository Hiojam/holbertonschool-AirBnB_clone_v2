#!/usr/bin/python3
"Starts a Web Application"
from flask import Flask
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

if __name__ == "__main__":
    """Starts a web app"""
    app.run(debug=True, host="0.0.0.0", port=5000)
