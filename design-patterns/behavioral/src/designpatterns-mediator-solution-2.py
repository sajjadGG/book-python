from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


class EventHandler(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self) -> None:
        pass


@dataclass
class UIControl(metaclass=ABCMeta):
    __observers: list[EventHandler] = field(default_factory=list)

    def add_event_handler(self, observer: EventHandler) -> None:
        self.__observers.append(observer)

    def _notify_event_handlers(self):
        for observer in self.__observers:
            observer.__call__()


class ListBox(UIControl):
    __selection: str

    def get_selection(self) -> str:
        return self.__selection

    def set_selection(self, selection: str) -> None:
        self.__selection = selection
        self._notify_event_handlers()


class TextBox(UIControl):
    __content: str

    def get_content(self) -> str:
        return self.__content

    def set_content(self, content: str) -> None:
        self.__content = content
        self._notify_event_handlers()


class Button(UIControl):
    __enabled: bool

    def set_enabled(self, enabled: bool) -> None:
        self.__enabled = enabled
        self._notify_event_handlers()

    def is_enabled(self) -> bool:
        return self.__enabled


@dataclass
class ArticlesDialogBox:
    __articles_listbox: ListBox = ListBox()
    __title_textbox: TextBox = TextBox()
    __save_button: Button = Button()

    def __post_init__(self):
        self.__articles_listbox.add_event_handler(self.__article_selected)
        self.__title_textbox.add_event_handler(self.__title_changed)

    def simulate_user_interaction(self) -> None:
        self.__articles_listbox.set_selection('Article 1')
        self.__title_textbox.set_content('')
        self.__title_textbox.set_content('Article 2')
        print(f'Text box: {self.__title_textbox.get_content()}')
        print(f'Button: {self.__save_button.is_enabled()}')

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
