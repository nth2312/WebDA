from database import Database
import os

class Utility:
    def __init__(self):
        self.db = Database()

        hotels = self.db.GetData('tbl_hotel')
        hotelkeys = ['hotel_id', 'hotel_name', 'hotel_address', 'average_price']
        self.hotelList = self.tupeToDict(hotels, hotelkeys)

        places = self.db.GetData('tbl_place')
        placekeys = ['place_id', 'place_name', 'place_address', 'entry_price']
        self.placeList = self.tupeToDict(places, placekeys)

    def getDetailPlaceInfor(self, place_name):
        otherData = self.db.Query(f'Select * from tbl_place where place_name = "{place_name}"')
        otherData = otherData[0]

        base_path = f"./static/detail/{otherData[0]}"
        historyPath = os.path.join(base_path, 'history.txt')
        descriptionPath = os.path.join(base_path, 'description.txt')
        entryPath = os.path.join(base_path, 'entry.txt')
        openPath = os.path.join(base_path, 'open.txt')
        videoPath = os.path.join(base_path, 'video.txt')

        with open(historyPath, 'r', encoding='utf-8') as f:
            history = f.read()
        with open(descriptionPath, 'r', encoding='utf-8') as f:
            description = f.read()
        with open(entryPath, 'r', encoding='utf-8') as f:
            entry = f.read()
        with open(openPath, 'r', encoding='utf-8') as f:
            op = f.read()
        with open(videoPath, 'r', encoding='utf-8') as f:
            video = f.read()
        
        try:
            place_time = op.split("/")
            dictPlaceTime = []
            for time in place_time:
                date = time.split("|")[0]
                hour = time.split("|")[1]
                dictPlaceTime.append({
                    'date': date,
                    'hour': hour
                })
        except:
            dictPlaceTime.append({
                    'date': "Giờ mở cửa",
                    'hour': "Luôn mở cửa"
                })

        try:
            place_price = entry.split('@')
            dictPlacePrice = []
            for time in place_price:
                type = time.split("|")[0]
                price = time.split("|")[1]
                dictPlacePrice.append({
                    'type': type,
                    'price': price
                })
        except:
            dictPlacePrice.append({
                    'type': "Giá vé",
                    'price': "Miễn phí"
                })

        detail = {
            'place_id': otherData[0],
            'place_name': otherData[1],
            'place_address': otherData[2],
            'place_history': history,
            'place_description': description,
            'place_time': dictPlaceTime,
            'place_price': dictPlacePrice,
            'place_video': video
        }
        return detail

    def isValidPassword(self, input):
        checkLower = 0
        checkUpper = 0
        checkNumb = 0
        if len(input) < 5 or len(input) > 12:
            return 1
        else:
            for char in input:
                if char.isupper():
                    checkUpper = 1
                if char.islower():
                    checkLower = 1
                if char.isdigit():
                    checkNumb = 1
            if (checkLower == 0):
                return 2
            if (checkUpper == 0):
                return 3
            if (checkNumb == 0):
                return 4
            if (checkLower == checkUpper == checkNumb):
                return 0

    def checkValidUsername(self, input):
        userList = self.db.GetDataWithCol('tbl_user', 'user_username')
        checkLower = 0
        checkUpper = 0
        checkNumb = 0
        for user in userList:
            if input == str(user[0]):
                return 5
        if len(input) < 5 or len(input) > 10:
            return 1
        else:
            for char in input:
                if char.isupper():
                    checkUpper = 1
                if char.islower():
                    checkLower = 1
                if char.isdigit():
                    checkNumb = 1
            if (checkLower == 0):
                return 2
            if (checkUpper == 0):
                return 3
            if (checkNumb == 0):
                return 4
            if (checkLower == checkUpper == checkNumb):
                return 0

    def isValidEmail(self, email):
        checkA = 0
        checkOther = 0
        Aidx = 0
        for i in range(len(email)):
            if (email[i] == '@' and i != 0):
                checkA = 1
                Aidx = i
        for i in range(Aidx, len(email)):
            if (email[i] == '.' and email[i - 1] != '@' and email[-1] != '.'):
                checkOther = 1
        if (checkA == checkOther == 1):
            return 1
        else:
            return 0

    def tupeToDict(self, data, key):
        returnDict = []
        for row in data:
            data_dict = {key: value for key, value in zip(key, row)}
            returnDict.append(data_dict)
        return returnDict

# u = Utility()
# u.getDetailPlaceInfor("Tràng Tiền Plaza")