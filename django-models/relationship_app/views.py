from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
# Create your views here.
def database_books(request):
    book = Book.objects.all()
    context = {
        'books' : Book
    }
    return(render, 'relationship_app/list_books.html', context)

class LibraryBooks(DetailView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'
    def library_name(self):
        library = self.kwargs['library_name']
        return Book.objects.filter(library_name='library_name')
    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})
            
