#%% Interfaces
class Widget:
    def render(self) -> None:
        raise NotImplementedError

class Button(Widget):
    pass

class Textbox(Widget):
    pass

class WidgetFactory:
    def create_button(self) -> Button:
        raise NotImplementedError

    def create_textbox(self) -> Textbox:
        raise NotImplementedError


#%% Material Theme
class MaterialButton(Button):
    def render(self) -> None:
        print('Material Button')

class MaterialTextbox(Textbox):
    def render(self) -> None:
        print('Material Textbox')

class MaterialWidgetFactory(WidgetFactory):
    def create_button(self) -> Button:
        return MaterialButton()

    def create_textbox(self) -> Textbox:
        return MaterialTextbox()


#%% Ant Theme
class AntButton(Button):
    def render(self) -> None:
        print('Ant Button')

class AntTextbox(Textbox):
    def render(self) -> None:
        print('Ant Textbox')

class AntWidgetFactory(WidgetFactory):
    def create_button(self) -> Button:
        return AntButton()

    def create_textbox(self) -> Textbox:
        return AntTextbox()


#%% Main
class ContactForm:
    def render(self, factory: WidgetFactory) -> None:
        factory.create_textbox().render()
        factory.create_button().render()


if __name__ == '__main__':
    theme = MaterialWidgetFactory()
    ContactForm().render(theme)
