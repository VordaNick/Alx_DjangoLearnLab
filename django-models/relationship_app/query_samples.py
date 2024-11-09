Author = Author.objects.get(name=author_name)
Books = Author.objects.filter(author=author)
print(Books)

Library = Library.objects.get(name=library_name)
Books = library.books.all()
print(Books)

Librarian = library.objects.get(name=library_name)
Librarian = library.librarian
print(Librarian)