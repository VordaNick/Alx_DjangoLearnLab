from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import (PostCreateView,
                    PostDeleteView, 
                    PostDetailView, 
                    PostListView, 
                    PostUpdateView, 
                    CommentCreateView, 
                    CommentDeleteView, 
                    CommentUpdateView, 
                    TaggedPostListView,
                    PostByTagListView)

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
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('tag/<str:tag_name>/', TaggedPostListView.as_view(), name='tagged_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_search')
]
