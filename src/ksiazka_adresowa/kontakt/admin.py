from django.contrib import admin

from kontakt.models import Adress
from kontakt.models import Contact



class AdressInline(admin.TabularInline):
    model = Adress
    extra = 1


@admin.register(Contact)
class KontaktAdmin(admin.ModelAdmin):
    inlines = [AdressInline]
    search_fields = ['^last_name']
    list_filter = ['first_name']
    list_display = ['last_name', 'first_name', 'phone', 'date_of_birth']
