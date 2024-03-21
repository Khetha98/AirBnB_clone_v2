#!/usr/bin/python3
"""It a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Print the Web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print the Web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Print char C followed by value of a text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Print Python, followed by value of a text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
