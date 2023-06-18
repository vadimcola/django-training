from django.urls import path

from main.views import *

urlpatterns = [
    path('', ProductListView.as_view()),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_list/<int:pk>/', BlogDetailView.as_view()),
    path('blog_list/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/update/<int:pk>/', UpdateView.as_view(), name='blog_update'),
]
