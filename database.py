import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="NTH23122",
            database="dtb_web"
        )

    def __del__(self):
        if self.db.is_connected():
            self.db.close()

    def GetData(self, table):
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def GetDataWithCol(self, table, col):
        cursor = self.db.cursor()
        cursor.execute(f"SELECT {col} FROM {table}")
        rows = cursor.fetchall()
        cursor.close()
        return [row[0] for row in rows]

    def InsertData(self, table_name, data):
        cursor = self.db.cursor()
        try:
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, list(data.values()))
            self.db.commit()
            print(f"Data inserted into {table_name}: {data}")
        except Exception as e:
            self.db.rollback()  # Rollback nếu có lỗi xảy ra
            print(f"Error inserting data: {e}")
        finally:
            cursor.close()

    def Query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def InsertQuery(self, query):
        cursor = self.db.cursor()
        try:
            cursor.execute(query)
            self.db.commit()
        except Exception as e:
            self.db.rollback()  # Rollback nếu có lỗi xảy ra
            print(f"Error executing query: {e}")
        finally:
            cursor.close()
