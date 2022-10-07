from abc import ABC, abstractmethod
from dataclasses import dataclass


class DialogBox(ABC):
    """Mediator class"""
    @abstractmethod
    def changed(self, control: 'UIControl') -> None:
        pass


@dataclass
class UIControl(ABC):
    owner: DialogBox


class ListBox(UIControl):
    selection: str

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def get_selection(self) -> str:
        return self.selection

    def set_selection(self, selection: str) -> None:
        self.selection = selection
        self.owner.changed(self)


class TextBox(UIControl):
    content: str

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str) -> None:
        self.content = content
        self.owner.changed(self)


class Button(UIControl):
    enabled: bool

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = enabled

    def is_enabled(self) -> bool:
        self.owner.changed(self)
        return self.enabled


class ArticlesDialogBox(DialogBox):
    articles_listbox: ListBox
    title_textbox: TextBox
    save_button: Button

    def simulate_user_interaction(self) -> None:
        self.articles_listbox.set_selection('Article 1')
        self.title_textbox.set_content('')
        self.title_textbox.set_content('Article 2')
        print(f'Text box: {self.title_textbox.get_content()}')
        print(f'Button: {self.save_button.is_enabled()}')

    def __init__(self) -> None:
        self.articles_listbox = ListBox(self)
        self.title_textbox = TextBox(self)
        self.save_button = Button(self)

    def changed(self, control: 'UIControl') -> None:
        if control == self.articles_listbox:
            self.article_selected()
        elif control == self.title_textbox:
            self.title_changed()

    def article_selected(self) -> None:
        self.title_textbox.set_content(self.articles_listbox.get_selection())
        self.save_button.set_enabled(True)

    def title_changed(self) -> None:
        content = self.title_textbox.get_content()
        is_empty = (content == None or content == '')
        self.save_button.set_enabled(not is_empty)


if __name__ == '__main__':
    dialog = ArticlesDialogBox()
    dialog.simulate_user_interaction()
