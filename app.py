from flask import Flask
from flask import render_template, url_for, make_response, request, session, redirect, flash, jsonify
from database import Database
from utility import Utility
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'DHCNHN'
db = Database()
utility = Utility()

def IsValidLogin(username, password):
    userInfor = db.GetData("tbl_user")
    adminInfor = db.GetData("tbl_admin")
    for user in userInfor:
        if (username == user[0] and utility.encode(password, username) == user[1]):
            return 1
    for admin in adminInfor:
        if (username == admin[0] and password == admin[1]):
            return 0
    return 2

@app.route('/')
def MainPage():
    cookie = request.cookies.get('username')
    if cookie is not None:
        return render_template('main.html', hotelList=utility.hotelList[:6], placeList=utility.placeList[:6])
    else:
        return redirect(url_for('LoginPage'))

@app.route('/login')
def LoginPage():
    return render_template('login.html')

@app.route('/signin')
def SignInPage():
    return render_template('signin.html')

@app.route('/all/hotel')
def AllPage():
    return render_template('allHotel.html')

@app.route('/all/place')
def AllPlace():
    return render_template('allPlace.html')

@app.route('/pdetail/<place_name>')
def PlaceDetailPage(place_name):
    place = utility.getDetailPlaceInfor(place_name)
    coordinates = utility.getPlacecoordinates(place['place_id'])
    stores = utility.getNearStore(place['place_id'])
    return render_template('detailPlace.html', place=place, stores=stores, coord=coordinates)

@app.route('/hdetail/<hotel_name>')
def HotelDetailPage(hotel_name):
    hotel = utility.getDetailHotelInfor(hotel_name)
    return render_template('detailHotel.html', hotel=hotel)

@app.route('/login', methods = ['POST', 'GET'])
def Login():
    if request.method == 'POST':
        if IsValidLogin(request.form['username'], request.form['password']) == 1:
            try:
                remember = request.form['remember-account']
            except:
                remember = "off"
            if remember == "on":
                    index = make_response(redirect(url_for('MainPage')))
                    index.set_cookie('username', request.form['username'])
                    return index
            else:
                index = make_response(redirect(url_for('MainPage')))
                index.set_cookie('username', request.form['username'], max_age=10)
                return index
        elif IsValidLogin(request.form['username'], request.form['password']) == 0:
            return render_template('adminView.html')
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
def Logout():
    res = make_response(redirect(url_for('Login')))
    res.delete_cookie('username')
    return res

@app.route('/signin', methods = ['POST', 'GET'])
def SignIn():
    if request.method == 'POST':
        userInfor = [request.form['username'], request.form['password'], request.form['email']]
        username = userInfor[0]
        password = userInfor[1]
        if (utility.checkValidUsername(userInfor[0]) == 0 and utility.isValidPassword(userInfor[1]) == 0 and utility.isValidEmail(userInfor[2]) == 1):
            db.InsertUser(username, utility.encode(password, username), request.form['email'])
            return redirect(url_for('LoginPage'))
        else:
            if (utility.checkValidUsername(userInfor[0]) == 5):
                flash('This username is already exist', 'error')
            if (utility.checkValidUsername(userInfor[0]) == 1):
                flash('Username must have 5-10 characters', 'error')
            if (utility.checkValidUsername(userInfor[0]) == 2):
                flash('Username must have at least 1 uppercase letter', 'error')
            if (utility.checkValidUsername(userInfor[0]) == 3):
                flash('Username must have at least 1 lowercase letter', 'error')
            if (utility.checkValidUsername(userInfor[0]) == 4):
                flash('Username must have at least 1 character', 'error')
            if (utility.isValidPassword(userInfor[1]) == 1):
                flash('Password must have 5-10 characters', 'error')
            if (utility.isValidPassword(userInfor[1]) == 2):
                flash('Password must have at least 1 uppercase letter', 'error')
            if (utility.isValidPassword(userInfor[1]) == 3):
                flash('Password must have at least 1 lowercase letter', 'error')
            if (utility.isValidPassword(userInfor[1]) == 4):
                flash('Password must have at least 1 character', 'error')
            if (utility.isValidEmail(userInfor[2]) == 0):
                flash('Invalid email', 'error')
            return render_template('signin.html')

#------------------------------------API-------------------------------------   

  
#------------------------------------PLACE-----------------------------------
@app.route('/PlaceCommentSubmit', methods=['POST'])
def submit_place_review():
    review = request.form.get('review')
    #Prepare data
    reviewList = db.GetData('tbl_place_review')
    comment_id = len(reviewList) + 1
    comment_username = request.cookies['username']
    comment_placeid = review.split("|")[0]
    comment_like = comment_dislike = 0
    comment_comment = review.split("|")[1]
    comment_time = datetime.now().strftime('%Y-%m-%d')

    comment = {
        'id': comment_id,
        'user_username': comment_username,
        'place_id': comment_placeid,
        'review_like': comment_like,
        'review_dislike': comment_dislike,
        'review_comment': comment_comment,
        'review_time': comment_time,    
    }
    db.InsertData('tbl_place_review', comment)

    return jsonify(comment)

@app.route('/GetPlaceComment', methods=['POST'])
def get_place_comment():
    place_id = request.json
    place_id = place_id['place_id']

    data = db.Query(f'Select * from tbl_place_review where place_id = {place_id}')
    data = utility.tupeToDict(data, ['id', 'user_username', 'place_id', 'review_like', 'review_dislike', 'review_comment', 'review_time'])
    return jsonify(data)

@app.route('/PlaceReact', methods=['POST'])
def react_comment():
    data = request.json
    comment_id = data['comment_id']
    action = data['action']
    # Return the new like or dislike count
    if action == 'like':
        currentLike = db.Query(f"select review_like from tbl_place_review where id = {comment_id}")[0][0]
        new_like_count = int(currentLike) + 1
        db.InsertQuery(f'Update tbl_place_review Set review_like = {new_like_count} Where id = {comment_id}')
        return jsonify({'new_like_count': new_like_count})
    elif action == 'dislike':
        currentDisLike = db.Query(f"select review_dislike from tbl_place_review where id = {comment_id}")[0][0]
        new_dislike_count = int(currentDisLike) + 1
        db.InsertQuery(f'Update tbl_place_review Set review_dislike = {new_dislike_count} Where id = {comment_id}')
        return jsonify({'new_dislike_count': new_dislike_count})
# -----------------------------------ENDPLACE--------------------------------



#------------------------------------HOTEL-----------------------------------
@app.route('/HotelCommentSubmit', methods=['POST'])
def submit_hotel_review():
    review = request.form.get('review')
    #Prepare data
    reviewList = db.GetData('tbl_hotel_review')
    comment_id = len(reviewList) + 1
    comment_username = request.cookies['username']
    comment_hotelid = review.split("|")[0]
    comment_like = comment_dislike = 0
    comment_comment = review.split("|")[1]
    comment_time = datetime.now().strftime('%Y-%m-%d')

    comment = {
        'id': comment_id,
        'user_username': comment_username,
        'hotel_id': comment_hotelid,
        'review_like': comment_like,
        'review_dislike': comment_dislike,
        'review_comment': comment_comment,
        'review_time': comment_time,   
    }
    db.InsertData('tbl_hotel_review', comment)

    return jsonify(comment)

@app.route('/GetHotelComment', methods=['POST'])
def get_hotel_comment():
    hotel_id = request.json
    hotel_id = hotel_id['hotel_id']

    data = db.Query(f'Select * from tbl_hotel_review where hotel_id = {hotel_id}')
    data = utility.tupeToDict(data, ['id', 'user_username', 'hotel_id', 'review_like', 'review_dislike', 'review_time', 'review_comment'])
    return jsonify(data)

@app.route('/HotelReact', methods=['POST'])
def react_hotel_comment():
    data = request.json
    comment_id = data['comment_id']
    action = data['action']
    # Return the new like or dislike count
    if action == 'like':
        currentLike = db.Query(f"select review_like from tbl_hotel_review where id = {comment_id}")[0][0]
        new_like_count = int(currentLike) + 1
        db.InsertQuery(f'Update tbl_hotel_review Set review_like = {new_like_count} Where id = {comment_id}')
        return jsonify({'new_like_count': new_like_count})
    elif action == 'dislike':
        currentDisLike = db.Query(f"select review_dislike from tbl_hotel_review where id = {comment_id}")[0][0]
        new_dislike_count = int(currentDisLike) + 1
        db.InsertQuery(f'Update tbl_hotel_review Set review_dislike = {new_dislike_count} Where id = {comment_id}')
        return jsonify({'new_dislike_count': new_dislike_count})
    
@app.route('/PlaceReact', methods=['POST'])
def react_place_comment():
    data = request.json
    comment_id = data['comment_id']
    action = data['action']
    # Return the new like or dislike count
    if action == 'like':
        currentLike = db.Query(f"select review_like from tbl_place_review where id = {comment_id}")[0][0]
        new_like_count = int(currentLike) + 1
        db.InsertQuery(f'Update tbl_place_review Set review_like = {new_like_count} Where id = {comment_id}')
        return jsonify({'new_like_count': new_like_count})
    elif action == 'dislike':
        currentDisLike = db.Query(f"select review_dislike from tbl_place_review where id = {comment_id}")[0][0]
        new_dislike_count = int(currentDisLike) + 1
        db.InsertQuery(f'Update tbl_place_review Set review_dislike = {new_dislike_count} Where id = {comment_id}')
        return jsonify({'new_dislike_count': new_dislike_count})
# -------------------------------------ENDHOTEL------------------------------


#-----------------------------------ELSE-------------------------------------
@app.route('/GetAllInfor', methods=['POST'])
def get_all_infor():
    type = request.json
    type = type['type']
    data = utility.getAllInfor(type)
    return data

@app.route('/GetFilteredInfor', methods=['POST'])
def get_filtered_infor():
    data = request.json
    range = data['inputLabelText']
    type = data['type']
    range = utility.handleInputRange(range)
    datas = utility.getFilteredInfor(range, type)
    if len(datas) > 0:
        return datas
    else:
        return {"data": "None"}
#---------------------------------ENDELSE------------------------------------

@app.route('/TestAPI')
def TestAPI():
    return utility.getAllInfor('place')

app.run(debug=True, host="0.0.0.0")