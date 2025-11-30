import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATAFILES_DIR = os.path.join(BASE_DIR, "..", "DataFiles")

BOOKS_PATH = os.path.join(DATAFILES_DIR, "books.json")
STUDENTS_PATH = os.path.join(DATAFILES_DIR, "students.json")


class Library:

    def __init__(self):
        self.books = self.load_books()
        self.students = self.load_students()

    # ---------------------- LOAD SAVE ---------------------- #
    def load_students(self):
        try:
            with open(STUDENTS_PATH, "r") as f:
                return json.load(f)
        except:
            return []

    def load_books(self):
        try:
            with open(BOOKS_PATH, "r") as f:
                return json.load(f)
        except:
            return []

    def save_students(self):
        with open(STUDENTS_PATH, "w") as f:
            json.dump(self.students, f, indent=4)

    def save_books(self):
        with open(BOOKS_PATH, "w") as f:
            json.dump(self.books, f, indent=4)

    # ---------------------- SHOW BOOKS ---------------------- #
    def showBooks(self):
        if not self.books:
            print("\nNo Books Found!")
            return

        print("\n*** THE AVAILABLE BOOKS ARE ***\n")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book['BookName']} (ID: {book['BookId']}) Author: {book['Author']}")

    # ---------------------- ADD STUDENT ---------------------- #
    def add_student(self, name, Class, email):

        # Duplicate Check
        for s in self.students:
            if s["Name"].lower() == name.lower() and s["email"] == email:
                print("❌ Student already exists!")
                return

        student = {
            "Name": name,
            "Class": Class,
            "email": email,
            "Borrowed": []
        }

        self.students.append(student)
        self.save_students()
        print("✅ Student Added Successfully!")

    # ---------------------- DELETE STUDENT ---------------------- #
    def delete_student(self, name, Class, email):

        before = len(self.students)
        self.students = [
            s for s in self.students
            if not (s["Name"] == name and s["Class"] == Class and s["email"] == email)
        ]

        self.save_students()

        if len(self.students) < before:
            print("✅ Student deleted successfully!")
        else:
            print("❌ Student not found!")

    # ---------------------- SHOW STUDENTS ---------------------- #
    def show_students(self):
        if not self.students:
            print("No Students Found!")
            return

        print("\n*** OUR MEMBERS ARE ***\n")
        for s in self.students:
            print(f"Name: {s['Name']}, Class: {s['Class']}, Email: {s['email']}")

    # ---------------------- ADD BOOK ---------------------- #
    def add_book(self, bookName, bookId, Author):

        for b in self.books:
            if b["BookId"] == bookId or b["BookName"].lower() == bookName.lower():
                print("❌ Book already exists!")
                return

        book = {
            "BookName": bookName,
            "BookId": bookId,
            "Author": Author
        }

        self.books.append(book)
        self.save_books()
        print("✅ Book Added Successfully!")

    # ---------------------- REMOVE BOOK ---------------------- #
    def remove_book(self, bookName, bookId, Author):

        before = len(self.books)

        self.books = [
            b for b in self.books
            if not (b["BookName"] == bookName and b["BookId"] == bookId and b["Author"] == Author)
        ]

        self.save_books()

        if len(self.books) < before:
            print("✅ Book deleted successfully!")
        else:
            print("❌ Book not found!")

    # ---------------------- SEARCH BOOK ---------------------- #
    def search_book(self, keyword):
        keyword = keyword.lower()

        for book in self.books:
            if book["BookId"].lower() == keyword or book["BookName"].lower() == keyword:
                print("\n✅ Book Found:")
                print(f"Name: {book['BookName']}")
                print(f"ID:   {book['BookId']}")
                print(f"Author: {book['Author']}")
                return

        print("❌ Book not found!")

    # ---------------------- BORROW BOOK ---------------------- #
    def borrow_book(self, student_name, bookId):

        # Student find
        student = None
        for s in self.students:
            if s["Name"].lower() == student_name.lower():
                student = s
                break

        if not student:
            print("❌ Student not found!")
            return

        # Book find
        book = None
        for b in self.books:
            if b["BookId"] == bookId:
                book = b
                break

        if not book:
            print("❌ Book not available!")
            return

        # Add to student
        student["Borrowed"].append(book)

        # Remove from library stock
        self.books = [b for b in self.books if b["BookId"] != bookId]

        self.save_books()
        self.save_students()

        print("✅ Book Borrowed Successfully!")

    # ---------------------- RETURN BOOK ---------------------- #
    def return_book(self, student_name, bookId):

        # Student find
        student = None
        for s in self.students:
            if s["Name"].lower() == student_name.lower():
                student = s
                break

        if not student:
            print("❌ Student not found!")
            return

        # Check if student borrowed this book
        borrowed_book = None
        for b in student["Borrowed"]:
            if b["BookId"] == bookId:
                borrowed_book = b
                break

        if not borrowed_book:
            print("❌ This book is not borrowed by the student!")
            return

        # Remove from student's list
        student["Borrowed"] = [b for b in student["Borrowed"] if b["BookId"] != bookId]

        # Add book back to library
        self.books.append(borrowed_book)

        self.save_books()
        self.save_students()

        print("✅ Book Returned Successfully!")