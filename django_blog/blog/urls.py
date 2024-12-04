from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import PostCreateView,PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view, name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
