from django.urls import path
from . import views
urlpatterns = [
    path('database_books/', views.database_books, name='database_books'),
    path('library/<int:library_name>/books/', views.LibraryBooks.as_view(), name='library_detail'),
]
