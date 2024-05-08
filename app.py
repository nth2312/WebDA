from flask import Flask
from flask import render_template, url_for, make_response, request, session, redirect, flash
from database import Database


app = Flask(__name__)
app.secret_key = 'DHCNHN'
db = Database()

def IsValidLogin(username, password):
    userInfor = db.GetData("tbl_user")
    for user in userInfor:
        if (username == user[0] and password == user[1]):
            return True

def LogUser(username):
    index = make_response(redirect(url_for('MainPage')))
    index.set_cookie('username', username)
    return index

@app.route('/')
def MainPage():
    cookie = request.cookies.get('username')
    if cookie is not None:
        return render_template('main.html')
    else:
        return redirect(url_for('LoginPage'))

@app.route('/login')
def LoginPage():
    return render_template('login.html')

@app.route('/signin')
def SignInPage():
    return render_template('signin.html')

@app.route('/login', methods = ['POST', 'GET'])
def Login():
    if request.method == 'POST':
        if IsValidLogin(request.form['username'], request.form['password']):
            return LogUser(request.form['username'])
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/signin', methods = ['POST', 'GET'])
def SignIn():
    error = None
    if request.method == 'POST':
        userInfor = [request.form['username'], request.form['password'], request.form['email']]
        print(userInfor)
        db.InsertUser(request.form['username'], request.form['password'], request.form['email'])
        return redirect(url_for('LoginPage'))

app.run(debug=True, host="0.0.0.0")