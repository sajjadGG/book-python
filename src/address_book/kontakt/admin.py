from django.contrib import admin
from kontakt.models import Kontakt
from kontakt.models import Address


class AddressAdmin(admin.TabularInline):
    model = Address
    extra = 1


@admin.register(Kontakt)
class KontaktAdmin(admin.ModelAdmin):
    inlines = [AddressAdmin]
    search_fields = ['last_name']


