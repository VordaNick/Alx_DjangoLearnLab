from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'List.html'
    context_object_name = 'books'
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'Detail.html'
    context_object_name = 'book'
    
class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    template_name = 'Form.html'
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('List')

class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    template_name = 'Form.html'
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('List')
    
class BookDeleteView(LoginRequiredMixin,DeleteView):
    model = Book
    template_name = 'Delete.html'
    success_url = reverse_lazy('List')