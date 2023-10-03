from textwrap import dedent


def display_books(books):
    print("List of all books")
    for book in books:
        for k, v in book.items():
            print(f"{k}: {v}")
        print("=" * 20)


def add_book_prompt():
    id = input("Enter book ID: ")
    title = input("Enter book title: ")
    return {"id": id, "title": title}


def add_book(books, new_book):
    new_books = books[:]
    new_books.append(new_book)
    return new_books


def borrow_book_prompt(books, borrower, name):
    print("List of available books:")
    available_books = []
    for book in books:
        book_id = book["id"]
        if book_id not in borrower.get(name, []):
            available_books.append(book_id)
            print(f"Book ID: {book_id}, Title: {book['title']}")

    if not available_books:
        print("No available books to borrow.")
        return None

    while True:
        book_id = input("Enter the ID of the book you want to borrow: ")
        if book_id in available_books:
            return {"name": name, "book_id": book_id}
        else:
            print("Invalid book ID. Please choose a valid book.")


def borrow_book(borrower, new_borrower):
    new_borrowers = borrower
    name = new_borrower["name"]
    book_id = new_borrower["book_id"]
    if name in new_borrowers:
        new_borrowers[name].append(book_id)
    else:
        new_borrowers[name] = [book_id]
    return new_borrowers


def return_book_prompt(borrowers, name):
    if name in borrowers and borrowers[name]:
        print(f"{name}'s borrowed books:")
        for book_id in borrowers[name]:
            print(f"Book ID: {book_id}")

        while True:
            returned_book_id = input("Enter the ID of the book you want to return: ")
            if returned_book_id in borrowers[name]:
                updated_borrower = borrowers
                updated_borrower[name].remove(returned_book_id)
                return updated_borrower
            else:
                print("Invalid book ID. Please choose a valid book to return.")
    else:
        print(f"{name} has no books to return.")
        return None


def return_book(borrowers, returned_book):
    new_borrowers = borrowers
    new_borrowers.update(returned_book)
    return new_borrowers


def main():
    books = [
        {"id": "001", "title": "Cosmos - Carl Sagan"},
        {"id": "002", "title": "Homo Deus - Harari"},
        {"id": "003", "title": "The Art of War"},
    ]

    borrowers = {}

    while True:
        account = input("Login as [admin/user/cancel]: ").lower()

        if account == "admin":
            choice = input(
                dedent(
                    """\
                    Admin Menu:
                    1. Add a book
                    2. View books
                    choose: """
                )
            )

            if choice == "1":
                new_book = add_book_prompt()
                books = add_book(books, new_book)
            elif choice == "2":
                display_books(books)
            else:
                print("Not a valid choice")
        elif account == "user":
            name = input("What's your name? ")
            choice = input(
                f"Hi {name}, What do you want to do?\n"
                "1. Borrow a book\n"
                "2. Return a book\n"
                "3. View your borrowed books\n"
                "choose: "
            )

            if choice == "1":
                new_borrower = borrow_book_prompt(books, borrowers, name)
                if new_borrower:
                    borrowers = borrow_book(borrowers, new_borrower)
            elif choice == "2":
                new_borrower = return_book_prompt(borrowers, name)
                if new_borrower:
                    borrowers = return_book(borrowers, new_borrower)
            elif choice == "3":
                if name in borrowers and borrowers[name]:
                    print(f"You borrowed these books:")
                    for book_id in borrowers[name]:
                        for book in books:
                            if book["id"] == book_id:
                                print(f"Book ID: {book_id}, Title: {book['title']}")
                else:
                    print(f"{name} has no borrowed books.")
            else:
                print("Not a valid choice")
        elif account == "cancel":
            break
        else:
            print("Input is not valid")


if __name__ == "__main__":
    main()
