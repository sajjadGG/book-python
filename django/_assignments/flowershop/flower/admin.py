from django.contrib import admin
from flower.models import Iris


@admin.register(Iris)
class IrisAdmin(admin.ModelAdmin):
    search_fields = ['^species']
    list_filter = ['species']
