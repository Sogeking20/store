from django.shortcuts import render
from products.models import Category, Products
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def catalog(request, category_id=None, page_number=1):
    products = Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'categories': Category.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)