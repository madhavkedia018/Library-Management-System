
import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import read_books, write_books

def AdminDashboard(root):
    window = tk.Toplevel(root)
    window.title("Admin Panel")

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

    tk.Button(window, text="Add New Book", command=add_book).pack(pady=5)
    tk.Button(window, text="Update Quantity", command=update_qty).pack(pady=5)
    tk.Button(window, text="View Books", command=view_books).pack(pady=5)
