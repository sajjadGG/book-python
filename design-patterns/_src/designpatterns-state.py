from abc import ABCMeta, abstractmethod


class Tool(metaclass=ABCMeta):
    @abstractmethod
    def mouse_down(self) -> None:
        pass

    @abstractmethod
    def mouse_up(self) -> None:
        pass


class SelectionTool(Tool):
    def mouse_down(self) -> None:
        print('Selection icon')

    def mouse_up(self) -> None:
        print('Draw dashed rectangle')


class BrushTool(Tool):
    def mouse_down(self) -> None:
        print('Brush icon')

    def mouse_up(self) -> None:
        print('Draw line')


class Canvas:
    _current_tool: Tool

    def mouse_down(self) -> None:
        self._current_tool.mouse_down()

    def mouse_up(self) -> None:
        self._current_tool.mouse_up()

    def get_current_tool(self):
        return self._current_tool

    def set_current_tool(self, newtool: Tool):
        self._current_tool = newtool


if __name__ == '__main__':
    canvas = Canvas()
    canvas.set_current_tool(SelectionTool())

    canvas.mouse_down()
    # Selection icon

    canvas.mouse_up()
    # Draw dashed rectangle
