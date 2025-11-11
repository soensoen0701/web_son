import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.deletedanhmuc import delete_danhmuc
ma = input("Nhập mã danh mục cần xóa: ")
delete_danhmuc(ma)