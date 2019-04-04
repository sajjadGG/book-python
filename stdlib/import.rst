*****************
Importing modules
*****************


Importing modules
=================

Import module
-------------
* ``import ...``

Syntax
^^^^^^
.. code-block:: python

    import module

.. code-block:: python

    import module.submodule

Example
^^^^^^^
.. code-block:: python

    import random

Importing function from module
------------------------------
* ``from ... import ...``

Syntax
^^^^^^
.. code-block:: python

    from module import function

.. code-block:: python

    from module.submodule import function

Example
^^^^^^^
.. code-block:: python

    from random import randint


Import and alias
----------------
* ``import ... as ...``

Syntax
^^^^^^
.. code-block:: python

    import module as alias

.. code-block:: python

    from module import function as alias

Example
^^^^^^^
.. code-block:: python

    import numpy as np

.. code-block:: python

    from django.utils.translation import ugettext_lazy as _

Relative imports
----------------
* ``from . import ...``
* ``from .. import ...``

Syntax
^^^^^^
.. code-block:: python

    from . import module

.. code-block:: python

    from .. import module

.. code-block:: python

    from .module import function

.. code-block:: python

    from ..module import function


What is Python Module
=====================
* Every Python file is a module
* Every directory with ``__init__.py`` file is a module
* Python does not recognize whether it is a file or dir with init
* Useful when you start simple, and then expand
* Usually ``__init__.py`` is empty
* If you define ``__all__: List[str]`` in ``__init__.py`` it will import only those functions when ``from MODULE import * ``

Python file is a module
-----------------------
.. code-block:: python

    game.py

Directory with ``__init__.py`` file
-----------------------------------
.. code-block:: python

    game
        __init__.py

Importing from own modules
--------------------------
.. code-block:: python

    from game import run


Example
=======
.. code-block:: text

    game
        __init__.py
        config.py
        api.py
        dragon
            __init__.py
            wawelski.py
            red.py
            black.py
            white.py

Importing variable or constant from module
------------------------------------------
.. code-block:: python

    from game.config import RESOLUTION_X
    from game.config import RESOLUTION_Y

.. code-block:: python
    :caption: Preferred

    from game.config import RESOLUTION_X, RESOLUTION_Y

Importing submodules
--------------------
.. code-block:: python

    from game.dragon import red
    from game.dragon import white


    my_dragon1 = red.RedDragon()
    my_dragon2 = white.WhiteDragon()

.. code-block:: python

    from game.dragon import red, white

    my_dragon1 = red.RedDragon()
    my_dragon2 = white.WhiteDragon()

Importing all
-------------
.. code-block:: python

    from game.dragon import *

    my_dragon1 = red.RedDragon()
    my_dragon2 = white.WhiteDragon()

Importing objects from modules
------------------------------
.. code-block:: python

    from game.dragon.red import RedDragon
    from game.dragon.white import WhiteDragon

    my_dragon1 = RedDragon()
    my_dragon2 = WhiteDragon()

Importing with aliases
----------------------
.. code-block:: python

    from game.dragon.red import RedDragon as Smok

    wawelski = Smok()


Import path
===========
* Watch-out module names which are the same as in stdlib

.. code-block:: python

    import sys

    sys.path
    # ['/Users/matt/Developer/book/python/_tmp',
    #  '/Applications/PyCharm.app/Contents/helpers/pydev',
    #  '/Applications/PyCharm.app/Contents/helpers/pycharm_display',
    #  '/Applications/PyCharm.app/Contents/helpers/third_party/thriftpy',
    #  '/Applications/PyCharm.app/Contents/helpers/pydev',
    #  '/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
    #  '/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
    #  '/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
    #  '/Users/matt/.virtualenvs/book-python/lib/python3.7/site-packages',
    #  '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend',
    #  '/Applications/PyCharm.app/Contents/helpers/pycharm',
    #  '/Applications/PyCharm.app/Contents/helpers/pydev']

    sys.path.append('/path/to/directory')
    sys.path.insert(0, '/path/to/directory')
