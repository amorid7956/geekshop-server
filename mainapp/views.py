from django.shortcuts import render
from .models import ProductCategory, Product

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'geekshop - каталог',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
