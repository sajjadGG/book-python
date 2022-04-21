.. testsetup::

    # doctest: +SKIP_FILE

.. todo:: REFACTOR THIS FILE


ORM
===


About
-----
* ``.create()``
* ``.save()``
* ``.update()``
* ``.update_or_create()``
* ``.delete()``

* ``.all()``
* ``.get()``
* ``.get_or_create()``
* ``.bulk_create()``
* ``.bulk_update()``
* ``.complex_filter()``
* ``.filter()``
* ``.count()``
* ``.distinct()``
* ``.values()``
* ``.values_list()``
* ``.exclude()``
* ``.order_by()``
* ``.annotate()``
* ``.aggregate()``
* ``.exist()``
* ``.last()``
* ``.first()``
* ``.earliest()``
* ``.latest()``
* ``.check()``
* ``.alias()``
* ``.dates()``
* ``.datetimes()``
* ``.difference()``
* ``.exists()``
* ``.explain()``
* ``.extra()``
* ``.in_bulk()``
* ``.intersection()``
* ``.none()``
* ``.union()``
* ``.only()``
* ``.reverse()``
* ``.raw()``
* ``.select_for_update()``
* ``.using()``

* ``.select_related()``
* ``.prefetch_related()``

# [1], [1:], [::2]

## Sequences
* ``__in``
* ``__isnull``

## String
* ``__startswith`` - case sensitive
* ``__istartswith`` - case insensitive
* ``__endswith`` - case sensitive
* ``__iendswith`` - case insensitive
* ``__contains`` - case sensitive
* ``__icontains`` - case insensitive
* ``__exact`` - case sensitive (default)
* ``__iexact`` - case insensitive

## Numeric, Dates
* ``__eq``
* ``__gt``
* ``__gte``
* ``__lt``
* ``__lte``

## Date
* ``__year``
* ``__month``
* ``__day``
* ``__hour``
* ``__minute``
* ``__second``
* ``__microsecond``
* ``__range`` - between two dates
* ``__in`` - a list of dates



QuerySet
--------
* sklejanie zapytań
* Tworzenie obiektów
* Zapisywanie ``save()`` ForeignKey

.. code-block:: python

    Model.save()
    Model.objects.all()
    Model.objects.get()
    Model.objects.filter()
    Model.objects.exclude()
    Model.objects.distinct()
    Model.objects.get().query
    Model.objects.all()[:5]
    Model.objects.all()[5:10]
    Model.objects.order_by('publish_date')[0]


Filtered QuerySets are unique
-----------------------------
.. code-block:: python

    q1 = Entry.objects.filter(headline__startswith="What")
    q2 = q1.exclude(pub_date__gte=datetime.date.today())
    q3 = q1.filter(pub_date__gte=datetime.date.today())


QuerySets are lazy
------------------
.. code-block:: python

    q = Entry.objects.filter(headline__startswith="What")
    q = q.filter(pub_date__lte=datetime.date.today())
    q = q.exclude(body_text__icontains="food")
    print(q)


Field lookups
-------------
.. code-block:: python

    Model.objects.filter(pub_date__lte='1969-07-24')
    Model.objects.get(title__exact='Man walk on Moon!')
    Model.objects.get(title__iexact='man walk on moon!')
    Model.objects.get(headline__contains='Moon')
    Model.objects.filter(title__startswith='Important')
    Model.objects.filter(title__istartswith='Important')
    Model.objects.filter(title__endswith='Important')
    Model.objects.filter(title__iendswith='Important')


Lookups that span relationships
-------------------------------
.. code-block:: python

    Entry.objects.filter(blog__name='Beatles Blog')
    Blog.objects.filter(entry__headline__contains='Lennon')
    Blog.objects.filter(entry__authors__name='Lennon')
    Blog.objects.filter(entry__authors__name__isnull=True)
    Blog.objects.exclude(
        entry__headline__contains='Lennon',
        entry__pub_date__year=2008,
    )
    Blog.objects.exclude(
        entry__in=Entry.objects.filter(
            headline__contains='Lennon',
            pub_date__year=2008,
        ),
    )


Filters can reference fields on the model
-----------------------------------------
.. code-block:: python

    from django.db.models import F


    Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
    Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
    Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
    Entry.objects.filter(authors__name=F('blog__name'))


.. code-block:: python

    from datetime import timedelta


    Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))


The pk lookup shortcut
----------------------
.. code-block:: python

    Blog.objects.get(id__exact=14)  # Explicit form
    Blog.objects.get(id=14)         # __exact is implied
    Blog.objects.get(pk=14)         # pk implies id__exact

    # Get blogs entries with id 1, 4 and 7
    Blog.objects.filter(pk__in=[1,4,7])

    # Get all blog entries with id > 14
    Blog.objects.filter(pk__gt=14)

    # pk lookups also work across joins
    Entry.objects.filter(blog__id__exact=3) # Explicit form
    Entry.objects.filter(blog__id=3)        # __exact is implied
    Entry.objects.filter(blog__pk=3)        # __pk implies __id__exact


Complex lookups with Q objects
------------------------------
.. code-block:: python

    from django.db.models import Q
    Q(question__startswith='What')
    Q(question__startswith='Who') | Q(question__startswith='What')
    # WHERE question LIKE 'Who%' OR question LIKE 'What%'

    Poll.objects.get(
        Q(question__startswith='Who'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )
    # SELECT * from polls WHERE question LIKE 'Who%'
    # AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')


Comparing objects
-----------------
.. code-block:: python

    some_entry == other_entry
    some_entry.id == other_entry.id

    some_obj == other_obj
    some_obj.name == other_obj.name


``Q()`` expressions
-------------------
.. code-block:: python

    from django.db.models import Q


    Q(question__startswith='What')

    Q(question__startswith='Who') | Q(question__startswith='What')
    Q(question__startswith='Who') | ~Q(pub_date__year=2005)     # negated query

.. code-block:: python

    Poll.objects.get(
        Q(question__startswith='Who'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )


``F()`` expressions
-------------------
An F() object represents the value of a model field or annotated column. It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.

.. code-block:: python

    Iris.objects.all().update(petal_length=F('petal_length') + 1)


Aggregations
------------
* Django ORM Cheat sheet

.. code-block:: python

    # Total number of books.
    Book.objects.count()
    # 2452

    # Total number of books with publisher=BaloneyPress
    Book.objects.filter(publisher__name='BaloneyPress').count()
    # 73

    # Average price across all books.
    from django.db.models import Avg
    Book.objects.all().aggregate(Avg('price'))
    # {'price__avg': 34.35}

    # Max price across all books.
    from django.db.models import Max
    Book.objects.all().aggregate(Max('price'))
    # {'price__max': Decimal('81.20')}

    from django.db.models import Avg, Max, Min
    Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
    # {'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}

    # Difference between the highest priced book and the average price of all books.
    from django.db.models import FloatField
    Book.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
    # {'price_diff': 46.85}

    # All the following queries involve traversing the Book<->Publisher
    # foreign key relationship backwards.

    # Each publisher, each with a count of books as a "num_books" attribute.
    from django.db.models import Count
    pubs = Publisher.objects.annotate(num_books=Count('book'))
    # <QuerySet [<Publisher: BaloneyPress>, <Publisher: SalamiPress>, ...]>
    pubs[0].num_books
    # 73

    # Each publisher, with a separate count of books with a rating above and below 5
    from django.db.models import Q
    above_5 = Count('book', filter=Q(book__rating__gt=5))
    below_5 = Count('book', filter=Q(book__rating__lte=5))
    pubs = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)
    pubs[0].above_5
    # 23
    pubs[0].below_5
    # 12

    # The top 5 publishers, in order by number of books.
    pubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:5]
    pubs[0].num_books
    # 1323


Functions
---------
* https://docs.djangoproject.com/en/dev/ref/models/database-functions/

>>> # doctest: +SKIP
... from django.db.models import Value
... from myapp.models import Person
...
...
... Person.objects
...     .all()
...     .annotate(fullname=Concat('firstname', Value(' '), 'lastname'))
...     .values('fullname')
<QuerySet [{'fullname': 'Melissa Lewis'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Alex Vogel'}, {'fullname': 'Beth Johnssen'}, {'fullname': 'Jan Twardowski'}, {'fullname': 'Jan Twardowski'}]>
