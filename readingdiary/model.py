from datetime import datetime

class Nota:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.date: datetime = date
        self.page: int = page

    def __str__(self):
        return f'{self.text} {self.date} {self.page}'

class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1
    def __init__(self, text: str, pages: int, isbn: str, title: str, author: str):
        self.text: str = text
        self.pages: int = pages
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.rating : int = Book.UNRATED
        self.notes : list[Nota] = []




