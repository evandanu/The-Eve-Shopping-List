import os

from flask import Flask, render_template,url_for,redirect,request,session

app= Flask(__name__, static_folder='design/UI')
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    # reset the session data
    session.clear()
    session["foo"] = "Foo"
    return render_template("index.html")
 
@app.route('/<path:path>')
def static_folder(path):
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
 
if __name__ == '__main__':
	app.run(debug=True)