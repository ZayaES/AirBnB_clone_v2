#!/usr/bin/python3
"""A flask web application. Still don't know what I'm doing"""

from flask import Flask

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
    return "C" + form_text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
