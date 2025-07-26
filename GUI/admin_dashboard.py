import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def issue_book():
    subprocess.Popen(["python", "issue_book.py"])

def return_book():
    subprocess.Popen(["python", "return_book.py"])

def view_books():
    os.system("notepad books.txt")

root = tk.Tk()
root.title("Admin Dashboard")
root.geometry("300x200")

tk.Label(root, text="Welcome Admin!", font=("Arial", 14)).pack(pady=15)

tk.Button(root, text="Issue Book", command=issue_book, width=20).pack(pady=5)
tk.Button(root, text="Return Book", command=return_book, width=20).pack(pady=5)
tk.Button(root, text="View Books File", command=view_books, width=20).pack(pady=5)

root.mainloop()
