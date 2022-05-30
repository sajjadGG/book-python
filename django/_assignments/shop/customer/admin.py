from django.contrib import admin
from customer.models import Customer, Address


class AddressInline(admin.TabularInline):
    model = Address
    max_num = 2
    can_delete = False


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    search_fields = ['^lastname']
