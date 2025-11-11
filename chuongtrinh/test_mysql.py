import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ketnoidb.ketnoi_mysql import connect_mysql

connect_mysql()
