#LibraryMGMTapp

class Book:
    def __init__(self, title, author, isbn, publication_date, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__genre = genre
        self.__is_borrowed = False

    # Getters and setters
    def get_title(self): return self.__title
    def set_title(self, title): self.__title = title
    def get_author(self): return self.__author
    def set_author(self, author): self.__author = author
    def get_isbn(self): return self.__isbn
    def set_isbn(self, isbn): self.__isbn = isbn
    def get_publication_date(self): return self.__publication_date
    def set_publication_date(self, publication_date): self.__publication_date = publication_date
    def get_genre(self): return self.__genre
    def set_genre(self, genre): self.__genre = genre
    def is_borrowed(self): return self.__is_borrowed
    def borrow(self): self.__is_borrowed = True
    def return_book(self): self.__is_borrowed = False


class FictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, genre, fiction_type):
        super().__init__(title, author, isbn, publication_date, genre)
        self.__fiction_type = fiction_type

    def get_fiction_type(self):
        return self.__fiction_type

    def set_fiction_type(self, fiction_type):
        self.__fiction_type = fiction_type


class NonFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, genre, subject):
        super().__init__(title, author, isbn, publication_date, genre)
        self.__subject = subject

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters and setters
    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name
    def get_library_id(self): return self.__library_id
    def set_library_id(self, library_id): self.__library_id = library_id
    def get_borrowed_books(self): return self.__borrowed_books
    def borrow_book(self, book): self.__borrowed_books.append(book)
    def return_book(self, book): self.__borrowed_books.remove(book)


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and setters
    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name
    def get_biography(self): return self.__biography
    def set_biography(self, biography): self.__biography = biography


class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    # Getters and setters
    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name
    def get_description(self): return self.__description
    def set_description(self, description): self.__description = description
    def get_category(self): return self.__category
    def set_category(self, category): self.__category = category


class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self):
        try:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            publication_date = input("Enter publication date: ")
            genre = input("Enter genre: ")
            book = Book(title, author, isbn, publication_date, genre)
            self.books.append(book)
            print("Book added successfully.")
        except Exception as e:
            print(f"Error adding book: {e}")

    def borrow_book(self):
        try:
            isbn = input("Enter ISBN of the book to borrow: ")
            user_name = input("Enter your name: ")
            for book in self.books:
                if book.get_isbn() == isbn and not book.is_borrowed():
                    for user in self.users:
                        if user.get_name() == user_name:
                            book.borrow()
                            user.borrow_book(book)
                            print("Book borrowed successfully.")
                            return
            print("Book is not available or user not found.")
        except Exception as e:
            print(f"Error borrowing book: {e}")

    def return_book(self):
        try:
            isbn = input("Enter ISBN of the book to return: ")
            user_name = input("Enter your name: ")
            for book in self.books:
                if book.get_isbn() == isbn and book.is_borrowed():
                    for user in self.users:
                        if user.get_name() == user_name:
                            book.return_book()
                            user.return_book(book)
                            print("Book returned successfully.")
                            return
            print("Book is not borrowed or user not found.")
        except Exception as e:
            print(f"Error returning book: {e}")

    def display_books(self):
        try:
            for book in self.books:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_isbn()}, Availability: {'Borrowed' if book.is_borrowed() else 'Available'}")
        except Exception as e:
            print(f"Error displaying books: {e}")

    def add_user(self):
        try:
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user = User(name, library_id)
            self.users.append(user)
            print("User added successfully.")
        except Exception as e:
            print(f"Error adding user: {e}")

    def display_users(self):
        try:
            for user in self.users:
                print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}")
        except Exception as e:
            print(f"Error displaying users: {e}")

    def add_author(self):
        try:
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author = Author(name, biography)
            self.authors.append(author)
            print("Author added successfully.")
        except Exception as e:
            print(f"Error adding author: {e}")

    def display_authors(self):
        try:
            for author in self.authors:
                print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
        except Exception as e:
            print(f"Error displaying authors: {e}")

    def add_genre(self):
        try:
            name = input("Enter genre name: ")
            description = input("Enter genre description: ")
            category = input("Enter genre category: ")
            genre = Genre(name, description, category)
            self.genres.append(genre)
            print("Genre added successfully.")
        except Exception as e:
            print(f"Error adding genre: {e}")

    def display_genres(self):
        try:
            for genre in self.genres:
                print(f"Name: {genre.get_name()}, Description: {genre.get_description()}, Category: {genre.get_category()}")
        except Exception as e:
            print(f"Error displaying genres: {e}")

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Select an option: ")
            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.genre_operations()
            elif choice == '5':
                break
            else:
                print("Invalid option, please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.display_books()  # Assuming search is part of display
            elif choice == '5':
                self.display_books()
            elif choice == '6':
                break
            else:
                print("Invalid option, please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.display_users()  # Assuming view details is part of display
            elif choice == '3':
                self.display_users()
            elif choice == '4':
                break
            else:
                print("Invalid option, please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.display_authors()  # Assuming view details is part of display
            elif choice == '3':
                self.display_authors()
            elif choice == '4':
                break
            else:
                print("Invalid option, please try again.")

    def genre_operations(self):
        while True:
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_genre()
            elif choice == '2':
                self.display_genres()  # Assuming view details is part of display
            elif choice == '3':
                self.display_genres()
            elif choice == '4':
                break
            else:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.main_menu()
