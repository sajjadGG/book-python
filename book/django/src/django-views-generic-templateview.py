import datetime
from django.views.generic import TemplateView


class TodayView(TemplateView):
    template_name = 'templates/index.html'

    def get_context_data(self, request, *args, **kwargs):
        return {
            'today': datetime.date.today(),
            'now': datetime.datetime.now(),
        }