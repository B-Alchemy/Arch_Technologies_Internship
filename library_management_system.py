# ======= Library List =======
library = []

# ======= Show Menu =======
def show_menu():
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Search Book")
    print("8. Exit")

# ======= Add Book =======
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book = {'Title': title, 'Author': author, 'Available': True}
    library.append(book)
    print(f"\nBook '{title}' added successfully!")

# ======= View All Books =======
def view_books():
    if not library:
        print("\nNo books in the library.")
    else:
        print("\n--- List of Books ---")
        for i, book in enumerate(library, start=1):
            status = "Available" if book['Available'] else "Borrowed"
            print(f"{i}. {book['Title']} by {book['Author']} - {status}")

# ======= Update Book =======
def update_book():
    if not library:
        print("\nNo books available to update.")
        return

    view_books()
    try:
        book_num = int(input("\nEnter the book number to update: ")) - 1
        if 0 <= book_num < len(library):
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            library[book_num]['Title'] = title
            library[book_num]['Author'] = author
            print("\nBook updated successfully!")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# ======= Delete Book =======
def delete_book():
    if not library:
        print("\nNo books to delete.")
        return

    view_books()
    try:
        book_num = int(input("\nEnter the book number to delete: ")) - 1
        if 0 <= book_num < len(library):
            removed = library.pop(book_num)
            print(f"\nBook '{removed['Title']}' deleted successfully!")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# ======= Borrow Book =======
def borrow_book():
    if not library:
        print("\nNo books to borrow.")
        return

    view_books()
    try:
        book_num = int(input("\nEnter the book number to borrow: ")) - 1
        if 0 <= book_num < len(library):
            if library[book_num]['Available']:
                library[book_num]['Available'] = False
                print(f"\nYou borrowed '{library[book_num]['Title']}'.")
            else:
                print("Sorry, that book is already borrowed.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# ======= Return Book =======
def return_book():
    if not library:
        print("\nNo books to return.")
        return

    view_books()
    try:
        book_num = int(input("\nEnter the book number to return: ")) - 1
        if 0 <= book_num < len(library):
            if not library[book_num]['Available']:
                library[book_num]['Available'] = True
                print(f"\nYou returned '{library[book_num]['Title']}'.")
            else:
                print("This book was not borrowed.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# ======= Search Book =======
def search_book():
    if not library:
        print("\nNo books in the library.")
        return

    keyword = input("\nEnter keyword to search (title/author): ").lower()
    found = False
    for book in library:
        if keyword in book['Title'].lower() or keyword in book['Author'].lower():
            status = "Available" if book['Available'] else "Borrowed"
            print(f"Found: {book['Title']} by {book['Author']} - {status}")
            found = True
    if not found:
        print("No matching books found.")

# ======= Main Program Loop =======
while True:
    show_menu()
    choice = input("\nEnter your choice (1-8): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        update_book()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        borrow_book()
    elif choice == '6':
        return_book()
    elif choice == '7':
        search_book()
    elif choice == '8':
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
