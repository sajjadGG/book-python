from django.shortcuts import render
from django.views.generic import TemplateView
from kontakt.models import Kontakt


class HelloWorldView(TemplateView):
    template_name = 'hello-world.html'

    def get_context_data(self, nazwisko, **kwargs):
        return {
            'kontakt': Kontakt.objects.get(nazwisko=nazwisko),
            'kontakty': Kontakt.objects.all(),
        }

