from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from kontakt.models import Kontakt


class KontaktView(TemplateView):
    template_name = 'kontakt/index.html'

    def get_context_data(self, **kwargs):
        return {
            'kontakty': Kontakt.objects.all()
        }

class KontaktAPIView(View):

    def get(self):

        return JsonResponse(
            status=200,
            data={Kontakt.objects.all()}
        )