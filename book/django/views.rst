*****
Views
*****

URLs
====

Global URLs
-----------

In app URLs
-----------

URLs reversing
--------------

URLs in templates
-----------------

Class Based Views
=================
.. code-block:: python

    class TodayView(View):
        http_method_names = ['get', 'head', 'options']

        def get(self, request, *args, **kwargs):
            data = {
                'today': datetime.date.today(),
                'now': datetime.datetime.now(),
            }
            return JsonResponse(status=status.HTTP_200_OK, data=data, safe=False)

.. code-block:: python

    class TodayView(TemplateView):
        template_name = 'templates/index.html'

        def get_context_data(self, request, *args, **kwargs):
            return {
                'today': datetime.date.today(),
                'now': datetime.datetime.now(),
            }


Generic Views
=============
- TemplateView
- View
- DetailView
- EditView
- ListView

Responses
=========
HttpResponse
JsonReponse

Http Error Codes
================


Decorators
==========
- ``@login_required``