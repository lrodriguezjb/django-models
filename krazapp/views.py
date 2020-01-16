from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy


from .models import Post

class HomePage(ListView):
    template_name = 'home.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts_detail.html'
    model = Post

class BlogCreateView(CreateView):
    model= Post
    template_name = 'post_new.html'
    fields = ['title','author', 'body']

class BlogUpdateView(UpdateView):
    model= Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    template_name = 'delete_post.html'
    model = Post
    success_url = reverse_lazy('home')