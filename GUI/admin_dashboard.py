# admin_dashboard.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import read_books, write_books

def AdminDashboard(root):
    window = tk.Toplevel(root)
    window.title("Admin Panel")
    window.geometry("400x300")
    
    def add_book():
        name = simpledialog.askstring("Book Name", "Enter book name:")
        qty = simpledialog.askinteger("Quantity", "Enter quantity:")
        if name and qty:
            books = read_books()
            if name in books:
                books[name]["total"] += qty
                books[name]["available"] += qty
            else:
                books[name] = {"total": qty, "available": qty}
            write_books(books)
            messagebox.showinfo("Success", f"Book '{name}' added/updated.")
    
    def update_qty():
        name = simpledialog.askstring("Book Name", "Enter book name:")
        qty = simpledialog.askinteger("Additional Quantity", "Enter quantity to add:")
        if name and qty:
            books = read_books()
            if name in books:
                books[name]["total"] += qty
                books[name]["available"] += qty
                write_books(books)
                messagebox.showinfo("Success", "Quantity updated.")
            else:
                messagebox.showerror("Not Found", "Book not found.")
    
    def view_books():
        books = read_books()
        text = "\n".join([f"{b}: Total={i['total']}, Available={i['available']}" for b, i in books.items()])
        messagebox.showinfo("Book List", text or "No books available.")
    
    # Title
    title_label = tk.Label(window, text="Admin Dashboard", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)
    
    # Buttons
    tk.Button(window, text="Add New Book", command=add_book, width=20).pack(pady=5)
    tk.Button(window, text="Update Quantity", command=update_qty, width=20).pack(pady=5)
    tk.Button(window, text="View Books", command=view_books, width=20).pack(pady=5)
    
    # Close button
    def close_dashboard():
        window.destroy()
    
    tk.Button(window, text="Close", command=close_dashboard, width=20, bg="red", fg="white").pack(pady=20)
