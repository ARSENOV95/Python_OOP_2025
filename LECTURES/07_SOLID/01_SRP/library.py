class Library:
    def __init__(self,title :str,author :str,location :str):
        self.title = title
        self.author = author
        self.location = location

    def find_book(self,title):
        if self.title == title:
            return self.location
