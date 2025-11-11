import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.insertdanhmuc import insert_danhmuc
while True:
    ten_danhmuc = input("Nhập tên danh mục: ")
    mota = input("Nhập mô tả danh mục: ")
    insert_danhmuc(ten_danhmuc, mota)
    con = input("Bạn có muốn thêm danh mục khác không? (y/n): ")
    if con.lower() != 'y':
        break