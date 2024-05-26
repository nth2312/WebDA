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
        shortDesPath = os.path.join(base_path, 'shortDes.txt')

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
        with open(shortDesPath, 'r', encoding='utf_8') as f:
            short = f.read()
        
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
            'status': 'ok',
            'place_id': otherData[0],
            'place_name': otherData[1],
            'place_address': otherData[2],
            'place_history': history,
            'place_description': description,
            'place_short': short,
            'place_time': dictPlaceTime,
            'place_price': dictPlacePrice,
            'place_entryPrice': otherData[3],
            'place_video': video
        }
        return detail
    
    def getDetailHotelInfor(self, hotel_name):
        otherData = self.db.Query(f'Select * from tbl_hotel where hotel_name = "{hotel_name}"')
        otherData = otherData[0]

        base_path = f"./static/hdetail/{otherData[0]}"
        historyPath = os.path.join(base_path, 'history.txt')
        descriptionPath = os.path.join(base_path, 'description.txt')
        entryPath = os.path.join(base_path, 'entry.txt')
        videoPath = os.path.join(base_path, 'video.txt')
        shortDesPath = os.path.join(base_path, 'shortDes.txt')

        with open(historyPath, 'r', encoding='utf-8') as f:
            history = f.read()
        with open(descriptionPath, 'r', encoding='utf-8') as f:
            description = f.read()
        with open(entryPath, 'r', encoding='utf-8') as f:
            entry = f.read()
        with open(videoPath, 'r', encoding='utf-8') as f:
            video = f.read()
        with open(shortDesPath, 'r', encoding='utf_8') as f:
            short = f.read()

        hotel_price = entry.split('@')
        dictHotelPrice = []
        for price in hotel_price:
            type = price.split("|")[0]
            price = price.split("|")[1]
            dictHotelPrice.append({
                'type': type,
                'price': price
            })

        detail = {
            'status': 'ok',
            'hotel_id': otherData[0],
            'hotel_name': otherData[1],
            'hotel_address': otherData[2],
            'hotel_history': history,
            'hotel_description': description,
            'hotel_short': short,
            'hotel_price': dictHotelPrice,
            'hotel_averagePrice': otherData[3],
            'hotel_video': video
        }
        return detail
    
    def getPlacecoordinates(self, place_id):
        # placeInfor = self.db.Query(f"select * from place where place_id = {place_id}")
        # lat = placeInfor[2]
        # long = placeInfor[3]
        ret = {
            'lat': 21.0248218,
            'long': 105.8507097
        }
        return ret

    def getNearStore(self, place_id):
        #stores = self.db.Query(f"select * from store inner join place_store on store.store_id = place_store.store_id where place.place_id = {place_id}")
        #stores = self.tupeToDict(stores)
        stores = [
            {
                'store_id': "1",
                'store_link': "url_to_link",
                'store_name': "store_name"
            },
            {
                'store_id': "1",
                'store_link': "url_to_link2",
                'store_name': "store_name2"
            },
            {
                'store_id': "1",
                'store_link': "url_to_link3",
                'store_name': "store_name3"
            }
        ]
        return stores
    def getAllInfor(self, type):
        details = []

        data = self.db.Query(f"select {type}_name from tbl_{type}")
        dataNameList = []
        for d in data:
            dataNameList.append(d[0])
        
        for data in dataNameList:
            if (type == "hotel"):
                details.append(self.getDetailHotelInfor(data))
            else:
                details.append(self.getDetailPlaceInfor(data))
        
        return details

    def handleInputRange(self, inputRange):
        range = []
        if "<" in inputRange:
            data = inputRange[1:]
            back = ""
            for numb in data:
                if numb != '.' and numb != 'đ':
                    back += str(numb)
            range.append(0)
            range.append(int(back))
            return range
        elif "+" in inputRange:
            data = inputRange.split(" - ")[0]
            top = ""
            for numb in data:
                if numb != '.' and numb != 'đ':
                    top += str(numb)
            range.append(top[:-1])
            range.append(1000000000)
            return range
        top = ""
        back = ""
        data = inputRange.split(" - ")[0]
        for numb in data:
            if numb != '.' and numb != 'đ':
                top += str(numb)
        data = inputRange.split(" - ")[-1]
        for numb in data:
            if numb != '.' and numb != 'đ':
                back += str(numb)
        range.append(top)
        range.append(back)
        return range

    def getFilteredInfor(self, range, type):
        if type == 'hotel':
            hotels = self.db.Query(f"Select hotel_name from tbl_hotel where average_price >= {int(range[0])} and average_price <= {int(range[1])}")
            hotelList = []
            if len(hotels) > 0:
                for hotel in hotels:
                    hotelList.append(hotel[0])
            else:
                return {'status': 'none'}
            ret = []
            for hotel in hotelList:
                ret.append(self.getDetailHotelInfor(hotel))
            return ret
        else:
            places = self.db.Query(f"Select place_name from tbl_place where entry_price >= {int(range[0])} and entry_price <= {int(range[1])}")
            placeList = []
            if len(places) > 0:
                for place in places:
                    placeList.append(place[0])
            else:
                return {'status': 'none'}
            ret = []
            for place in placeList:
                ret.append(self.getDetailPlaceInfor(place))
            return ret

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