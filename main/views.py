from django.shortcuts import render
from django.views.generic import ListView

from main.models import Product


# def home(request):
#     context = {
#         'object_list': Product.objects.all()
#     }
#     return render(request, 'main/product_list.html', context)


class ProductListView(ListView):
    model = Product
