from library.Shelf import Shelf


class Bookshelf:
    def __init__(self):
        self.shelves = [Shelf() for _ in range(6)]
