from django.contrib import admin

# Register your models here.

from products.models import Category, Products, Basket

admin.site.register(Category)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'category')
    fields = ('title', 'content', ('price', 'quantity'), 'image', 'category')

