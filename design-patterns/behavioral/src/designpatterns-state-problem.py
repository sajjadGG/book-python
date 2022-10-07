from enum import Enum


class Tool(Enum):
    SELECTION = 1
    PENCIL = 2
    ERASE = 3
    BRUSH = 4


class Window:
    current_tool: Tool

    def on_left_mouse_button(self):
        if self.current_tool == Tool.SELECTION:
            print('Select')
        elif self.current_tool == Tool.PENCIL:
            print('Draw')
        elif self.current_tool == Tool.ERASE:
            print('Erase')
        elif self.current_tool == Tool.BRUSH:
            print('Paint')

    def on_right_mouse_button(self):
        if self.current_tool == Tool.SELECTION:
            print('Unselect')
        elif self.current_tool == Tool.PENCIL:
            print('Stop drawing')
        elif self.current_tool == Tool.ERASE:
            print('Undo erase')
        elif self.current_tool == Tool.BRUSH:
            print('Stop painting')



if __name__ == '__main__':
    window = Window()

    window.current_tool = Tool.BRUSH
    window.on_left_mouse_button()
    window.on_right_mouse_button()

    window.current_tool = Tool.SELECTION
    window.on_left_mouse_button()
    window.on_right_mouse_button()

    window.current_tool = Tool.ERASE
    window.on_left_mouse_button()
    window.on_right_mouse_button()

# Paint
# Stop painting
# Select
# Unselect
# Erase
# Undo erase
