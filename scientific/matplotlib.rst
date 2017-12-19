.. _matplotlib::

**********
Matplotlib
**********

Moduł ``matplotlib`` pozwala na rysowanie wykresów i diagramów. Jest to bardzo rozbudowana biblioteka z setkami opcji konfiguracyjnych. Najczęściej używanym modułem biblioteki ``matplotlib`` jest moduł ``pyplot``, który implementuje szereg funkcji umożliwiających rysowanie wykresów 2d.

Instalacja
----------
.. code-block:: console

    $ pip install matplotlib

Podstawowe użycie
-----------------
.. code-block:: python

    from matplotlib import pyplot as plt

    plt.plot(0, 0, 'o')
    plt.show()

Bardziej zaawansowany przykład
------------------------------
.. code-block:: python

    from matplotlib import pyplot as plt

    x1 = [x*0.01 for x in range(0,628)]
    y1 = [math.sin(x*0.01)+random.gauss(0, 0.1) for x in range(0,628)]
    plt.plot(x1, y1)

    x2 = [x*0.5 for x in range(0,round(63/5))]
    y2 = [math.cos(x*0.5) for x in range(0,round(63/5))]
    plt.plot(x2, y2, 'o-')

    plt.show()