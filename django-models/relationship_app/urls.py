from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('database_books/', views.database_books, name='database_books'),
    path('library/<int:library_name>/books/', views.LibraryBooks.as_view(), name='library_detail'),
]
