import os

from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__, static_folder='design/UI')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>')
def styles_paths(path):
    return app.send_static_file(path)