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
    
    def Query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows

db = Database()
# print(db.GetDataWithCol('tbl_user', 'user_username'))
# print(db.GetData('tbl_place'))

# places = db.GetData('tbl_place')
# placekeys = ['place_id', 'place_name', 'place_address', 'entry_price']
# placeList = tupeToDict(places, placekeys)