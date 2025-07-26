import tkinter as tk
from tkinter import messagebox
import os
from student_dashboard import launch_dashboard

def load_students():
    students = {}
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    sid, name, stream = parts
                    students[int(sid)] = {"name": name, "stream": stream}
    return students

def save_student(sid, name, stream):
    with open("students.txt", "a") as f:
        f.write(f"{sid},{name},{stream}\n")

def login():
    sid = sid_entry.get()
    if not sid.isdigit():
        messagebox.showerror("Error", "Invalid ID format.")
        return
    sid = int(sid)
    students = load_students()
    if sid in students:
        root.destroy()
        launch_dashboard(sid)
    else:
        messagebox.showerror("Login Failed", "Student ID not found.")

def create_account():
    def submit_new_account():
        sid = new_id_entry.get()
        name = new_name_entry.get()
        stream = new_stream_entry.get()
        if not sid.isdigit():
            messagebox.showerror("Error", "ID must be numeric.")
            return
        sid = int(sid)
        students = load_students()
        if sid in students:
            messagebox.showerror("Error", "ID already exists.")
            return
        if not name or not stream:
            messagebox.showerror("Error", "Please fill all fields.")
            return
        save_student(sid, name, stream)
        messagebox.showinfo("Success", "Account created.")
        new_account_win.destroy()
        root.destroy()
        launch_dashboard(sid)

    new_account_win = tk.Toplevel(root)
    new_account_win.title("Create New Account")

    tk.Label(new_account_win, text="Student ID:").pack()
    new_id_entry = tk.Entry(new_account_win)
    new_id_entry.pack()

    tk.Label(new_account_win, text="Name:").pack()
    new_name_entry = tk.Entry(new_account_win)
    new_name_entry.pack()

    tk.Label(new_account_win, text="Stream:").pack()
    new_stream_entry = tk.Entry(new_account_win)
    new_stream_entry.pack()

    tk.Button(new_account_win, text="Create Account", command=submit_new_account).pack(pady=10)

# GUI
root = tk.Tk()
root.title("Student Login")
root.geometry("300x300")

tk.Label(root, text="Enter Student ID:", font=("Arial", 12)).pack(pady=10)
sid_entry = tk.Entry(root)
sid_entry.pack()

tk.Button(root, text="Login", command=login, height=2, width=20).pack(pady=20)
tk.Label(root, text="OR").pack()
tk.Button(root, text="Create New Account", command=create_account, height=2, width=20).pack(pady=10)

root.mainloop()

    
def main():
    open_student_login()
