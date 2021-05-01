from django.shortcuts import render
import json, os
from geekshop.settings import BASE_DIR
from .models import ProductCategory, Product

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    # with open(os.path.join(BASE_DIR,'mainapp/fixtures/products.json'), 'rb') as f:
    #     products = json.load(f)
    context = {
        'title': 'geekshop - каталог',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

