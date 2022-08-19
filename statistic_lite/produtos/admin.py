from django.contrib import admin
from .models import Products

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_description', 'price',)
    list_filter = ('product_id',)

admin.site.register(Products, ProductAdmin)