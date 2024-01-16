from django.db import models
from .utils.validators import validate_phone_number, validate_image


class User(models.Model):
    fullname = models.CharField(max_length=128)
    phone = models.CharField(max_length=13, validators=[validate_phone_number])
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = "-created_at",
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"

    def __str__(self) -> str:
        return self.fullname


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    image = models.ImageField(upload_to="category", validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = "name",
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    
    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=80, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = "name",
        verbose_name = "Rang"
        verbose_name_plural = "Ranglar"
    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class RateChoice(models.IntegerChoices):
        KG = 1, "KG"
        MR = 2, "METR"
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product", validators=[validate_image])
    description = models.TextField(blank=True, null=True)
    types = models.PositiveIntegerField(choices=RateChoice.choices, default=RateChoice.KG)
    size = models.PositiveIntegerField()
    color = models.ManyToManyField(Color, related_query_name="product")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = "-created_at",
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
    
    def __str__(self) -> str:
        return self.name


class Media(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = "-created_at",
        verbose_name = "Media"
        verbose_name_plural = "Medialar"
    
    def __str__(self) -> str:
        return self.name
