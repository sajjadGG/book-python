**********
Statistics
**********


``statistics``
==============
.. csv-table:: Averages and measures of central location
    :header-rows: 1

    "Function", "Description"
    "``statistics.mean()``", "Arithmetic mean ('average') of data"
    "``statistics.fmean()``", "faster, floating point variant of ``statistics.mean()``, since Python 3.8"
    "``statistics.harmonic_mean()``", "Harmonic mean of data"
    "``statistics.median()``", "Median (middle value) of data"
    "``statistics.median_low()``", "Low median of data"
    "``statistics.median_high()``", "High median of data"
    "``statistics.median_grouped()``", "Median, or 50th percentile, of grouped data"
    "``statistics.mode()``", "Mode (most common value) of discrete data"
    "``statistics.multimode()``", "returns a list of the most common values, since Python 3.8"
    "``statistics.geometric_mean()``", "Since Python 3.8"
    "``statistics.quantiles()``", "divides data or a distribution in to equiprobable intervals (e.g. quartiles, deciles, or percentiles), since Python 3.8"
    "``statistics.NormalDist``", "tool for creating and manipulating normal distributions of a random variable"

.. csv-table:: Measures of spread
    :header-rows: 1

    "Function", "Description"
    "``statistics.pstdev()``", "Population standard deviation of data"
    "``statistics.pvariance()``", "Population variance of data"
    "``statistics.stdev()``", "Sample standard deviation of data"
    "``statistics.variance()``", "Sample variance of data"

.. code-block:: python

    temperature_feb = NormalDist.from_samples([4, 12, -3, 2, 7, 14])

    temperature_feb.mean    # 6.0
    temperature_feb.stdev   # 6.356099432828281

    # Chance of being under 3 degrees
    temperature_feb.cdf(3)  # 0.3184678262814532

    # Relative chance of being 7 degrees versus 10 degrees
    temperature_feb.pdf(7) / temperature_feb.pdf(10)  # 1.2039930378537762


    el_niño = NormalDist(4, 2.5)

    # Add in a climate effect
    temperature_feb += el_niño

    temperature_feb                 # NormalDist(mu=10.0, sigma=6.830080526611674)

    # Convert to Fahrenheit
    temperature_feb * (9/5) + 32    # NormalDist(mu=50.0, sigma=12.294144947901014)

    # Generate random samples
    temperature_feb.samples(3)      # [7.672102882379219, 12.000027119750287, 4.647488369766392]

.. code-block:: python

    from statistics import mean


    mean([1, 2, 3, 4, 4])           # 2.8
    mean([-1.0, 2.5, 3.25, 5.75])   # 2.625

.. code-block:: python

    from statistics import harmonic_mean


    harmonic_mean([2.5, 3, 10])     # 3.6

.. code-block:: python

    from statistics import median


    median([1, 3, 5])               # 3
    median([1, 3, 5, 7])            # 4.0

The low median is always a member of the data set. When the number of data points is odd, the middle value is returned. When it is even, the smaller of the two middle values is returned.

.. code-block:: python

    from statistics import median_low


    median_low([1, 3, 5])           # 3
    median_low([1, 3, 5, 7])        # 3

The high median is always a member of the data set. When the number of data points is odd, the middle value is returned. When it is even, the larger of the two middle values is returned.

.. code-block:: python

    from statistics import median_high


    median_high([1, 3, 5])          # 3
    median_high([1, 3, 5, 7])       # 5

Return the median of grouped continuous data, calculated as the 50th percentile, using interpolation.

.. code-block:: python

    from statistics import median_grouped


    median_grouped([52, 52, 53, 54])              # 52.5
    median_grouped([1, 3, 3, 5, 7], interval=1)   # 3.25
    median_grouped([1, 3, 3, 5, 7], interval=2)   # 3.5

.. code-block:: python

    from statistics import mode


    mode([1, 1, 2, 3, 3, 3, 3, 4])                                  # 3
    mode(["red", "blue", "blue", "red", "green", "red", "red"])     # 'red'

Return the population standard deviation (the square root of the population variance).

.. code-block:: python

    from statistics import pstdev


    pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
    # 0.986893273527251

.. code-block:: python

    from statistics import pvariance


    pvariance([0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25])
    # 1.25

.. code-block:: python

    from statistics import stdev


    stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
    # 1.0810874155219827

.. code-block:: python

    from statistics import variance


    variance([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5])
    # 1.3720238095238095

Assignments
===========

Iris Stats
----------
* Complexity level: easy
* Lines of code to write: 30 lines
* Estimated time of completion: 30 min
* Filename: :download:`solution/statistics_iris.py`

:English:
    #. Create dict ``species: Dict[str, dict]``
    #. For each species calculate:

            - mean,
            - median,
            - standard deviation,
            - variance.

    #. Save data to ``species`` dict

:Polish:
    #. Stwórz słownik ``species: Dict[str, dict]``
    #. Dla każdego gatunku wylicz:

            - średnią,
            - medianę,
            - odchylenie standardowe,
            - wariancję.

    #. Dane zapisz w słowniku ``species``

:Non-functional requirements:
    #. Use``statistics``
    #. Calculate only numerical parameters
    #. Those are the total values from all rows

:Input:
    .. code-block:: python
        :caption: Input

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

        {'setosa': {
            'petal_length': {'mean': 1.4428571428571428,
                             'median': 1.4,
                             'stdev': 0.12724180205607036,
                             'values': [1.4, 1.3, 1.4, 1.4, 1.7, 1.4, 1.5],
                             'variance': 0.01619047619047619},
            'petal_width': {'mean': 0.2571428571428572,
                            'median': 0.2,
                            'stdev': 0.07867957924694431,
                            'values': [0.2, 0.2, 0.2, 0.3, 0.4, 0.3, 0.2],
                            'variance': 0.006190476190476191},
            'sepal_length': {'mean': 4.9,
                             'median': 4.9,
                             'stdev': 0.2943920288775951,
                             'values': [5.1, 4.7, 4.9, 4.6, 5.4, 5.0, 4.6],
                             'variance': 0.08666666666666677},
            'sepal_width': {'mean': 3.3857142857142857,
                            'median': 3.4,
                            'stdev': 0.31320159337914943,
                            'values': [3.5, 3.2, 3.0, 3.4, 3.9, 3.6, 3.1],
                            'variance': 0.09809523809523807}},
         ...
