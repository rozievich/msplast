from django.urls import path
from main.views import Home, About, Shop, Contact, Medias, ProductAbout, Error

urlpatterns = [
    path("", Home, name="home"),
    path("about/", About, name="about"),
    path("product/", Shop, name="product"),
    path("product/<int:pk>/", ProductAbout, name="product_about"),
    path("contact/", Contact, name="contact"),
    path("media/", Medias, name="media"),
    path("404/", Error, name="error")
]
