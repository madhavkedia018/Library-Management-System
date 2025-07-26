# admin_login.py
import tkinter as tk
from tkinter import messagebox
from admin_dashboard import AdminDashboard

def AdminLogin(root):
    window = tk.Toplevel(root)
    window.title("Librarian Login")

    tk.Label(window, text="User ID").pack(pady=5)
    uid_entry = tk.Entry(window)
    uid_entry.pack(pady=5)

    tk.Label(window, text="Password").pack(pady=5)
    pwd_entry = tk.Entry(window, show='*')
    pwd_entry.pack(pady=5)

    def login():
        if uid_entry.get() == "admin" and pwd_entry.get() == "1234":
            window.destroy()
            AdminDashboard(root)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    tk.Button(window, text="Login", command=login).pack(pady=10)
