from library.Bookshelf import Bookshelf


class Floor:
    def __init__(self):
        self.bookshelves = {f"SC{i}": Bookshelf() for i in range(1, 31)}
