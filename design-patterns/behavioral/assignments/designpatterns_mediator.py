"""
* Assignment: DesignPatterns Behavioral Mediator
* Complexity: easy
* Lines of code: 34 lines
* Time: 21 min

English:
    1. Implement Mediator pattern
    2. Create form with Username, Password and Submit button
    3. If Username and Password are provided enable Submit button
    4. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Mediator
    2. Stwórz formularz logowania z Username, Password i przyciskiem Submit
    3. Jeżeli Username i Password odblokuj przycisk Submit
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> form = LoginForm()
    >>> form.set_username('root')
    >>> form.set_password('')
    >>> form.submit()
    Traceback (most recent call last):
    PermissionError: Cannot submit form without Username and Password

    >>> form = LoginForm()
    >>> form.set_username('root')
    >>> form.set_password('MyVoiceIsMyPasswordVerifyMe')
    >>> form.submit()
    'Submitted'
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


class EventHandler(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self) -> None:
        pass


@dataclass
class UIControl(metaclass=ABCMeta):
    name: str
    __observers: list[EventHandler] = field(default_factory=list)

    def add_event_handler(self, observer: EventHandler) -> None:
        self.__observers.append(observer)

    def _notify_event_handlers(self):
        for observer in self.__observers:
            observer.__call__()



class Input(UIControl):
    __content: str

    def get_content(self) -> str:
        raise NotImplementedError

    def set_content(self, content: str) -> None:
        raise NotImplementedError


class Button(UIControl):
    __enabled: bool

    def set_enabled(self, enabled: bool) -> None:
        raise NotImplementedError

    def is_enabled(self) -> bool:
        raise NotImplementedError


@dataclass
class LoginForm:
    __username_input: Input = Input('Username')
    __password_input: Input = Input('Password')
    __submit_button: Button = Button('Submit')

    def __post_init__(self):
        raise NotImplementedError

    def set_username(self, username: str):
        raise NotImplementedError

    def set_password(self, password: str):
        raise NotImplementedError

    def __username_changed(self) -> None:
        raise NotImplementedError

    def __password_changed(self) -> None:
        raise NotImplementedError

    def __try_enable_submit(self):
        raise NotImplementedError

    def submit(self):
        raise NotImplementedError


# Solution
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


class EventHandler(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self) -> None:
        pass


@dataclass
class UIControl(metaclass=ABCMeta):
    name: str
    __observers: list[EventHandler] = field(default_factory=list)

    def add_event_handler(self, observer: EventHandler) -> None:
        self.__observers.append(observer)

    def _notify_event_handlers(self):
        for observer in self.__observers:
            observer.__call__()


class Input(UIControl):
    __content: str

    def get_content(self) -> str:
        if hasattr(self, '__content'):
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
        if not hasattr(self, '__enabled'):
            return False
        return self.__enabled


@dataclass
class LoginForm:
    __username_input: Input = Input('Username')
    __password_input: Input = Input('Password')
    __submit_button: Button = Button('Submit')

    def __post_init__(self):
        self.__username_input.add_event_handler(self.__username_changed)
        self.__password_input.add_event_handler(self.__password_changed)

    def set_username(self, username: str):
        self.__username_input.set_content(username)

    def set_password(self, password: str):
        self.__password_input.set_content(password)

    def __username_changed(self) -> None:
        self.__try_enable_submit()

    def __password_changed(self) -> None:
        self.__try_enable_submit()

    def __try_enable_submit(self):
        username = self.__username_input.get_content()
        password = self.__password_input.get_content()
        if username is not None and password is not None:
            self.__submit_button.set_enabled(True)

    def submit(self):
        if not self.__submit_button.is_enabled():
            raise PermissionError('Cannot submit form without Username and Password')
        else:
            return 'Submitted'
