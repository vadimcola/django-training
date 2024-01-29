from django.urls import path
from django.views.generic import *

from main.apps import MainConfig
from main.views import ProductListView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view()),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug:the_slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/update/<slug:the_slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<slug:the_slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]
