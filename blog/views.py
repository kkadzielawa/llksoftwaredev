from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class BlogPageView(ListView):
    template_name = 'blog.html'
    model = Post
    
class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = Post