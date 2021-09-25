from typing import List


def osztaly_atlagok(osztalyzatok: List) -> float:
  return sum(osztalyzatok) / len(osztalyzatok)


# osztaly_atlagok(23)


class Book:
  pass


class BookShelf:
  def __init__(self, books: List[Book]):
    self.books = books


book1: Book = Book()

my_shelf = BookShelf([book1])
type(book1)