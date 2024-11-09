from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView
# Create your views here.
def database_books(request):
    book = Book.objects.all()
    context = {
        'books' : books,
    }
    return(render, 'relationship_app/list_books.html', context)

class LibraryBooks(ListView):
    model = Book
    template_name = 'library_detail.html'
    context_object_name = 'books'
    def library_name(self):
        library = self.kwargs['library_name']
        return Book.objects.filter(library_name=library_name)