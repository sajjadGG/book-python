from django.contrib import admin
from contact.models import Address
from contact.models import Contact
from contact.models import Document


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    classes = ["collapse"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'phone', 'email']
    list_filter = ['gender']
    search_fields = ['^last_name']
    inlines = [AddressInline]