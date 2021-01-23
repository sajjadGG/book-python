UML Class Diagram
=================


Attributes
----------
.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        firstname: str
        lastname: str
    }
    ```

.. figure:: img/uml-classdiagram-attributes.png

Methods Without Parameters
--------------------------
.. code-block:: python

    class Astronaut:
        def say_hello():
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        say_hello()
    }
    ```

.. figure:: img/uml-classdiagram-method-noparams.png

Methods With Parameters
-----------------------
.. code-block:: python

    class Astronaut:
        def say_hello(firstname: str, lastname: str):
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        say_hello(firstname: str, lastname: str)
    }
    ```

.. figure:: img/uml-classdiagram-method-params.png

Method Return Type
------------------
.. code-block:: python

    class Astronaut:
        def say_hello() -> str:
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        say_hello() str
    }
    ```

.. figure:: img/uml-classdiagram-method-return.png

Abstract Methods
----------------
.. code-block:: python

    from abc import abstractmethod, ABCMeta

    class Astronaut(metaclass=ABCMeta):
        @abstractmethod
        def say_hello():
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        say_hello()*
    }
    ```

.. figure:: img/uml-classdiagram-method-abstract.png

Static Methods
--------------
.. code-block:: python

    class Astronaut:
        @staticmethod
        def say_hello():
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        say_hello()$
    }
    ```

.. figure:: img/uml-classdiagram-method-static.png

Types
-----
.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str

        def say_hello(name: str) -> str:
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        firstname: str
        lastname: str

        say_hello(name: str) str
    }
    ```

.. figure:: img/uml-classdiagram-types.png


Access Modifiers
----------------
* ``+`` - Public
* ``-`` - Private
* ``#`` - Protected
* ``~`` - Package/Internal


Access Modifiers - Public
-------------------------
.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str

        def say_hello() -> str:
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        +firstname: str
        +lastname: str
        +say_hello() str
    }
    ```
.. figure:: img/uml-classdiagram-accessmodifiers-public.png

Access Modifiers - Protected
----------------------------
.. code-block:: python

    class Astronaut:
        _firstname: str
        _lastname: str

        def _say_hello() -> str:
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        #firstname: str
        #lastname: str
        #say_hello() str
    }
    ```
.. figure:: img/uml-classdiagram-accessmodifiers-protected.png

Access Modifiers - Private
--------------------------
.. code-block:: python

    class Astronaut:
        __firstname: str
        __lastname: str

        def __say_hello() -> str:
            pass

.. code-block:: md

    ```mermaid
    classDiagram

    class Astronaut {
        -firstname: str
        -lastname: str
        -say_hello() str
    }
    ```

.. figure:: img/uml-classdiagram-accessmodifiers-private.png


Cardinality
-----------
* ``1`` - Only 1
* ``0..1`` - Zero or One
* ``1..*`` - One or more
* ``*`` - Many
* ``n n`` - {where n>1}
* ``0..n`` - zero to n {where n>1}
* ``1..n`` - one to n {where n>1}


Boxes and Arrows
----------------
.. figure:: img/uml-classdiagram-usecase-01.jpg


Use Cases
---------
.. figure:: img/uml-classdiagram-usecase-02.png
.. figure:: img/uml-classdiagram-usecase-03.png
.. figure:: img/uml-classdiagram-usecase-04.png
.. figure:: img/uml-classdiagram-usecase-05.png
.. figure:: img/uml-classdiagram-usecase-06.png
.. figure:: img/uml-classdiagram-usecase-07.png
.. figure:: img/uml-classdiagram-usecase-08.jpg
.. figure:: img/uml-classdiagram-usecase-09.jpg
.. figure:: img/uml-classdiagram-usecase-10.png


Django
------
* GraphViz + Dot
* Django Extensions: https://django-extensions.readthedocs.io/en/latest/graph_models.html

.. figure:: img/uml-django.png
.. figure:: img/uml-django-models.png
