from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['=ean13', '^name']
    list_display = ['ean13', 'name', 'price']
