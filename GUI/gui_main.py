import tkinter as tk
from admin_login import open_admin_login
from student_login import open_student_login

def main_gui():
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("350x250")
    root.resizable(False, False)

    label = tk.Label(root, text="Library System", font=("Helvetica", 16, "bold"))
    label.pack(pady=20)

    admin_btn = tk.Button(root, text="Admin Login", width=20, height=2, command=lambda: open_admin_login(root))
    admin_btn.pack(pady=10)

    student_btn = tk.Button(root, text="Student Login", width=20, height=2, command=lambda: open_student_login(root))
    student_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
