import os

from flask import Flask, render_template,url_for,redirect,request

from app import app

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/<path:path>')
def styles_paths(path):
	return app.send_static_file(path)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template('view.html')

@app.route('/addshopinglist', methods=['GET', 'POST'])
def addshopinglist():
    return render_template('addshopinglist.html')
 