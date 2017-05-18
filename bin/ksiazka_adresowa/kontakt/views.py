from django.views.generic import TemplateView
from kontakt.models import Contact


class ContactView(TemplateView):
    template_name = 'kontakt/wizytowka.html'

    def get_context_data(self, **kwargs):

        Contact.objejcts.filter(date_of_birth__gt=date)

        return {'contacts': Contact.objects.all()}
