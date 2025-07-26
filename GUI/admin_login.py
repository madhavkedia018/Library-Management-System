import tkinter as tk
from tkinter import messagebox
import subprocess

# Define the password
ADMIN_PASSWORD = "admin123"  # You can change this

def check_password():
    entered = password_entry.get()
    if entered == ADMIN_PASSWORD:
        root.destroy()
        subprocess.Popen(["python", "admin_dashboard.py"])
    else:
        messagebox.showerror("Access Denied", "Incorrect password.")

root = tk.Tk()
root.title("Admin Login")
root.geometry("300x150")

tk.Label(root, text="Enter Admin Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=25)
password_entry.pack()

login_btn = tk.Button(root, text="Login", command=check_password)
login_btn.pack(pady=10)

root.mainloop()
