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
