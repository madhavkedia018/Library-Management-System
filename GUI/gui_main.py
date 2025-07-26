import tkinter as tk
from admin_login import AdminLogin
from student_login import StudentLogin

def main():
    root = tk.Tk()
    root.title("Library Management System")

    tk.Label(root, text="Welcome to Library System", font=("Helvetica", 16)).pack(pady=20)

    tk.Button(root, text="Librarian Login", width=20, command=lambda: AdminLogin(root)).pack(pady=10)
    tk.Button(root, text="Student Login", width=20, command=lambda: StudentLogin(root)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
