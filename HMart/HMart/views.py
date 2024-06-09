from django.shortcuts import render, redirect
from store_app.models import Product, Categories


def BASE(request):
    return render(request, 'Main/base.html')


def HOME(request):
    product = Product.objects.filter(status='PUBLISH')

    context = {
        'product': product,

    }
    return render(request, 'Main/index.html', context)


def PRODUCT(request):
    product = Product.objects.filter(status='PUBLISH')
    categories = Categories.objects.all()

    context = {
        'product': product,
        'categories': categories,
    }
    return render(request, 'Main/product.html')


def CONTACT(request):
    return render(request, 'Main/contact.html')
