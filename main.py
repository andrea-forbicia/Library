from library.Library import Library

library = Library()

try:
    library.add_book(title="title1", author="author1", floor_number=2, bookshelf_name="SC22", shelf_number=1)
except Exception:
    print("Shelf if full!")
try:
    library.add_book(title="title2", author="author2", floor_number=2, bookshelf_name="SC22", shelf_number=2)
except Exception:
    print("Shelf if full!")
try:
    library.add_book(title="title3", author="author3", floor_number=2, bookshelf_name="SC22", shelf_number=1)
except Exception:
    print("Shelf if full!")

print(library.contains(floor_number=2, bookshelf_name="SC22", shelf_number=5))

library.get_books(floor_number=2, bookshelf_name="SC22")

library.search_book(title="title1", author="author1")
