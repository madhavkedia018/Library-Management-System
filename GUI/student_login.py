# student_login.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import read_students, write_students
from student_dashboard import StudentDashboard

def StudentLogin(root):
    window = tk.Toplevel(root)
    window.title("Student Login")

    def create_account():
        sid = simpledialog.askinteger("ID", "Enter new Student ID:")
        students = read_students()
        if sid in students:
            messagebox.showerror("Exists", "Student ID already exists.")
            return
        name = simpledialog.askstring("Name", "Enter name:")
        stream = simpledialog.askstring("Stream", "Enter stream:")
        students[sid] = {"name": name, "stream": stream}
        write_students(students)
        messagebox.showinfo("Created", "Account created.")

    def login():
        sid = simpledialog.askinteger("ID", "Enter Student ID:")
        students = read_students()
        if sid not in students:
            messagebox.showerror("Not Found", "Student ID not found.")
            return
        StudentDashboard(root, sid, students[sid]["name"])

    tk.Button(window, text="Create New Account", command=create_account).pack(pady=10)
    tk.Button(window, text="Login", command=login).pack(pady=10)
