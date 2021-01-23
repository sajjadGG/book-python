References in the Book
======================


Assignment levels
-----------------
* Easy - taks is almost identical to listings described in this section, changes are only in variable names and values
* Medium - task uses knowledge and skills acquired prior to this chapter
* Hard - task requires extra skills or Python stdlib and ecosystem knowledge (check hints section below assignment)
* Sub-project - task is part of bigger project completed over whole chapter


Ehlo World!
-----------
W lekcjach programowania utarło się, że zawsze zaczynamy od już przysłowiowego "Hello World".
Tym razem jednak zaczniemy od 'Ehlo World!' i nie jest to pomyłka.
Jest to przywitanie serwera SMTP.
W tej książce znajdziesz kilka żartów informatycznych i nawiązań do starych


Datasets
--------
>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...         (7.6, 3.0, 6.6, 2.1, 'virginica'),
...         (4.9, 3.0, 1.4, 0.2, 'setosa'),
...         (4.9, 2.5, 4.5, 1.7, 'virginica'),
...         (7.1, 3.0, 5.9, 2.1, 'virginica'),
...         (4.6, 3.4, 1.4, 0.3, 'setosa'),
...         (5.4, 3.9, 1.7, 0.4, 'setosa'),
...         (5.7, 2.8, 4.5, 1.3, 'versicolor'),
...         (5.0, 3.6, 1.4, 0.3, 'setosa'),
...         (5.5, 2.3, 4.0, 1.3, 'versicolor'),
...         (6.5, 3.0, 5.8, 2.2, 'virginica'),
...         (6.5, 2.8, 4.6, 1.5, 'versicolor'),
...         (6.3, 3.3, 6.0, 2.5, 'virginica'),
...         (6.9, 3.1, 4.9, 1.5, 'versicolor'),
...         (4.6, 3.1, 1.5, 0.2, 'setosa')]

>>> X = [5.8, 2.7, 5.1, 1.9]
>>> y = 'virginica'
>>>
>>> X = [5.8, 2.7, 5.1, 1.9]
>>> x1 = 5.8
>>> x2 = 2.7
>>> x3 = 5.1
>>> x4 = 1.9
>>>
>>> for x in X:
...     pass
>>>
>>> for *X,y in DATA[1:]:
...     pass

Iris flower species:

.. figure:: img/about-references-iris-species.jpg

Iris dataset:

.. figure:: img/about-references-iris-dataset.png

Iris features distribution:

.. figure:: img/about-references-iris-grid.png


Addresses
---------
* POLSA - Polish Space Agency
* ESA - European Space Agency
* NASA - National Aeronautics and Space Administration, USA

.. csv-table:: Addresses used in a book
    :header-rows: 1

    "name", "street", "city", "post_code", "state", "country"
    "Kosmodrom Bajkonur", "Wochod", "Bajkonur", "101503", "Kyzyłordyński", "Kazachstan"
    "Johnson Space Center", "2101 E NASA Pkwy", "Huston", "77058", "Texas", "USA"
    "Kennedy Space Center", None, "Cape Canaveral", "32899", "Floryda", "USA"
    "NASA Jet Propulsion Laboratory", "4800 Oak Grove Dr", "Pasadena", "91109", "California", "USA"
    "NASA Armstrong Research Center", "2825 E Ave P", "Palmdale", 93550, "California", "USA"
    "ESA EAC", "Linder Hoehe", "Köln", "51147", "North Rhine-Westphalia", "Germany"

.. code-block:: python

    DATA = [
        {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
            {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Małopolskie", "country": "Poland"}]},

        {"firstname": "José", "lastname": "Jiménez", "addresses": [
            {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
            {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

        {"firstname": "Mark", "lastname": "Watney", "addresses": [
            {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
            {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

        {"firstname": "Иван", "lastname": "Иванович", "addresses": [
            {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
            {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

        {"firstname": "Melissa", "lastname": "Lewis"},

        {"firstname": "Alex", "lastname": "Vogel", "addresses": [
            {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
    ]


Dates and Timezones
-------------------
* ``1957-10-04 19:28:34 UTC`` - Sputnik launch
* ``1961-04-12 06:07:00 UTC`` - Yuri Gagarin's launch
* ``1969-07-21 02:56:15 UTC`` - Apollo 11 Neil Armstrong's first step on the Moon

>>> from datetime import datetime, date, timezone
>>> DATA = {'mission': 'Ares 3',
...         'launch_date': datetime(2035, 6, 29, tzinfo=timezone.utc),
...         'destination': 'Mars',
...         'destination_landing': datetime(2035, 11, 7, tzinfo=timezone.utc),
...         'destination_location': 'Acidalia Planitia',
...         'crew': [{'astronaut': 'Melissa Lewis', 'date_of_birth': date(1995, 7, 15)},
...                  {'astronaut': 'Rick Martinez', 'date_of_birth': date(1996, 1, 21)},
...                  {'astronaut': 'Alex Vogel', 'date_of_birth': date(1994, 11, 15)},
...                  {'astronaut': 'Chris Beck', 'date_of_birth': date(1999, 8, 2)},
...                  {'astronaut': 'Beth Johansen', 'date_of_birth': date(2006, 5, 9)},
...                  {'astronaut': 'Mark Watney', 'date_of_birth': date(1994, 10, 12)}]}

.. code-block:: json

    {"mission": "Ares 3",
     "launch_date": "2035-06-29T00:00:00+00:00",
     "destination": "Mars",
     "destination_landing": "2035-11-07T00:00:00+00:00",
     "destination_location": "Acidalia Planitia",
     "crew": [{"astronaut": "Melissa Lewis", "date_of_birth": "1995-07-15"},
              {"astronaut": "Rick Martinez", "date_of_birth": "1996-01-21"},
              {"astronaut": "Alex Vogel", "date_of_birth": "1994-11-15"},
              {"astronaut": "Chris Beck", "date_of_birth": "1999-08-02"},
              {"astronaut": "Beth Johansen", "date_of_birth": "2006-05-09"},
              {"astronaut": "Mark Watney", "date_of_birth": "1994-10-12"}]}

.. code-block:: json

    [{"model":"authorization.user","pk":1,"fields":{"firstname":"Melissa","lastname":"Lewis","role":"commander","username":"mlewis","password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","email":"melissa.lewis@nasa.gov","date_of_birth":"1995-07-15","last_login":"1970-01-01T00:00:00.000Z","is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"firstname":"Rick","lastname":"Martinez","role":"pilot","username":"rmartinez","password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","date_of_birth":"1996-01-21","last_login":null,"email":"rick.martinez@ansa.gov","is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"firstname":"Alex","lastname":"Vogel","role":"chemist","username":"avogel","password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","email":"alex.vogel@esa.int","date_of_birth":"1994-11-15","last_login":null,"is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"firstname":"Chris","lastname":"Beck","role":"crew-medical-officer","username":"cbeck","password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","email":"chris.beck@nasa.gov","date_of_birth":"1999-08-02","last_login":"1970-01-01T00:00:00.000Z","is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"firstname":"Beth","lastname":"Johansen","role":"sysop","username":"bjohansen","password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","email":"","date_of_birth":"2006-05-09","last_login":null,"is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"firstname":"Mark","lastname":"Watney","role":"botanist","username":"mwatney","password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","email":"","date_of_birth":"1994-10-12","last_login":null,"is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}}]


Characters
----------
Jan Twardowski:

    * Wizard from Polish fairytale who escaped before the devil to the Moon
    * Modern Film Adaptation by Allegro: https://www.youtube.com/watch?v=hRdYz8cnOW4

    .. figure:: img/about-references-jan-twardowski.jpg

Mark Watney:

    * Fictional NASA Astronaut
    * From Andy Weir's book "The Martian"
    * From Ridley Scott movie "The Martian" (book adaptation)

    .. figure:: img/about-references-mark-watney.jpg

Иван Иванович:

    * Ivan Ivanovich
    * Dummy used in Soviet space program before Gagarin's Launch

    .. figure:: img/about-references-ivan-ivanovich.jpg

José Jiménez:

    * Fictional character created and performed by comedian Bill Dana
    * Introduced himself with the catch phrase: "My name... José Jiménez"
    * Jiménez as an astronaut, 1963. Fictional character created and performed by comedian Bill Dana
    * https://www.youtube.com/watch?v=kPnaaHR9pLc
    * https://www.youtube.com/watch?v=i6ckW7uRRNw
    * https://www.youtube.com/watch?v=PVxfJYw59cM
    * https://www.youtube.com/watch?v=i6ckW7uRRNw
    * https://www.youtube.com/watch?v=PVxfJYw59cM
    * https://youtu.be/kPnaaHR9pLc?t=16

    .. figure:: img/about-references-jose-jimenez.jpg

Melissa Lewis:

    * Fictional NASA Astronaut
    * From Andy Weir's book "The Martian"
    * From Ridley Scott movie "The Martian" (book adaptation)

    .. figure:: img/about-references-melissa-lewis.jpg

Ryan Stone:

    * Fictional NASA Astronaut
    * From the movie "Gravity"

    .. figure:: img/about-references-ryan-stone.jpg

Matt Kowalski:

    * Fictional NASA Astronaut
    * From the movie "Gravity"
    * From Alfonso Cuarón's movie `Gravity <https://www.imdb.com/title/tt1454468/>`_

    .. figure:: img/about-references-matt-kowalski.jpg

Alex Vogel:

    * Fictional NASA Astronaut
    * From Andy Weir's book "The Martian"
    * From Ridley Scott movie "The Martian" (book adaptation)

    .. figure:: img/about-references-alex-vogel.jpg

National Geographic Mars Crew Members:

    * Robert Foucault (top left)
    * Javier Delgado (top center)
    * Amelie Durand (top right)
    * Hana Seung (bottom left)
    * Ben Sawyer (bottom center)
    * Marta Kamen (bottom right)

    .. figure:: img/about-references-crew-mars-natgeo.jpg

Martian Movie Crew Members:

    * Melissa Lewis (top left)
    * Alex Vogel (top center)
    * Mark Watney (top right)
    * Chris Beck (bottom left)
    * Beth Johanssen (bottom center)
    * Rick Martinez (bottom right)

    .. figure:: img/about-references-crew-martian.jpg

