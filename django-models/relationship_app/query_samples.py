author = Author.objects.get(name=author_name)
Books = author.books.all()
print(Books)

Library = Library.objects.get(name=library_name)
Books = library.books.all()
print(Books)

Librarian = library.objects.get(name=library_name)
Librarian = library.librarian
print(Librarian)