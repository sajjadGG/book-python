from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass


class Button:
    __label: str
    __command: Command

    def __init__(self, command: Command):
        self.__command = command

    def set_label(self, name):
        self.__label = name

    def get_label(self):
        return self.__label

    def click(self):
        self.__command.execute()


class CustomerService:
    def add_customer(self) -> None:
        print('Add customer')


@dataclass
class AddCustomerCommand(Command):
    __service: CustomerService

    def execute(self) -> None:
        self.__service.add_customer()


if __name__ == '__main__':
    service = CustomerService()
    command = AddCustomerCommand(service)
    button = Button(command)
    button.click()
    # Add customer

