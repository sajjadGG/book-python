.. _Advanced OOP:

************
Advanced OOP
************


Everything is an object
=======================
* W Pythonie wszystkie rzeczy są obiektem.
* Każdy element posiada swoje metody, które możemy na nim uruchomić.
* W dalszej części tych materiałów będziemy korzystali z polecenia ``help()`` aby zobaczyć jakiego z jakiego typu obiektem mamy okazję pracować oraz co możemy z nim zrobić.


Duck typing
===========
W językach programowania można doszukać się wielu systemów typowania. System typowania informuje kompilator o obiekcie oraz o jego zachowaniach. Ponadto niesie za sobą informację na temat ilości pamięci, którą trzeba dla takiego obiektu zarezerwować. Istnieje nawet cała gałąź zajmująca się systemami typów. Obecnie najczęściej wykorzystywane języki programowania dzielą się na statycznie - silnie typowane (JAVA, C, C++ i pochodne) oraz dynamicznie - słabo typowane (Python, Ruby, PHP itp.). Oczywiście mogą znaleźć się rozwiązania hybrydowe oraz z tzw. inrefencją typów itp.

W naszym przypadku skupmy się na samym mechanizmie dynamicznego typowania. Określenie to oznacza, że język nie posiada typów zmiennych i obiektów, które jawnie trzeba deklarować. Inicjując zmienną nie musimy powiedzieć, że jest to ``int``. Co więcej po chwili do tej zmiennej możemy przypisać dowolny obiekt, np. łańcuch znaków i kompilator nie powie nam złego słowa. Kompilator podczas działania oprogramowania niejawnie może zmienić typ obiektu i dokonać na nim konwersji.

Wśród programistów popularne jest powiedzenie "jeżeli chodzi jak kaczka i kwacze jak kaczka, to musi być to kaczka". Od tego powiedzenia wzięła się nazwa Duck typing. Określenie to jest wykorzystywane w stosunku do języków, których typy obiektów rozpoznawane są po metodach, które można na nich wykonać. Nie zawsze takie zgadywanie jest celne i jednoznacznie i precyzyjnie określa typ. Może się okazać, że obiekt np. ``Samochód`` posiada metody ``uruchom_silnik()`` i ``jedz_prosto()`` podobnie jak ``Motor``. Jeden i drugi obiekt będzie zachowywał się podobnie. Języki wykorzystujące ten mechanizm wykorzystują specjalne metody porównawcze, które jednoznacznie dają informację kompilatorowi czy dwa obiekty są równe.

Sam mechanizm dynamicznego typowania jest dość kontrowersyjny, ze względu na możliwość bycia nieścisłym. W praktyce okazuje się, że rozwój oprogramowania wykorzystującego ten sposób jest dużo szybszy. Za to zwolennicy statycznego typowania, twierdzą, że projekty wykorzystujące duck typing są trudne w utrzymaniu po latach. Celem tego dokumentu nie jest udowadnianie wyższości jednego rozwiązania nad drugim. Zachęcam jednak do zapoznania się z wykładem "The Unreasonable Effectiveness of Dynamic Typing for Practical Programs", którego autorem jest "Robert Smallshire". Wykład zamieszczonym został w serwisie InfoQ (http://www.infoq.com/presentations/dynamic-static-typing). Wykład w ciekawy sposób dotyka problematyki porównania tych dwóch metod systemu typów. Wykład jest o tyle ciekawy, że bazuje na statystycznej analizie projektów umieszczonych na https://github.com a nie tylko bazuje na domysłach i flamewar jakie programiści lubią prowadzić.

.. literalinclude:: src/oop-duck-typing.py
    :language: python
    :caption: Duck typing

What should be in the class and what not?
=========================================
* Jeżeli metoda w swoim ciele ma ``self`` i z niego korzysta to powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` to nie powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` ale wybitnie pasuje do klasy, to można ją tam zamieścić oraz dodać dekorator ``@staticmethod``

.. literalinclude:: src/oop-staticmethod-without.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``

.. literalinclude:: src/oop-staticmethod-with.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``

.. literalinclude:: src/oop-staticmethod-decorator.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``


``_`` and ``__`` - Private, protected, public?!
===============================================
* Brak pól protected i private
* Wszystkie pola są public
* ``_nazwa`` - pola prywatne (tylko konwencja)
* ``__nazwa__`` - funkcje systemowe
* ``nazwa_`` - używane przy kolizji nazw

.. literalinclude:: src/oop-private-public.py
    :language: python
    :caption: ``_`` and ``__`` - Private, protected, public?!


Inheritance vs. Composition (Mixin Classes)
===========================================
* Kompozycja ponad dziedziczenie!

.. literalinclude:: src/oop-composition.py
    :language: python
    :caption: Composition (Mixin Classes)


Dynamically creating fields
===========================
.. literalinclude:: src/oop-init-dynamic.py
    :language: python
    :caption: Funkcja inicjalizująca, która automatycznie dodaje pola do naszej klasy w zależności od tego co zostanie podane przy tworzeniu obiektu


Accessors
=========

Accessing class fields
----------------------
.. literalinclude:: src/oop-accessor-fields.py
    :language: python
    :caption: Accessing class fields

.. literalinclude:: src/oop-getter.py
    :language: python
    :caption: Case Study uzasadnionego użycia gettera w kodzie

``@property``, ``@x.setter``, ``@x.deleter``
--------------------------------------------
* ``@propery`` - for defining getters
* ``@kola.setter`` - for defining setter
* ``@kola.deleter`` - for defining deleter
* Blokowanie możliwości edycji pola klasy
* Dodawanie logowania przy ustawianiu wartości

.. literalinclude:: src/oop-property.py
    :language: python
    :caption: ``@property``, ``@x.setter``, ``@x.deleter``


``__str__()`` and ``__repr__()``
================================
* ``__repr__`` jest dla developerów (być jednoznacznym),
* ``__str__`` dla użytkowników (być czytelnym).

.. literalinclude:: src/oop-repr.py
    :language: python
    :caption: Using ``__repr__()`` on a class

.. code-block:: python

    import datetime

    datetime.datetime.now()  # ``__repr__``
    # datetime.datetime(2018, 7, 3, 11, 32, 51, 684972)

    print(datetime.datetime.now())  # ``__str__``
    # 2018-07-03 11:32:58.927387


``@staticmethod``
=================
* Using class as namespace
* Will not pass instance as a first argument
* ``self`` is not required

.. literalinclude:: src/oop-staticmethod.py
    :language: python
    :caption: Using ``@staticmethod``


Method Resolution Order
=======================
.. literalinclude:: src/oop-mro.py
    :language: python
    :caption: Method Resolution Order


Hash
====
* ``set()`` można zrobić z dowolnego hashowalnego obiektu
* ``dict()`` może mieć klucze, które są dowolnym hashowalnym obiektem

.. literalinclude:: src/oop-hash-dict.py
    :language: python
    :caption: ``dict()`` może mieć klucze, które są dowolnym hashowalnym obiektem

.. literalinclude:: src/oop-hash-set.py
    :language: python
    :caption: ``set()`` można zrobić z dowolnego hashowalnego obiektu

.. literalinclude:: src/oop-hash-generate-bad.py
    :language: python
    :caption: Generating hash and object comparision

.. literalinclude:: src/oop-hash-generate-good.py
    :language: python
    :caption: Generating hash and object comparision


Polymorphism
============
.. literalinclude:: src/oop-polymorphism-switch.py
    :language: python
    :caption: Switch moves business logic to the execution place

.. literalinclude:: src/oop-polymorphism-function.py
    :language: python
    :caption: Polymorphism on Function

.. literalinclude:: src/oop-polymorphism-class.py
    :language: python
    :caption: Polymorphism on Classes


Interfaces
==========
* Nie można tworzyć instancji
* Wszystkie metody muszą być zaimplementowane przez potomków
* Tylko deklaracje metod
* Metody nie mogą mieć implementacji

.. literalinclude:: src/oop-interface.py
    :language: python
    :caption: Interfaces


Abstract Classes
================
* Nie można tworzyć instancji
* Można tworzyć implementację metod

.. literalinclude:: src/oop-abstract-class.py
    :language: python
    :caption: Abstract Class


``is``
======
* ``is`` porównuje czy dwa obiekty są tożsame
* Najczęściej służy do sprawdzania czy coś jest ``None``

.. code-block:: python

    if name is None:
        print('Name is not set')
    else:
        print('You have set your name')

Bardzo kuszący jest następujący przykład:

 .. code-block:: python

     if name is 'Max Peck':
        print('You are Max!')
     else:
        print('You are not Max!')

**Nie jest on jednak do końca poprawny. Słowo kluczowe ``is`` porównuje czy dwa obiekty są tym samym obiektem, nie czy mają taką samą wartość.**
* Poniższy przykład ilustruje, że pomimo że dwa obiekty przechowują takiego samego stringa to nie są sobie tożsame, mimo że są sobie równe.

 .. code-block:: python

    a = 'hello'
    b = 'hello'

    print(f'a is {a}, b is {b}')        # a is hello, b is hello
    print(f'a == b returns: {a==b}')    # a == b returns: True
    print(f'a is b returns: {a is b}')  # a is b returns: True

.. code-block:: python

    a = 'hello'
    b = ''.join('hello')

    print(f'a is {a}, b is {b}')        # a is hello, b is hello
    print(f'a == b returns: {a==b}')    # a == b returns: True
    print(f'a is b returns: {a is b}')  # a is b returns: False


Good Engineering Practises
==========================

Tell - don't ask
----------------
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

.. literalinclude:: src/oop-tell-dont-ask.py
    :language: python
    :caption: Tell - don't ask

Do not run methods in ``__init__()``
------------------------------------
* Nie powinniśmy uruchamiać innych metod na obiekcie.
* Obiekt nie jest jeszcze w pełni zainicjalizowany!
* Konstruktor się nie wykonał do końca.
* Dopiero jak się skończy ``__init__`` to możemy uruchamiać metody obiektu

.. literalinclude:: src/oop-init-calls.py
    :language: python
    :caption: Do not run methods in ``__init__()``


Monkey Patching
===============
.. literalinclude:: src/oop-monkey-patching-1.py
    :language: python
    :caption: Monkey Patching

.. literalinclude:: src/oop-monkey-patching-2.py
    :language: python
    :caption: Monkey Patching

.. literalinclude:: src/oop-monkey-patching-3.py
    :language: python
    :caption: Monkey Patching


Objects and instances
=====================
.. literalinclude:: src/oop-objects-and-instances.py
    :language: python
    :caption: Objects and instances


S.O.L.I.D.
==========

Single responsibility principle
-------------------------------
a class should have only a single responsibility (i.e. changes to only one part of the software's specification should be able to affect the specification of the class)

The single responsibility principle is a computer programming principle that states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility. Robert C. Martin expresses the principle as, "A class should have only one reason to change."

Open/closed principle
---------------------
software entities … should be open for extension, but closed for modification

The name open/closed principle has been used in two ways. Both ways use generalizations (for instance, inheritance or delegate functions) to resolve the apparent dilemma, but the goals, techniques, and results are different.

Liskov substitution principle
-----------------------------
objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program. See also design by contract.

Substitutability is a principle in object-oriented programming stating that, in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S (i.e. an object of type T may be substituted with any object of a subtype S) without altering any of the desirable properties of the program (correctness, task performed, etc.).

Interface segregation principle
-------------------------------
many client-specific interfaces are better than one general-purpose interface

The interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy. ISP is one of the five SOLID principles of object-oriented design, similar to the High Cohesion Principle of GRASP.

Dependency inversion principle
------------------------------
one should depend upon abstractions, [not] concretions

In object-oriented design, the dependency inversion principle refers to a specific form of decoupling software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:

    #. High-level modules should not depend on low-level modules. Both should depend on abstractions.
    #. Abstractions should not depend on details. Details should depend on abstractions.

By dictating that both high-level and low-level objects must depend on the same abstraction this design principle inverts the way some people may think about object-oriented programming.

GRASP
=====
**General responsibility assignment software patterns (or principles)**, abbreviated GRASP, consist of guidelines for assigning responsibility to classes and objects in object-oriented design.

The different patterns and principles used in GRASP are controller, creator, indirection, information expert, high cohesion, low coupling, polymorphism, protected variations, and pure fabrication. All these patterns answer some software problem, and these problems are common to almost every software development project. These techniques have not been invented to create new ways of working, but to better document and standardize old, tried-and-tested programming principles in object-oriented design.

Dependency injection
====================
- http://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

Dependency injection, as a software design pattern, has number of advantages that are common for each language (including Python):

    - Dependency Injection decreases coupling between a class and its dependency.
    - Because dependency injection doesn’t require any change in code behavior it can be applied to legacy code as a refactoring. The result is clients that are more independent and that are easier to unit test in isolation using stubs or mock objects that simulate other objects not under test. This ease of testing is often the first benefit noticed when using dependency injection.
    - Dependency injection can be used to externalize a system’s configuration details into configuration files allowing the system to be reconfigured without recompilation (rebuilding). Separate configurations can be written for different situations that require different implementations of components. This includes, but is not limited to, testing.
    - Reduction of boilerplate code in the application objects since all work to initialize or set up dependencies is handled by a provider component.
    - Dependency injection allows a client to remove all knowledge of a concrete implementation that it needs to use. This helps isolate the client from the impact of design changes and defects. It promotes reusability, testability and maintainability.
    - Dependency injection allows a client the flexibility of being configurable. Only the client’s behavior is fixed. The client may act on anything that supports the intrinsic interface the client expects.

.. literalinclude:: src/oop-dependency-injection.py
    :language: python
    :caption: Dependency injection



Metaclass
=========
* Można zmienić, że obiekt nie dziedziczy po ``object``
* Każdy obiekt klasy jest instancją tej klasy
* Każda napisana klasa jest instancją obiektu, który nazywa się metaklasą
* Na 99% tego nie potrzebujesz

.. warning:: więcej na ten temat w rozdziale :ref:`Metaclass`

.. literalinclude:: src/oop-metaclass.py
    :language: python
    :caption: Metaclass


Assignments
===========

Address Book (Medium)
---------------------
#. API programu powinno być tak jak na :numref:`listing-oop-addressbook-medium`
#. Zrób tak, aby się ładnie wyświetlało zarówno dla jednego wyniku jak i dla wszystkich w książce
#. ``Address`` ma mieć zmienną liczbę argumentów
#. Jeżeli argument jest różny od ``None`` powinien być dynamicznie ustawiony (``setattr()``).

:About:
    * Filename: ``oop_addressbook_medium.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * Korzystanie z operatorów ``*args`` i ``**kwargs``
    * Korzystanie i rozróżnianie ``.__repr__()`` od ``.__str__()``
    * Dynamiczne tworzenie pól w obiekcie

.. literalinclude:: src/oop-assignment-addressbook-medium.py
    :name: listing-oop-addressbook-medium
    :language: python
    :caption: Address Book
