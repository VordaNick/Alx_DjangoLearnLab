from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('database_books/', views.database_books, name='database_books'),
    path('library/<int:library_name>/books/', views.LibraryBooks.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
