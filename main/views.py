from django.shortcuts import render, HttpResponse


def Home(request):
    context = {

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


def Media(request):
    context = {

    }

    return render(request, 'blog-2-column.html', context)
