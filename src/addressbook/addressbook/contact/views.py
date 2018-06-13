from django.views.generic import TemplateView
from contact.models import Contact


class ListView(TemplateView):
    template_name = 'contact/list.html'

    def get_context_data(self, **kwargs):
        return {'contacts': Contact.objects.all()}


class DetailView(TemplateView):
    template_name = 'contact/detail.html'

    def get_context_data(self, id, **kwargs):
        return {'contact': Contact.objects.get(id=id)}


# api view