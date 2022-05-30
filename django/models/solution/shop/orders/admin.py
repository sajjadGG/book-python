from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer', 'product']
    # list_display = ['customer', 'product__name', 'product__ean13', 'product__price']
    list_display = ['customer', 'product']
