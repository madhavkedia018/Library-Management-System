import tkinter as tk
from tkinter import messagebox
import subprocess

def open_student_login():
    subprocess.Popen(["python", "student_login.py"])

def open_librarian_dashboard():
    subprocess.Popen(["python", "librarian_dashboard.py"])

root = tk.Tk()
root.title("Library System - Select Role")
root.geometry("300x180")

label = tk.Label(root, text="Select Your Role:", font=("Helvetica", 14))
label.pack(pady=15)

student_button = tk.Button(root, text="Student", width=20, command=open_student_login)
student_button.pack(pady=5)

librarian_button = tk.Button(root, text="Librarian", width=20, command=open_librarian_dashboard)
librarian_button.pack(pady=5)

root.mainloop()
