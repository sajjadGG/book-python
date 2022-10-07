from abc import ABC, abstractmethod


#%% Abstracts

class WindowEvents(ABC):
    @abstractmethod
    def on_left_mouse_button(self): ...

    @abstractmethod
    def on_right_mouse_button(self): ...


class Tool(WindowEvents, ABC):
    pass


#%% Tools

class SelectionTool(Tool):
    def on_left_mouse_button(self):
        print('Select')

    def on_right_mouse_button(self):
        print('Unselect')


class EraseTool(Tool):
    def on_left_mouse_button(self):
        print('Erase')

    def on_right_mouse_button(self):
        print('Undo erase')

class PencilTool(Tool):
    def on_left_mouse_button(self):
        print('Draw')

    def on_right_mouse_button(self):
        print('Stop drawing')

class BrushTool(Tool):
    def on_left_mouse_button(self):
        print('Paint')

    def on_right_mouse_button(self):
        print('Stop painting')


#%% Main

class Window(WindowEvents):
    current_tool: Tool

    def on_left_mouse_button(self):
        self.current_tool.on_left_mouse_button()

    def on_right_mouse_button(self):
        self.current_tool.on_right_mouse_button()


if __name__ == '__main__':
    window = Window()

    window.current_tool = BrushTool()
    window.on_left_mouse_button()
    window.on_right_mouse_button()

    window.current_tool = SelectionTool()
    window.on_left_mouse_button()
    window.on_right_mouse_button()

    window.current_tool = EraseTool()
    window.on_left_mouse_button()
    window.on_right_mouse_button()

# Paint
# Stop painting
# Select
# Unselect
# Erase
# Undo erase
