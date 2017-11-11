import os

from flask import Flask, render_template, url_for, redirect, request, session,flash
from models.item.item import Item
from models.shoppinglist.shoppinglist import Shoppinglist
from models.user.user import User 


app= Flask(__name__)
app._static_folder = 'design/UI'
app.secret_key = os.urandom(24)

app.users = {}
app.usernames = []
app.shoppinglist = {}


@app.route("/")
def index():
    # reset the session data
    session.clear()
    session["foo"] = "Foo"
    return render_template("index.html")
 
@app.route('/<path:path>')
def _static_folder(path):
	return app.send_static_file(path)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None 
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in app.usernames:
            error = 'You do not have an account, please register.'
        else:
            user_id = get_id_for_username(username)
            if app.users[user_id].password != password:
                error = 'Wrong password, please try again'
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
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        address = request.form['address']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if username not in app.usernames:
            if password1 == password2:
                new_user = user(fullname, username, email, phonenumber, address, password1)
                app.users[new_user_id] = new_user
                app.usernames.append(usernames)
                session['logged_in'] = True
                session['username'] = username
                session['id'] = user_id
                flash ('You are now registered and logged in.')
                return redirect(url_for('view'))
            else:
                error = 'Passwords do not match'
        else:
            error = 'Username already exists'

    return render_template('register.html', error=error)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    flash ('You are logged out.')
    return redirect(url_for('index'))
   

@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template('view.html')

@app.route('/addshopinglist', methods=['GET', 'POST'])
def addshopinglist():
    return render_template('addshopinglist.html')
 
if __name__ == '__main__':
	app.run(debug=True)