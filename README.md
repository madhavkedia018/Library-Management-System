# Library-Management-System

A console-based Library Management System implemented in C++ with support for student and librarian roles, binary search tree-based book catalog, issue/return logic, due date tracking, and fine calculation.

---

##  Features

- **Role-Based Access**  
  ➤ Librarian: Add/update/view books  
  ➤ Student: Issue/return books (max 2 at a time)

- **Binary Search Tree (BST)**  
  ➤ Books stored and retrieved using an in-order BST for efficient alphabetical access

- **Book Inventory Management**  
  ➤ Tracks total and available quantity per book  
  ➤ Uses `unordered_map` for real-time access and updates

- **Issue and Return Logic**  
  ➤ On book issue: current timestamp + 2 weeks = due date  
  ➤ On book return: compares with due date  
  ➤ If overdue, fine = ₹5 per day 

- **Clean Data Structures**  
  ➤ `BookInfo`, `BookIssueRecord`, and `Student` structs  
  ➤ Modular functions and clear separation of concerns

