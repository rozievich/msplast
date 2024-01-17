from django.urls import path
from main.views import Home, About, Shop, Contact, Media

urlpatterns = [
    path("", Home, name="home"),
    path("about/", About, name="about"),
    path("product/", Shop, name="product"),
    path("contact/", Contact, name="contact"),
    path("media/", Media, name="media")
]
