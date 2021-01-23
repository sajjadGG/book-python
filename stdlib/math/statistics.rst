Math Statistics
===============

* ``statistics`` module


Mean
----
.. csv-table:: Mean
    :widths: 25,75
    :header: "Function", "Description"

    "``statistics.mean()``", "Arithmetic mean ('average') of data"
    "``statistics.fmean()``", "faster, floating point variant of ``statistics.mean()``, since Python 3.8"
    "``statistics.harmonic_mean()``", "Harmonic mean of data"
    "``statistics.geometric_mean()``", "since Python 3.8"

Arithmetic mean ('average') of data:

.. code-block:: python

    from statistics import mean


    mean([1, 2, 3, 4, 4])
    # 2.8
    mean([-1.0, 2.5, 3.25, 5.75])
    # 2.625

Harmonic mean of data:

.. code-block:: python

    from statistics import harmonic_mean


    harmonic_mean([2.5, 3, 10])
    # 3.6


Median
------
.. csv-table:: Median
    :widths: 25,75
    :header: "Function", "Description"

    "``statistics.median()``", "Median (middle value) of data"
    "``statistics.median_low()``", "Low median of data"
    "``statistics.median_high()``", "High median of data"
    "``statistics.median_grouped()``", "Median, or 50th percentile, of grouped data"

Median (middle value) of data:

.. code-block:: python

    from statistics import median


    median([1, 3, 5])
    # 3
    median([1, 3, 5, 7])
    # 4.0

* The low median is always a member of the data set.
* When the number of data points is odd, the middle value is returned.
* When it is even, the smaller of the two middle values is returned.

Low median of data:

.. code-block:: python

    from statistics import median_low


    median_low([1, 3, 5])
    # 3
    median_low([1, 3, 5, 7])
    # 3

* The high median is always a member of the data set.
* When the number of data points is odd, the middle value is returned.
* When it is even, the larger of the two middle values is returned.

High median of data:

.. code-block:: python

    from statistics import median_high


    median_high([1, 3, 5])
    # 3
    median_high([1, 3, 5, 7])
    # 5

* Median of grouped continuous data.
* Calculated using interpolation as the 50th percentile.

Median, or 50th percentile, of grouped data:

.. code-block:: python

    from statistics import median_grouped


    median_grouped([52, 52, 53, 54])
    # 52.5
    median_grouped([1, 3, 3, 5, 7], interval=1)
    # 3.25
    median_grouped([1, 3, 3, 5, 7], interval=2)
    # 3.5


Mode
----
.. csv-table:: Mode
    :widths: 25,75
    :header: "Function", "Description"

    "``statistics.mode()``", "Mode (most common value) of discrete data"
    "``statistics.multimode()``", "returns a list of the most common values, since Python 3.8"
    "``statistics.quantiles()``", "divides data or a distribution in to equiprobable intervals (e.g. quartiles, deciles, or percentiles), since Python 3.8"

Mode (most common value) of discrete data:

.. code-block:: python

    from statistics import mode


    mode([1, 1, 2, 3, 3, 3, 3, 4])
    # 3
    mode(["red", "blue", "blue", "red", "green", "red", "red"])
    # 'red'


Distribution
------------
.. csv-table:: Distribution
    :widths: 25,75
    :header: "Function", "Description"

    "``statistics.NormalDist``", "tool for creating and manipulating normal distributions of a random variable"


Standard Deviation
------------------
.. csv-table:: Standard Deviation
    :widths: 25,75
    :header: "Function", "Description"

    "``statistics.pstdev()``", "Population standard deviation of data"
    "``statistics.stdev()``", "Sample standard deviation of data"

Sample standard deviation of data:

.. code-block:: python

    from statistics import stdev


    stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
    # 1.0810874155219827

* Population standard deviation
* Is the square root of the population variance

Population standard deviation:

.. code-block:: python

    from statistics import pstdev


    pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
    # 0.986893273527251


Variance
--------
.. csv-table:: Variance
    :widths: 25,75
    :header: "Function", "Description"

    "``statistics.pvariance()``", "Population variance of data"
    "``statistics.variance()``", "Sample variance of data"

Sample variance of data:

.. code-block:: python

    from statistics import variance


    variance([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5])
    # 1.3720238095238095

Population variance of data:

.. code-block:: python

    from statistics import pvariance


    pvariance([0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25])
    # 1.25


Examples
--------
.. code-block:: python

    temperature_feb = NormalDist.from_samples([4, 12, -3, 2, 7, 14])

    temperature_feb.mean
    # 6.0
    temperature_feb.stdev
    # 6.356099432828281

    # Chance of being under 3 degrees
    temperature_feb.cdf(3)  # 0.3184678262814532

    # Relative chance of being 7 degrees versus 10 degrees
    temperature_feb.pdf(7) / temperature_feb.pdf(10)  # 1.2039930378537762


    el_niño = NormalDist(4, 2.5)

    # Add in a climate effect
    temperature_feb += el_niño

    temperature_feb
    # NormalDist(mu=10.0, sigma=6.830080526611674)

    # Convert to Fahrenheit
    temperature_feb * (9/5) + 32
    # NormalDist(mu=50.0, sigma=12.294144947901014)

    # Generate random samples
    temperature_feb.samples(3)
    # [7.672102882379219, 12.000027119750287, 4.647488369766392]


Assignments
-----------
.. literalinclude:: assignments/stdlib_statistics_stats.py
    :caption: :download:`Solution <assignments/stdlib_statistics_stats.py>`
    :end-before: # Solution

.. literalinclude:: assignments/stdlib_statistics_iris.py
    :caption: :download:`Solution <assignments/stdlib_statistics_iris.py>`
    :end-before: # Solution
