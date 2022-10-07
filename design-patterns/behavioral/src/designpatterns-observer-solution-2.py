from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


@dataclass
class Subject:
    """
    Observable - class which is observed
    """
    observers: list[Observer] = field(default_factory=list)

    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class DataSource(Subject):
    value: int

    def get_value(self) -> int:
        return self.value

    def set_value(self, value) -> None:
        self.value = value
        self.notify_observers()


@dataclass
class Spreadsheet(Observer):
    datasource: DataSource

    def update(self) -> None:
        value = self.datasource.get_value()
        print(f'Spreadsheet got updated: {value}')


@dataclass
class Chart(Observer):
    datasource: DataSource

    def update(self) -> None:
        value = self.datasource.get_value()
        print(f'Chart got updated: {value}')


if __name__ == '__main__':
    datasource = DataSource()
    sheet1 = Spreadsheet(datasource)
    sheet2 = Spreadsheet(datasource)
    chart = Chart(datasource)

    datasource.add_observer(sheet1)
    datasource.add_observer(sheet2)
    datasource.add_observer(chart)

    datasource.set_value(1)
