from abc import ABC, abstractmethod
from dataclasses import dataclass


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Button:
    label: str
    command: Command

    def __init__(self, command: Command):
        self.command = command

    def set_label(self, name):
        self.label = name

    def get_label(self):
        return self.label

    def click(self):
        self.command.execute()


class CustomerService:
    def add_customer(self) -> None:
        print('Add customer')


@dataclass
class AddCustomerCommand(Command):
    service: CustomerService

    def execute(self) -> None:
        self.service.add_customer()


if __name__ == '__main__':
    service = CustomerService()
    command = AddCustomerCommand(service)
    button = Button(command)
    button.click()
    # Add customer
