from django.urls import path

from main.views import *

urlpatterns = [
    path('', ProductListView.as_view()),
    path('main/blog_list/', BlogListView.as_view()),
]