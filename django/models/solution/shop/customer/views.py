from django.views.generic import TemplateView
from contact.models import Person


class ContactListView(TemplateView):
    template_name = 'contact/contact-list.html'

    def get_context_data(self, **kwargs) -> dict:
        return {'contacts': Person.objects.all()}


class ContactDetailsView(TemplateView):
    template_name = 'contact/contact-details.html'

    def get_context_data(self, id, **kwargs) -> dict:
        return {'contact': Person.objects.get(id=id)}


class ContactDetailsByNameView(TemplateView):
    template_name = 'contact/contact-details.html'

    def get_context_data(self, firstname, lastname, **kwargs) -> dict:
        return {'contact': Person.objects.get(firstname__iexact=firstname, lastname__iexact=lastname)}
