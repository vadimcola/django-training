from django.forms import FileField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import *

from main.models import *


class ProductListView(ListView):
    model = Product


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'picture', 'is_published')
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'picture', 'is_published')
    success_url = reverse_lazy('blog_list')
