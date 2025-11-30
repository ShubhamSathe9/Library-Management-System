# 📘 Library Management System (Python + JSON)

A lightweight and beginner-friendly Library Management System built using Python with JSON-based storage instead of a database. It supports book management, student management, borrowing/returning flow, and a student login dashboard — all with clean, modular code.

## ✨ Features

### 🔹 Book Management
- Add new books
- Remove books
- Search books by ID or name
- View all available books

### 🔹 Student Management
- Add students
- Remove students
- View all students
- JSON auto-update for Borrowed books

### 🔹 Borrow/Return System
- Students can borrow books (removed from library stock)
- Students can return books (added back to library stock)
- Auto-creates Borrowed list if missing

### 🔹 Student Login Portal
- Login using name + email
- Personal dashboard
- View your borrowed books
- Borrow and return directly from dashboard

## 📁 Project Structure

Library-Management-System/
│
├── main.py
├── Modules/
│   ├── Library.py
│   └── student_data.py
│
└── DataFiles/
    ├── books.json
    └── students.json

## 🚀 How to Run

1. Clone the repository
   git clone https://github.com/YOUR_USERNAME/Library-Management-System.git
   cd Library-Management-System

2. Run the program
   python main.py

Works on both PC and Android (Pydroid 3).

## 🛠 Technologies Used
- Python
- JSON
- File Handling
- OOP
- Modular Programming

## 🔮 Future Improvements
- Admin Login System
- Fine/Overdue System
- Multiple copies of a book
- Book categories & filters
- GUI (Tkinter / Web UI)
- Export reports

## 📄 License
MIT License

## ❤️ Author
Shubham — built for learning file handling and OOP in Python.
