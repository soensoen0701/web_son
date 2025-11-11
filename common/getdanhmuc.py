from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def get_all_danhmuc():
    """
    Hàm lấy danh sách toàn bộ danh mục từ bảng DanhMuc.
    Trả về list các tuple (MaDanhMuc, TenDanhMuc, MoTa)
    """
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return []

    danh_sach = []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT MaDanhMuc, TenDanhMuc, MoTa FROM DanhMuc")
        danh_sach = cursor.fetchall()

        if danh_sach:
            print("📋 Danh sách danh mục:")
            for row in danh_sach:
                print(f"  🆔 {row[0]} | 📦 {row[1]} | 📝 {row[2]}")
        else:
            print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")
    except Error as e:
        print(f"❌ Lỗi khi lấy danh sách danh mục: {e}")
    finally:
        cursor.close()
        connection.close()

    return danh_sach