****************
Matplotlib Plots
****************


Line Plot
=========
.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]

    plt.plot(x, y)
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = np.linspace(0, 10, 1000)
    sin = np.sin(x)
    cos = np.cos(x)

    plt.plot(x, sin)
    plt.plot(x, cos)
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = np.linspace(0, 10, 1000)

    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = np.linspace(0, 2, 100)

    plt.plot(x, x, label='linear')
    plt.plot(x, x**2, label='quadratic')
    plt.plot(x, x**3, label='cubic')

    plt.show()


Scatter Plot
============
.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]

    plt.plot(x, y, 'o')
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plt.scatter(x, y)
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plt.scatter(x=x, y=y,
        label='my points',
        color='black',
        marker='*',        # type of the points
        s=100,             # size
    )

    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plt.scatter(x=x, y=y,
        label='my points',
        color='black',
        marker='x',        # type of the points
        s=100,             # size
    )

    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = [1,2,3,4,5,6,7,8]
    y = [4,7,6,2,7,4,5,2]

    plt.scatter(x, y, marker='*', color='red', s=500)   # ``s`` = size
    plt.scatter(y, x, marker='o', color='blue')

    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = x = np.linspace(0, 10, 50)
    y = np.sin(x)

    plt.scatter(x, y)
    plt.show()


Bar
===
.. code-block:: python

    import matplotlib.pyplot as plt


    x = [2, 4, 6, 8, 10]
    y = [6, 7, 8, 2, 4]

    plt.bar(x, y)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    bluex = [2, 4, 6, 8, 10]
    bluey = [6, 7, 8, 2, 4]
    redx = [1, 3, 5, 7, 9]
    redy = [7, 8, 2, 4, 2]

    plt.bar(x1, y1, color='blue')
    plt.bar(x2, y2, color='red')
    plt.show()


Histogram
=========
.. code-block:: python

    import matplotlib.pyplot as plt


    age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
           110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
           65, 54, 44, 43, 42, 48]

    population = [x for x,y in enumerate(y)]

    plt.bar(age, population)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
           110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
           65, 54, 44, 43, 42, 48]

    age = sorted(age)
    population = [x for x,y in enumerate(y)]

    plt.bar(age, population)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
           110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
           65, 54, 44, 43, 42, 48]

    plt.hist(age, bins=6)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
           110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
           65, 54, 44, 43, 42, 48]

    plt.hist(age, bins=6, rwidth=0.8)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
           110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
           65, 54, 44, 43, 42, 48]

    plt.hist(age,
             bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],
             histtype='bar',
             rwidth=0.8)

    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
           110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
           65, 54, 44, 43, 42, 48]

    plt.hist(age,
             bins=[0, 6, 18, 25, 65, max(age)],
             histtype='bar',
             rwidth=0.8)

    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    np.random.seed(0)

    mu = 0
    sigma = 1
    x = mu + sigma * np.random.randn(10000)

    plt.hist(x, bins=50)
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    np.random.seed(0)

    x = np.random.normal(size=10000)

    plt.hist(x, bins=50)
    plt.show()


Pie Chart
=========
.. code-block:: python

    import matplotlib.pyplot as plt


    slices = [20, 6, 3, 13]
    status = ['todo', 'in progress', 'in test', 'done']
    colors = ['#0052CC', '#F6C242ff', '#F6C242aa', '#008759']

    plt.pie(
        x=slices,            # data
        labels=status,       # name of the slices
        colors=colors,       # colors
        startangle=90,       # angle at which start plotting
        shadow=False,         # drop shadow outline?
        explode=[0,1,0,0],   # which piece to explode out from the chart
        autopct='%1.2f%%',   # number formatting
        radius=2,            # size of the chart
    )

    plt.show()


Donut Chart
===========
.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    fig, ax = plt.subplots()

    size = 0.3
    vals = np.array([[60., 32.],
                     [37., 40.],
                     [29., 10.]])

    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3)*4)
    inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

    ax.pie(vals.sum(axis=1),
           radius=1,
           colors=outer_colors,
           wedgeprops={'width': size, 'edgecolor': 'w'})

    ax.pie(vals.flatten(),
           radius=1-size,
           colors=inner_colors,
           wedgeprops={'width': size, 'edgecolor': 'w'})

    plt.show()


Stack Plot
==========
.. code-block:: python

    import matplotlib.pyplot as plt


    labels = ['To Do', 'In Progress', 'In Test', 'In Review', 'Done']
    colors = ['#0052CC', '#F6C242ff', '#F6C242aa', '#F6C24266', '#008759']

    day         = [1, 2, 3, 4, 5]
    todo        = [10, 8, 6, 4, 2]
    in_progress = [2, 3, 4, 3, 2]
    in_test     = [7, 8, 7, 2, 2]
    in_review   = [8, 5, 7, 8, 1]
    done        = [0, 2, 4, 6, 12]

    plt.stackplot(day, todo, in_progress, in_test, in_review, done, labels=labels, colors=colors)
    plt.legend(loc='upper left')
    plt.show()


Box Plot
========
.. code-block:: python

    import matplotlib.pyplot as plt


    age = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102,
               110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
               65, 54, 44, 43, 42, 48]

    plt.boxplot(age)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    np.random.seed(0)

    x = np.random.normal(size=1000)

    plt.boxplot(x)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    np.random.seed(0)

    a = np.random.normal(size=1000)
    b = np.random.normal(size=1000)
    c = np.random.normal(size=1000)
    d = np.random.normal(size=1000)
    data = [a, b, c, d]

    plt.boxplot(data)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    center = [5]
    spread = [5.0, 6, 5.1, 5.2, 5.5, 5.0, 4.1]
    flier_high = [7, 7.5]
    flier_low = [3, 3.3]
    data = spread + center + flier_high + flier_low

    plt.boxplot(data)
    plt.show()


Error
=====
.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]
    e = [0.5, 1.0, 1.5, 0.7]

    plt.errorbar(x, y, yerr=e, fmt='o')
    plt.show()

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]
    e = [0.5, 1.0, 1.5, 0.7]

    plt.errorbar(x, y, yerr=e, fmt='o-')
    plt.show()
