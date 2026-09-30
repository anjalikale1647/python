

library = {}

def add_book():
    book_id = input("Enter Book ID: ")

    if book_id in library:
        print("Book already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = input("Enter Publication Year: ")

    library[book_id] = {
        "title": title,
        "author": author,
        "year": year
    }

    print("Book added successfully!")


def view_books():
    if not library:
        print("No books available.")
        return

    print("\n--- Library Books ---")
    for book_id, details in library.items():
        print("Book ID:", book_id)
        print("Title:", details["title"])
        print("Author:", details["author"])
        print("Year:", details["year"])
        print("--------------------")


def update_book():
    book_id = input("Enter Book ID to update: ")

    if book_id not in library:
        print("Book not found!")
        return

    print("Leave blank if you don't want to change a detail.")

    title = input("Enter new title: ")
    author = input("Enter new author: ")
    year = input("Enter new publication year: ")

    if title:
        library[book_id]["title"] = title
    if author:
        library[book_id]["author"] = author
    if year:
        library[book_id]["year"] = year

    print("Book updated successfully!")


def delete_book():
    book_id = input("Enter Book ID to delete: ")

    if book_id in library:
        del library[book_id]
        print("Book deleted successfully!")
    else:
        print("Book not found!")



while True:
    print("\n===== Library Book Record System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")