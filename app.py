from flask import Flask
from flask import render_template, url_for, make_response, request

app = Flask(__name__)

def IsValidLogin(username, password):
    if (username == "admin" and password == "admin"):
        return True
    return False

def LogUser(username):
    index = make_response(render_template('main.html'))
    index.set_cookie('username', username)
    return index

@app.route('/')
def MainPage():
    cookie = request.cookies.get('username')
    if cookie is not None:
        return render_template('main.html')
    else:
        return render_template('login.html')

@app.route('/login')
def LoginPage():
    return render_template('login.html')

@app.route('/login', methods = ['POST', 'GET'])
def Login():
    error = None
    if request.method == 'POST':
        if IsValidLogin(request.form['username'], request.form['password']):
            return LogUser(request.form['username'])
        else:
            error = "Invalid username or password"
    return render_template('login.html')

app.run(debug=True, host="0.0.0.0")