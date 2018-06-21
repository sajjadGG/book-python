*******
Jupyter
*******

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more.

Jupyter notebook is a language-agnostic HTML notebook application for Project Jupyter. In 2015, Jupyter notebook was released as a part of The Big Split™ of the IPython codebase. IPython 3 was the last major monolithic release containing both language-agnostic code, such as the IPython notebook, and language specific code, such as the IPython kernel for Python. As computing spans across many languages, Project Jupyter will continue to develop the language-agnostic Jupyter notebook in this repo and with the help of the community develop language specific kernels which are found in their own discrete repos.

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
* ``%%``

    * ``%%timeit``

Execute terminal commands
-------------------------
* ``!``

    * ``!pwd``
    * ``!ls``
    * .. code-block:: python

        files = !dir
        for f in files:
            if f.find("1_") >= 0:
                print(f)

HTML
----
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

Markdown
========

Unorganized lists
-----------------
* ``* `` or ``- ``

Organized lists
---------------
* ``#. ``

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

Slides
======
View -> Cell Toolbar -> Slideshow

.. code-block:: console

    jupyter nbconvert filename.ipynb --to slides --post serve


Zadania kontrolne
=================

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