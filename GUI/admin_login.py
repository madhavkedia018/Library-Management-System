import tkinter as tk
from tkinter import messagebox
from admin_dashboard import open_admin_dashboard

def open_admin_login():
    def check_credentials():
        uid = entry_user.get()
        pwd = entry_pass.get()
        if uid == "admin" and pwd == "1234":
            window.destroy()
            open_admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid login credentials")

    window = tk.Tk()
    window.title("Admin Login")

    tk.Label(window, text="Admin UserID:").pack(pady=5)
    entry_user = tk.Entry(window)
    entry_user.pack(pady=5)

    tk.Label(window, text="Password:").pack(pady=5)
    entry_pass = tk.Entry(window, show='*')
    entry_pass.pack(pady=5)

    tk.Button(window, text="Login", command=check_credentials).pack(pady=20)

    window.mainloop()
    
def main():
    open_admin_login()

