#!/usr/bin/python3
"""
Working with Flask
displays a defualt if nothing is provided
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def to_hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def to_nextpage(text):
    """returns HBNB"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def to_python_text(text='is cool'):
    """returns Python is cool if nothing is passed
        else return python followed by the world that was passed
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def to_isNum(n):
    """returns HBNB"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def to_num_tem(n):
    """Render's a static file"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def to_odd_even(n):
    """Render's a static file"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
