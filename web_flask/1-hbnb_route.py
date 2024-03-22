#!/usr/bin/python3
from flask import Flask
"""
Initiate Flask
- Create route to hbnb /hbnb
"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Creating the home route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Creating the hbnb route """
    return "HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
