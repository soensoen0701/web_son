import tkinter as tk
from tkinter import ttk, messagebox
import sys, os
import mysql.connector
from mysql.connector import Error

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.insertdanhmuc import insert_danhmuc
from common.deletedanhmuc import delete_danhmuc
from common.updatedanhmuc import update_danhmuc
from common.getdanhmuc import get_all_danhmuc

get_all_danhmuc()
# -------------------------------
root = tk.Tk()
root.title("Quản lý Danh Mục - CRUD MySQL")
root.geometry("700x500")
# Hàm cập nhật danh sách trên Treeview
# -------------------------------
def load_data():
    for i in tree.get_children():
        tree.delete(i)
    data = get_all_danhmuc()
    for row in data:
        tree.insert("", tk.END, values=row)

# -------------------------------
# Hàm thêm danh mục
# -------------------------------
def add_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()
    if ten.strip() == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return
    insert_danhmuc(ten, mota)
    load_data()
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)

# -------------------------------
# Hàm xóa danh mục
# -------------------------------
def delete_selected():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần xóa.")
        return
    ma = tree.item(selected)['values'][0]
    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa danh mục ID {ma}?")
    if confirm:
        delete_danhmuc(ma)
        load_data()

# -------------------------------
# Hàm chọn hàng trong Treeview để sửa
# -------------------------------
def on_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected)['values']
        entry_id.delete(0, tk.END)
        entry_id.insert(0, values[0])
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.delete(0, tk.END)
        entry_mota.insert(0, values[2])

# -------------------------------
# Hàm cập nhật danh mục
# -------------------------------
def update_current():
    ma = entry_id.get()
    ten = entry_ten.get()
    mota = entry_mota.get()
    if ma == "":
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để sửa.")
        return
    update_danhmuc(ma, ten, mota)
    load_data()

# --- Frame nhập liệu ---
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Mã Danh Mục:").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_input, width=10, state='normal')
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tên Danh Mục:").grid(row=1, column=0, padx=5, pady=5)
entry_ten = tk.Entry(frame_input, width=30)
entry_ten.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=2, column=0, padx=5, pady=5)
entry_mota = tk.Entry(frame_input, width=50)
entry_mota.grid(row=2, column=1, padx=5, pady=5)

# --- Nút chức năng ---
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Thêm", bg="#4CAF50", fg="white", command=add_danhmuc).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Sửa", bg="#2196F3", fg="white", command=update_current).grid(row=0, column=1, padx=10)
tk.Button(frame_buttons, text="Xóa", bg="#F44336", fg="white", command=delete_selected).grid(row=0, column=2, padx=10)
tk.Button(frame_buttons, text="Tải lại", command=load_data).grid(row=0, column=3, padx=10)

# --- Bảng hiển thị Treeview ---
columns = ("Mã", "Tên Danh Mục", "Mô tả")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<ButtonRelease-1>", on_select)

# --- Tải dữ liệu ban đầu ---
load_data()

root.mainloop()