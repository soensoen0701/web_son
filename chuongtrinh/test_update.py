import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.updatedanhmuc import update_danhmuc

while True:
    ma_danhmuc = input("Nhập mã danh mục cần cập nhật: ")
    ten = input("Nhập tên danh mục mới: ")
    mota = input("Nhập mô tả danh mục mới: ")
    update_danhmuc(ma_danhmuc=input("Nhập mã danh mục cần cập nhật: "), ten_moi=ten, mota_moi=mota)
    con = input("Bạn có muốn cập nhật danh mục khác không? (y/n): ")
    if con.lower() != 'y':
        break