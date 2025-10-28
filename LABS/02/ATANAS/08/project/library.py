from project.user import User

class Library:
    def __init__(self):
        self.user_records:list[User] = []
        self.books_available:dict[str,list[str]] = {} #annotating the contets of dictionary
        self.rented_books:dict[str,dict[str,int]] = {}

    def get_book(self,author: str, book_name: str, days_to_return: int, user: User):
        if self.books_available.get(author):
            if book_name in self.books_available[author]:
                self.books_available[author].remove(book_name)
