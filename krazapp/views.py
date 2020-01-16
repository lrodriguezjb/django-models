from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView

from .models import Post

class HomePage(ListView):
    template_name = 'home.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts_detail.html'
    model = Post