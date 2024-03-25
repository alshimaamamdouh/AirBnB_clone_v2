#!/usr/bin/python3
""" script starts a Flask web application """

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


def teardown_db(exception):
    storage.close()


@app.teardown_appcontext
def teardown_context(exception):
    teardown_db(exception)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
