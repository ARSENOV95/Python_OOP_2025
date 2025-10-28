class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: list[str] = []

    def info(self) -> str:
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}  # {author: [book_name1, book_name2, ...]}
        self.rented_books: dict[str, dict[str, int]] = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        # If the book is available under the author
        if author in self.books_available and book_name in self.books_available[author]:
            # remove from available
            self.books_available[author].remove(book_name)
            # add to user's books
            user.books.append(book_name)
            # record the rental
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        # If the book is already rented, find who rented it and return remaining days
        for username, books in self.rented_books.items():
            if book_name in books:
                days_left = books[book_name]
                return f'The book "{book_name}" is already rented and will be available in {days_left} days!'

        # If the book is neither available nor recorded as rented, do nothing (returns None)
        return None

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available.setdefault(author, []).append(book_name)

            if user.username in self.rented_books and book_name in self.rented_books[user.username]:
                del self.rented_books[user.username][book_name]
                # if not self.rented_books[user.username]:
                #     del self.rented_books[user.username]
            return None

        return f"{user.username} doesn't have this book in his/her records!"


from project.user import User
from project.library import Library


class Registration:

    @staticmethod
    def add_user(user: User, library: Library):
        if any(u.user_id == user.user_id for u in library.user_records):
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        return None

    @staticmethod
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            if user.username in library.rented_books:
                del library.rented_books[user.username]
            return None
        return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                old_username = user.username
                user.username = new_username

                if old_username in library.rented_books:
                    old_rentals = library.rented_books.pop(old_username)
                    if new_username in library.rented_books:
                        library.rented_books[new_username].update(old_rentals)
                    else:
                        library.rented_books[new_username] = old_rentals

                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"