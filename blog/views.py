# blog/views.py
from django.views.generic import ListView, DetailView # new
from django.shortcuts import render
from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'