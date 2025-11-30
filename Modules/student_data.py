import json
import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Library import Library 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATAFILES_DIR = os.path.join(BASE_DIR, "..", "DataFiles")
STUDENTS_PATH = os.path.join(DATAFILES_DIR, "students.json")
BOOKS_PATH = os.path.join(DATAFILES_DIR, "books.json")


class StudentPortal:

    def __init__(self):
        self.lib = Library()     # Library ko connect kiya
        self.current_student = None

    # -------------------- LOGIN -------------------- #
    def login(self):
        name = input("Enter Your Name: ")
        email = input("Enter Your Email: ")

        for s in self.lib.students:
            if s["Name"].lower() == name.lower() and s["email"] == email:
                self.current_student = s
    
                # FIX: add Borrowed key if missing
                if "Borrowed" not in self.current_student:
                    self.current_student["Borrowed"] = []
                    self.lib.save_students()
    
                print(f"\n🎉 Welcome {s['Name']}!")
                self.dashboard()
                return
    
        print("❌ Invalid name or email!")
    
    # -------------------- DASHBOARD -------------------- #
    def dashboard(self):
        while True:
            print("\n===== STUDENT DASHBOARD =====")
            print("1. Borrow a Book")
            print("2. Return a Book")
            print("3. My Borrowed Books")
            print("4. Search Book")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.borrow_ui()

            elif choice == "2":
                self.return_ui()

            elif choice == "3":
                self.show_my_books()

            elif choice == "4":
                keyword = input("Enter Book ID or name: ")
                self.lib.search_book(keyword)

            elif choice == "5":
                print("Logging out...")
                break

            else:
                print("Invalid choice!")

    # -------------------- BORROW BOOK (UI) -------------------- #
    def borrow_ui(self):
        bookId = input("Enter Book ID to borrow: ")
        self.lib.borrow_book(self.current_student["Name"], bookId)

        # Update local data
        self.lib = Library()

    # -------------------- RETURN BOOK (UI) -------------------- #
    def return_ui(self):
        bookId = input("Enter Book ID to return: ")
        self.lib.return_book(self.current_student["Name"], bookId)

        # Update local data
        self.lib = Library()

    # -------------------- SHOW MY BORROWED BOOKS -------------------- #
    def show_my_books(self):
        print("\n📚 Your Borrowed Books:\n")

        if not self.current_student["Borrowed"]:
            print("You have not borrowed any books!")
            return

        for i, b in enumerate(self.current_student["Borrowed"], start=1):
            print(f"{i}. {b['BookName']} (ID: {b['BookId']})")