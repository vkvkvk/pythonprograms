import os
from flask import flask

app =Flask(_name_)
@app.route('/')
def hello():
    return 'Hello World!'


