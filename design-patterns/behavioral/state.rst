State
=====


Rationale
---------
* EN: State
* PL: Stan
* Type: object


Use Cases
---------
* Changes based on class
* Open/Close principle
* Using polymorphism

Problem
-------
* Canvas object can behave differently depending on selected Tool
* All behaviors are represented by subclass of the tool interface

.. code-block:: python

    from enum import Enum


    class ToolType(Enum):
        SELECTION = 1
        BRUSH = 2
        ERASER = 3


    class Canvas:
        _current_tool: ToolType

        def get_current_tool(self) -> ToolType:
            return self._current_tool

        def set_current_tool(self, tool: ToolType) -> None:
            self._current_tool = tool

        def mouse_down(self) -> None:
            if self._current_tool == ToolType.SELECTION:
                print('Selection icon')
            elif self._current_tool == ToolType.BRUSH:
                print('Brush icon')
            elif self._current_tool == ToolType.ERASER:
                print('Eraser icon')

        def mouse_down(self) -> None:
            if self._current_tool == ToolType.SELECTION:
                print('Draw dashed rectangle')
            elif self._current_tool == ToolType.BRUSH:
                print('Draw line')
            elif self._current_tool == ToolType.ERASER:
                print('Erase something')


Design
------
.. figure:: img/designpatterns-state-gof.png


Implementation
--------------
.. figure:: img/designpatterns-state-usecase.png

.. literalinclude:: ../_src/designpatterns-state.py
    :language: python


Assignments
-----------
Change the following code to implement the State pattern:

.. code-block:: python

    from enum import Enum


    class Language(Enum):
        POLISH = 'pl'
        ENGLISH = 'en'
        RUSSIAN = 'ru'


    class Translation:
        _language: Language

        def __init__(self, language: Language):
            self._language = language

        def hello(self) -> str:
            if self._language is Language.POLISH:
                return 'Cześć'
            elif self._language is Language.ENGLISH:
                return 'Hello'
            elif self._language is Language.RUSSIAN:
                return 'Здравствуй'
            else:
                return 'Unknown language'

        def goodbye(self) -> str:
            if self._language is Language.POLISH:
                return 'Do widzenia'
            elif self._language is Language.ENGLISH:
                return 'Goodbye'
            elif self._language is Language.RUSSIAN:
                return 'До свидания'
            else:
                return 'Unknown language'


Then add another language:

    * Chinese hello: 你好
    * Chinese goodbye: 再见


.. todo:: Create assignments
