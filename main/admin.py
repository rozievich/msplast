from django.contrib import admin
from .models import User, Category, Color, Media, Product

# Register your models here.
admin.site.register((User, Product, Color, Media, Category))