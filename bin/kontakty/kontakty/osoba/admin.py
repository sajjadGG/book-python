from django.contrib import admin
from kontakty.osoba.models import Osoba
from kontakty.osoba.models import Adres

@admin.register(Adres)
class AdresAdmin(admin.ModelAdmin):
    pass

class AdresInline(admin.TabularInline):
    model = Adres
    extra = 1

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko']
    search_fields = ['^nazwisko']
    inlines = [AdresInline]

