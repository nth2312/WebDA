import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="nth2312",
            password="NTH23122",
            database="dtb_web"
        )

    def __del__(self):
        self.db.close()

    def GetData(self, table):
        cursor = self.db.cursor()
        cursor.execute(f"select * from {table}")
        rows = cursor.fetchall()

        cursor.close()
        return rows

    def GetDataWithCol(self, table, col):
        cursor = self.db.cursor()
        cursor.execute(f"select {col} from {table}")
        rows = cursor.fetchall()

        cursor.close()
        return rows


    def InsertUser(self, username, password, email):
        cursor = self.db.cursor()
        try:
            placeholder = [username, password, email]
            sql = f"insert into tbl_user values(%s, %s, %s)"
            cursor.execute(sql, placeholder)
            self.db.commit()
        except:
            print("Error")

        cursor.close()
    
    def InsertData(self, table_name, data):
        cursor = self.db.cursor()
        try:
            placeholders = ','.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, list(data.values()))
            self.db.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
    
    def Query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows

    def InsertQuery(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()
        cursor.close()

db = Database()
# data = {
#     'user_username': 'user1',
#     'user_password': "password",
#     'user_email': "user@gmail.com"
# }
# db.InsertData('tbl_user', data)
# print(db.GetDataWithCol('tbl_user', 'user_username'))
# print(db.GetData('tbl_place'))

# places = db.GetData('tbl_place')
# placekeys = ['place_id', 'place_name', 'place_address', 'entry_price']
# placeList = tupeToDict(places, placekeys)