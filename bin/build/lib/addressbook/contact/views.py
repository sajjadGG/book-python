from django.views.generic import TemplateView
from contact.models import Contact


class WizytowkaView(TemplateView):
    template_name = 'contact/wizytowka.html'

    def get_context_data(self, name, *args, **kwargs):
        return {'users': Contact.objects.filter(last_name=name)}