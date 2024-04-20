#!/usr/bin/python3

""" Module that starts a flask application """


from flask import Flask, render_template


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
def C_is_fun(text):
    """ Function that returns custom text"""
    text_str = str(text)

    if '_' in text_str:
        text_str = text_str.replace('_', ' ')
    return f"C {text_str}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """ Function that returns a custom text """
    text = str(text)

    if '_' in text:
        text = text.replace('_', ' ')

    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Prints out the value of n followed by 'is a number' """

    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Prints out the value of the rendered page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_odd_even(n):
    """ Printes out the value of the renderd page"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
