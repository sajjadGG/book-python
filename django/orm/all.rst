.. testsetup::

    # doctest: +SKIP_FILE


ORM All
=======


All
---
>>> Address.objects.all()
<QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>, <Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>


>>> Address.objects.all()
<QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>, <Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>


Order
-----
>>> Person.objects.all().order_by('lastname')
<QuerySet [<Person: Mark Watney>, <Person: Melissa Lewis>, <Person: Rick Martinez>, <Person: Mark W>, <Person: Mark Watney>]>

>>> Person.objects.all().order_by('-lastname')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>, <Person: Rick Martinez>, <Person: Melissa Lewis>, <Person: Mark Watney>]>

>>> Person.objects.all().order_by('-lastname', 'firstname')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>, <Person: Rick Martinez>, <Person: Melissa Lewis>, <Person: Mark Watney>]>


Values
------
>>> Person.objects.all().values('firstname')
<QuerySet [{'firstname': 'Mark'}, {'firstname': 'Rick'}, {'firstname': 'Melissa'}, {'firstname': 'Mark'}, {'firstname': 'Watney'}, {'firstname': 'Mark'}]>

>>> Person.objects.all().values('firstname').distinct()
<QuerySet [{'firstname': 'Mark'}, {'firstname': 'Rick'}, {'firstname': 'Melissa'}, {'firstname': 'Mark'}]>

>>> c = Person.objects.all()
>>> fname = c.values('firstname')
>>> lname = c.values('lastname')
>>>
>>> fname
<QuerySet [{'firstname': 'Mark'}, {'firstname': 'Rick'}, {'firstname': 'Melissa'}, {'firstname': 'Mark'}, {'firstname': 'Mark'}]>
>>>
>>> lname
<QuerySet [{'lastname': 'Watney'}, {'lastname': 'Lewis'}, {'lastname': 'Martinez'}, {'lastname': 'W'}, {'lastname': 'Watney'}]>


Debug
-----
>>> str(Person.objects.all().query)
'SELECT "Person_Person"."id", "Person_Person"."created_date", "Person_Person"."created_author_id", "Person_Person"."modified_date", "Person_Person"."modified_author_id", "Person_Person"."firstname", "Person_Person"."lastname", "Person_Person"."salary", "Person_Person"."job", "Person_Person"."born", "Person_Person"."age", "Person_Person"."gender", "Person_Person"."is_adult", "Person_Person"."weight", "Person_Person"."height", "Person_Person"."email", "Person_Person"."homepage", "Person_Person"."phone_country_code", "Person_Person"."phone_number", "Person_Person"."picture", "Person_Person"."attachment", "Person_Person"."notes" FROM "Person_Person"'

>>> str(Person.objects.all().values('firstname').query)
'SELECT "Person_Person"."firstname" FROM "Person_Person"'

>>> str(Person.objects.all().values('firstname', 'lastname').query)
'SELECT "Person_Person"."firstname", "Person_Person"."lastname" FROM "Person_Person"'
