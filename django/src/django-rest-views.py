import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from contact.models import Contact


class ContactAPI(View):
    http_method_names = ['get', 'post', 'options']

    def options(self, request, *args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = ', '.join(self.http_method_names).upper()
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    def get(self, *args, **kwargs):
        result = {'contacts': list(Contact.objects.all().values())}
        return JsonResponse(status=200, data=result, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body, encoding='utf-8')
        try:
            contact, created = Contact.objects.update_or_create(**data)

            if created:
                return JsonResponse(status=201, data={'status': 'Created'}, safe=False)
            else:
                return JsonResponse(status=200, data={'status': 'Updated'}, safe=False)

        except Exception:
            return JsonResponse(status=400, data={'status': 'Bad Request'}, safe=False)
