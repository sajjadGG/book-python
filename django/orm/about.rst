ORM
===


Important
---------
# .create()
# .save()
# .update()
# .update_or_create()
# .delete()

# .all()
# .get()
# .get_or_create()
# .bulk_create()
# .bulk_update()
# .complex_filter()
# .filter()
# .count()
# .distinct()
# .values()
# .values_list()
# .exclude()
# .order_by()
# .annotate()
# .aggregate()
# .exist()
# .last()
# .first()
# .earliest()
# .latest()
# .check()
# .alias()
# .dates()
# .datetimes()
# .difference()
# .exists()
# .explain()
# .extra()
# .in_bulk()
# .intersection()
# .none()
# .union()
# .only()
# .reverse()
# .raw()
# .select_for_update()
# .using()

# .select_related()
# .prefetch_related()

# [1], [1:], [::2]

## Sequences
# __in
# __isnull

## String
# __startswith
# __istartswith
# __endswith
# __iendswith
# __contains
# __icontains
# __exact
# __iexact

## Numeric, Dates
# __eq
# __gt
# __gte
# __lt
# __lte

## Date
# __year
# __month
# __day
# __hour
# __minute
# __second
# __microsecond





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
    Model.objects.order_by('headline')[0]

Examples
--------
.. code-block:: python

    str(Contact.objects.all().query)
    'SELECT "contact_contact"."id", "contact_contact"."created_date", "contact_contact"."created_author_id", "contact_contact"."modified_date", "contact_contact"."modified_author_id", "contact_contact"."firstname", "contact_contact"."lastname", "contact_contact"."salary", "contact_contact"."job", "contact_contact"."born", "contact_contact"."age", "contact_contact"."gender", "contact_contact"."is_adult", "contact_contact"."weight", "contact_contact"."height", "contact_contact"."email", "contact_contact"."homepage", "contact_contact"."phone_country_code", "contact_contact"."phone_number", "contact_contact"."picture", "contact_contact"."attachment", "contact_contact"."notes" FROM "contact_contact"'

    str(Contact.objects.all().values('firstname').query)
    'SELECT "contact_contact"."firstname" FROM "contact_contact"'

    str(Contact.objects.all().values('firstname', 'lastname').query)
    'SELECT "contact_contact"."firstname", "contact_contact"."lastname" FROM "contact_contact"'

    Contact.objects.all().last()
    <Contact: Mark W>
    Contact.objects.all().first()
    <Contact: Mark Watney>

    Contact.objects.filter(firstname='Mark')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>

    Contact.objects.filter(firstname='Mark', lastname='Watney')
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects.filter(firstname='Mark', lastname__startswith='W')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>



    Contact.objects.filter(firstname='Mark', lastname__startswith='W')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>
    Contact.objects.filter(firstname='Mark', lastname__startswith='w')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>
    Contact.objects.filter(firstname='Mark', lastname__istartswith='w')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>
    Contact.objects.filter(firstname='Mark', lastname__istartswith='W')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>


.. code-block:: python

    Contact.objects.filter(firstname='Mark', created_date__year='2021')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>

    Contact.objects.filter(firstname='Mark', created_date__gt='2021-09-07')
    /Users/matt/Developer/2021-09-djangof-aptiv/.venv/lib/python3.9/site-packages/django/db/models/fields/__init__.py:1416: RuntimeWarning: DateTimeField Contact.created_date received a naive datetime (2021-09-07 00:00:00) while time zone support is active.
      warnings.warn("DateTimeField %s received a naive datetime (%s)"
    <QuerySet [<Contact: Mark W>]>

    Contact.objects.filter(firstname='Mark', created_date__gt='2021-09-07 00:00:00+00:00')
    <QuerySet [<Contact: Mark W>]>

    Contact.objects.filter(age__lt=18)
    <QuerySet []>
    Contact.objects.filter(age__lt=50)
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects.filter(age__lte=50)
    <QuerySet [<Contact: Mark Watney>]>


    Contact.objects.filter(age__gt=50)
    <QuerySet []>
    Contact.objects.filter(age__gte=50)
    <QuerySet []>

    Contact.objects.filter(lastname__contains='ney')
    <QuerySet [<Contact: Mark Watney>]>
    Contact.objects.filter(lastname__icontains='ney')
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects.filter(born='1970-01-01')
    <QuerySet [<Contact: Mark Watney>]>
    Contact.objects.filter(born__gt='1970-01-01')
    <QuerySet []>
    Contact.objects.filter(born__gte='1970-01-01')
    <QuerySet [<Contact: Mark Watney>]>
    Contact.objects.filter(born__lt='1970-01-01')
    <QuerySet []>
    Contact.objects.filter(born__lte='1970-01-01')
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects.filter(born__in=('1970-01-01', '1969-07-21'))
    <QuerySet [<Contact: Mark Watney>]>
    Contact.objects.filter(lastname__in=[])
    <QuerySet []>
    Contact.objects.filter(lastname__in=['Watney', 'Lewis'])
    <QuerySet [<Contact: Melissa Lewis>, <Contact: Mark Watney>]>

    DATA = [1,2,3]
    Contact.objects.filter(pk__in=DATA)
    <QuerySet [<Contact: Mark Watney>, <Contact: Rick Martinez>, <Contact: Melissa Lewis>]>
    Contact.objects.filter(id__in=DATA)
    <QuerySet [<Contact: Mark Watney>, <Contact: Rick Martinez>, <Contact: Melissa Lewis>]>

    str(Contact.objects.filter(id__in=DATA).query)
    'SELECT "contact_contact"."id", "contact_contact"."created_date", "contact_contact"."created_author_id", "contact_contact"."modified_date", "contact_contact"."modified_author_id", "contact_contact"."firstname", "contact_contact"."lastname", "contact_contact"."salary", "contact_contact"."job", "contact_contact"."born", "contact_contact"."age", "contact_contact"."gender", "contact_contact"."is_adult", "contact_contact"."weight", "contact_contact"."height", "contact_contact"."email", "contact_contact"."homepage", "contact_contact"."phone_country_code", "contact_contact"."phone_number", "contact_contact"."picture", "contact_contact"."attachment", "contact_contact"."notes" FROM "contact_contact" WHERE "contact_contact"."id" IN (1, 2, 3)'


    Contact.objects.filter(born__gte='1969-07-21', born__lte='1970-01-01')
    <QuerySet [<Contact: Mark Watney>]>

    Address.objects.all()
    <QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>, <Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>
    Address.objects.filter(contact__lastname='Watney')
    <QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>]>
    str(Address.objects.filter(contact__lastname='Watney').query)
    'SELECT "contact_address"."id", "contact_address"."contact_id", "contact_address"."type", "contact_address"."street", "contact_address"."house", "contact_address"."apartment", "contact_address"."postcode", "contact_address"."city", "contact_address"."region", "contact_address"."country" FROM "contact_address" INNER JOIN "contact_contact" ON ("contact_address"."contact_id" = "contact_contact"."id") WHERE "contact_contact"."lastname" = Watney'

    str(Address.objects.filter(contact__lastname__contains='ney').query)
    'SELECT "contact_address"."id", "contact_address"."contact_id", "contact_address"."type", "contact_address"."street", "contact_address"."house", "contact_address"."apartment", "contact_address"."postcode", "contact_address"."city", "contact_address"."region", "contact_address"."country" FROM "contact_address" INNER JOIN "contact_contact" ON ("contact_address"."contact_id" = "contact_contact"."id") WHERE "contact_contact"."lastname" LIKE %ney% ESCAPE \'\\\''
    str(Address.objects.filter(contact__lastname__startswith='Wat').query)
    'SELECT "contact_address"."id", "contact_address"."contact_id", "contact_address"."type", "contact_address"."street", "contact_address"."house", "contact_address"."apartment", "contact_address"."postcode", "contact_address"."city", "contact_address"."region", "contact_address"."country" FROM "contact_address" INNER JOIN "contact_contact" ON ("contact_address"."contact_id" = "contact_contact"."id") WHERE "contact_contact"."lastname" LIKE Wat% ESCAPE \'\\\''

    Contact.objects.all().order_by('lastname')
    <QuerySet [<Contact: Ivan Ivanovich>, <Contact: Melissa Lewis>, <Contact: Rick Martinez>, <Contact: Jan Twardowski>, <Contact: Mark W>, <Contact: Mark Watney>, <Contact: Jan X>]>
    Contact.objects.all().order_by('-lastname')
    <QuerySet [<Contact: Jan X>, <Contact: Mark Watney>, <Contact: Mark W>, <Contact: Jan Twardowski>, <Contact: Rick Martinez>, <Contact: Melissa Lewis>, <Contact: Ivan Ivanovich>]>

    Contact.objects.all().order_by('-lastname', 'firstname')
    <QuerySet [<Contact: Jan X>, <Contact: Mark Watney>, <Contact: Mark W>, <Contact: Jan Twardowski>, <Contact: Rick Martinez>, <Contact: Melissa Lewis>, <Contact: Ivan Ivanovich>]>

    Contact.objects.all().values('firstname')
    <QuerySet [{'firstname': 'Mark'}, {'firstname': 'Rick'}, {'firstname': 'Melissa'}, {'firstname': 'Jan'}, {'firstname': 'Ivan'}, {'firstname': 'Jan'}, {'firstname': 'Mark'}]>

    Contact.objects.all().values('firstname').distinct()
    <QuerySet [{'firstname': 'Mark'}, {'firstname': 'Rick'}, {'firstname': 'Melissa'}, {'firstname': 'Jan'}, {'firstname': 'Ivan'}]>

    c = Contact.objects.all()
    fname = c.values('firstname')
    lname = c.values('lastname')

    fname
    <QuerySet [{'firstname': 'Mark'}, {'firstname': 'Rick'}, {'firstname': 'Melissa'}, {'firstname': 'Jan'}, {'firstname': 'Ivan'}, {'firstname': 'Jan'}, {'firstname': 'Mark'}]>

    lname
    <QuerySet [{'lastname': 'Ivanovich'}, {'lastname': 'Lewis'}, {'lastname': 'Martinez'}, {'lastname': 'Twardowski'}, {'lastname': 'W'}, {'lastname': 'Watney'}, {'lastname': 'X'}]>


    Contact.objects.get(id=1)
    <Contact: Mark Watney>

    Contact.objects.get(id=999)
    Traceback (most recent call last):
    contact.models.contact.Contact.DoesNotExist: Contact matching query does not exist.


    try:
        user = Contact.objects.get(firstname='Mark', lastname='Jimenez')
    except Contact.DoesNotExist:
        print('Sorry user does not exist')
    Sorry user does not exist


    Contact.objects.filter(firstname='Mark')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>
    Contact.objects.filter(firstname='Mark').exclude(lastname='W')
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects \
           .filter(firstname='Mark') \
           .filter(created_date__gte='2021-09-07 00:00:00+00:00') \
           .exclude(lastname='W') \
           .distinct() \
           .order_by('lastname', 'firstname')

    from datetime import datetime, timezone

    Contact.objects \
           .filter(firstname='Mark') \
           .filter(created_date__lte=datetime.now(timezone.utc)) \
           .exclude(lastname='W') \
           .distinct() \
           .order_by('lastname', 'firstname')
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects.filter(firstname='Mark')[1]
    <Contact: Mark W>
    Contact.objects.filter(firstname='Mark')[1:]
    <QuerySet [<Contact: Mark W>]>
    Contact.objects.filter(firstname='Mark')[1:5]
    <QuerySet [<Contact: Mark W>]>
    Contact.objects.filter(firstname='Mark')[:5]
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>


    q = Contact.objects
    q = q.filter(firstname='Mark')
    q = q.filter(created_date__lte=datetime.now(timezone.utc))
    q = q.exclude(lastname='W')
    q = q.distinct()
    q = q.order_by('lastname', 'firstname')
    q
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects.filter(lastname__endswith='ney')
    <QuerySet [<Contact: Mark Watney>]>
    Contact.objects.filter(lastname__iendswith='ney')
    <QuerySet [<Contact: Mark Watney>]>
    Contact.objects.filter(lastname__startswith='Wat')
    <QuerySet [<Contact: Mark Watney>]>
    Contact.objects.filter(lastname__istartswith='Wat')
    <QuerySet [<Contact: Mark Watney>]>

    Contact.objects.filter(age__isnull=True)
    <QuerySet [<Contact: Rick Martinez>, <Contact: Melissa Lewis>, <Contact: Jan Twardowski>, <Contact: Ivan Ivanovich>, <Contact: Jan X>, <Contact: Mark W>]>

    Address.objects.all()
    <QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>, <Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>

    Address.objects.filter(contact__age__isnull=True)
    <QuerySet [<Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>


    Contact.objects.filter(firstname='Mark')
    <QuerySet [<Contact: Mark Watney>, <Contact: Mark W>]>

    Address.objects.filter(contact__in=Contact.objects.filter(firstname='Mark'))
    <QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>]>

    str(Address.objects.filter(contact__in=Contact.objects.filter(firstname='Mark')).query)
    'SELECT "contact_address"."id", "contact_address"."contact_id", "contact_address"."type", "contact_address"."street", "contact_address"."house", "contact_address"."apartment", "contact_address"."postcode", "contact_address"."city", "contact_address"."region", "contact_address"."country" FROM "contact_address" WHERE "contact_address"."contact_id" IN (SELECT U0."id" FROM "contact_contact" U0 WHERE U0."firstname" = Mark)'



    Contact.objects.filter(lastname='XYZ').exists()
    False
    Contact.objects.filter(lastname='Watney').exists()
    True

    Contact.objects.get(firstname='Mark')
    Traceback (most recent call last):
    contact.models.contact.Contact.MultipleObjectsReturned: get() returned more than one Contact -- it returned 2!

    from django.db.models import Q
    fname = Q(firstname='Mark')
    lname = Q(lastname='Watney')
    Contact.objects.get(fname & lname)
    <Contact: Mark Watney>


    from django.db.models import Q
    fname = Q(firstname='Mark')
    lname = Q(lastname='Watney')
    Contact.objects.get(fname & lname)
    <Contact: Mark Watney>

    Contact.objects.filter(fname & lname)
    <QuerySet [<Contact: Mark Watney>]>


    astro1 = Q(firstname='Mark', lastname='Watney')
    astro2 = Q(firstname='Melissa', lastname='Lewis')
    Contact.objects.filter(astro1 | astro2)
    <QuerySet [<Contact: Mark Watney>, <Contact: Melissa Lewis>]>

    Contact.objects.filter(astro1|astro2 | (fname&lname))
    <QuerySet [<Contact: Mark Watney>, <Contact: Melissa Lewis>]>
    Contact.objects.filter(astro1|astro2 | ~(fname&lname))
    <QuerySet [<Contact: Mark Watney>, <Contact: Rick Martinez>, <Contact: Melissa Lewis>, <Contact: Jan Twardowski>, <Contact: Ivan Ivanovich>, <Contact: Jan X>, <Contact: Mark W>]>

    Contact.objects.filter( (astro1|astro2) & ~(fname&lname) )
    <QuerySet [<Contact: Melissa Lewis>]>

    mark = Q(contact__firstname='Mark')
    melissa = Q(contact__firstname='Melissa')
    Address.objects.filter(mark|melissa)
    <QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>, <Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>

    str(Address.objects.filter(mark|melissa).query)
    'SELECT "contact_address"."id", "contact_address"."contact_id", "contact_address"."type", "contact_address"."street", "contact_address"."house", "contact_address"."apartment", "contact_address"."postcode", "contact_address"."city", "contact_address"."region", "contact_address"."country" FROM "contact_address" INNER JOIN "contact_contact" ON ("contact_address"."contact_id" = "contact_contact"."id") WHERE ("contact_contact"."firstname" = Mark OR "contact_contact"."firstname" = Melissa)'



    Contact.objects.all().values('firstname', 'lastname')
    <QuerySet [{'firstname': 'Mark', 'lastname': 'Watney'}, {'firstname': 'Rick', 'lastname': 'Martinez'}, {'firstname': 'Melissa', 'lastname': 'Lewis'}, {'firstname': 'Jan', 'lastname': 'Twardowski'}, {'firstname': 'Ivan', 'lastname': 'Ivanovich'}, {'firstname': 'Jan', 'lastname': 'X'}, {'firstname': 'Mark', 'lastname': 'W'}]>
    Contact.objects.all().annotate(fullname=Concat('firstname', 'lastname'))
    <QuerySet [<Contact: Mark Watney>, <Contact: Rick Martinez>, <Contact: Melissa Lewis>, <Contact: Jan Twardowski>, <Contact: Ivan Ivanovich>, <Contact: Jan X>, <Contact: Mark W>]>
    Contact.objects.all().annotate(fullname=Concat('firstname', 'lastname')).values('fullname')
    <QuerySet [{'fullname': 'MarkWatney'}, {'fullname': 'RickMartinez'}, {'fullname': 'MelissaLewis'}, {'fullname': 'JanTwardowski'}, {'fullname': 'IvanIvanovich'}, {'fullname': 'JanX'}, {'fullname': 'MarkW'}]>
    Contact.objects.all().annotate(fullname=Concat('firstname', '', 'lastname')).values('fullname')
    Traceback (most recent call last):
    django.core.exceptions.FieldError: Cannot resolve keyword '' into field. Choices are: address, age, attachment, born, created_author, created_author_id, created_date, email, firstname, gender, height, homepage, id, is_adult, job, lastname, modified_author, modified_author_id, modified_date, notes, phone_country_code, phone_number, picture, salary, weight
    Contact.objects.all().annotate(fullname=Concat('firstname', Value(''), 'lastname')).values('fullname')
    <QuerySet [{'fullname': 'MarkWatney'}, {'fullname': 'RickMartinez'}, {'fullname': 'MelissaLewis'}, {'fullname': 'JanTwardowski'}, {'fullname': 'IvanIvanovich'}, {'fullname': 'JanX'}, {'fullname': 'MarkW'}]>
    Contact.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values('fullname')
    <QuerySet [{'fullname': 'Mark Watney'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Melissa Lewis'}, {'fullname': 'Jan Twardowski'}, {'fullname': 'Ivan Ivanovich'}, {'fullname': 'Jan X'}, {'fullname': 'Mark W'}]>

    Contact.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values('fullname')
    <QuerySet [{'fullname': 'Mark Watney'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Melissa Lewis'}, {'fullname': 'Jan Twardowski'}, {'fullname': 'Ivan Ivanovich'}, {'fullname': 'Jan X'}, {'fullname': 'Mark W'}]>



    result = Contact.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values('fullname')
    list(result)
    [{'fullname': 'Mark Watney'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Melissa Lewis'}, {'fullname': 'Jan Twardowski'}, {'fullname': 'Ivan Ivanovich'}, {'fullname': 'Jan X'}, {'fullname': 'Mark W'}]
    result = Contact.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).value_list('fullname')
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    AttributeError: 'QuerySet' object has no attribute 'value_list'
    result = Contact.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values_list('fullname')
    result
    <QuerySet [('Mark Watney',), ('Rick Martinez',), ('Melissa Lewis',), ('Jan Twardowski',), ('Ivan Ivanovich',), ('Jan X',), ('Mark W',)]>
    result = Contact.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values_list('fullname', flat=True)
    result
    <QuerySet ['Mark Watney', 'Rick Martinez', 'Melissa Lewis', 'Jan Twardowski', 'Ivan Ivanovich', 'Jan X', 'Mark W']>
    list(result)
    ['Mark Watney', 'Rick Martinez', 'Melissa Lewis', 'Jan Twardowski', 'Ivan Ivanovich', 'Jan X', 'Mark W']


    Contact.objects.count()
    7
    Contact.objects.filter(firstname='Mark').count()
    2


    from django.db.models import Avg, Sum, Min, Max, Count

    Contact.objects.all().aggregate(Avg('age'))
    {'age__avg': 30.0}
    Contact.objects.all().aggregate(Avg('age'))
    {'age__avg': 34.0}
    Contact.objects.all().aggregate(Max('age'))
    {'age__max': 45}
    Contact.objects.all().aggregate(Min('age'))
    {'age__min': 27}
    Contact.objects.all().aggregate(Sum('age'))
    {'age__sum': 102}
    Contact.objects.all().aggregate(Sum('salary'))
    {'salary__sum': Decimal('1024')}
    Contact.objects.all().aggregate(Avg('age'), Min('age'), Max('age'))
    {'age__avg': 34.0, 'age__min': 27, 'age__max': 45}

    below_30 = Count('age', filter=Q(age__lte=30))
    above_30 = Count('age', filter=Q(age__gt=30))
    Contact.objects.annotate(above_30=above_30).annotate(below_30=below_30).values('above_30', 'below_30')
    <QuerySet [{'above_30': 0, 'below_30': 1}, {'above_30': 1, 'below_30': 0}, {'above_30': 0, 'below_30': 0}, {'above_30': 0, 'below_30': 0}, {'above_30': 0, 'below_30': 1}, {'above_30': 0, 'below_30': 0}, {'above_30': 0, 'below_30': 0}]>


    from django.db.models import F
    Contact.objects.all().update(age=F('age')+1)



    mark = Contact.objects.get(firstname='Mark', lastname='Watney')
    mark.age = 10
    mark.save()
    mark = Contact.objects.get(firstname='Mark', lastname='Watney').update(age=37)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    AttributeError: 'Contact' object has no attribute 'update'
    Contact.objects.filter(firstname='Mark', lastname='Watney').update(age=37)
    1
    Contact.objects.filter(firstname='Mark').update(age=37)
    2



    Contact.objects.update_or_create(firstname='Mark', lastname='Watney')
    (<Contact: Mark Watney>, False)
    Contact.objects.update_or_create(firstname='Mark', lastname='WatneyXXX')
    (<Contact: Mark WatneyXXX>, True)
    c, status = Contact.objects.update_or_create(firstname='Mark', lastname='Watney')

    if status is True:
        print('Created')
    else:
        print('Updated')

    Updated
    c
    <Contact: Mark Watney>


    c, status = Contact.objects.update_or_create(firstname='Mark', lastname='Watney', defaults={'age': 30})
    c
    <Contact: Mark Watney>
    status
    False


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
... from myapp.models import Contact
...
...
... Contact.objects
...     .all()
...     .annotate(fullname=Concat('firstname', Value(' '), 'lastname'))
...     .values('fullname')
<QuerySet [{'fullname': 'Melissa Lewis'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Alex Vogel'}, {'fullname': 'Beth Johnssen'}, {'fullname': 'Jan Twardowski'}, {'fullname': 'Jan Twardowski'}]>
