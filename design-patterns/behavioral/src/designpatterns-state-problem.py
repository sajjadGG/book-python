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
