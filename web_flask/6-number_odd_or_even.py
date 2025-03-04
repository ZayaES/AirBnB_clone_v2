#!/usr/bin/python3
"""A flask web application. Still don't know what I'm doing"""

from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def display_text(text):
    form_text = text.replace('_', ' ')
    return "C " + form_text


@app.route('/python/')
@app.route('/python/<text>')
def python(text=None):
    if text is None:
        text = "is cool"
    form_text = text.replace('_', ' ')
    return "Python " + form_text


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def n_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_odd(n):
    if n % 2 == 0:
        type_ = 'even'
    else:
        type_ = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, type_=type_)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
