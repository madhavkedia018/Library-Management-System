import tkinter as tk
import subprocess

def open_admin_dashboard():
    window = tk.Tk()
    window.title("Admin Dashboard")

    tk.Label(window, text="Welcome Admin!", font=("Helvetica", 14, "bold")).pack(pady=15)

    def add_book():
        subprocess.run(["library_backend.exe", "add_book"])

    def update_quantity():
        subprocess.run(["library_backend.exe", "update_quantity"])

    def view_books():
        subprocess.run(["library_backend.exe", "view_books"])

    def view_inorder():
        subprocess.run(["library_backend.exe", "view_inorder"])

    tk.Button(window, text="Add Book", width=20, command=add_book).pack(pady=5)
    tk.Button(window, text="Update Quantity", width=20, command=update_quantity).pack(pady=5)
    tk.Button(window, text="View Books", width=20, command=view_books).pack(pady=5)
    tk.Button(window, text="View Inorder", width=20, command=view_inorder).pack(pady=5)

    window.mainloop()
