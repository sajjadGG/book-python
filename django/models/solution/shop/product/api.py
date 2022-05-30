import json
from http import HTTPStatus
from django.http import JsonResponse
from django.views import View
from product.models import Product


class ProductAPI(View):
    def get(self, request, pk=None):
        data = Product.objects.all().values()
        if pk is not None:
            data = data.filter(pk=pk)
        return JsonResponse(status=HTTPStatus.OK,
                            data=list(data))

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data['name']
            ean13 = data['ean13']
            price = data['price']
        except json.JSONDecodeError as err:
            status = HTTPStatus.BAD_REQUEST
            data = {'details': f'Json Decode Error: {err}'}
            return JsonResponse(data, status=status)
        except KeyError as err:
            status = HTTPStatus.NOT_ACCEPTABLE
            data = {'details': f'Missing field: {err}'}
            return JsonResponse(data, status=status)
        else:
            Product.objects.create(name=name, ean13=ean13, price=price)
            return JsonResponse(status=HTTPStatus.OK, data={'details': 'created'})
