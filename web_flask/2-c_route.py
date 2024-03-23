#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
