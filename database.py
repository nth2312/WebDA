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

dtb = Database()
print(dtb.GetData('tbl_user'))