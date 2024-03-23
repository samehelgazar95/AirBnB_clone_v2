#!/usr/bin/python3
"""
Initiate Flask
- Create route to /
- Create route to hbnb /hbnb
- Create route to /c/<text>
- Create route to /python/<text>
- Create route to /number/<n>
- Create route to /number_template/<n>
"""
from flask import Flask, render_template


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
