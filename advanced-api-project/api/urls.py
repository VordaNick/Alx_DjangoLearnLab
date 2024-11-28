from django.urls import path
from .views import BookListView,BookDetailView,BookCreateView,BookUpdateView,BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='List'),
    path('<int:pk>/', BookDetailView.as_view(), name='Detail'),
    path('Create/', BookCreateView.as_view(), name='Create'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='Update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='Delete'),
]
