from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class DialogBox(metaclass=ABCMeta):
    """Mediator class"""
    @abstractmethod
    def changed(self, control: 'UIControl') -> None:
        pass


@dataclass
class UIControl(metaclass=ABCMeta):
    _owner: DialogBox


class ListBox(UIControl):
    __selection: str

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def get_selection(self) -> str:
        return self.__selection

    def set_selection(self, selection: str) -> None:
        self.__selection = selection
        self._owner.changed(self)


class TextBox(UIControl):
    __content: str

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def get_content(self) -> str:
        return self.__content

    def set_content(self, content: str) -> None:
        self.__content = content
        self._owner.changed(self)


class Button(UIControl):
    __enabled: bool

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def set_enabled(self, enabled: bool) -> None:
        self.__enabled = enabled

    def is_enabled(self) -> bool:
        self._owner.changed(self)
        return self.__enabled


class ArticlesDialogBox(DialogBox):
    __articles_listbox: ListBox
    __title_textbox: TextBox
    __save_button: Button

    def simulate_user_interaction(self) -> None:
        self.__articles_listbox.set_selection('Article 1')
        self.__title_textbox.set_content('')
        self.__title_textbox.set_content('Article 2')
        print(f'Text box: {self.__title_textbox.get_content()}')
        print(f'Button: {self.__save_button.is_enabled()}')

    def __init__(self) -> None:
        self.__articles_listbox = ListBox(self)
        self.__title_textbox = TextBox(self)
        self.__save_button = Button(self)

    def changed(self, control: 'UIControl') -> None:
        if control == self.__articles_listbox:
            self.__article_selected()
        elif control == self.__title_textbox:
            self.__title_changed()

    def __article_selected(self) -> None:
        self.__title_textbox.set_content(self.__articles_listbox.get_selection())
        self.__save_button.set_enabled(True)

    def __title_changed(self) -> None:
        content = self.__title_textbox.get_content()
        is_empty = (content == None or content == '')
        self.__save_button.set_enabled(not is_empty)


if __name__ == '__main__':
    dialog = ArticlesDialogBox()
    dialog.simulate_user_interaction()
