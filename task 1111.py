from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    price: float

    def sort_year(self):
        return sorted(self, key=lambda b: b.year)

    def __iter__(self):
        pass


books = [
    Book('Название1', 'Автор1', 2020, 850.43),
    Book('Название2', 'Автор12133', 1900, 1850.43),
    Book('Название3', 'Автор31', 1888, 450.43)
]


sorted_books = books[0].sort_year()
for book in sorted_books:
    print(book)
