from project.user import User
from project.library import  Library

class Registration:

    @staticmethod
    def add_user(user: User, library: Library): #static method does not need self
        if any(u.user_id == user.user_id for u in library.user_records): #returns true if ther is any match ofr the user in the  liubraty users
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        return None

    @staticmethod
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            if user.username in library.rented_books.keys():
                del library.rented_books[user.username]
            return  None
        return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        pass

