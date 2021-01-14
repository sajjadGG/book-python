from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass

class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self) -> None:
        pass


@dataclass
class History:
    __commands: list[UndoableCommand] = field(default_factory=list)

    def push(self, command: UndoableCommand) -> None:
        self.__commands.append(command)

    def pop(self):
        return self.__commands.pop()

    def size(self) -> int:
        return len(self.__commands)


@dataclass
class HtmlDocument:
    __content: str = ''

    def set_content(self, content):
        self.__content = content

    def get_content(self):
        return self.__content


@dataclass
class BoldCommand(UndoableCommand):
    __document: HtmlDocument
    __history: History = History()
    __previous_content: Optional[str] = None

    def unexecute(self) -> None:
        self.__document.set_content(self.__previous_content)

    def apply(self, content):
        return f'<b>{content}</b>'

    def execute(self) -> None:
        current_content = self.__document.get_content()
        self.__previous_content = current_content
        self.__document.set_content(self.apply(current_content))
        self.__history.push(self)


@dataclass
class UndoCommand(Command):
    __history: History

    def execute(self) -> None:
        if self.__history.size() > 0:
            self.__history.pop().unexecute()


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
