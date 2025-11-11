import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def delete_danhmuc(ma_danhmuc):
    """
    Hàm xóa 1 danh mục theo mã.
    """
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return

    try:
        cursor = connection.cursor()
        sql = "DELETE FROM DanhMuc WHERE MaDanhMuc = %s"
        cursor.execute(sql, (ma_danhmuc,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Đã xóa danh mục có mã {ma_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {ma_danhmuc}")
    except Error as e:
        print(f"❌ Lỗi khi xóa danh mục: {e}")
    finally:
        cursor.close()
        connection.close()