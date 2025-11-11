from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def update_danhmuc(ma_danhmuc, ten_moi, mota_moi):
    """
    Hàm cập nhật tên và mô tả danh mục theo mã danh mục.
    """
    connection = connect_mysql()
    if connection is None:
        print("⚠️ Không thể kết nối CSDL.")
        return

    try:
        cursor = connection.cursor()
        sql = """
            UPDATE DanhMuc
            SET TenDanhMuc = %s, MoTa = %s
            WHERE MaDanhMuc = %s
        """
        cursor.execute(sql, (ten_moi, mota_moi, ma_danhmuc))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"📝 Đã cập nhật danh mục có mã {ma_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {ma_danhmuc}")
    except Error as e:
        print(f"❌ Lỗi khi cập nhật danh mục: {e}")
    finally:
        cursor.close()
        connection.close()