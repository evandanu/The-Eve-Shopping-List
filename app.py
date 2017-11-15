import os

from flask import Flask, flash, render_template, url_for, redirect, request, session, send_from_directory
from .models.item import Item
from .models.shoppinglist import Shoppinglist
from .models.user import User
from functools import wraps 


app= Flask(__name__)
app._static_folder = 'design/UI'
app.secret_key = os.urandom(24)
app.debug = True

app.users = {}
app.usernames = []
app.shoppinglist = {}
id = 0

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('you need to login first.')
            return redirect(url_for('login'))
    return wrap

def get_id_for_username(username):
    print (username)
    for user in app.users:
        if app.users[user].username == username:
            return app.users[user].id

def add_shoppinglist():

    return

def delete_shoppinglist():
    return

def edit_shoppinglist():
    return

def add_item():
    return

def delete_item():
    return

def edit_item():
    return
            
        

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route('/<path:path>')
def _static_folder(path):
	return app.send_static_file(path)

@app.route('/favicon.ico')
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='images/bag2.jpg')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in app.usernames:
            error = 'You do not have an account, please register!'
        else:
            user_id = get_id_for_username(username)
            print (user_id)
            print (app.users)
            if app.users[user_id].password != password:
                error = 'Wrong password, please try again!'
            else:
                session['logged_in']=True
                session['username']= username
                session['id']=user_id
                flash ('You are logged in.')
                return redirect(url_for('view'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        fullname = request.form['fullname'].lower()
        username = request.form['username'].lower()
        email = request.form['email'].lower()
        phonenumber = request.form['phonenumber'].lower()
        address = request.form['address'].lower()
        password = request.form['password'].lower()
        password1 = request.form['password1'].lower()

        if username not in app.usernames:
            
            if password == password1:
                global id
                id += 1
                new_user = User(id, fullname, username, email, phonenumber, address, password)
                app.users[new_user.id] = new_user
                app.usernames.append(username)
                session['logged_in'] = True
                session['username'] = username
                session['id'] = new_user.id
                flash ('You are now registered and logged in.')
                return redirect(url_for('view'))
            else:
                error = 'Passwords do not match'
        else:
            error = 'Username already exists'

    return render_template('register.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session['logged_in'] = False
    flash ('You are logged out.')
    return redirect(url_for('index'))
   

@app.route('/view', methods=['GET', 'POST'])
@login_required
def view():
    return render_template('view.html')

@app.route('/addshoppinglist', methods=['GET', 'POST'])
@login_required
def addshoppinglist():
    return render_template('addshoppinglist.html')
 
if __name__ == '__main__':
	app.run()