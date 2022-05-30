from django.contrib import admin
from contact.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['^lastname']
    list_filter = ['is_astronaut', 'nationality', 'group']
