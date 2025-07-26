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
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3 and int(parts[0]) == sid:
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
    dashboard.geometry("500x500")

    tk.Label(dashboard, text=f"Welcome, {user['name']} ({user['stream']})", font=("Arial", 14, "bold")).pack(pady=10)

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
        name = entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter book name.")
            return
        if name not in books or books[name]['available'] <= 0:
            messagebox.showerror("Unavailable", "Book not available.")
            return
        # Check if already issued
        for book in issued_books:
            if book['book'] == name:
                messagebox.showerror("Already Issued", "You have already issued this book.")
                return
        
        now = int(time.time())
        due = now + 14*24*60*60
        issued_books.append({"book": name, "issue": now, "due": due})
        books[name]['available'] -= 1
        save_issued_books(sid, issued_books)
        save_books(books)
        messagebox.showinfo("Success", f"Issued '{name}' until {datetime.fromtimestamp(due).strftime('%d/%m/%Y')}")
        entry.delete(0, tk.END)
        refresh_issued_list()

    def return_book():
        name = entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter book name.")
            return
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
                entry.delete(0, tk.END)
                refresh_issued_list()
                return
        messagebox.showwarning("Not Found", "You haven't issued this book.")

    def view_available_books():
        books = load_books()
        available = [f"{name} (Available: {info['available']})" for name, info in books.items() if info['available'] > 0]
        if available:
            messagebox.showinfo("Available Books", "\n".join(available))
        else:
            messagebox.showinfo("Available Books", "No books available.")

    # Book name entry
    tk.Label(dashboard, text="Book Name:", font=("Arial", 12)).pack(pady=(20, 5))
    entry = tk.Entry(dashboard, width=30, font=("Arial", 11))
    entry.pack(pady=5)

    # Buttons
    button_frame = tk.Frame(dashboard)
    button_frame.pack(pady=10)
    
    tk.Button(button_frame, text="Issue Book", command=issue_book, width=15, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Return Book", command=return_book, width=15, bg="orange", fg="white").pack(side=tk.LEFT, padx=5)
    
    tk.Button(dashboard, text="View Available Books", command=view_available_books, width=20, bg="blue", fg="white").pack(pady=10)

    # Issued books list
    tk.Label(dashboard, text="Your Issued Books:", font=("Arial", 12, "bold")).pack(pady=(20, 5))
    listbox = tk.Listbox(dashboard, width=60, height=8)
    listbox.pack(pady=5)

    # Logout button
    def logout():
        dashboard.destroy()
    
    tk.Button(dashboard, text="Logout", command=logout, width=20, bg="red", fg="white").pack(pady=20)

    refresh_issued_list()
    dashboard.mainloop()
