**************
Dynamic Typing
**************


Duck typing
===========
W językach programowania można doszukać się wielu systemów typowania. System typowania informuje kompilator o obiekcie oraz o jego zachowaniach. Ponadto niesie za sobą informację na temat ilości pamięci, którą trzeba dla takiego obiektu zarezerwować. Istnieje nawet cała gałąź zajmująca się systemami typów. Obecnie najczęściej wykorzystywane języki programowania dzielą się na statycznie - silnie typowane (JAVA, C, C++ i pochodne) oraz dynamicznie - słabo typowane (Python, Ruby, PHP itp.). Oczywiście mogą znaleźć się rozwiązania hybrydowe oraz z tzw. inrefencją typów itp.

W naszym przypadku skupmy się na samym mechanizmie dynamicznego typowania. Określenie to oznacza, że język nie posiada typów zmiennych i obiektów, które jawnie trzeba deklarować. Inicjując zmienną nie musimy powiedzieć, że jest to ``int``. Co więcej po chwili do tej zmiennej możemy przypisać dowolny obiekt, np. łańcuch znaków i kompilator nie powie nam złego słowa. Kompilator podczas działania oprogramowania niejawnie może zmienić typ obiektu i dokonać na nim konwersji.

Wśród programistów popularne jest powiedzenie "jeżeli chodzi jak kaczka i kwacze jak kaczka, to musi być to kaczka". Od tego powiedzenia wzięła się nazwa Duck typing. Określenie to jest wykorzystywane w stosunku do języków, których typy obiektów rozpoznawane są po metodach, które można na nich wykonać. Nie zawsze takie zgadywanie jest celne i jednoznacznie i precyzyjnie określa typ. Może się okazać, że obiekt np. ``Samochód`` posiada metody ``uruchom_silnik()`` i ``jedz_prosto()`` podobnie jak ``Motor``. Jeden i drugi obiekt będzie zachowywał się podobnie. Języki wykorzystujące ten mechanizm wykorzystują specjalne metody porównawcze, które jednoznacznie dają informację kompilatorowi czy dwa obiekty są równe.

Sam mechanizm dynamicznego typowania jest dość kontrowersyjny, ze względu na możliwość bycia nieścisłym. W praktyce okazuje się, że rozwój oprogramowania wykorzystującego ten sposób jest dużo szybszy. Za to zwolennicy statycznego typowania, twierdzą, że projekty wykorzystujące duck typing są trudne w utrzymaniu po latach. Celem tego dokumentu nie jest udowadnianie wyższości jednego rozwiązania nad drugim. Zachęcam jednak do zapoznania się z wykładem "The Unreasonable Effectiveness of Dynamic Typing for Practical Programs", którego autorem jest "Robert Smallshire". Wykład zamieszczonym został w serwisie InfoQ (http://www.infoq.com/presentations/dynamic-static-typing). Wykład w ciekawy sposób dotyka problematyki porównania tych dwóch metod systemu typów. Wykład jest o tyle ciekawy, że bazuje na statystycznej analizie projektów umieszczonych na https://github.com a nie tylko bazuje na domysłach i flamewar jakie programiści lubią prowadzić.

.. code-block:: python
    :caption: Duck typing

    {}  # dict
    {1}  # set
    {1, 2}  # set
    {1: 2}  # dict
    {1: 1, 2: 2}  # dict

    my_data = {}
    isinstance(my_data, (set, dict))  # True

    isinstance(my_data, dict)  # True
    isinstance(my_data, set)  # False

    my_data = {1}
    isinstance(my_data, set)  # True
    isinstance(my_data, dict)  # False

    my_data = {1: 1}
    isinstance(my_data, set)  # False
    isinstance(my_data, dict)  # True


Everything is an object
=======================
* W Pythonie wszystkie rzeczy są obiektem.
* Każdy element posiada swoje metody, które możemy na nim uruchomić.
* W dalszej części tych materiałów będziemy korzystali z polecenia ``help()`` aby zobaczyć jakiego z jakiego typu obiektem mamy okazję pracować oraz co możemy z nim zrobić.

Object properties
-----------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b

    add_numbers.__doc__             # 'Function add numbers'
    add_numbers.__name__            # 'add_numbers'
    add_numbers.__annotations__     # {}
    add_numbers.__class__           # <class 'function'>

Object methods
--------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b

    add_numbers.__call__()          # TypeError: function() missing 2 required positional arguments: 'a' and 'b'
    add_numbers.__call__(1, 2)      # 3

Injecting properties
--------------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b


    add_numbers.my_variable = 10

    print(add_numbers.my_variable)
    # 10

Injecting methods
-----------------
 .. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b


    add_numbers.say_hello = lambda name: print(f'Hello {name}')

    add_numbers.say_hello('Jan Twardowski')
    # Hello Jan Twardowski


Monkey Patching
===============

Recap information about classes and objects
-------------------------------------------
.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jose Jimenez'

        def hello(self):
            print(f'My name... {self.name}')

    u = User()
    u.hello()
    # My name... Jose Jimenez

.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jose Jimenez'

        def hello(self):
            print(f'My name... {self.name}')

    User.hello()
    # TypeError: hello() missing 1 required positional argument: 'self'

Injecting fields
----------------
.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jose Jimenez'

        def hello(self):
            print(f'My name... {self.name}')


    User.agency = 'NASA'    # Injecting static field

    print(User.agency)
    # NASA


Injecting methods
-----------------
.. code-block:: python

    class User:
        def hello(self):
            print('Hello from User')


    def my_function():
        print('New Version')


    User.hello = my_function
    User.hello()
    # 'New Version'

.. code-block:: python

    class User:
        pass


    User.hello = lambda name: print(f'Hello {name}')

    User.hello('Jan Twardowski')
    # Hello Jan Twardowski

.. code-block:: python

    class User:
        pass

    u = User()
    u.hello = lambda name: print(f'Hello {name}')

    u.hello('Jan Twardowski')
    # Hello Jan Twardowski

.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jan Twardowski'
        pass

    u = User()
    u.hello = lambda self: print(f'Hello {self.name}')

    u.hello()
    # TypeError: <lambda>() missing 1 required positional argument: 'self'

.. code-block:: python

    class User:
        pass

    User.hello = lambda self: print(f'Hello {self.name}')

    u = User()
    u.name = 'Jan Twardowski'

    u.hello()
    # Hello Jan Twardowski

Use case
--------
.. code-block:: python

    import datetime
    import json


    def datetime_encoder(self, obj):
        if isinstance(obj, datetime.date):
            return f'{obj:%Y-%m-%d}'
        else:
            return str(obj)

    json.JSONEncoder.default = datetime_encoder

    data = {"datetime": datetime.date(1961, 4, 12)}
    json.dumps(data)
    # {"datetime": "1961-04-12"}
