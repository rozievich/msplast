from django.shortcuts import render
from .models import Product, Category, Media

def Home(request):
    categories = Category.objects.all()
    medias = Media.objects.all()
    for media in medias:
        media.url = media.url.split("=")[1]
    context = {
        "categories": categories,
        "medias": medias,
    }

    return render(request, 'index.html', context)


def About(request):
    context = {

    }

    return render(request, 'about-us.html', context)


def Shop(request):
    context = {

    }

    return render(request, 'shop-grid-fullwidth.html', context)


def Contact(request):
    context = {

    }

    return render(request, 'contact.html', context)


def Medias(request):
    context = {

    }

    return render(request, 'blog-2-column.html', context)

def Media_about(request):
    context = {

    }
    return render(request, 'single-product.html', context)