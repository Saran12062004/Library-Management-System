class LibraryManagementSystem:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        genre = input("Enter book genre: ").strip()
        
        book = {
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Status": "Available"
        }
        self.books.append(book)
        print(f"Book '{title}' by {author} has been added successfully!\n")

    def view_books(self):
        if not self.books:
            print("No books in the library.\n")
            return

        print("====== Library Books ======")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")
        print("===========================\n")

    def search_book(self):
        title = input("Enter the title of the book to search: ").strip()
        
        for book in self.books:
            if book["Title"].lower() == title.lower():
                print(f"Book found: Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}\n")
                return
        print(f"Book '{title}' not found in the library.\n")

    def borrow_book(self):
        title = input("Enter the title of the book to borrow: ").strip()

        for book in self.books:
            if book["Title"].lower() == title.lower():
                if book["Status"] == "Available":
                    book["Status"] = "Borrowed"
                    print(f"You have successfully borrowed the book '{title}'.\n")
                else:
                    print(f"The book '{title}' is already borrowed.\n")
                return
        print(f"Book '{title}' not found in the library.\n")

    def return_book(self):
        title = input("Enter the title of the book to return: ").strip()

        for book in self.books:
            if book["Title"].lower() == title.lower():
                if book["Status"] == "Borrowed":
                    book["Status"] = "Available"
                    print(f"You have successfully returned the book '{title}'.\n")
                else:
                    print(f"The book '{title}' is not currently borrowed.\n")
                return
        print(f"Book '{title}' not found in the library.\n")

    def menu(self):
        while True:
            print("====== Library Management System ======")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Search Book by Title")
            print("4. Borrow Book")
            print("5. Return Book")
            print("6. Exit")
            print("=======================================")

            try:
                choice = int(input("Enter your choice (1-6): ").strip())
                print()
                if choice == 1:
                    self.add_book()
                elif choice == 2:
                    self.view_books()
                elif choice == 3:
                    self.search_book()
                elif choice == 4:
                    self.borrow_book()
                elif choice == 5:
                    self.return_book()
                elif choice == 6:
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 6.\n")
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.menu()
