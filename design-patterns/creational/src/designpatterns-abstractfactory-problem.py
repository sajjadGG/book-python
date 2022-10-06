from enum import Enum


#%% Interfaces
class Widget:
    def render(self) -> None:
        raise NotImplementedError

class Button(Widget):
    pass

class Textbox(Widget):
    pass


#%% Material Theme
class MaterialButton(Button):
    def render(self) -> None:
        print('Material Button')

class MaterialTextbox(Textbox):
    def render(self) -> None:
        print('Material Textbox')


#%% Flat Theme
class FlatButton(Button):
    def render(self) -> None:
        print('Flat Button')

class FlatTextbox(Textbox):
    def render(self) -> None:
        print('Flat Textbox')


#%% Main
class Theme(Enum):
    MATERIAL = 1
    FLAT = 2


class ContactForm:
    def render(self, theme: Theme) -> None:
        if self.theme == Theme.MATERIAL:
            MaterialTextbox().render()
            MaterialButton().render()
        elif self.theme == Theme.FLAT:
            FlatTextbox().render()
            FlatButton().render()
