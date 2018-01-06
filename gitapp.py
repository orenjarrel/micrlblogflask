import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, this is a GIT Simple Flask site!"
