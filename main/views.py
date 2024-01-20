from django.shortcuts import render, redirect
from django.db.models import Q
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
    if request.GET:
        key = request.GET.get('q')
        products = Product.objects.filter(
            Q(name__contains=key) |
            Q(description__contains=key))
        
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop-grid-fullwidth.html', {"products": products, "categories": categories})


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
    categories = Category.objects.all()
    if request.GET:
        key = request.GET.get('q')
        medias = Media.objects.filter(
            Q(name__contains=key) |
            Q(description__contains=key))
    else:
        medias = Media.objects.all()
    return render(request, 'blog-2-column.html', {"categories": categories, "medias": medias})


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
