*************
Import/Export
*************

Reading data
============
* ``with open('filename.csv')`` - context manager
* ``numpy.loadtxt('filename.csv', delimeter=',', unpack=True)``
* ``csv.DictReader()``
* ``pandas`` ``DataFrame``


``pandas`` and ``matplotlib``
=============================
* All of plotting functions expect ``np.array`` or ``np.ma.masked_array`` as input
* Classes that are 'array-like' such as ``pandas`` data objects and ``np.matrix`` may or may not work as intended
* It is best to convert these to ``np.array`` objects prior to plotting
* Convert a ``pandas.DataFrame``:

    .. code-block:: python

        a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
        a_asndarray = a.values

Exporting
=========
.. glossary::

    agg
    cairo
    eps
    pdf
    png
    ps
    svg
    raster graphics
    vector graphics


=============   ============   ================================================
Renderer        Filetypes      Description
=============   ============   ================================================
:term:`AGG`     :term:`png`    :term:`raster graphics` -- high quality images
                               using the Anti-Grain Geometry engine
PS              :term:`ps`     :term:`vector graphics` -- Postscript output
                :term:`eps`
PDF             :term:`pdf`    :term:`vector graphics` --
                               Portable Document Format
SVG             :term:`svg`    :term:`vector graphics` --
                               Scalable Vector Graphics
:term:`Cairo`   :term:`png`    :term:`raster graphics` and
                :term:`ps`     :term:`vector graphics` -- using the
                :term:`pdf`    Cairo graphics library
                :term:`svg`
=============   ============   ================================================

