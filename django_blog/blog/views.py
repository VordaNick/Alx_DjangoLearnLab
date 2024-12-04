from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post-list')
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author