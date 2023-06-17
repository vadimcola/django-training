from django.shortcuts import render
from django.views.generic import ListView

from main.models import *


class ProductListView(ListView):
    model = Product


class BlogListView(ListView):
    model = Blog
