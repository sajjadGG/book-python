*******
Jupyter
*******

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

* http://jupyter.org/
* http://jupyter.readthedocs.io/en/latest/install.html
* https://github.com/jupyter/notebook


Install
=======
.. code-block:: console

    pip install jupyter


Run
===
.. code-block:: console

    $ jupyter notebook
    [I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
    [I 08:58:24.417 NotebookApp] 0 active kernels
    [I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

    $ jupyter notebook filename.ipynb
    $ jupyter notebook --port 9999


Using
=====
* Add code
* Run code
* Modify code and run
* Autocomplete
* Cell type (Markdown, LaTeX, Code)


Cells
=====
Insert Below/Above Cells
------------------------

Add, Delete Cells
-----------------

Cut, Copy, Pase Cells
---------------------

Move Up/Down Cells
------------------

Merge, Split Cells
------------------


Run
===
Run Cell
--------
Shift-Enter

Run All (above/below)
---------------------

Clear Output
------------


LaTeX
=====
.. code-block:: python

    from IPython.display import display, Math, Latex

    display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))

.. code-block:: python

    %%latex

    $$c = \sqrt{a^2 + b^2}$$

.. code-block:: python

    %%latex

    \begin{equation}
    H← ​​​60 ​+​ \frac{​​30(B-R)​​}{Vmax-Vmin}  ​​, if V​max​​ = G
    \end{equation}


Magic commands
==============
* ``%run``
* ``%%timeit``
* ``%%latex``
* ``%matplotlib inline``


Execute terminal commands
=========================
* ``!``

    * ``!pwd``
    * ``!ls``
    * .. code-block:: python

        files = !dir
        for f in files:
            if f.find("1_") >= 0:
                print(f)


HTML and Javascript
===================
.. code-block:: python

    from IPython.display import Javascript, HTML
    Javascript("alert('It is JavaScript!')")
    HTML("We can <i>generate</i> <code>html</code> code <b>directly</b>!")


Kernels
=======

Functions
=========

Checkpoints
-----------

Download
--------

Trust Notebook
--------------

Close and Halt
--------------


Markdown
========

Unorganized lists
-----------------
* ``*`` or ``-``

Organized lists
---------------
* ``#.``

Headers
-------
* ``# Title``
* ``## Title``
* ``### Title``
* ``#### Title``
* ``##### Title``
* ``###### Title``

Formatting
----------
* Bold
* Underline
* Strikethrought
* Italics

Tables
------


Embedding objects
=================

Image
-----

YouTube
-------
.. code-block:: python

    from IPython.display import YouTubeVideo
    YouTubeVideo("wupToqz1e2g")


Slides
======
View -> Cell Toolbar -> Slideshow

.. code-block:: console

    jupyter nbconvert filename.ipynb --to slides --post serve


Assignments
===========

Podstawy korzystania
--------------------
#. Stwórz notebook jupyter o nazwie ``first.ipynb``
#. Dodaj tekst opisujący następne polecenia
#. Dodaj trzy różne 'Code Cell'
#. Uruchom Code Cell z wynikiem wszystkich powyżej
#. Dodaj Code Cell, który pokaże czas wykonywania instrukcji
#. Dodaj Code Cell, który wyświetli wykres funkcji ``sin()`` inplace

Slajdy
------
#. Poprzedni skrypt przekonwertuj na slajdy i uruchom prezentację w przeglądarce