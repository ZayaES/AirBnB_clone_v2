#!/usr/bin/python3
"""A flask web application. Still don't know what I'm doing"""

from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


# @app.route('/airbnb-onepage/')
@app.route('/')
def hello():
    """ returns hello on query of /"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
