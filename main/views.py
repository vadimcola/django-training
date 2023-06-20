from django.forms import FileField
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import *

from main.models import Product, Blog


class ProductListView(generic.ListView):
    model = Product


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/blog_detail.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'picture', 'is_published')
    success_url = reverse_lazy('main:blog_list')
    template_name = 'main/blog_form.html'

class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'picture', 'is_published')
    success_url = reverse_lazy('main:blog_list')
    template_name = 'main/blog_form.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('main:blog_list')
    template_name = 'main/blog_confirm_delete.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'
