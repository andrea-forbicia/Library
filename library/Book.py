class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def to_string(self):
        return f"{self.get_title()}, {self.get_author()}"

    def get_shelf(self, library):
        pass

    def get_bookshelf(self, library):
        pass

    def get_floor(self, library):
        pass
