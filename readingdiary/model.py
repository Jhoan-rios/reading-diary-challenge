from datetime import datetime
from operator import truediv


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

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        else:
            note = Nota(text, page, date)
            self.notes.append(note)
            return True

    def set_rating(self, rating: int) -> bool:
        if rating not in [Book.EXCELLENT, Book.GOOD, Book.BAD]:
            return  False
        else:
            self.rating = rating
            return True

    def get_note_of_page(self, page: int) -> list[Nota]:
        notes_of_page = list[Nota] = []
        for note in self.notes:
            if note.page == page:
                notes_of_page.append(note)
        return  notes_of_page





