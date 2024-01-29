from django.urls import path
from django.views.generic import *
from django.views.decorators.cache import cache_page
from main.apps import MainConfig
from main.views import ProductListView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, \
    ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='prod_list'),
    path('prod/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='prod_item'),
    path('prod/create/', ProductCreateView.as_view(), name='prod_create'),
    path('prod/update/<int:pk>/', ProductUpdateView.as_view(), name='prod_update'),
    path('prod/delete/<int:pk>/', ProductDeleteView.as_view(), name='prod_delete'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug:the_slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/update/<slug:the_slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<slug:the_slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]
