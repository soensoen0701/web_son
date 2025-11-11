import mysql.connector
from mysql.connector import Error

def connect_mysql():
   
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='qlthuoc'
        )
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection
    except Error as e:
        print(f"❌ Lỗi khi kết nối MySQL: {e}")
    return None
