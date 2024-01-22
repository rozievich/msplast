from modeltranslation.translator import register, TranslationOptions

from .models import User, Product, Media, Category, Color


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
