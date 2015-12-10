from django.contrib import admin
from .models import Kontakt
from .models import Adres


class AdresAdmin(admin.TabularInline):
    model = Adres
    extra = 1


@admin.register(Kontakt)
class KontaktAdmin(admin.ModelAdmin):
    search_fields = ['^nazwisko', '^telefon']
    list_filter = ['jest_adminem']

    inlines = [
        AdresAdmin,
    ]
