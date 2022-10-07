from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class EventHandler(ABC):
    @abstractmethod
    def __call__(self) -> None:
        pass


@dataclass
class UIControl(ABC):
    observers: list[EventHandler] = field(default_factory=list)

    def add_event_handler(self, observer: EventHandler) -> None:
        self.observers.append(observer)

    def _notify_event_handlers(self):
        for observer in self.observers:
            observer.__call__()


class ListBox(UIControl):
    selection: str

    def get_selection(self) -> str:
        return self.selection

    def set_selection(self, selection: str) -> None:
        self.selection = selection
        self._notify_event_handlers()


class TextBox(UIControl):
    content: str

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str) -> None:
        self.content = content
        self._notify_event_handlers()


class Button(UIControl):
    enabled: bool

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = enabled
        self._notify_event_handlers()

    def is_enabled(self) -> bool:
        return self.enabled


@dataclass
class ArticlesDialogBox:
    articles_listbox: ListBox = ListBox()
    title_textbox: TextBox = TextBox()
    save_button: Button = Button()

    def __post_init__(self):
        self.articles_listbox.add_event_handler(self.article_selected)
        self.title_textbox.add_event_handler(self.title_changed)

    def simulate_user_interaction(self) -> None:
        self.articles_listbox.set_selection('Article 1')
        self.title_textbox.set_content('')
        self.title_textbox.set_content('Article 2')
        print(f'Text box: {self.title_textbox.get_content()}')
        print(f'Button: {self.save_button.is_enabled()}')

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
