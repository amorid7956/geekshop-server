from django.shortcuts import render
import json, os
from geekshop.settings import BASE_DIR

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    with open(os.path.join(BASE_DIR,'mainapp/fixtures/products.json'), 'rb') as f:
        products = json.load(f)
    context = {
        'title': 'geekshop - каталог',
        'products' : products,
        # 'products' : [
        #     { 'name' : 'Худи черного цвета с монограммами adidas Originals' , 'price' : '6 090,00',
        #       'description' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.' , 'img' : 'Adidas-hoodie.png' },
        #     { 'name' : 'Синяя куртка The North Face' , 'price' : '23 725,00',
        #       'description' : 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.' ,
        #       'img' : 'Blue-jacket-The-North-Face.png', 'is_danger' : True },
        #     { 'name' : 'Коричневый спортивный oversized-топ ASOS DESIGN' , 'price' : '3 390,00',
        #       'description' : 'Материал с плюшевой текстурой. Удобный и мягкий.' , 'img' : 'Brown-sports-oversized-top-ASOS-DESIGN.png'},
        #     { 'name' : 'Черный рюкзак Nike Heritage' , 'price' : '2 340,00',
        #       'description' : 'Плотная ткань. Легкий материал.' , 'img' : 'Black-Nike-Heritage-backpack.png'},
        #     { 'name' : 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex' , 'price' : '13 590,00',
        #       'description' : 'Гладкий кожаный верх. Натуральный материал.' , 'img' : 'Black-Dr-Martens-shoes.png'},
        #     { 'name' : 'Темно-синие широкие строгие брюки ASOS DESIGN' , 'price' : '2 890,00',
        #       'description' : 'Легкая эластичная ткань сирсакер Фактурная ткань.' , 'img' : 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        # ]
    }
    return render(request, 'mainapp/products.html', context)

