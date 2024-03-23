#!/usr/bin/python3
"""
Initiate Flask
- Declare the tearing down concept
- Create route to /
- Create route to hbnb /hbnb
- Create route to /c/<text>
- Create route to /python/<text>
- Create route to /number/<n>
- Create route to /number_template/<n>
- Create route to /number_odd_or_even/<n>
- Create route to /states_list
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tearing_down(exception=None):
    """ Removing current session after each req """
    if exception:
        print("An exception occured: {}".format(exception))
    storage.close()


@app.route('/', strict_slashes=False)
def home():
    """ route to home """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ route to hbnb route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_url(text):
    """ route to /c/<text> """
    text_val = text.replace('_', ' ')
    return "C {}".format(text_val)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_url(text):
    """ route to /python/<text> """
    text_val = text.replace('_', ' ')
    return "Python {}".format(text_val)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ route to /number/<n> """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ route to /number_template/<n> """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """ route to /number_odd_or_even/<n> """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_cities():
    """ route to /states_list """
    states_obj = storage.all(State)
    return render_template('7-states_list.html', states=states_obj)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
