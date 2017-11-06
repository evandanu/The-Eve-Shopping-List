import os
from flask import Flask,render_template, session, url_for,request,redirect
from app import app, views

app= Flask(__name__, static_folder='design/UI')

if __name__ == "__main__":
    app.run()