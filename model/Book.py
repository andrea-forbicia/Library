class Book:
    def __init__(self, title, author, shelf):
        self.title = title
        self.author = author
        self.shelf = shelf

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def to_string(self):
        return f"{self.get_title()}, {self.get_author()}"

    def get_floor(self):
        pass

    def get_bookshelf(self):
        pass

    def get_shelf(self):
        return self.shelf


