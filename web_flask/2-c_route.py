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


@app.route('/c/<text>', strict_slashes=False)
def custom(text):
    text_str = str(text)

    if '_' in text_str:
        text_str = text_str.replace('_', ' ')
    return f"C {text_str}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
