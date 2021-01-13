from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass


class ResizeCommand(Command):
    def execute(self) -> None:
        print('Resize')

class BlackAndWhiteCommand(Command):
    def execute(self) -> None:
        print('Black And White')


@dataclass
class CompositeCommand(Command):
    __commands: list[Command] = field(default_factory=list)

    def add(self, command: Command) -> None:
        self.__commands.append(command)

    def execute(self) -> None:
        for command in self.__commands:
            command.execute()


if __name__ == '__main__':
    composite = CompositeCommand()
    composite.add(ResizeCommand())
    composite.add(BlackAndWhiteCommand())
    composite.execute()
    # Resize
    # Black And White
