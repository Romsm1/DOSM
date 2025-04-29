from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    price: float


books = [
    Book('Название1', 'Автор1', 2020, 850.43),
    Book('Название2', 'Автор12133', 1900, 1850.43),
    Book('Название3', 'Автор31', 1888, 50.43)
]


def get_year(book):
    return book.year


books.sort(key=get_year)

for book in books:
    print(book)
