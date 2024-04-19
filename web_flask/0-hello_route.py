#!/usr/bin/python3

""" This module demonstrate how to start a flask app"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """ This function runs an app that prints Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
