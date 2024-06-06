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
        if (username == admin[0] and utility.encode(password, username) == admin[1]):
            return 0
    return 2

@app.route('/')
def MainPage():
    cookie = request.cookies.get('username')
    if cookie is not None:
        return render_template('main.html', hotelList=utility.hotelList[:6], placeList=utility.placeList[:6])
    else:
        return redirect(url_for('LoginPage'))

@app.route('/administrator')
def AdminPage():
    return render_template('adminView.html')

@app.route('/login')
def LoginPage():
    return render_template('login.html')

@app.route('/signup')
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

@app.route('/logout')
def Logout():
    res = make_response(redirect(url_for('Login')))
    res.delete_cookie('username')
    return res

#------------------------------------API-------------------------------------   
#-----------------------------------LOGIN/SIGNUP-----------------------------

@app.route('/login', methods = ['POST', 'GET'])
def Login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        if IsValidLogin(username, password) == 1:
            try:
                remember = request.form['remember-account']
            except:
                remember = "off"
            if remember == "on":
                    index = make_response(redirect(url_for('MainPage')))
                    index.set_cookie('username', username)
                    return index
            else:
                index = make_response(redirect(url_for('MainPage')))
                index.set_cookie('username', username, max_age=20)
                return index
        elif IsValidLogin(username, password) == 0:
            return redirect(url_for('AdminPage'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/requestSignUp', methods = ['POST'])
def SignIn():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    if utility.isValidUsername(username) == False:
        response_data = {
            "redirect": "/signup",
            "error": "Username đã tồn tại"
        }
        return jsonify(response_data)
    elif utility.isValidEmail(email) == False:
        response_data = {
            "redirect": "/signup",
            "error": "Email da ton tai"
        }
        return jsonify(response_data)
    
    response_data = {
        "redirect": "/login",
        "error": "None"
    }
    db.InsertUser(username, utility.encode(password, username), email)
    return jsonify(response_data)
#-----------------------------------END LOGIN--------------------------------
  
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
    
@app.route('/chatbot',methods=['POST'])
def test():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    if intent_name == 'detail_diadiem':
        query = "SELECT * FROM tbl_place"
        data = db.Query(query=query)
        list_items = []
        for row in data:
            list_item = {
                "type": "info",
                "title": row[1],  # Tên địa điểm
                "subtitle": f"Địa chỉ: {row[2]}, Phí vào cửa: {row[3]} VND",
                "actionLink": f"https://c128-2402-800-61ae-fcf1-9d04-370e-eea5-784a.ngrok-free.app/pdetail/{row[1]}"
            }
            list_items.append(list_item)
            list_items.append({"type": "divider"})
        
        if list_items and list_items[-1]["type"] == "divider":
            list_items.pop()
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "info",
                                    "title": "Đây là toàn bộ thông tin các địa điểm mà chúng tôi biết:"
                                }
                            ] + list_items
                        ]
                    }
                }
            ]
        }

        return jsonify(response)

    if intent_name == 'detail_hotel':
        query = "SELECT * FROM tbl_hotel"
        data = db.Query(query=query)
        list_items = []
        for row in data:
            list_item = {
                "type": "info",
                "title": row[1],  # Tên địa điểm
                "subtitle": f"Địa chỉ: {row[2]}, Giá phòng 1 đêm: {row[3]} VND",
                "actionLink": "https://www.youtube.com/watch?v=_qLaIDHWjtU&t=153s"

            }
            list_items.append(list_item)
            list_items.append({"type": "divider"})
            list_items.append(list_item)
            list_items.append({"type": "divider"}) 
        if list_items and list_items[-1]["type"] == "divider":
            list_items.pop()
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "info",
                                    "title": "Đây là toàn bộ thông tin hotel mà chúng tôi biết:"
                                }
                            ] + list_items
                        ]
                    }
                }
            ]
        }

        return jsonify(response)
    if intent_name == 'gia_vevaocua':
        #lấy giá trị từ request
        place_name = req.get('queryResult').get("parameters").get("diadiem_dulich")
        query = f"SELECT entry_price FROM tbl_place WHERE place_name = '{place_name}'"
        data = db.Query(query=query)
        if data:
            entry_fee = data[0][0]
            response_text = f"Giá vé vào cửa của {place_name} là {entry_fee} VND."
        else:
            response_text = "Xin lỗi, chúng tôi không tìm thấy thông tin về địa điểm này hay chắc chắn rằng bạn nhập đúng tên điạ điểm"

        return jsonify({
        'fulfillmentText':response_text
        })
    if intent_name == 'giaphong_khachsan':
        #lấy tên địa điểm từ request
        place_name = req.get('queryResult').get("parameters").get("hotel_name")
        # print(place_name)
        query = f"SELECT average_price FROM tbl_hotel WHERE hotel_name = '{place_name}'"
        data = db.Query(query=query)
        if data:
            entry_fee = data[0][0]
            response_text = f"Giá phòng trung bình 1 đêm của {place_name} là {entry_fee} VND."
        else:
            response_text = "Xin lỗi, chúng tôi không tìm thấy thông tin về địa điểm này hay chắc chắn rằng bạn nhập đúng tên điạ điểm"
        return jsonify({
        'fulfillmentText':response_text
        })

    if intent_name == 'vitri_dddl':
        #lấy giá trị tên địa điểm du lịch từ request
        place_name = req.get('queryResult').get("parameters").get("diadiem_dulich")
        # print(place_name)
        query = f"SELECT place_address FROM tbl_place WHERE place_name = '{place_name}'"
        data = db.Query(query=query)
        if data:
            place_address = data[0][0]
            response_text = f"Vị tri của {place_name} ở {place_address}"
        else:
            response_text = "Xin lỗi, chúng tôi không tìm thấy thông tin về địa điểm này hay chắc chắn rằng bạn nhập đúng tên điạ điểm"
        return jsonify({
        'fulfillmentText':response_text
        })
    if intent_name == 'vitri_hotel':
        #lấy giá trị tên địa điểm du lịch từ request
        place_name = req.get('queryResult').get("parameters").get("hotel_name")
        # print(place_name)
        query = f"SELECT hotel_address FROM tbl_hotel WHERE hotel_name = '{place_name}'"
        data = db.Query(query=query)
        if data:
            place_address = data[0][0]
            response_text = f"Vị tri của {place_name} ở {place_address}"
        else:
            response_text = "Xin lỗi, chúng tôi không tìm thấy thông tin về địa điểm này hay chắc chắn rằng bạn nhập đúng tên điạ điểm"

        return jsonify({
        'fulfillmentText':response_text
        })

@app.route('/directions')
def Directionpage():
    return render_template('directions.html')
#---------------------------------ENDELSE------------------------------------

@app.route('/TestAPI')
def TestAPI():
    return utility.getAllInfor('place')

app.run(debug=True)