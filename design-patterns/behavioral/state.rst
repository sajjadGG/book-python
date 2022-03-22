State
=====
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
.. literalinclude:: assignments/designpatterns_state.py
    :caption: :download:`Solution <assignments/designpatterns_state.py>`
    :end-before: # Solution
