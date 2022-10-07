from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self) -> None:
        pass


@dataclass
class History:
    commands: list[UndoableCommand] = field(default_factory=list)

    def push(self, command: UndoableCommand) -> None:
        self.commands.append(command)

    def pop(self):
        return self.commands.pop()

    def size(self) -> int:
        return len(self.commands)


@dataclass
class HtmlDocument:
    content: str = ''

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content


@dataclass
class BoldCommand(UndoableCommand):
    document: HtmlDocument
    history: History = History()
    previous_content: str | None = None

    def unexecute(self) -> None:
        self.document.set_content(self.previous_content)

    def apply(self, content):
        return f'<b>{content}</b>'

    def execute(self) -> None:
        current_content = self.document.get_content()
        self.previous_content = current_content
        self.document.set_content(self.apply(current_content))
        self.history.push(self)


@dataclass
class UndoCommand(Command):
    history: History

    def execute(self) -> None:
        if self.history.size() > 0:
            self.history.pop().unexecute()


if __name__ == '__main__':
    history = History()
    document = HtmlDocument('Hello World')

    # This should be onButtonClick or KeyboardShortcut
    BoldCommand(document, history).execute()
    print(document.get_content())
    # <b>Hello World</b>

    # This should be onButtonClick or KeyboardShortcut
    UndoCommand(history).execute()
    print(document.get_content())
    # Hello World
