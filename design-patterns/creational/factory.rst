*******
Factory
*******


.. literalinclude:: src/design-patterns-factory-1.py
    :language: python
    :caption: Factory Design Pattern

.. literalinclude:: src/design-patterns-factory-2.py
    :language: python
    :caption: Factory Design Pattern

.. code-block:: python

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        cls = {
            'setosa': Setosa,
            'versicolor': Versicolor,
            'viriginica': Virginica,
        }.get(species, None)

        if not cls:
            raise NotImplementedError

        return cls

    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

.. code-block:: python

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        return {
            'setosa': Setosa,
            'versicolor': Versicolor,
            'viriginica': Virginica,
        }.get(species, None)

    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

.. code-block:: python

    import sys


    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        try:
            CURRENT_MODULE = sys.modules[__name__]
            return getattr(CURRENT_MODULE, species.capitalize())
        except AttributeError:
            raise NotImplementedError


    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>
