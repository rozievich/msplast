from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from .models import Product, Category, Media
from .forms import SubscribeForm


def Home(request):
    categories = Category.objects.all()
    medias = Media.objects.all()
    context = {
        "categories": categories,
        "medias": medias,
    }

    return render(request, 'index.html', context)


def About(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }

    return render(request, 'about-us.html', context)


def Shop(request):
    page = 1
    key = request.GET.get('q', '')
    if request.GET.get('p'):
        page = request.GET.get('p')
        products = Product.objects.all()
    elif key:
        products = Product.objects.filter(Q(name__contains=key) | Q(description__contains=key))
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    pages = Paginator(products, 6)

    try:
        result = pages.page(int(page))
    except EmptyPage:
        result = pages.page(1)

    return render(request, 'shop-grid-fullwidth.html', {"products": result, "categories": categories})


def Contact(request):
    categories = Category.objects.all()
    message = ""
    if request.POST:
        data = SubscribeForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/')
        else:
            message = "Telefon raqamingizni to\'g\'ri kiriting, masalan: +998901234567"
    return render(request, 'contact.html', {"categories": categories, "message": message})


def Medias(request):
    page = 1
    categories = Category.objects.all()
    key = request.GET.get('q', '')
    if request.GET.get('p'):
        page = request.GET.get('p')
        medias = Media.objects.all()
    if key:
        medias = Media.objects.filter(
            Q(name__contains=key) |
            Q(description__contains=key))
    else:
        medias = Media.objects.all()
    pages = Paginator(medias, 4)

    try:
        result = pages.page(int(page))
    except EmptyPage:
        result = pages.page(1)
    return render(request, 'blog-2-column.html', {"categories": categories, "medias": result})


def Media_about(request):
    context = {

    }
    return render(request, 'single-product.html', context)


def Search(request):
    context = {

    }

    return render(request, 'wishlist.html', context)


def Error(request):
    context = {

    }

    return render(request, '404.html', context)
