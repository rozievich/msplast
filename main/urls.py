from django.urls import path
from main.views import Home, About, Shop, Contact, Media, Media_about, Search

urlpatterns = [
    path("", Home, name="home"),
    path("about/", About, name="about"),
    path("product/", Shop, name="product"),
    path("contact/", Contact, name="contact"),
    path("media/", Media, name="media"),
    path("media/about/", Media_about, name="media-about"),
    path("search/", Search, name="test")
]
