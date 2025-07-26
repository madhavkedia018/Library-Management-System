import tkinter as tk
from tkinter import messagebox
import os
import time
from datetime import datetime

def load_books():
    books = {}
    if os.path.exists("books.txt"):
        with open("books.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, total, available = parts
                    books[name] = {"total": int(total), "available": int(available)}
    return books

def save_books(books):
    with open("books.txt", "w") as f:
        for name, info in books.items():
            f.write(f"{name},{info['total']},{info['available']}\n")

def get_student_data(sid):
    with open("students.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if int(parts[0]) == sid:
                return {"name": parts[1], "stream": parts[2]}
    return None

def get_issued_file(sid):
    return f"issued_{sid}.txt"

def load_issued_books(sid):
    issued = []
    file = get_issued_file(sid)
    if os.path.exists(file):
        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    issued.append({
                        "book": parts[0],
                        "issue": int(parts[1]),
                        "due": int(parts[2])
                    })
    return issued

def save_issued_books(sid, records):
    with open(get_issued_file(sid), "w") as f:
        for rec in records:
            f.write(f"{rec['book']},{rec['issue']},{rec['due']}\n")

def launch_dashboard(sid):
    user = get_student_data(sid)
    if not user:
        messagebox.showerror("Error", "Student data not found.")
        return

    dashboard = tk.Tk()
    dashboard.title(f"{user['name']}'s Dashboard")
    dashboard.geometry("400x400")

    tk.Label(dashboard, text=f"Welcome, {user['name']} ({user['stream']})", font=("Arial", 12)).pack(pady=10)

    issued_books = load_issued_books(sid)
    books = load_books()

    def refresh_issued_list():
        listbox.delete(0, tk.END)
        issued_books[:] = load_issued_books(sid)
        for book in issued_books:
            due = datetime.fromtimestamp(book['due']).strftime("%d/%m/%Y")
            listbox.insert(tk.END, f"{book['book']} (Due: {due})")

    def issue_book():
        if len(issued_books) >= 2:
            messagebox.showwarning("Limit", "You can issue only 2 books.")
            return
        name = entry.get()
        if name not in books or books[name]['available'] <= 0:
            messagebox.showerror("Unavailable", "Book not available.")
            return
        now = int(time.time())
        due = now + 14*24*60*60
        issued_books.append({"book": name, "issue": now, "due": due})
        books[name]['available'] -= 1
        save_issued_books(sid, issued_books)
        save_books(books)
        messagebox.showinfo("Success", f"Issued '{name}' until {datetime.fromtimestamp(due).strftime('%d/%m/%Y')}")
        refresh_issued_list()

    def return_book():
        name = entry.get()
        for rec in issued_books:
            if rec['book'] == name:
                now = int(time.time())
                fine = 0
                if now > rec['due']:
                    days_late = (now - rec['due']) // (60*60*24)
                    fine = days_late * 5
                issued_books.remove(rec)
                books[name]['available'] += 1
                save_issued_books(sid, issued_books)
                save_books(books)
                msg = f"Returned '{name}'."
                if fine > 0:
                    msg += f" Late by {days_late} days. Fine: Rs. {fine}"
                else:
                    msg += " Returned on time."
                messagebox.showinfo("Returned", msg)
                refresh_issued_list()
                return
        messagebox.showwarning("Not Found", "You haven't issued this book.")

    entry = tk.Entry(dashboard, width=30)
    entry.pack(pady=5)

    tk.Button(dashboard, text="Issue Book", command=issue_book).pack(pady=5)
    tk.Button(dashboard, text="Return Book", command=return_book).pack(pady=5)

    tk.Label(dashboard, text="Books Issued:").pack(pady=10)
    listbox = tk.Listbox(dashboard, width=50)
    listbox.pack()

    refresh_issued_list()
    dashboard.mainloop()
