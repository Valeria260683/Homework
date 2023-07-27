# В папке "classes" создадим файл "book.py" и опишем
# в нем класс "Book" с различными атрибутами:
class Book:
    def __init__(self):
        self.title: str = ""
        self.author: str = ""
        self.publication_year: int = 0
        self.is_fiction: bool = False
        self.genres: list[str] = []