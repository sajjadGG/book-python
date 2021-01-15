from abc import ABCMeta, abstractmethod


class RemoteControl(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass


class AdvancedRemoteControl(RemoteControl, metaclass=ABCMeta):
    @abstractmethod
    def set_channel(self, number: int) -> None:
        pass

class SonyRemoteControl(RemoteControl):
    def turn_off(self) -> None:
        print('Sony turn off')

    def turn_on(self) -> None:
        print('Sony turn on')


class SonyAdvancedRemoteControl(AdvancedRemoteControl):
    def set_channel(self, number: int) -> None:
        print('Sony set channel')

    def turn_off(self) -> None:
        print('Sony turn off')

    def turn_on(self) -> None:
        print('Sony turn on')
