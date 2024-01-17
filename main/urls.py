from django.urls import path
from main.views import Home, About, Shop, Contact, Medias, Media_about

urlpatterns = [
    path("", Home, name="home"),
    path("about/", About, name="about"),
    path("product/", Shop, name="product"),
    path("contact/", Contact, name="contact"),
    path("media/", Medias, name="media"),
    path("media/about/", Media_about, name="media-about")
]
