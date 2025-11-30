import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "Modules")

if MODULES_DIR not in sys.path:
    sys.path.append(MODULES_DIR)

from Library import Library
from student_data import StudentPortal

def main():
    lib = Library()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Show all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Search a book")
        print("5. Show all students")
        print("6. Add a student")
        print("7. Remove a student")
        print("8. Borrow a book")
        print("9. Return a book")
        print("10. Student Login")
        print("11. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            lib.showBooks()

        elif choice == "2":
            name = input("Book Name: ")
            book_id = input("Book ID: ")
            author = input("Author: ")
            lib.add_book(name, book_id, author)

        elif choice == "3":
            name = input("Book Name to remove: ")
            book_id = input("Book ID: ")
            author = input("Author: ")
            lib.remove_book(name, book_id, author)

        elif choice == "4":
            keyword = input("Enter Book ID or Book Name: ")
            lib.search_book(keyword)

        elif choice == "5":
            lib.show_students()

        elif choice == "6":
            name = input("Student Name: ")
            Class = input("Class: ")
            email = input("Email: ")
            lib.add_student(name, Class, email)

        elif choice == "7":
            name = input("Student Name to remove: ")
            Class = input("Class: ")
            email = input("Email: ")
            lib.delete_student(name, Class, email)

        elif choice == "8":
            student = input("Student Name: ")
            bookId = input("Book ID: ")
            lib.borrow_book(student, bookId)

        elif choice == "9":
            student = input("Student Name: ")
            bookId = input("Book ID: ")
            lib.return_book(student, bookId)

        elif choice == "10":
            portal = StudentPortal()
            portal.login()
            
        elif choice == "11":
            print("Exiting...")
            break;


        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()