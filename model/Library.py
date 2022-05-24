from library.Book import Book
from library.Floor import Floor


class Library:
    def __init__(self, ):
        self.floors = [Floor() for _ in range(3)]

    def add_book(self, title: str, author: str, floor_number: int, bookshelf_name: str, shelf_number: int):
        floor = self.floors[floor_number]
        bookshelf = floor.bookshelves[bookshelf_name]
        shelf = bookshelf.shelves[shelf_number - 1]
        if len(shelf.books) >= 10:
            raise Exception("Shelf full!")
        shelf.books.append(Book(title, author))

    def contains(self, floor_number: int, bookshelf_name: str, shelf_number: int) -> bool:
        floor = self.floors[floor_number]
        bookshelf = floor.bookshelves[bookshelf_name]
        shelf = bookshelf.shelves[shelf_number - 1]
        if len(shelf.books) > 0:
            return True
        else:
            return False

    def get_books(self, floor_number: int, bookshelf_name: str):
        floor = self.floors[floor_number]
        bookshelf = floor.bookshelves[bookshelf_name]
        for i, shelf in enumerate(bookshelf.shelves, 1):
            print(f"Shelf n.{i}:")
            for book in shelf.books:
                print(book.to_string())

    def search_book(self, title: str, author: str):
        for i, floor in enumerate(self.floors):
            for key, bookshelf in floor.bookshelves.items():
                for j, shelf in enumerate(bookshelf.shelves, 1):
                    for y, book in enumerate(shelf.books):
                        if book.title == title and book.author == author:
                            print(f"Book found! Floor: {i}, bookshelf: {key}, shelf: {j}")
                            return
        print("Book Not Found!")
