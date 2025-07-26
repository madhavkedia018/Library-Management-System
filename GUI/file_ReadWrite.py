# utils.py
import os
from datetime import datetime, timedelta

BOOK_FILE = "books.txt"
STUDENT_FILE = "students.txt"

def read_books():
    books = {}
    if not os.path.exists(BOOK_FILE):
        return books
    with open(BOOK_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name, total, available = parts
                books[name] = {"total": int(total), "available": int(available)}
    return books

def write_books(books):
    with open(BOOK_FILE, 'w') as f:
        for name, info in books.items():
            f.write(f"{name},{info['total']},{info['available']}\n")

def read_students():
    students = {}
    if not os.path.exists(STUDENT_FILE):
        return students
    with open(STUDENT_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                sid, name, stream = parts
                students[int(sid)] = {"name": name, "stream": stream}
    return students

def write_students(students):
    with open(STUDENT_FILE, 'w') as f:
        for sid, info in students.items():
            f.write(f"{sid},{info['name']},{info['stream']}\n")
