from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1 style='text-align: center; color: blue;'>Hello World</h1>")