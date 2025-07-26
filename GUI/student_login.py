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
                if len(parts) >= 3:
                    sid, name, stream = parts[0], parts[1], parts[2]
                    students[int(sid)] = {"name": name, "stream": stream}
    return students

def save_student(sid, name, stream):
    with open("students.txt", "a") as f:
        f.write(f"{sid},{name},{stream}\n")

def login():
    sid = sid_entry.get().strip()
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
        sid = new_id_entry.get().strip()
        name = new_name_entry.get().strip()
        stream = new_stream_entry.get().strip()
        
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
        messagebox.showinfo("Success", "Account created successfully!")
        new_account_win.destroy()
        root.destroy()
        launch_dashboard(sid)
    
    new_account_win = tk.Toplevel(root)
    new_account_win.title("Create New Account")
    new_account_win.geometry("300x250")
    
    tk.Label(new_account_win, text="Student ID:", font=("Arial", 11)).pack(pady=5)
    new_id_entry = tk.Entry(new_account_win, width=25)
    new_id_entry.pack(pady=5)
    
    tk.Label(new_account_win, text="Name:", font=("Arial", 11)).pack(pady=5)
    new_name_entry = tk.Entry(new_account_win, width=25)
    new_name_entry.pack(pady=5)
    
    tk.Label(new_account_win, text="Stream:", font=("Arial", 11)).pack(pady=5)
    new_stream_entry = tk.Entry(new_account_win, width=25)
    new_stream_entry.pack(pady=5)
    
    tk.Button(new_account_win, text="Create Account", command=submit_new_account, 
              bg="green", fg="white", width=15).pack(pady=20)

def main():
    global root, sid_entry
    
    # GUI
    root = tk.Tk()
    root.title("Student Login")
    root.geometry("350x300")
    
    # Title
    tk.Label(root, text="Student Login System", font=("Arial", 16, "bold")).pack(pady=20)
    
    tk.Label(root, text="Enter Student ID:", font=("Arial", 12)).pack(pady=10)
    sid_entry = tk.Entry(root, width=25, font=("Arial", 11))
    sid_entry.pack(pady=5)
    
    tk.Button(root, text="Login", command=login, height=2, width=20, 
              bg="blue", fg="white").pack(pady=20)
    
    tk.Label(root, text="OR", font=("Arial", 10)).pack()
    
    tk.Button(root, text="Create New Account", command=create_account, 
              height=2, width=20, bg="green", fg="white").pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
