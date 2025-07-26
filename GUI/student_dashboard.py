# student_dashboard.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import read_books, write_books
from datetime import datetime, timedelta
import os
import json

ISSUE_FILE = "issue_data.json"

def load_issues():
    if os.path.exists(ISSUE_FILE):
        with open(ISSUE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_issues(data):
    with open(ISSUE_FILE, 'w') as f:
        json.dump(data, f)

def StudentDashboard(root, sid, name):
    window = tk.Toplevel(root)
    window.title(f"Welcome {name}")

    issues = load_issues()
    sid = str(sid)
    if sid not in issues:
        issues[sid] = []

    def issue_book():
        if len(issues[sid]) >= 2:
            messagebox.showwarning("Limit", "Can't issue more than 2 books.")
            return
        book = simpledialog.askstring("Issue", "Enter book name:")
        books = read_books()
        if book not in books or books[book]["available"] <= 0:
            messagebox.showerror("Unavailable", "Book not available.")
            return
        books[book]["available"] -= 1
        now = datetime.now()
        due = now + timedelta(days=14)
        issues[sid].append({
            "book": book,
            "issued_at": now.isoformat(),
            "due": due.isoformat()
        })
        save_issues(issues)
        write_books(books)
        messagebox.showinfo("Issued", f"Issued '{book}'\nDue: {due.strftime('%d/%m/%Y')}")

    def return_book():
        book = simpledialog.askstring("Return", "Enter book name to return:")
        for i, b in enumerate(issues[sid]):
            if b["book"] == book:
                now = datetime.now()
                due = datetime.fromisoformat(b["due"])
                days_late = (now - due).days
                fine = max(0, days_late * 5)
                issues[sid].pop(i)
                save_issues(issues)
                books = read_books()
                books[book]["available"] += 1
                write_books(books)
                if fine > 0:
                    messagebox.showinfo("Returned", f"Returned late. Fine: Rs. {fine}")
                else:
                    messagebox.showinfo("Returned", "Returned on time. No fine.")
                return
        messagebox.showerror("Not Found", "Book not issued.")

    tk.Button(window, text="Issue Book", command=issue_book).pack(pady=10)
    tk.Button(window, text="Return Book", command=return_book).pack(pady=10)
