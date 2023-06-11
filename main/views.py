from django.shortcuts import render

from main.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'main/home.html', context)
