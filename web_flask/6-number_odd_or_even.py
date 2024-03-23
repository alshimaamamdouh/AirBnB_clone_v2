#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """" hello hbnb """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def disp_HBNB():
    """" hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def disp_c(text):
    """" c text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ python """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        flag = ""
        if (n % 2):
            flag = "odd"
        else:
            flag = "even"

        return render_template('6-number_odd_or_even.html', n=n, flag=flag)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
