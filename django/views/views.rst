Views
=====


Function View
-------------
.. code-block:: python

    from django.http import HttpResponse
    import datetime

    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

.. code-block:: python

    from django.http import HttpResponse, HttpResponseNotFound

    def my_view(request):
        # ...
        if foo:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            return HttpResponse('<h1>Page was found</h1>')

.. code-block:: python

    from django.http import HttpResponse

    def my_view(request):
        # ...

        # Return a "created" (201) response code.
        return HttpResponse(status=201)

.. code-block:: python

    from django.http import Http404
    from django.shortcuts import render
    from polls.models import Poll

    def detail(request, poll_id):
        try:
            p = Poll.objects.get(pk=poll_id)
        except Poll.DoesNotExist:
            raise Http404("Poll does not exist")
        return render(request, 'polls/detail.html', {'poll': p})


Async Views
-----------
* Since Django 3.1

.. code-block:: python

    import datetime
    from django.http import HttpResponse

    async def current_datetime(request):
        now = datetime.datetime.now()
        html = '<html><body>It is now %s.</body></html>' % now
        return HttpResponse(html)



Class Based Views
-----------------


Generic Views
-------------
* ``DetailView``
* ``EditView``
* ``ListView``


TemplateView
------------
.. literalinclude:: src/django-views-generic-templateview.py
    :language: python
    :caption: TemplateView


RedirectView
------------
.. literalinclude:: src/django-views-generic-redirectview.py
    :language: python
    :caption: RedirectView

View
----
.. literalinclude:: src/django-views-generic-view.py
    :language: python
    :caption: View

Responses
---------
* ``HttpResponse``
* ``JsonResponse``


Permissions in Views
--------------------

Class Based Views
-----------------
* https://docs.djangoproject.com/en/2.1/topics/auth/default/#the-permissionrequiredmixin-mixin

.. code-block:: python

    from django.contrib.auth.mixins import PermissionRequiredMixin

    class MyView(PermissionRequiredMixin, View):
        permission_required = 'polls.can_vote'
        # Or multiple of permissions:
        permission_required = ('polls.can_open', 'polls.can_edit')

Decorators
----------
* ``@login_required``


Use Case - 0x01
---------------
.. code-block:: python

    import json
    from http import HTTPStatus
    from django.contrib.auth.mixins import PermissionRequiredMixin
    from django.http import JsonResponse
    from django.utils.decorators import method_decorator
    from django.views import View
    from django.views.decorators.csrf import csrf_exempt
    from contact.models import Person


    @method_decorator(csrf_exempt, name='dispatch')
    class ContactAPI(PermissionRequiredMixin, View):
        permission_required = ['contact.view_person']
        raise_exception = True
        http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']

        def head(self, request):
            return JsonResponse(status=HTTPStatus.OK, data={})

        def options(self, request):
            return JsonResponse(status=HTTPStatus.OK, data=self.http_method_names, safe=False)

        def get(self, request, pk=None):
            data = Person.objects.all().values()
            if pk is not None:
                data = data.filter(pk=pk)
            if data.exists():
                return JsonResponse(
                    status=HTTPStatus.OK,
                    data=list(data),
                    safe=False)
            else:
                return JsonResponse(
                    status=HTTPStatus.NOT_FOUND,
                    data={'details': 'User with this ID does not exist'})

        def post(self, request):
            try:
                data = json.loads(request.body.decode('utf-8'))
                firstname = data['firstname']
                lastname = data['lastname']
            except json.JSONDecodeError as err:
                return JsonResponse(
                    status=HTTPStatus.BAD_REQUEST,
                    data={'details': f'JSON Decode Error: {err}'})
            except KeyError as err:
                return JsonResponse(
                    status=HTTPStatus.NOT_ACCEPTABLE,
                    data={'details': f'Missing field: {err}'})
            except Exception as err:
                return JsonResponse(
                    status=HTTPStatus.INTERNAL_SERVER_ERROR,
                    data={'details': f'Some other error: {err}'})
            else:
                Person.objects.create(
                    firstname=firstname,
                    lastname=lastname)
                return JsonResponse(
                    status=HTTPStatus.CREATED,
                    data={'details': 'created'})

        def delete(self, request, pk):
            Person.objects.get(pk=pk).delete()
            return JsonResponse(
                status=HTTPStatus.ACCEPTED,
                data={'details': 'deleted'})

        def put(self, request, pk):
            try:
                data = json.loads(request.body.decode('utf-8'))
                firstname = data['firstname']
                lastname = data['lastname']
            except json.JSONDecodeError as err:
                return JsonResponse(
                    status=HTTPStatus.BAD_REQUEST,
                    data={'details': f'JSON Decode Error: {err}'})
            except KeyError as err:
                return JsonResponse(
                    status=HTTPStatus.NOT_ACCEPTABLE,
                    data={'details': f'Missing field: {err}'})
            except Exception as err:
                return JsonResponse(
                    status=HTTPStatus.INTERNAL_SERVER_ERROR,
                    data={'details': f'Some other error: {err}'})
            else:
                Person.objects.filter(pk=pk).update(
                    firstname=firstname,
                    lastname=lastname)
                return JsonResponse(
                    status=HTTPStatus.ACCEPTED,
                    data={'details': 'updated'})

        def patch(self, request, pk):
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError as err:
                return JsonResponse(
                    status=HTTPStatus.BAD_REQUEST,
                    data={'details': f'JSON Decode Error: {err}'})
            except Exception as err:
                return JsonResponse(
                    status=HTTPStatus.INTERNAL_SERVER_ERROR,
                    data={'details': f'Some other error: {err}'})
            else:
                person = Person.objects.get(pk=pk)
                if firstname := data.get('firstname'):
                    person.firstname = firstname
                if lastname := data.get('lastname'):
                    person.lastname = lastname
                person.save()
                return JsonResponse(
                    status=HTTPStatus.ACCEPTED,
                    data={'details': 'updated'})
