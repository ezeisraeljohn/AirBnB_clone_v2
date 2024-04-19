#!/usr/bin/python3

""" Module that starts a flask application """


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome_hbnb():
    """ Function that returns HBNB"""
    return "Hello HBHB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that returns HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
