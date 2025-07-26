import tkinter as tk
import subprocess

def open_student_login():
    subprocess.Popen(["python", "student_login.py"])

def open_admin_login():
    subprocess.Popen(["python", "admin_login.py"])

root = tk.Tk()
root.title("Library System - Select Role")
root.geometry("300x180")

label = tk.Label(root, text="Select Role", font=("Arial", 14))
label.pack(pady=15)

student_btn = tk.Button(root, text="Student Login", width=20, command=open_student_login)
student_btn.pack(pady=5)

admin_btn = tk.Button(root, text="Admin Login", width=20, command=open_admin_login)
admin_btn.pack(pady=5)

root.mainloop()
