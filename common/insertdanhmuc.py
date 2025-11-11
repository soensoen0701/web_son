#ham kết nối danh mục
from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def insert_danhmuc(ten_danhmuc, mota):
    """
    Hàm thêm 1 danh mục mới vào bảng DanhMuc.
    """
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO DanhMuc (TenDanhMuc, MoTa) VALUES (%s, %s)"
        cursor.execute(sql, (ten_danhmuc, mota))
        connection.commit()
        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
    except Error as e:
        print(f"❌ Lỗi khi thêm danh mục: {e}")
    finally:
        cursor.close()
        connection.close()