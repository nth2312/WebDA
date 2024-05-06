from flask import Flask
from flask import render_template, url_for, make_response, request, session, redirect, flash
from database import Database
from utility import *

app = Flask(__name__)
app.secret_key = 'DHCNHN'
db = Database()

def IsValidLogin(username, password):
    userInfor = db.GetData("tbl_user")
    for user in userInfor:
        if (username == user[0] and password == user[1]):
            return True

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
            try:
                remember = request.form['remember-account']
            except:
                remember = "off"
            if request.form['remember-account'] == "on":
                    index = make_response(redirect(url_for('MainPage')))
                    index.set_cookie('username', request.form['username'])
                    return index
            else:
                index = make_response(redirect(url_for('MainPage')))
                index.set_cookie('username', request.form['username'], max_age=10)
                return index
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/signin', methods = ['POST', 'GET'])
def SignIn():
    if request.method == 'POST':
        userInfor = [request.form['username'], request.form['password'], request.form['email']]
        if (isValidInput(userInfor[0]) == 0 and isValidInput(userInfor[1]) == 0 and isValidEmail(userInfor[2]) == 1):
            db.InsertUser(request.form['username'], request.form['password'], request.form['email'])
            return redirect(url_for('LoginPage'))
        else:
            if (isValidInput(userInfor[0]) == 1):
                flash('Username must have 5-10 characters', 'error')
            if (isValidInput(userInfor[0]) == 2):
                flash('Username must have at least 1 uppercase letter', 'error')
            if (isValidInput(userInfor[0]) == 3):
                flash('Username must have at least 1 lowercase letter', 'error')
            if (isValidInput(userInfor[0]) == 4):
                flash('Username must have at least 1 character', 'error')
            if (isValidInput(userInfor[1]) == 1):
                flash('Password must have 5-10 characters', 'error')
            if (isValidInput(userInfor[1]) == 2):
                flash('Password must have at least 1 uppercase letter', 'error')
            if (isValidInput(userInfor[1]) == 3):
                flash('Password must have at least 1 lowercase letter', 'error')
            if (isValidInput(userInfor[1]) == 4):
                flash('Password must have at least 1 character', 'error')
            if (isValidEmail(userInfor[2]) == 0):
                flash('Invalid email', 'error')
            return render_template('signin.html')

app.run(debug=True, host="0.0.0.0")