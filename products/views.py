from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context ={
        'featured_products': featured_products,
        'latest_products': latest_products
    }
    return render(request, 'index.html', context)


def list_product(request):
    page = request.GET.get('page', 1)  # Retrieve the page number (default to 1)

    product_list = Product.objects.order_by('priority')
    product_paginator = Paginator(product_list, 8)
    product_page = product_paginator.get_page(page)  # Use the retrieved page number

    context = {'products': product_page}
    return render(request, 'products.html', context)
def detail_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product_details.html', context)
