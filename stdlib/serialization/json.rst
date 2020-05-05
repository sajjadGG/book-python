******************
Serialization JSON
******************


JSON syntax
===========
* JSON format is similar to ``dict`` notation in Python
* Differences:

    * Coma ``,`` is not allowed after the last element in list or object
    * Fields are enclosed only by double quote ``"`` character
    * ``true`` and ``false`` is always lower-cased
    * Instead of ``None`` there is ``null``
    * ``camelCase`` is convention, although ``snake_case`` is also valid

.. code-block:: json
    :caption: Example JSON file

    [
        {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
        {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
        {"sepalLength": false, "sepalWidth": true, "petalLength": null, "petalWidth": 0.2, "species": null}
    ]

.. code-block:: json
    :caption: JSON or Python ``List[dict]``?

    [
        {"first_name": "Jan", "last_name": "Twardowski", "addresses": [
            {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Małopolskie", "country": "Poland"}]},

        {"first_name": "José", "last_name": "Jiménez", "addresses": [
            {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
            {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

        {"first_name": "Mark", "last_name": "Watney", "addresses": [
            {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
            {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

        {"first_name": "Иван", "last_name": "Иванович", "addresses": [
            {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
            {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

        {"first_name": "Melissa", "last_name": "Lewis", "addresses": []},

        {"first_name": "Alex", "last_name": "Vogel", "addresses": [
            {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
    ]

JSON Serialization of simple objects
====================================
To file:

    * ``json.dump(DATA: dict, file: TextIOWrapper) -> None``
    * ``json.load(file: TextIOWrapper) -> None``

To string:

    * ``json.dumps(DATA: dict) -> str``
    * ``json.loads(DATA: str) -> dict``

Serialize to JSON
-----------------
.. code-block:: python
    :caption: Serialize to JSON

    import json


    DATA = {
        'first_name': 'Jan',
        'last_name': 'Twardowski'
    }

    output = json.dumps(DATA)
    print(output)
    # '{"first_name": "Jan", "last_name": "Twardowski"}'

Deserialize from JSON
---------------------
.. code-block:: python
    :caption: Deserialize from JSON

    import json


    DATA = '{"first_name": "Jan", "last_name": "Twardowski"}'

    output = json.loads(DATA)
    print(output)
    # {
    #     'first_name': 'Jan',
    #     'last_name': 'Twardowski'
    # }


Serializing ``datetime`` and ``date``
=====================================

Encoding ``datetime`` and ``date``
----------------------------------
* Encoder will be used, when standard procedure fails

.. code-block:: python
    :caption: Exception during encoding datetime

    from datetime import datetime, date
    import json


    DATA = {
        'name': 'Jan Twardowski',
        'date': date(1961, 4, 12),
        'datetime': datetime(1969, 7, 21, 2, 56, 15),
    }

    output = json.dumps(DATA)
    # TypeError: Object of type date is not JSON serializable

.. code-block:: python
    :caption: Encoding ``datetime`` and ``date``

    from datetime import datetime, date
    import json


    DATA = {
        'name': 'Jan Twardowski',
        'date': date(1961, 4, 12),
        'datetime': datetime(1969, 7, 21, 2, 56, 15),
    }


    class JSONDatetimeEncoder(json.JSONEncoder):
        def default(self, value):

            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

            if isinstance(value, date):
                return value.strftime('%Y-%m-%d')


    output = json.dumps(DATA, cls=JSONDatetimeEncoder)
    print(output)
    # '{"name": "Jan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T02:56:15.000Z"}'


Decoding ``datetime`` and ``date``
----------------------------------
.. code-block:: python
    :caption: Simple loading returns ``str`` not ``datetime`` or ``date``

    import json


    DATA = '{"name": "Jan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T02:56:15.000Z"}'

    output = json.loads(DATA)
    print(output)
    # {
    #     'name': 'Jan Twardowski',
    #     'date': '1961-04-12',
    #     'datetime': '1969-07-21T02:56:15.000Z',
    # }

.. code-block:: python
    :caption: Decoding ``datetime`` and ``date``

    from datetime import datetime, timezone
    import json


    DATA = '{"name": "Jan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T02:56:15.000Z"}'


    class JSONDatetimeDecoder(json.JSONDecoder):
        DATE_FIELDS = ['date', 'date_of_birth']
        DATETIME_FIELDS = ['datetime']

        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, output: dict) -> dict:
            for field, value in output.items():

                if field in self.DATE_FIELDS:
                    value = datetime.strptime(value, '%Y-%m-%d').date()

                if field in self.DATETIME_FIELDS:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)

                output[field] = value
            return output


    output = json.loads(DATA, cls=JSONDatetimeDecoder)
    print(output)
    # {
    #     'name': 'Jan Twardowski',
    #     'date': date(1961, 4, 12),
    #     'datetime': datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc),
    # }


Serializing objects
===================

Encoding nested objects with relations to JSON
----------------------------------------------
* Encoder will be used, when standard procedure fails

.. code-block:: python
    :caption: Encoding nested objects with relations to JSON

    import json


    class Astronaut:
        def __init__(self, name, missions=()):
            self.name = name
            self.missions = missions


    class Mission:
        def __init__(self, year, name):
            self.year = year
            self.name = name


    CREW = [
        Astronaut('Jan Twardowski', missions=(
            Mission(1969, 'Apollo 18'),
            Mission(2024, 'Artemis 3'))),

        Astronaut('Mark Watney', missions=(
            Mission(2035, 'Ares 3'))),

        Astronaut('Melissa Lewis'),
    ]


    class JSONObjectEncoder(json.JSONEncoder):
        def default(self, obj):
            result = obj.__dict__
            result['__class_name__'] = obj.__class__.__name__
            return result


    output = json.dumps(CREW, cls=JSONObjectEncoder, sort_keys=True, indent=2)
    print(output)
    # [
    #   {
    #     "name": "Jan Twardowski",
    #     "missions": [
    #       {
    #         "year": 1969,
    #         "name": "Apollo 18",
    #         "__class_name__": "Mission"
    #       },
    #       {
    #         "year": 2024,
    #         "name": "Artemis 3",
    #         "__class_name__": "Mission"
    #       }
    #     ],
    #     "__class_name__": "Astronaut"
    #   },
    #   {
    #     "name": "Mark Watney",
    #     "missions": {
    #       "year": 2035,
    #       "name": "Ares 3",
    #       "__class_name__": "Mission"
    #     },
    #     "__class_name__": "Astronaut"
    #   },
    #   {
    #     "name": "Melissa Lewis",
    #     "missions": [],
    #     "__class_name__": "Astronaut"
    #   }
    # ]

Decoding nested objects with relations to JSON
----------------------------------------------
.. code-block:: python
    :caption:  Encoding nested objects with relations to JSON

    import json
    import sys

    DATA = """[{"name": "Jan Twardowski", "missions": [{"year": 1969, "name": "Apollo 18", "__class_name__": "Mission"}, {"year": 2024, "name": "Artemis 3", "__class_name__": "Mission"}], "__class_name__": "Astronaut"}, {"name": "Mark Watney", "missions": {"year": 2035, "name": "Ares 3", "__class_name__": "Mission"}, "__class_name__": "Astronaut"}, {"name": "Melissa Lewis", "missions": [], "__class_name__": "Astronaut"}]"""


    class Astronaut:
        def __init__(self, name, missions=()):
            self.name = name
            self.missions = missions

        def __repr__(self):
            return f'\n\nAstronaut(name="{self.name}", missions={self.missions})'


    class Mission:
        def __init__(self, year, name):
            self.year = year
            self.name = name

        def __repr__(self):
            return f'\n\tMission(year={self.year}, name="{self.name}")'


    class JSONObjectDecoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, obj):
            class_name = obj.pop('__class_name__')
            cls = getattr(sys.modules[__name__], class_name)
            return cls(**obj)


    output = json.loads(DATA, cls=JSONObjectDecoder)
    print(output)
    # Astronaut(name="Jan Twardowski", missions=[
    #    Mission(year=1969, name="Apollo 18"),
    #    Mission(year=2024, name="Artemis 3")]),
    #
    # Astronaut(name="Mark Watney", missions=
    #    Mission(year=2035, name="Ares 3")),
    #
    # Astronaut(name="Melissa Lewis", missions=[])]


Pretty Printing JSON
====================

JSON can be minified
--------------------
* Save space for network transmission
* It is not very readable

.. code-block:: console
    :caption: Minified JSON file

    $ DATA='https://raw.githubusercontent.com/AstroMatt/book-python/master/stdlib/serialization/data/iris.json'
    $ curl $DATA
    [{"sepalLength":5.1,"sepalWidth":3.5,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.7,"sepalWidth":3.2,"petalLength":1.3,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.6,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5.4,"sepalWidth":3.9,"petalLength":1.7,"petalWidth":0.4,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.4,"petalLength":1.4,"petalWidth":0.3,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.4,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.4,"sepalWidth":2.9,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.1,"species":"setosa"},{"sepalLength":7,"sepalWidth":3.2,"petalLength":4.7,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.4,"sepalWidth":3.2,"petalLength":4.5,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":6.9,"sepalWidth":3.1,"petalLength":4.9,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.5,"sepalWidth":2.3,"petalLength":4,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.5,"sepalWidth":2.8,"petalLength":4.6,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.7,"sepalWidth":2.8,"petalLength":4.5,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":4.7,"petalWidth":1.6,"species":"versicolor"},{"sepalLength":4.9,"sepalWidth":2.4,"petalLength":3.3,"petalWidth":1,"species":"versicolor"},{"sepalLength":6.6,"sepalWidth":2.9,"petalLength":4.6,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":5.2,"sepalWidth":2.7,"petalLength":3.9,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":6,"petalWidth":2.5,"species":"virginica"},{"sepalLength":5.8,"sepalWidth":2.7,"petalLength":5.1,"petalWidth":1.9,"species":"virginica"},{"sepalLength":7.1,"sepalWidth":3,"petalLength":5.9,"petalWidth":2.1,"species":"virginica"},{"sepalLength":6.3,"sepalWidth":2.9,"petalLength":5.6,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.5,"sepalWidth":3,"petalLength":5.8,"petalWidth":2.2,"species":"virginica"},{"sepalLength":7.6,"sepalWidth":3,"petalLength":6.6,"petalWidth":2.1,"species":"virginica"},{"sepalLength":4.9,"sepalWidth":2.5,"petalLength":4.5,"petalWidth":1.7,"species":"virginica"},{"sepalLength":7.3,"sepalWidth":2.9,"petalLength":6.3,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.7,"sepalWidth":2.5,"petalLength":5.8,"petalWidth":1.8,"species":"virginica"},{"sepalLength":7.2,"sepalWidth":3.6,"petalLength":6.1,"petalWidth":2.5,"species":"virginica"}]

Pretty Printing JSON
--------------------
.. code-block:: console
    :caption: Pretty Printing JSON

    $ DATA='https://raw.githubusercontent.com/AstroMatt/book-python/master/stdlib/serialization/data/iris.json'
    $ curl $DATA |python -m json.tool
    [
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 5.1,
            "sepalWidth": 3.5,
            "species": "setosa"
        },
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 4.9,
            "sepalWidth": 3,
            "species": "setosa"
        },
        {
            "petalLength": 1.3,
            "petalWidth": 0.2,
            "sepalLength": 4.7,
            "sepalWidth": 3.2,
            "species": "setosa"
        },
    ...

Check JSON syntax validity
--------------------------
.. code-block:: console
    :caption: ``json.tool`` checks JSON syntax validity

    $ echo '{"sepalLength":5.1,"sepalWidth":3.5,}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 37 (char 36)


Assignments
===========

Serialize nested sequences to JSON
----------------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/json_dump.py`

:English:
    #. Extract from input a header and data
    #. Create ``List[dict]``

        - key: name from the header
        - value: measurement or species

    #. Write structure to file ``iris_serialize.json`` in JSON format

:Polish:
    #. Z danych wydziel nagłówek i pomiary
    #. Wygeneruj ``List[dict]``

        - klucz: nazwa z nagłówka
        - wartość: wyniki pomiarów lub gatunek

    #. Zapisz strukturę do pliku ``iris_serialize.json`` w formacie JSON

:The whys and wherefores:
    * Serializing nested data structures
    * Using stdlib ``json`` library
    * Type casting
    * Working with files

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python
        :caption: Output

        output: List[dict] = [
            {'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            ...
        ]

Deserialize nested sequences from JSON
--------------------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/json_load.py`

:English:
    #. Write input data to "iris_deserialize.json"
    #. Read file and print data in ``List[tuple]`` format
    #. First line must be a header
    #. Other lines must contain data

:Polish:
    #. Dane z listingu poniżej skopiuj do pliku "iris_deserialize.json"
    #. Odczytaj dane z pliku, i wyświetl je w formacie ``List[tuple]``
    #. Pierwsza linijka ma zawierać nagłówek
    #. Kolejne linie mają mieć dane

:The whys and wherefores:
    * Serializing nested data structures
    * Using stdlib ``json`` library
    * Type casting
    * Working with files

:Input:
    .. literalinclude:: data/iris.json
        :language: json

Serializing datetime to JSON
----------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/json_datetime.py`

:Enlish:
    #. Copy input data to your script
    #. Save data to file in JSON format
    #. Read data from file
    #. Recreate data structure

:Polish:
    #. Skopiuj dane wejściowe do swojego skryptu
    #. Zapisz dane do pliku w formacie JSON
    #. Odczytaj dane z pliku
    #. Odtwórz strukturę danych

:The whys and wherefores:
    * Serializing nested data structures
    * Using stdlib ``json`` library
    * Serialize and deserialize ``date`` and ``datetime`` objects

:Input:
    .. code-block:: python

        from datetime import datetime, date


        DATA = {
            "astronaut": {
                "date": date(1961, 4, 12),
                "person": "jose.jimenez@nasa.gov"
            },
            "flight": [
                {"datetime": datetime(1969, 7, 21, 2, 56, 15), "action": "landing"}
            ]
        }

Serializing objects to JSON
---------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

:English:
    #. Copy input data in JSON format to your script
    #. Convert from JSON format to Python
    #. Create classes ``Setosa``, ``Virginica``, ``Versicolor`` representing data
    #. Reading file create instances of those classes based on value in field "species"

:Polish:
    #. Skopiuj dane wejściowe w formacie JSON do swojego skryptu
    #. Przekonwertuj dane z JSON do Python
    #. Stwórz klasy ``Setosa``, ``Virginica``, ``Versicolor`` reprezentujące dane
    #. Czytając plik twórz obiekty powyższych klas w zależności od wartości pola "species"

:The whys and wherefores:
    * Serializing nested data structures
    * Using stdlib ``json`` library
    * Serialize and deserialize objects

:Input:
    .. code-block:: json

        [
            {"sepalLength": 5.0, "sepalWidth": 3.6, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 4.9, "sepalWidth": 3.1, "petalLength": 1.5, "petalWidth": 0.1, "species": "setosa"},
            {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 7.0, "sepalWidth": 3.2, "petalLength": 4.7, "petalWidth": 1.4, "species": "versicolor"},
            {"sepalLength": 4.6, "sepalWidth": 3.1, "petalLength": 1.5, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 6.5, "sepalWidth": 3.0, "petalLength": 5.8, "petalWidth": 2.2, "species": "virginica"},
            {"sepalLength": 7.1, "sepalWidth": 3.0, "petalLength": 5.9, "petalWidth": 2.1, "species": "virginica"},
            {"sepalLength": 6.7, "sepalWidth": 2.5, "petalLength": 5.8, "petalWidth": 1.8, "species": "virginica"},
            {"sepalLength": 5.2, "sepalWidth": 2.7, "petalLength": 3.9, "petalWidth": 1.4, "species": "versicolor"},
            {"sepalLength": 5.0, "sepalWidth": 3.4, "petalLength": 1.5, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 4.9, "sepalWidth": 2.4, "petalLength": 3.3, "petalWidth": 1.0, "species": "versicolor"},
            {"sepalLength": 6.5, "sepalWidth": 2.8, "petalLength": 4.6, "petalWidth": 1.5, "species": "versicolor"},
            {"sepalLength": 5.4, "sepalWidth": 3.9, "petalLength": 1.7, "petalWidth": 0.4, "species": "setosa"},
            {"sepalLength": 6.3, "sepalWidth": 3.3, "petalLength": 4.7, "petalWidth": 1.6, "species": "versicolor"},
            {"sepalLength": 6.4, "sepalWidth": 3.2, "petalLength": 4.5, "petalWidth": 1.5, "species": "versicolor"},
            {"sepalLength": 6.6, "sepalWidth": 2.9, "petalLength": 4.6, "petalWidth": 1.3, "species": "versicolor"},
            {"sepalLength": 5.8, "sepalWidth": 2.7, "petalLength": 5.1, "petalWidth": 1.9, "species": "virginica"},
            {"sepalLength": 6.3, "sepalWidth": 2.9, "petalLength": 5.6, "petalWidth": 1.8, "species": "virginica"},
            {"sepalLength": 7.6, "sepalWidth": 3.0, "petalLength": 6.6, "petalWidth": 2.1, "species": "virginica"},
            {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 7.3, "sepalWidth": 2.9, "petalLength": 6.3, "petalWidth": 1.8, "species": "virginica"},
            {"sepalLength": 4.7, "sepalWidth": 3.2, "petalLength": 1.3, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 6.9, "sepalWidth": 3.1, "petalLength": 4.9, "petalWidth": 1.5, "species": "versicolor"},
            {"sepalLength": 7.2, "sepalWidth": 3.6, "petalLength": 6.1, "petalWidth": 2.5, "species": "virginica"},
            {"sepalLength": 4.4, "sepalWidth": 2.9, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
            {"sepalLength": 5.5, "sepalWidth": 2.3, "petalLength": 4.0, "petalWidth": 1.3, "species": "versicolor"},
            {"sepalLength": 4.6, "sepalWidth": 3.4, "petalLength": 1.4, "petalWidth": 0.3, "species": "setosa"},
            {"sepalLength": 6.3, "sepalWidth": 3.3, "petalLength": 6.0, "petalWidth": 2.5, "species": "virginica"},
            {"sepalLength": 4.9, "sepalWidth": 2.5, "petalLength": 4.5, "petalWidth": 1.7, "species": "virginica"},
            {"sepalLength": 5.7, "sepalWidth": 2.8, "petalLength": 4.5, "petalWidth": 1.3, "species": "versicolor"}
        ]

Deserialize data from GitHub
----------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/json_github.py`

:English:
    #. Use ``requests`` library (requires installation)
    #. Download data from https://api.github.com/users
    #. Model data as class ``User``
    #. Iterate over records and create instances of this class
    #. Collect all instances to one list

:Polish:
    #. Użyj biblioteki ``requests`` (wymagana instalacja)
    #. Pobierz dane z https://api.github.com/users
    #. Zamodeluj dane za pomocą klasy ``User``
    #. Iterując po rekordach twórz instancje tej klasy
    #. Zbierz wszystkie instancje do jednej listy

:The whys and wherefores:
    * Serializing nested data structures
    * Using stdlib ``json`` library
    * Serialize and deserialize nested objects
    * Model data from API
