from contact.models import Person
from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'contact/list.html'

    def get_context_data(self, **kwargs):
        return {'people': Person.objects.all()}


class DetailView(TemplateView):
    template_name = 'contact/detail.html'

    def get_context_data(self, id, **kwargs):
        return {'person': Person.objects.get(id=id)}
