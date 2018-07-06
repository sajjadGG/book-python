import datetime
from django.http import JsonResponse
from django.views.generic import View


class TodayView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(),
            'now': datetime.datetime.now(),
        }
        return JsonResponse(status=200, data=data, safe=False)
